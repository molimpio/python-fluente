"""
Números Primos
Para um número ser primo ele deve atender as regras:
1) Maior do que 1
2) Divisível apenas por 1 e Divisível apenas por ele mesmo

Encontre os numeros primos menor que 100
"""

numbers_primos = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41,
    43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
]
numbers_not_primos = [n for n in range(2, 100) if n not in numbers_primos]

qty_dividers = lambda number: len([n for n in range(1, 100) if (number % n) == 0])


def check_primo(number):
    return False if number < 1 else qty_dividers(number) == 2


if __name__ == '__main__':
    assert all(check_primo(n) for n in numbers_primos)
    assert not all(check_primo(n) for n in numbers_not_primos)
