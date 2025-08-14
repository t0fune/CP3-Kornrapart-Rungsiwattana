import tkinter as tk
from tkinter import messagebox
from tkinter import font

def check_login():
    username = username_entry.get().lower()
    password = password_entry.get().lower()

    if username == "Jupiter".lower() and password == "238855":
        messagebox.showinfo("Login Success", "Welcome!!!")
        log_in.destroy()  # ปิดหน้าต่าง login
        show_main_page()  # เรียกฟังก์ชันหน้าหลัก
    else:
        messagebox.showerror("Login Failed", "Username or password incorrect try again ")
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

def show_main_page():
    main_window = tk.Tk()
    main_window.title("Main Page")
    main_window.geometry("400x200")
    tk.Label(main_window, text="You're brilliant , Welcome !!!", font=("Arial", 18)).pack(expand=True)
    main_window.mainloop()

def show_hint():
    hint_window = tk.Tk()
    hint_window.title("Hint Page")
    hint_window.geometry("650x170")
    hint_window.configure(bg="#f0f0f0")
    tk.Label(hint_window, text="Username Hint : What is the largest planet in our solar system?", font=lbl_font, bg="#f0f0f0").place(x=50, y=40)
    tk.Label(hint_window, text="Password Hint : What is the average mile distance between Earth and the moon? ", font=lbl_font, bg="#f0f0f0").place(x=50, y=90)


# สร้างหน้าต่าง login
log_in = tk.Tk()
log_in.title("Login")
log_in.geometry("350x200")
log_in.configure(bg="#f0f0f0")

# ฟอนต์
lbl_font = font.Font(family="Arial", size=12)
entry_font = font.Font(family="Arial", size=12)

# Label สำหรับ Username
tk.Label(log_in, text="Username:", font=lbl_font, bg="#f0f0f0").place(x=50, y=50)
username_entry = tk.Entry(log_in, font=entry_font)
username_entry.place(x=150, y=50)

# Label สำหรับ Password
tk.Label(log_in, text="Password:", font=lbl_font, bg="#f0f0f0").place(x=50, y=90)
password_entry = tk.Entry(log_in, font=entry_font, show="*")
password_entry.place(x=150, y=90)


# ปุ่ม Login
login_btn = tk.Button(log_in, text="Login", font=("Arial", 12), width=10, bg="#4CAF50", fg="white", command=check_login)
login_btn.place(x=125, y=140)

#ปุ่ม Hint
hint_btn = tk.Button(log_in, text="Hint", font=("Arial", 7), width=5, bg="white", fg="black", command=show_hint)
hint_btn.place(x=240, y=145)

log_in.mainloop()