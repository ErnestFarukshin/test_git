"""Учебный калькулятор: демонстрация для пары по Git."""

VERSION = "1.0"


def add(a, b):
    """Возвращает сумму a и b."""
    return a + b


def sub(a, b):
    """Возвращает разность a и b."""
    return b - a  # TODO: кажется, здесь ошибка


def main():
    print(f"Калькулятор, версия {VERSION}")
    while True:
        print()
        print("Выберите операцию:")
        print("  1) add — сложение")
        print("  2) sub — вычитание")
        print("  0) выход")
        choice = input("> ").strip()
        if choice == "0":
            print("До встречи!")
            break
        if choice not in ("1", "2"):
            print("Неизвестная операция, попробуйте ещё раз.")
            continue
        a = float(input("Введите a: "))
        b = float(input("Введите b: "))
        if choice == "1":
            print("Результат:", add(a, b))
        else:
            print("Результат:", sub(a, b))


if __name__ == "__main__":
    main()
