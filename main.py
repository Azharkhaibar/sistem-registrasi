import tkinter as tk
from tkinter import messagebox


data_pengguna = {"azhar": "password123"}

def daftar():
    username = entry_username.get()
    password = entry_password.get()

    if username and password:
        data_pengguna[username] = password
        messagebox.showinfo("Sukses Daftar", "Pendaftaran berhasil untuk " + username)
        bersihkan_input()
    else:
        messagebox.showerror("Error", "kalau belum selesai sama masa lalu , silakan sembuh sendiri")

def masuk():
    username = entry_username.get()
    password = entry_password.get()

    if username in data_pengguna and data_pengguna[username] == password:
        messagebox.showinfo("Login Berhasil", "Selamat datang, " + username + "!")
        bersihkan_input()
    else:
        messagebox.showerror("Login Gagal", "Username atau password salah. Coba lagi, ya.")

def bersihkan_input():
    entry_username.delete(0, tk.END)
    entry_password.delete(0, tk.END)
root = tk.Tk()
root.title("Registrasi & Login Santai")

tk.Label(root, text="Username:").grid(row=0, column=0, padx=10, pady=5)
tk.Label(root, text="Password:").grid(row=1, column=0, padx=10, pady=5)

entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show="*")

entry_username.grid(row=0, column=1, padx=10, pady=5)
entry_password.grid(row=1, column=1, padx=10, pady=5)

tombol_daftar = tk.Button(root, text="Daftar", command=daftar)
tombol_masuk = tk.Button(root, text="Masuk", command=masuk)

tombol_daftar.grid(row=2, column=0, columnspan=2, pady=10)
tombol_masuk.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()
