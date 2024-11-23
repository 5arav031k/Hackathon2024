from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os


def upload():
    gauth = GoogleAuth()

    # Спробуємо завантажити збережені токени
    gauth.LoadCredentialsFile("credentials.json")

    # Якщо токени не знайдені або вони не валідні, запускаємо процес авторизації
    if not gauth.credentials:
        gauth.LocalWebserverAuth()  # Цей крок відкриває браузер для авторизації
    elif gauth.access_token_expired:
        gauth.Refresh()  # Оновлюємо токен, якщо він застарів
    else:
        gauth.Authorize()

    # Зберігаємо токени для подальших сесій
    gauth.SaveCredentialsFile("credentials.json")

    # Після авторизації ініціалізуємо PyDrive
    drive = GoogleDrive(gauth)

    folder_path = 'datasets'

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Перевіряємо, чи це файл (а не папка)
        if os.path.isfile(file_path):
            print(f"Завантаження файлу: {filename}")

            # Створення файлу на Google Диску з ім'ям 'filename'
            file_drive = drive.CreateFile({'title': filename})

            # Завантажуємо вміст локального файлу на Google Диск
            file_drive.SetContentFile(file_path)

            # Завантажуємо файл на Google Диск
            file_drive.Upload()

            print(f"Файл {filename} успішно завантажено на Google Диск!")


if __name__ == '__main__':
    upload()
