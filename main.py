from datetime import datetime
import random
import re


# 1. Функція для обчислення кількості днів від заданої дати до сьогодні
def get_days_from_today(date):
    try:
        # Перетворення рядка у дату
        given_date = datetime.strptime(date, "%Y-%m-%d").date()

        # Поточна дата
        today = datetime.today().date()

        # Різниця між датами
        delta = today - given_date

        return delta.days

    except ValueError:
        return "Неправильний формат дати! Використовуйте YYYY-MM-DD"


# Приклад використання
print(get_days_from_today("2021-10-09"))


# 2. Функція генерації унікальних випадкових чисел
def get_numbers_ticket(min, max, quantity):
    # Перевірка коректності параметрів
    if (
        min < 1
        or max > 1000
        or quantity < 1
        or quantity > (max - min + 1)
        or min > max
    ):
        return []

    # Генерація унікальних чисел
    numbers = random.sample(range(min, max + 1), quantity)

    # Повертаємо відсортований список
    return sorted(numbers)


# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# 3. Функція нормалізації телефонних номерів
def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та "+"
    cleaned_number = re.sub(r"[^\d+]", "", phone_number)

    # Якщо номер починається з "+"
    if cleaned_number.startswith("+"):
        return cleaned_number

    # Якщо номер починається з "380"
    if cleaned_number.startswith("380"):
        return "+" + cleaned_number

    # Якщо номер без коду країни
    return "+38" + cleaned_number


# Приклад використання
raw_numbers = [
    "067\t123 4567",
    "(095) 234-5678\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]

print("Нормалізовані номери:")
print(sanitized_numbers)