# quadratic_solver.py

from sympy import symbols, Eq, solve

def solve_quadratic(a, b, c):
    x = symbols('x')
    equation = Eq(a*x**2 + b*x + c, 0)
    solutions = solve(equation, x)
    return solutions

if __name__ == "__main__":
    a = float(input("Введите коэффициент a: "))
    b = float(input("Введите коэффициент b: "))
    c = float(input("Введите коэффициент c: "))
    
    solutions = solve_quadratic(a, b, c)
    print(f"Корни уравнения: {solutions}")
