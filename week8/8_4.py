#   Ноль или не ноль
"""
Проверьте, есть ли среди данных N чисел нули.
    Формат ввода
Вводится число N, а затем N чисел.
    Формат вывода
Выведите True, если среди введенных чисел есть хотя бы один нуль,
или False в противном случае.
"""
print(
    any(
        map(
            lambda x: x == 0,
            map(
                int,
                map(
                    lambda x: input(),
                    range(
                        int(input())
                    )
                )
            )
        )
    )
)
