import streamlit as st
def prin (): 
    st.title("Resumen del codigo hecho")
    st.markdown("Muchos tipos de rocas son expulsadas por un volcán al momento de la explosión (como obsidiana, lapilli, escoria, etc.). Estas rocas pueden medir de 2mm hasta 7mm aproximadamente. (Sieron, s.f.) Este proyecto se enfocará en el Popocatépetl. Los proyectiles lanzados por este volcán tienen angulos entre 40° y 90° (del Pozzo, 2017). Tiene una altura de 5426 m sobre el nivel del mar y una prominencia de 3800 m. (del Pozzo, 2017)")
    st.markdown("El rango de velocidad fue recuperado de un documento de la UNAM.")
    st.image("Tabla2.jpg",caption="Tabla de datos recuperados de videos de erupciones del Popocatéptl. Se utilizaron como parametro la velocidad mínima y máxima encontradas en esta tabla ubicada en la página 82. (del Pozzo, 2017)")
    st.markdown("En la primera parte del código se tienen que importar las librerias que se ocuparan y el nombre en el cual lo vas a exportar, por ejemplo numpy se exportó con el nombre de np. Numpy ayuda para escribir raices cuadradas, seno y coseno. Matplot podrá plasmar las gráficas necesarias.")
    st.image("imagen1.jpg")
    st.markdown("Se va a crear una función, la cuál falicitará hacer la gráfica más adelante. Lo que hace la función es convertir los grados a radianes, calcular la velocidad inicial en x, calcular la velocidad inicial en y, calcular la posición inicial en x y calcular la posición inicial en y.")
    st.latex(r"""v_{ox} = v_o\cos\theta""")
    st.latex(r"""v_{oy} = v_o\sin\theta""")
    st.latex(r"""r_{ox} = v_{ox}t""")
    st.latex(r"""r_{oy} = -4.9t^2+v_{oy}+y_{o}  """)
    st.image("imagen2.jpg")
    st.markdown("Se establecerá la variable de las posiciones igual a la función para mandarla llamar, y poder crear una gráfica correctamente.")
    st.image("imagen2_1.jpg")
    st.markdown("Toda la siguiente parte es el código para crear la gráfica, poner el titulo, una cuadricula y los limites de x y y.")
    st.image("imagen3.jpg")
    st.image("graf1.jpg",caption="Gráfica sin resistencia al aire")
    st.markdown("En la siguiente parte del código se establecen las variables que afectarán al proyectil en un caso de la vida real. Para saber las dimensiones de un balístico lanzado por el Popocatépetl, se hizo un análisis de fragmentos de proyectiles con mayor distancia del cráter. Fueron mandados a un laboratorio para calcular mejor los datos. (del Pozzo, 2017) ")
    st.image("Tabla1.jpg",caption="Tabla de características de balísticos del Popocatéptl localizada en la página 76.(del Pozzo, 2017)")
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


