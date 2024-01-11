import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

df = pd.read_csv("employees.csv")

st.title('EMPLEATRONIX')

st.write('Todos los datos sobre los empleados en una aplicación')
st.write(df)
st.divider()
col1, col2, col3 = st.columns(3)

with col1:
    color = st.color_picker('Selecciona un color', '#3475B3')

with col2:
    nombre = st.toggle('Mostrar el nombre')

with col3:
    sueldo = st.toggle('Mostrar el sueldo en la barra')

with st.container():
    if not df.empty:
        sns.set_style("white")
        plt.figure(figsize=(10, 8))
        plot = sns.barplot(x="salary", y="full name", data=df, color=color)

        if nombre:
            # Mostrar el full name de la gráfica:
            plt.yticks(df.index, df['full name'], fontsize=10)
        else:
            # Ocultar el full name de la gráfica:
            plt.yticks([])

        if sueldo:
            for i in range(len(df)):
                plt.text(df.salary[i], i, df.salary[i], ha='left', va='center', color='black', fontsize=10)
                print(i, df.salary[i])

        # Invierte todos los resultados del eje y:
        plt.gca().invert_yaxis()

        # sin etiquetas
        plt.xlabel('')
        plt.ylabel('')
        plt.title("Salario de empleados")

        plt.grid(axis='x', linestyle='-')

        plt.xlim(0, 4500)
        plt.show()
        st.pyplot(plot.get_figure())
