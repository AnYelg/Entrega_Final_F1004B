import streamlit as st
def prin (): 
    st.title("Resumen del codigo hecho")
    st.markdown("Para los datos que han sido capturados, se utilizó estimados de la información recuperada en distintas fuentes. Se utilizó como altura 5426, que es la altura de el Popocatépetl sobre el nivel del mar. En la posición incial en y, se utilizá 3800, que es la prominencia del volcán. (del Pozzo, 2017)")
    st.markdown("En la primera parte del código se tienen que importar las librerias que se ocuparan y el nombre en el cual lo vas a exportar, por ejemplo numpy lo exporte con el nombre de np. Numpy ayuda para escribir raices cuadradas, seno y coseno. Matplot podrá hacer las gráficas necesarias. ")
    st.image("imagen1.jpg")
    st.markdown("Vamos a crear una función, la cual nos falicitará hacer la gráfica más adelante. Lo que hace la función es convertir los grados a radianes, calcular la velocidad inicial en x, calcular la velocidad inicial en y, calcular la posición inicial en x y calcular la posición inicial en y.")
    st.latex(r"""v_{ox} = v_o\cos\theta""")
    st.latex(r"""v_{oy} = v_o\sin\theta""")
    st.latex(r"""r_{ox} = v_{ox}t""")
    st.latex(r"""r_{oy} = -4.9t^2+v_{oy}+y_{o}  """)
    st.image("imagen2.jpg")
    st.markdown("Luego dirás que tu variable r_x, r_y es igual a la función de arriba, para que cuando hagas la gráfica sea más facil que te den los resultados.")
    st.image("imagen2_1.jpg")
    st.markdown("Toda la siguiente parte es el código para crear la gráfica, poner el titulo, una cuadricula y los limites de x y y.")
    st.image("imagen3.jpg")
    st.image("graf1.jpg",caption="Gráfica sin resistencia al aire")
    st.markdown("Aquí meteremos otras variables para hacer la gráfica con resistencia al aire. Las ecuaciones para calcular la densidad del aire, el coeficiente de arrastre, la estimación de la temperatura del volcán en una erupción se obtuvieron en la monografía escrita por Martín Del Pozzo. La densidad del proyectil se obtuvo en el artículo de Diana Rodriguez, Gustavo Córdoba y Antonio Costa.")
    st.image("imagen4.jpg")
    st.markdown("Vamos a definir D, que es la contante de la resitencia al aire. La equación es la siguiente:")
    st.latex(r"""D = \frac{\rho \cdot C\cdot A}{2} """ )
    st.markdown(r"""
    Volveremos a crear una función que nos ayudará a calcular los valores necesarios para hacer la gráfica con resistencia al aire. 
    
    1. Convertir los grados a radianes.   
    2. Calcular la velocidad inicial en x. $v_{ox} = v_o\cos\theta$   
    3. Calcular la velocidad inicial en y. $v_{oy} = v_o\sin\theta$    
    4. Establecer el tiempo inicial como 0 y crear una lista donde guardar todos los valores de t.
    5. Cambiar los nombres de la velocidad inicial, la velocidad inicial en x y la velocidad inicial en y, y como en el tiempo crear una lista donde guardar los valores obtenidos.
    6. Repetir la siguiente parte N número de veces para sacar los datos. (En este caso N=100)
    7. Establecer la posicion x en 0 y y en 3800 y creamos la lista.
    8. Calcular las velocidades para y y x $\vec{v}(t+\Delta t) = \vec{v}+\vec{a}\Delta t$   Agregar los valores a la lista
    9. Calcular las posiciones para y y x $\vec{s}(t+\Delta t) = \vec{s}+\vec{v}\Delta t+\frac{1}{2}\vec{a}\Delta t^2$   Agregar los valores a la lista
    10. Calcular la aceleración en x considerando el drag $a_x(t+\Delta t) = -\frac{D}{m}vv_x$   Agregar los valores a la lista
    11. Calcular la aceleración en y considerando el drag $a_y(t+\Delta t)= -g-Dvv_y$   Agregar los valores a la lista
    12. Cambiar el valor de las variables para continuar el loop con los nuevos valores obtenidos.""")
    st.image("imagen5_1.jpg")
    st.image("imagen5_2.jpg")
    st.markdown("Marcar que los valores de las listas es igual a la función para gráficarlo.")
    st.image("imagen6.jpg")
    st.markdown("Crear la gráfica de resistencia al aire y sin resistencia al aire.")
    st.image("imagen7.jpg")
    st.image("graf2.jpg",caption="Gráfica con y sin resistencia al aire")
    st.header("Referencias")
    st.markdown(r"""
    Alatorre, M.A. , Delgado Granados, H., Abimelec Farraz. I. (s.f.) Mapa de Peligros por Caída de Productos Balísticos del Volcán Popocatépetl [Sitio web] Recuperado de: http://sgpwe.izt.uam.mx/pages/cbi/ruth/MecanicaElementalI/practicas/balisticos.pdf

    Del Pozzo, M. (2017) Estudios geológicos y actualización del mapa de peligros del volcán Popocatépetl. UNAM. UNAM: México. [Sitio web] Recuperado de: http://www.geofisica.unam.mx/assets/monografias22.pdf

    Rodriguez,D., Córdoba, G., Antonio Costa (2018) Análisis de la amenaza por proyectiles balísticos en el área de
    influencia del volcán galeras [Sitio web] Recuperado de:https://app.ingemmet.gob.pe/biblioteca/pdf/FIVI-2018-51.pdf

    Sieron, K. (s.f.) Volcanismo [Sitio Web] Recuperado de: https://www.uv.mx/apps/vulcanismo/  """)


