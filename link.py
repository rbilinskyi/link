import os

def scan_and_remove_rtf_lnk_files(directory):
    found_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith(".rtf.lnk"):
                found_files.append(os.path.join(root, file))

    if not found_files:
        print("Не знайдено жодного файлу з розширенням .rtf.lnk.")
        return

    print(f"Знайдено {len(found_files)} файлів з розширенням .rtf.lnk:")
    for file_path in found_files:
        print(file_path)

    confirmation = input("Ви впевнені, що хочете видалити ці файли? (Так/Ні): ").lower()
    if confirmation == "так":
        for file_path in found_files:
            try:
                os.remove(file_path)
                print(f"Файл {file_path} видалено.")
            except Exception as e:
                print(f"Помилка при видаленні файлу {file_path}: {e}")
    else:
        print("Видалення скасовано.")

# Введіть шлях до папки, яку ви хочете просканувати та очистити
directory_to_scan = input("Введіть шлях до папки: ")

# Почнемо сканування та видалення файлів
scan_and_remove_rtf_lnk_files(directory_to_scan)