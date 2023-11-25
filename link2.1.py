import os
import tkinter as tk
from tkinter import filedialog
import psutil

def scan_rtf_lnk_files(directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".rtf.lnk"):
                found_files.append(os.path.join(root, file))

    if not found_files:
        result_text.set("Не знайдено жодного файлу з розширенням .rtf.lnk.")
        return

    result_text.set(f"Знайдено {len(found_files)} файлів з розширенням .rtf.lnk:")
    for file_path in found_files:
        result_text.set(result_text.get() + '\n' + file_path)

def remove_rtf_lnk_files(directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".rtf.lnk"):
                found_files.append(os.path.join(root, file))

    if not found_files:
        result_text.set("Не знайдено жодного файлу з розширенням .rtf.lnk.")
        return

    result_text.set(f"Знайдено {len(found_files)} файлів з розширенням .rtf.lnk:")
    for file_path in found_files:
        result_text.set(result_text.get() + '\n' + file_path)

    confirmation = tk.messagebox.askquestion("Підтвердження", "Ви впевнені, що хочете видалити ці файли?")
    if confirmation == "yes":
        for file_path in found_files:
            try:
                os.remove(file_path)
                result_text.set(result_text.get() + f"\nФайл {file_path} видалено.")
            except Exception as e:
                result_text.set(result_text.get() + f"\nПомилка при видаленні файлу {file_path}: {e}")
    else:
        result_text.set(result_text.get() + "\nВидалення скасовано.")

def browse_directory():
    directory_to_scan = filedialog.askdirectory()
    directory_var.set(directory_to_scan)

def check_powershell_process():
    # Перевіряємо процеси та перевіряємо наявність powershell.exe
    for process in psutil.process_iter(['pid', 'name']):
        if process.info['name'] == 'powershell.exe':
            tk.messagebox.showinfo("Попередження", "powershell.exe запущено. Необхідно перевірити більш детально.")

# Створення основного вікна
root = tk.Tk()
root.title("link remover")

# Інтерфейс
directory_var = tk.StringVar()
directory_label = tk.Label(root, text="Оберіть папку для сканування:")
directory_label.pack(pady=10)

directory_entry = tk.Entry(root, textvariable=directory_var, width=40)
directory_entry.pack(pady=10)

browse_button = tk.Button(root, text="Обрати папку", command=browse_directory)
browse_button.pack(pady=10)

scan_button = tk.Button(root, text="Сканувати", command=lambda: [scan_rtf_lnk_files(directory_var.get()), check_powershell_process()])
scan_button.pack(pady=10)

remove_button = tk.Button(root, text="Видалити", command=lambda: remove_rtf_lnk_files(directory_var.get()))
remove_button.pack(pady=10)

result_text = tk.StringVar()
result_label = tk.Label(root, textvariable=result_text)
result_label.pack(pady=10)

# Додавання тексту вверху програми
header_label = tk.Label(root, text="link remover")
header_label.pack(side=tk.TOP)

# Додавання тексту внизу програми
footer_label = tk.Label(root, text="146 ОРВП / ПВЗ © romko.bilinskyi@gmail.com")
footer_label.pack(side=tk.BOTTOM)

# Запуск головного циклу подій
root.mainloop()
