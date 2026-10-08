"""Учебный калькулятор: демонстрация для пары по Git."""

VERSION = "1.2"


def add(a, b):
    """Возвращает сумму a и b."""
    return a + b


def sub(a, b):
    """Возвращает разность a и b."""
    return a - b  # исправлено: раньше возвращали b - a


def mul(a, b):
    """Возвращает произведение a и b."""
    return a * b


def div(a, b):
    """Возвращает частное a и b."""
    if b == 0:
        raise ValueError("На ноль делить нельзя!")
    return a / b

def pow(a, b):
    return a ^ b


def main():
    print(f"Калькулятор, версия {VERSION}")
    while True:
        print()
        print("Выберите операцию:")
        print("  1) add — сложение")
        print("  2) sub — вычитание")
        print("  3) mul — умножение")
        print("  4) div — деление")
        print("  5) pow — степень")
        print("  0) выход")
        choice = input("> ").strip()
        if choice == "0":
            print("До встречи!")
            break
        if choice not in ("1", "2", "3", "4"):
            print("Неизвестная операция, попробуйте ещё раз.")
            continue
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        if choice == "1":
            print("Результат:", add(a, b))
        elif choice == "2":
            print("Результат:", sub(a, b))
        elif choice == "3":
            print("Результат:", mul(a, b))
        elif choice == "4":
            print("Результат:", div(a, b))
        else
            print("Результат:", pow_(a, b))


if __name__ == "__main__":
    main()
