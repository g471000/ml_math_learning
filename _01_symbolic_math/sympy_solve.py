from sympy import Symbol, solve


def solve_equation(equation):
    print(solve(equation))

def solve_equations(equaiton1, equation2):
    print(solve((equaiton1, equation2), dict=True))


if __name__ == '__main__':
    solve_equation('2 * x - 6')
    solve_equation('2 * k - 10')
    solve_equation('8 - (k / 2)')

    solve_equations('3 * x + y - 1', 'x - 2 * y - 3')


