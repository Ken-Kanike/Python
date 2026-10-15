import os
import tkinter as tk
from PIL import Image, ImageTk
import threading

gif_frames = []
frame_delay = 0
frame_count = -1
current_frame = None
screen_width = 0
screen_height = 0

class Main:
    def __init__(self, root):
        self.root = root

        global screen_width, screen_height

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth() - 400
        screen_height = self.root.winfo_screenheight() - 100

        # Set the geometry using screen dimensions
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face Recognition System")

        self.gif_lb = tk.Label(root)
        self.gif_lb.place(x=0, y=0, width=screen_width, height=screen_height)

        # Create the title label
        title_lbl = tk.Label(self.root, text="FACE RECOGNITION ATTENDANCE SYSTEM", font=('times new roman', 35, "bold"), bg="black",fg="Cyan")
        title_lbl.place(x=0, y=0, width=screen_width, height=50)

        # b1_lbl = tk.Button(self.gif_lb,text="Student Details",cursor="hand2",font=('times new roman', 15, "bold"), bg="darkblue", fg="white")
        # b1_lbl.place(x=200,y=300,width=220,height=40)

        threading.Thread(target=self.ready_gif).start()

    def ready_gif(self):
        global frame_delay
        try:
            gif_path = os.path.join(os.path.dirname(__file__), "face_phone.gif")
            gif_file = Image.open(gif_path)
            for frame in range(gif_file.n_frames):
                gif_file.seek(frame)
                copy = gif_file.copy()
                resized_frame = copy.resize((screen_width, screen_height), Image.LANCZOS)
                gif_frames.append(ImageTk.PhotoImage(resized_frame))

            frame_delay = gif_file.info['duration']
            self.play_gif()

        except FileNotFoundError:
            print("The file 'face_bg.gif' was not found. Please check the file path.")
        except AttributeError:
            print("The Pillow version might be outdated or the file might not be a GIF.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

    def play_gif(self):
        global frame_count, current_frame

        frame_count = (frame_count + 1) % len(gif_frames)
        current_frame = gif_frames[frame_count]
        self.gif_lb.config(image=current_frame)
        self.root.after(frame_delay, self.play_gif)

if __name__ == "__main__":
    root = tk.Tk()
    obj = Main(root)
    root.mainloop()
