import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog

mydata=[]

class Attendance:
    def __init__(self, root):
        self.root = root

        # Get the screen width and height
        screen_width = self.root.winfo_screenwidth() -400
        screen_height = self.root.winfo_screenheight() - 200

        #--------------------varible----------------
        self.var_attendance_id = tk.StringVar()
        self.var_roll = tk.StringVar()
        self.var_name = tk.StringVar()
        self.var_dep = tk.StringVar()
        self.var_time = tk.StringVar()
        self.var_date = tk.StringVar()
        self.var_attendance_status = tk.StringVar()




        #-------------------Main Window----------------
        # Set the geometry using screen dimensions
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        self.root.title("Face Recognition System")

        # Open and resize the image
        image_path = r"image_assets\bg1.jpeg"
        image = Image.open(image_path)
        image = image.resize((screen_width, screen_height))  # Resize image to fit screen
        self.photo_image = ImageTk.PhotoImage(image)

        # Create the image label
        bg_image = tk.Label(self.root, image=self.photo_image)
        bg_image.place(x=0, y=0, width=screen_width, height=screen_height)

        # Create the title label
        title_lbl = tk.Label(self.root, text="STUDENT ATTENDANCE", font=('times new roman', 35, "bold"), bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=screen_width, height=50)

        #Create Main Frame
        main_frame = tk.Frame(bg_image,bd=2)
        main_frame.place(x=20, y=250, width=screen_width-45, height=600)

        #-----------------Left LabelFrame---------------------------
        left_frame = tk.LabelFrame(main_frame,bd=2,relief="ridge",text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10, y=10, width=(screen_width/2)-40, height=575)

        #Create Main Frame
        lf1 = tk.Frame(left_frame,bd=2,relief="ridge",bg="white")
        lf1.place(x=10, y=10, width=(screen_width/2)-70, height=500)

        #--attendance id--
        att_id_lable = tk.Label(lf1,text="AttendanceID",font=("times new roman",12,"bold"),bg="white")
        att_id_lable.grid(row=0,column=0,padx=5,pady=10)
        att_id_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_attendance_id)
        att_id_entry.grid(row=0,column=1,padx=5,pady=10,sticky="W")

        #--roll no--
        roll_lable = tk.Label(lf1,text="Roll No",font=("times new roman",12,"bold"),bg="white")
        roll_lable.grid(row=0,column=2,padx=5,pady=10)
        roll_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_roll)
        roll_entry.grid(row=0,column=3,padx=5,pady=10,sticky="W")

        #--Name--
        name_lable = tk.Label(lf1,text="Name",font=("times new roman",12,"bold"),bg="white")
        name_lable.grid(row=1,column=0,padx=5,pady=10)
        name_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_name)
        name_entry.grid(row=1,column=1,padx=5,pady=10,sticky="W")

        #--Department--
        dep_lable = tk.Label(lf1,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_lable.grid(row=1,column=2,padx=5,pady=10)
        dep_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_dep)
        dep_entry.grid(row=1,column=3,padx=5,pady=10,sticky="W")

        #--Time--
        time_lable = tk.Label(lf1,text="Time",font=("times new roman",12,"bold"),bg="white")
        time_lable.grid(row=2,column=0,padx=5,pady=10)
        time_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_time)
        time_entry.grid(row=2,column=1,padx=5,pady=10,sticky="W")

        #--Date--
        date_lable = tk.Label(lf1,text="Date",font=("times new roman",12,"bold"),bg="white")
        date_lable.grid(row=2,column=2,padx=5,pady=10)
        date_entry = ttk.Entry(lf1,width=18,font=("times new roman",12,"bold"),textvariable=self.var_date)
        date_entry.grid(row=2,column=3,padx=5,pady=10,sticky="W")

        #--attendance status--
        at_status_lable = tk.Label(lf1,text="Attendance Status",font=("times new roman",12,"bold"),bg="white")
        at_status_lable.grid(row=3,column=0,padx=5,pady=10)
        at_status_combo=ttk.Combobox(lf1,font=("times new roman",12,"bold"),width=16,state="readonly",textvariable=self.var_attendance_status)
        at_status_combo["values"]=("Status","Absent","Present")
        at_status_combo.current(0)
        at_status_combo.grid(row=3,column=1,padx=5,pady=10,sticky="W")


        #Button Frame 
        button_frame = tk.Frame(lf1,bd=2,relief="flat",bg="White")
        button_frame.place(x=5,y=400,width=(screen_width/2)-85,height=50)

        #Import CSV button
        import_button = tk.Button(button_frame,text="Import CSV",width=16,font=("times new roman",13,"bold"),bg="blue",fg="White",command=self.import_csv)
        import_button.grid(row=0,column=0,pady=4)

        #Export CSV button
        export_button = tk.Button(button_frame,text="Export CSV",width=16,font=("times new roman",13,"bold"),bg="blue",fg="White",command=self.export_csv)
        export_button.grid(row=0,column=1,pady=4)

        #Update button
        update_button = tk.Button(button_frame,text="Update",width=16,font=("times new roman",13,"bold"),bg="blue",fg="White",command=self.update_data)
        update_button.grid(row=0,column=2,pady=4)

        #reset button
        reset_button = tk.Button(button_frame,text="Reset",width=16,font=("times new roman",13,"bold"),bg="blue",fg="White",command=self.reset_data)
        reset_button.grid(row=0,column=3,pady=4)

        #-----------------Right LabelFrame------------------
        right_frame = tk.LabelFrame(main_frame,bd=2,relief="ridge",text="Attendance Data",font=("times new roman",12,"bold"))
        right_frame.place(x=(screen_width/2)-10, y=10, width=(screen_width/2)-50, height=575)

        # Create table Frame
        table_frame = tk.Frame(right_frame, bd=2, relief="ridge", bg="white")
        table_frame.place(x=10, y=10, width=(screen_width/2)-80, height=500)

        scroll_x = ttk.Scrollbar(table_frame, orient="horizontal")
        scroll_y = ttk.Scrollbar(table_frame, orient="vertical")

        self.AttReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "dep", "time", "date", "attendance"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.AttReportTable.xview)
        scroll_y.config(command=self.AttReportTable.yview)

        self.AttReportTable.heading("id", text="StudentID")
        self.AttReportTable.heading("roll", text="RollNo")
        self.AttReportTable.heading("name", text="Name")
        self.AttReportTable.heading("dep", text="Department")
        self.AttReportTable.heading("time", text="Time")
        self.AttReportTable.heading("date", text="Date")
        self.AttReportTable.heading("attendance", text="Attendance")
        self.AttReportTable["show"] = "headings"

        self.AttReportTable.column("id", width=100)
        self.AttReportTable.column("roll", width=100)
        self.AttReportTable.column("name", width=100)
        self.AttReportTable.column("dep", width=100)
        self.AttReportTable.column("time", width=100)
        self.AttReportTable.column("date", width=100)
        self.AttReportTable.column("attendance", width=100)

        self.AttReportTable.pack(fill="both", expand=1)

        self.AttReportTable.bind("<ButtonRelease>",self.get_cursor)

    
    #--------Fetch data Function-------
    def fetch_data(self,rows):
        self.AttReportTable.delete(*self.AttReportTable.get_children())
        for row in rows:
            self.AttReportTable.insert("", "end", values=row)

    #--------Import CSV Function-------
    def import_csv(self):
        global mydata
        mydata.clear()
        # Open a file dialog to select the CSV file
        file1 = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
            parent=self.root
        )
        
        # Check if a file was selected
        if file1:
            with open(file1, mode='r') as myfile:
                csv_reader = csv.reader(myfile, delimiter=',')
                mydata.clear()  # Clear existing data if needed
                for row in csv_reader:
                    mydata.append(row)
                self.fetch_data(mydata)  # Assuming fetch_data is defined elsewhere in the class

    #--------Export CSV Function-------
    def export_csv(self):
        try:
            if len(mydata)<1:
                messagebox.showerror("Error", "No data to export",parent=self.root)
                return False
            # Open a file dialog to select the CSV file
            file2 = filedialog.asksaveasfilename(
                initialdir=os.getcwd(),
                title="Open CSV",
                filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                parent=self.root
            )

            # Check if a file was selected and write data
            if file2:
                with open(file2, mode='w',newline="") as myfile:
                    csv_writer = csv.writer(myfile, delimiter=',')
                    for row in mydata:
                        csv_writer.writerow(row)
                    messagebox.showinfo("Data Export", "Data Exported to " + os.path.basename(file2) + " successfully!",parent=self.root)
        except Exception as es:
            messagebox.showerror("Error", f"Failed to export data to CSV\n{str(es)}",parent=self.root)

    
    #--------get cursor Function-------
    def get_cursor(self,event=""):
        cursor_row = self.AttReportTable.focus()
        content = self.AttReportTable.item(cursor_row)
        row = content["values"]
        self.var_attendance_id.set(row[0])
        self.var_roll.set(row[1])
        self.var_name.set(row[2])
        self.var_dep.set(row[3])
        self.var_time.set(row[4])
        self.var_date.set(row[5])
        self.var_attendance_status.set(row[6])

    
    #--------reset Function-------
    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_roll.set("")
        self.var_name.set("")
        self.var_dep.set("")
        self.var_time.set("")
        self.var_date.set("")
        self.var_attendance_status.set("")

    #--------Update data Function-------
    def update_data(self):
        if (
            self.var_attendance_id.get() == ""
            or self.var_roll.get() == ""
            or self.var_name.get() == ""
            or self.var_dep.get() == ""
            or self.var_time.get() == ""
            or self.var_date.get() == ""
            or self.var_attendance_status.get() == ""
        ):
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            update = messagebox.askyesno("Update", "Do you want to update this record?", parent=self.root)
            if update > 0:
                try:
                    # Get the selected row index
                    selected_row = self.AttReportTable.focus()
                    content = self.AttReportTable.item(selected_row)
                    row_index = self.AttReportTable.index(selected_row)

                    # Update the data in the mydata list
                    mydata[row_index] = [
                        self.var_attendance_id.get(),
                        self.var_roll.get(),
                        self.var_name.get(),
                        self.var_dep.get(),
                        self.var_time.get(),
                        self.var_date.get(),
                        self.var_attendance_status.get()
                    ]

                    # Refresh the table
                    self.fetch_data(mydata)

                    # Reset the fields after updating
                    self.reset_data()

                    # Update the CSV file
                    file_path = filedialog.askopenfilename(
                        initialdir=os.getcwd(),
                        title="Select CSV file to update",
                        filetypes=(("CSV File", "*.csv"), ("All Files", "*.*")),
                        parent=self.root
                    )

                    if file_path:
                        with open(file_path, mode='w', newline="") as myfile:
                            csv_writer = csv.writer(myfile, delimiter=',')
                            csv_writer.writerows(mydata)
                        messagebox.showinfo("Success", f"Record updated successfully in {os.path.basename(file_path)}", parent=self.root)

                except Exception as es:
                    messagebox.showerror("Error", f"Due to : {str(es)}", parent=self.root)

        
    
if __name__ == "__main__":
    root = tk.Tk()
    obj = Attendance(root)
    root.mainloop()