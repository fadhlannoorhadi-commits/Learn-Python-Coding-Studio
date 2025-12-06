# Error handling
import tkinter as tk
from tkinter import messagebox #untuk popup error

window=tk.Tk()
window.title("my applicatioon")
window.geometry("400x300")

def hitung_pembagian():
    try:
        angka1 = float(entry1.get())
        angka2 = float(entry2.get())

        hasil = angka1/angka2
        label_hasil.config(text=f"hasil: {hasil}", foreground = "green")

    except ValueError:
        messagebox.showerror("input salah", "harap masukkan angka yang valid")
        label_hasil.config(text = "")
    except ZeroDivisionError:
        messagebox.showerror("kesalahan matematis", "tidak bisa membagi dengan nol")
        label_hasil.config(text = "")


# label
tk.Label(window, text = "masukkan angka pertama").pack(pady = 10)
entry1 = tk.Entry(window, width=20)
entry1.pack(pady = 5)

label_hasil=tk.Label(window, text ="")
label_hasil.pack(pady=10)

tk.Label(window, text = "masukkan angka kedua").pack(pady = 10)
entry2 = tk.Entry(window, width=20)
entry2.pack(pady = 5)


# tombol hitung
tombol = tk.Button(window, text ="hitung", command=hitung_pembagian)
tombol.pack(pady=10)


window.mainloop()