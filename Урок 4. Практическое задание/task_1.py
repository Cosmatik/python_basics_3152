"""
1. Реализовать скрипт, в котором должна быть предусмотрена функция
расчета заработной платы сотрудника. В расчете необходимо использовать формулу:
(выработка в часах*ставка в час) + премия.

Для выполнения расчета для конкретных значений
необходимо запускать скрипт с параметрами.
"""

def calculate_salary(hours_worked, hourly_rate, bonus):
    """Функция расчёта заработной платы сотрудника."""
    salary = (hours_worked * hourly_rate) + bonus
    return salary

# Пример использования функции:
result = calculate_salary(hours_worked=160, hourly_rate=100, bonus=5000)
print("Заработная плата сотрудника: ", result)