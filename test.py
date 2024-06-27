import platform
import datetime
import os

# Визначення операційної системи
os_name = platform.system()

# Визначення поточної дати і часу
current_datetime = datetime.datetime.now()

# Визначення імені користувача
user_name = os.getlogin()

# Вивід інформації
print(f"Операційна система: {os_name}")
print(f"Поточна дата і час: {current_datetime}")
print(f"Ім'я користувача: {user_name}")

