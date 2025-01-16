import tkinter as tk
from tkinter import messagebox
import mysql.connector as c
import json

with open(r'PyMySQL\data.json', 'r') as file:
    config = json.load(file)

db_password = config.get("db_password")

try:
    con = c.connect(host='localhost', user='root', passwd=db_password, database='pydb')
    if con.is_connected():
        print("Connection successful!")
except Exception as e:
    messagebox.showerror("Database Connection Error", str(e))
    exit()

cursor = con.cursor()

def insert_data():
    try:
        id = entry_id.get()
        name = entry_name.get()
        code = entry_code.get()

        if not (id and name and code):
            messagebox.showwarning("Input Error", "All fields are required!")
            return

        insert_query = f"INSERT INTO demo VALUES('{id}', '{name}', '{code}')"
        cursor.execute(insert_query)
        con.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")

        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_code.delete(0, tk.END)
        fetch_data()
    except Exception as e:
        messagebox.showerror("Error", str(e))

def fetch_data():
    try:
        select_query = 'SELECT * FROM demo'
        cursor.execute(select_query)
        rows = cursor.fetchall()

        result_text.delete(1.0, tk.END)
        for row in rows:
            result_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Code: {row[2]}\n")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def search_data():
    try:
        id = entry_id.get()
        if not id:
            messagebox.showwarning("Input Error", "Please enter an ID to search!")
            return

        search_query = f"SELECT * FROM demo WHERE id = '{id}'"
        cursor.execute(search_query)
        row = cursor.fetchone()

        if row:
            result_text.delete(1.0, tk.END)
            result_text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Code: {row[2]}\n")
        else:
            messagebox.showinfo("Not Found", "No record found with the given ID.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

def update_data():
    try:
        id = entry_id.get()
        name = entry_name.get()
        code = entry_code.get()

        if not (id and name and code):
            messagebox.showwarning("Input Error", "All fields are required for updating!")
            return

        update_query = f"UPDATE demo SET name = '{name}', code = '{code}' WHERE id = '{id}'"
        cursor.execute(update_query)
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Data updated successfully!")
            fetch_data()
        else:
            messagebox.showinfo("Not Found", "No record found with the given ID to update.")

        entry_id.delete(0, tk.END)
        entry_name.delete(0, tk.END)
        entry_code.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def delete_data():
    try:
        id = entry_id.get()
        if not id:
            messagebox.showwarning("Input Error", "Please enter an ID to delete!")
            return

        delete_query = f"DELETE FROM demo WHERE id = '{id}'"
        cursor.execute(delete_query)
        con.commit()

        if cursor.rowcount > 0:
            messagebox.showinfo("Success", "Data deleted successfully!")
            fetch_data()
        else:
            messagebox.showinfo("Not Found", "No record found with the given ID to delete.")

        entry_id.delete(0, tk.END)
    except Exception as e:
        messagebox.showerror("Error", str(e))

def exit_app():
    con.close()
    root.destroy()

# UI Setup
root = tk.Tk()
root.title("Database Management UI")
root.geometry("500x600")

frame_input = tk.Frame(root)
frame_input.pack(pady=10)

tk.Label(frame_input, text="ID:").grid(row=0, column=0, padx=5, pady=5)
entry_id = tk.Entry(frame_input)
entry_id.grid(row=0, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Name:").grid(row=1, column=0, padx=5, pady=5)
entry_name = tk.Entry(frame_input)
entry_name.grid(row=1, column=1, padx=5, pady=5)

tk.Label(frame_input, text="Code:").grid(row=2, column=0, padx=5, pady=5)
entry_code = tk.Entry(frame_input)
entry_code.grid(row=2, column=1, padx=5, pady=5)

frame_buttons = tk.Frame(root)
frame_buttons.pack(pady=10)

tk.Button(frame_buttons, text="Insert Data", command=insert_data).grid(row=0, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Fetch Data", command=fetch_data).grid(row=0, column=1, padx=10, pady=5)
tk.Button(frame_buttons, text="Search Data", command=search_data).grid(row=0, column=2, padx=10, pady=5)
tk.Button(frame_buttons, text="Update Data", command=update_data).grid(row=1, column=0, padx=10, pady=5)
tk.Button(frame_buttons, text="Delete Data", command=delete_data).grid(row=1, column=1, padx=10, pady=5)
tk.Button(frame_buttons, text="Exit", command=exit_app).grid(row=1, column=2, padx=10, pady=5)

frame_result = tk.Frame(root)
frame_result.pack(pady=10, fill=tk.BOTH, expand=True)

result_text = tk.Text(frame_result, height=15, width=60)
result_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame_result, command=result_text.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
result_text.config(yscrollcommand=scrollbar.set)

root.mainloop()
