import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

f_str = input("Ingrese la función: ").replace(" ", "")
f = sp.sympify(f_str)
n = int(input("Ingrese el número de derivada: "))


derivada = f
for i in range(n):
    derivada = sp.diff(derivada)
print(f"La {n}-ésima derivada de {f} es {derivada}")

x = sp.symbols('x')
f_lambdify = sp.lambdify(x, f, "numpy")
derivada_lambdify = sp.lambdify(x, derivada, "numpy")
xs = np.linspace(-10, 10, 500)
ys = f_lambdify(xs)

plt.plot(xs, ys, label="Función original")
for i in range(n):
    derivada_i = derivada
    for j in range(i):
        derivada_i = sp.diff(derivada_i)
    derivada_i_lambdify = sp.lambdify(x, derivada_i, "numpy")
    ys += derivada_i_lambdify(xs)
    plt.plot(xs, ys, label=f"{i+1}-ésima derivada")
    
plt.legend()
plt.show()
