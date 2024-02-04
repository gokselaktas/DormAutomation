import tkinter as tk
from tkinter import ttk

# Create the main window
root = tk.Tk()
root.title("Öğrenci Kayıt")

# Create a frame for padding
frame = tk.Frame(root, padx=10, pady=10)
frame.pack(padx=10, pady=10)

# Add labels and entry widgets for each field
labels = ['Öğrenci Adı:', 'Öğrenci Soyadı:', 'TC:', 'Telefon:', 'Doğum Tarihi:', 'Öğrenci Bölüm:', 'Mail:', 'Oda No:', 'Veli Ad Soyad:', 'Veli Telefon:', 'Adres:']
for i, text in enumerate(labels):
    label = tk.Label(frame, text=text)
    label.grid(row=i, column=0, sticky="W")
    if text in ['Öğrenci Bölüm:', 'Oda No:']:  # Dropdowns
        entry = ttk.Combobox(frame)
    else:
        entry = tk.Entry(frame)
    entry.grid(row=i, column=1, pady=2, sticky="WE")

# Add save button
save_button = tk.Button(frame, text="Kaydet", command=lambda: print("Save button clicked!"))
save_button.grid(row=len(labels), column=1, pady=10, sticky="E")

# Run the application
root.mainloop()
