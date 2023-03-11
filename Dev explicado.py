#Esto importa las bibliotecas necesarias para el código. SymPy se utiliza para la manipulación simbólica y el cálculo de derivadas.
#NumPy se utiliza para convertir las expresiones simbólicas en funciones de Python que se pueden graficar, y Matplotlib se utiliza para la visualización de datos
import sympy as sp
import numpy as np
import matplotlib.pyplot as plt

#Esta línea solicita al usuario que ingrese una función, y luego elimina cualquier espacio en blanco en la entrada para facilitar el análisis
f_str = input("Ingrese la función: ").replace(" ", "")
#Esta línea convierte la cadena que se ingresó en una expresión simbólica de SymPy que se puede manipula
f = sp.sympify(f_str)
#Esta línea solicita al usuario que ingrese el número de derivadas que desea calcular
n = int(input("Ingrese el número de derivada: "))

#Estas líneas calculan la n-ésima derivada de la función ingresada por el usuario utilizando la
#función diff de SymPy, que toma la derivada simbólica de una expresión
derivada = f
for i in range(n):
    derivada = sp.diff(derivada)
    #Esta línea imprime la n-ésima derivada calculada
print(f"La {n}-ésima derivada de {f} es {derivada}")

#Estas líneas crean una función de Python a partir de la expresión simbólica utilizando la función
#lambdify de SymPy y luego la evalúa en un conjunto de valores x. El resultado se almacena en la variable ys
x = sp.symbols('x')
f_lambdify = sp.lambdify(x, f, "numpy")
derivada_lambdify = sp.lambdify(x, derivada, "numpy")
xs = np.linspace(-10, 10, 500)
ys = f_lambdify(xs)

#Estas líneas grafican la función original y todas las derivadas hasta la n-ésima utilizando plt.plot de Matplotlib.
#La función original se grafica primero y se etiqueta con el nombre "Función original".
#Luego, en un bucle for, se calcula cada derivada, se convierte en una función de Python utilizando lambdify,
#se evalúa en los valores x y se agrega a la variable ys. El resultado se grafica y se etiqueta
#con el nombre de la derivada correspondiente. Por último, plt.legend() agrega una leyenda a la gráfica
#y plt.show() muestra la gráfica en una ventana
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
