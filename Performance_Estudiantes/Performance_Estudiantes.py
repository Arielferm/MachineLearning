# -*- coding: utf-8 -*-
"""1_PerformanceEstudiantes.ipynb

## PERFORMANCE DE ESTUDIANTES: CARGANDO BASES DE DATOS Y ANALIZANDOLAS

En este proyecto se cargará una base de datos que contiene información sobre el rendimiento académico de un conjunto de estudiantes, junto con otra información de los mismos, como las horas de sueño, su rendimiento anterior, etc. Partiendo de esta base analizaremos su contenido mediante parámetros estadísticos y diferentes gráficos, de manera de realizar una práctica en Python sobre dichos análisis de datos.
"""

# Empezaremos importando los módulos que necesitaremos:
# Pandas para el manejo de DataFrames (tablas), numpy para el análisis matemático y estadístico, y matplotlib para realizar gráficos:
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Permito que este cuadernillo entre a mis archivos en Google Drive:
from google.colab import drive

#Por las dudas que ya se haya ejecutado este bloque borro todos los cambios:
drive.flush_and_unmount()

#el módulo drive nos permite acceder a nuestros archivos de Google Drive mediante la función mount:
drive.mount('/content/drive')

# A continuación procedemos a leer una base de datos de un archivo de extension csv, mediante la función read_csv, del módulo pandas:
data = pd.read_csv("/content/drive/MyDrive/ML/Student_Performance.csv")

# Como vimos en ejemplos anteriores, los DataFrame tienen una función head que les permite mostrar los primeros 5
# elementos. Si quisiéramos ver más filas, podemos hacerlo enviándole a la función la cantidad de filas que queremos
# ver como parámetro. Por ejemplo data.head(10) nos mostrará las primeras 10 filas.

data.head()

"""De la misma manera que tenemos la función head(), Pandas nos ofrece una gran cantidad de funciones en sus DataFrames. **Info** nos da una explicación del nombre y tamaño de cada columna, **Shape** nos muestra cuántas filas y columnas tiene el DF, y **Describe** nos entrega algunos valores estadísticos del DF. Veamos estas funciones y su comportamiento cuando las ejecutamos:"""

# Shape: Dimensiones del DF:

data.shape

#Describe: conjunto de valores estadísticos: Suma, valor medio, estándar, valor mínimo, máximo y percentiles:

data.describe()

"""A continuación crearemos nuestra primer función. Una función es un bloque de código que llamaremos varias veces a lo largo de nuestro código. Utilizaremos la palabra reservada **def** para darle un nombre a nuestra función, y le daremos un nombre a los parámetros que utilizaremos a lo largo de dicha función. Estos parámetros luego tomarán un valor cuando invoquemos la función. Por ejemplo, en este caso, definiremos la función **box_plot**, en la que realizaremos un gráfico, y en donde el eje x y el eje y se los pasaremos como parámetros cada vez que invoquemos a dicha función. En este caso realizaremos un gráfico **catplot**, que a diferencia del boxplot que vimos anteriormente relaciona 2 datos distintos, uno en el eje x y otro en el eje y. Para realizar dicho gráfico importaremos el módulo **seaborn**"""

# create function that visualized numeric columns using box plot
import seaborn as sns

def box_plot(x_axis = None, y_axis = None, hue = None, col = None):
    """
    parámetros : x_axis, y_axis y hue column, column data type must be numeric in y_axis
    """
    sns.catplot(x = x_axis, y = y_axis, data = data, hue = hue, kind = "box", col = col, palette='pastel', legend=False)
    plt.xlabel(x_axis)
    plt.ylabel(y_axis)
    plt.show()

"""## Visualización de variables en una Base de datos

Veremos ahora como podemos invocar a nuestra función, para intentar relacionar la performance de los estudiantes con la cantidad de horas de estudio. Veamos el gráfico e intentemos sacar conclusiones:
"""

# What is "Hours Studied" and "Performance Index" distribution

box_plot(x_axis = "Hours Studied", y_axis = "Performance Index", hue="Hours Studied") # call function i create it in cell 11

"""Como podemos ver en el gráfico anterior, parecería haber una relación lineal: A mayor cantidad de horas de estudio, mayor performance por parte de los estudiantes, tanto en valores mínimos, máximos como en promedio.

Veamos ahora si también hay una relación entre las actividades extracurriculares de los estudiantes y su performance:
"""

# What is "	Extracurricular Activities" and "Performance Index" distribution

box_plot(x_axis = "Extracurricular Activities", y_axis = "Performance Index", hue="Extracurricular Activities") # call function i create it in cell 11

"""Como vemos esta vez, el gráfico no muestra una correlación entre estos dos parámetros. ¿Qué parámetros influirán a la hora de mejorar la performance de los estudiantes, y cuáles no?

### EJERCICIO 1. Realizar los graficos BoxPlot que analicen la Performance del alumno en función de las horas de sueño. Saque conclusiones.
"""

box_plot(x_axis = "Sleep Hours", y_axis = "Performance Index", hue = "Sleep Hours")

"""El grafico mide las horas de sueño vs. el índice de performance de los estudiantes, donde se observa que casi no influye en la nota del estudiante. Esto permite deducir que, para el estudio, la cantidad de horas de sueño es información poco relevante.

### EJERCICIO 2. Realizar los graficos BoxPlot que analicen la Performance del alumno en función de las resultados Previos. Saque conclusiones.
"""

box_plot(x_axis = "Hours Studied", y_axis = "Performance Index", hue = "Hours Studied")

box_plot(x_axis = "Extracurricular Activities", y_axis = "Performance Index", hue = "Extracurricular Activities")

"""En el grafico donde se mide las horas de estudio vs. el índice de performance de los estudiantes, se observa que, cuantas más horas estudio es mejor la nota del estudiante. Esto permite predecir la nota del estudiante, según la cantidad de horas de estudio como información relevante. También se deduce que el gráfico de actividades extracurriculares vs. Índice de performance, las actividades extracurriculares son información irrelevante para este estudio.

### Matriz de Correlación

La correlación de 2 elementos indica la incidencia que tiene un elemento sobre otro. También puede verse como un factor que indica si las tendencias de 2 variables son similares (crecen al mismo ritmo), inversas (una crece a medida que otra decrece), o bien no tienen correlación.

La matriz de correlación es un gráfico que nos permite analizar este indicador para todos los elementos de un dataframe. En cada fila tendremos una columna distinta del DF y en cada columna también. Donde se crucen las mismas variables veremos una correlación absoluta, indicada por el número 1, ya que se trata de la misma variable. Una correlación cercana a 0 indica que no hay correlación, o que la misma es inversa, mientras que una correlación cercada a 1 muestra una gran correlación entre los elementos. Veamos el gráfico:
"""

# first visualize correlation matrix between numerical columns
data=data.drop(columns="Extracurricular Activities")
plt.figure(figsize = (10,6))
sns.heatmap(data.corr(), annot = True, fmt = ".2f", linewidths = 0.2)
plt.show()

"""### EJERCICIO 3. Describir la matriz de correlación. ¿Que columnas eliminaría?

La matriz de correlación cuan correlacionada o relevantes esta una información con la otra. Eliminaría las columnas de horas de sueño y cuestionarios de practica por ser poca relevantes.
"""
