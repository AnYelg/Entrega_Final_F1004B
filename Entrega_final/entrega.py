import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def prin():
    st.title("Simulador del Volcán")
    diamet = st.slider("Diametro del proyectil",0.2,0.6,0.6 )
    densidad = st.slider("Densidad del proyectil", 2100,2600,2300)
    temperatura = st.slider("Temperatura del ambiente",0,50,21)
    velocidad_in = st.slider("Velocidad Inicial",110,250)
    grados = st.slider ("Grados", 40,90,45)
    tiempo_v = st.slider ("Tiempo de vuelo", 0.0 , 10.0, 0.5)


    v_0 = velocidad_in   #Velocidad inicial
    theta_deg= grados   #Grados
    y_0=3800        #posicion inicial en y
    t=np.linspace(0,100, num=2000) #Tiempo, primero es el rango del tiempo y num es cuantas divisiones se hacen entre 0 y 5

    def proyectile_no_drag(v_0, theta_deg, y_0, t, g = 9.81):
        theta_rads = np.radians(theta_deg)
        v_0x = v_0*np.cos(theta_rads)
        v_0y = v_0*np.sin(theta_rads)
        r_x=v_0x*t
        r_y=(-4.9*t**2)+(v_0y*t) + y_0
        
        return r_x,r_y


    r_x, r_y = proyectile_no_drag(v_0, theta_deg, y_0,t)

    

    max_x = np.amax(r_x)
    max_y = (np.amax(r_y) + 500)

    fig = plt.figure(figsize=(15,4))
    plt.plot(r_x,r_y)
    plt.title("Trayectoria del Proyectil")
    plt.grid()
    plt.axis('scaled')
    _ = plt.xticks(np.arange(0,max_x,500))
    _ = plt.yticks(np.arange(0,max_y,500))
    _ = plt.xlim([0,max_x])
    _ = plt.ylim([0,max_y])


    r = (diamet/2) #radio del proyectil
    d = densidad #densidad del proyectil
    v = 4/3*np.pi*r**3 #volumen del proyectil
    m = d*v #masa del proyectil
    y_0 = 5426 #altura del volcán sobre el nivel del mar
    temp = temperatura #temperatura del ambiente
    rho = (348.42*(1-(y_0*0.000105)))/(273+temp) #densidad del aire
    A = np.pi*r**2 #área del proyectil
    C = (2*m*9.81)/(rho*A*(v_0**2)) #coeficiente de arrastre
    dt = tiempo_v #delta t (tiempo)
    N = 1000 #número de iteraciones
    v_0 = velocidad_in   #Velocidad inicial
    theta_deg = grados  #Grados

    D=((rho)*(C)*(A))/2 

    def proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N, g=9.81):
        theta_rads = np.radians(theta_deg)
        v_0x = v_0*np.cos(theta_rads)
        v_0y = v_0*np.sin(theta_rads)
        
        this_t = 0
        t_list = [this_t]

        v = v_0
        v_x = v_0x
        v_y = v_0y

        v_list = [v]
        v_x_list = [v_0x]
        v_y_list = [v_0y]

        x = 0
        y = 3800

        x_list = [x]
        y_list = [y]

        
        a_x = (-D/m)*(v)*(v_x)
        a_y = -g-D/m*(v)*(v_y)

        a_x_list = [a_x]
        a_y_list = [a_y]
        
        for i in range(N):
            v_x_next = (v_x)+(a_x*dt)
            v_y_next = (v_y)+(a_y*dt)
            v_next = np.sqrt((v_x_next**2)+(v_y_next**2))

            v_list.append(v_next)
            v_x_list.append(v_x_next)
            v_y_list.append(v_y_next)

            x_next = x+(v_x*dt)+((1/2)*(a_x)*(dt**2))
            y_next = y+(v_y*dt)+((1/2)*(a_y)*(dt**2))
    
            x_list.append(x_next)
            y_list.append(y_next)

        
            a_x_next = (-D/m)*(v)*(v_x_next)
            a_y_next = -g-D/m*(v)*(v_y_next)

            a_x_list.append(a_x_next)
            a_y_list.append(a_y_next)

            
            v_x = v_x_next
            v_y = v_y_next
            v = v_next

            x = x_next
            y = y_next

            a_x = a_x_next
            a_y = a_y_next

            this_t += dt
            t_list.append(this_t)
            
        return x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list

    [x_list, y_list, v_list, v_x_list, 
    v_y_list, a_x_list, a_y_list, t_list] =proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N)

    max_y_list = np.amax(y_list)


    for i in (y_list):
        if i<0:
            b=y_list.index (i)
            break
    
    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")
    plt.plot(x_list,y_list, label="Con Resistencia de Aire")
    plt.axis('scaled')
    plt.title("Trayectoria con y sin resistencia de aire")
    plt.xlim([0, max_x])
    plt.ylim([0,max_y])
    _ = plt.xticks(np.arange(0,max_x,1000))
    _ = plt.yticks(np.arange(0,max_y,1000))
    _ = plt.legend()
    st.pyplot(plt)
    max_y = np.amax(r_y)
    st.write("La altura máxima del proyectil sin resistencia al aire es:","{0:.2f}".format(max_y),"m")
    st.write("La altura máxima del proyectil con resistencia al aire es:","{0:.2f}".format(max_y_list),"m")
    st.write("La distancia que llegó el proyectil con resistencia al aire al tocar el suelo es:","{0:.2f}".format(x_list[b]),"m")

    
