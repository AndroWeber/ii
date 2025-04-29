import os

def list_external_drives():
    drives = []
    try:
        if os.name == "nt":  # Для Windows
            import string
            drives = [f"{d}:\\" for d in string.ascii_uppercase if os.path.exists(f"{d}:\\")]
        elif os.name == "posix":  # Для macOS/Linux
            drives = [os.path.join("/media", user, folder) for user in os.listdir("/media") for folder in os.listdir(os.path.join("/media", user))]
    except Exception as e:
        print(f"Ошибка при поиске дисков: {e}")
    return drives

if __name__ == "__main__":
    external_drives = list_external_drives()
    print("Найденные диски:", external_drives)