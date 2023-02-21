from sympy import Symbol, solve


def solve_equation(equation):
    print(solve(equation))


if __name__ == '__main__':
    solve_equation('2 * x - 6')
    solve_equation('2 * k - 10')
    solve_equation('8 - (k / 2)')


