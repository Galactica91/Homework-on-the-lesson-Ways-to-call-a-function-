def get_password(n):
    result = ""
    used_numbers = set()
    for i in range(1, n):
        for j in range(i + 1, n + 1):
            if (i + j) % n == 0 and i not in used_numbers and j not in used_numbers:
                result += str(i) + str(j)
                used_numbers.add(i)
                used_numbers.add(j)
    return result

n = int(input("Введите число (от 3 до 20): "))
if 3 <= n <= 20:
    password = get_password(n)
    print("Пароль:", password)
else:
    print("Некорректный ввод. Число должно быть от 3 до 20.")
