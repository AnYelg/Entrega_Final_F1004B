import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

def prin ():
    st.title("Resultados del código")
    st.header("Gráficas")
    v_0 =250   
    theta_deg=45   
    y_0=3800        
    t=np.linspace(0,100, num=2000)

    def proyectile_no_drag(v_0, theta_deg, y_0, t, g = 9.81):
        theta_rads = np.radians(theta_deg)
        v_0x = v_0*np.cos(theta_rads)
        v_0y = v_0*np.sin(theta_rads)
        r_x=v_0x*t
        r_y=(-4.9*t**2)+(v_0y*t) + y_0
        
        return r_x,r_y

    r_x, r_y = proyectile_no_drag(v_0, theta_deg, y_0,t)

    fig = plt.figure(figsize=(15,4))
    plt.plot(r_x,r_y)
    plt.title("Trayectoria del Proyectil")
    plt.grid()
    plt.axis('scaled')
    x_ticks = plt.xticks(np.arange(0,9500,1000))
    y_ticks = plt.yticks(np.arange(0,5500,1000))
    x_limt = plt.xlim([0,9500])
    y_limt = plt.ylim([0,5500])
    st.pyplot(plt)
    r = 0.06/2 #radio del proyectil
    d=2300 #densidad del proyectil
    v= 4/3*np.pi*r**3 #volumen del proyectil
    m =d*v #masa del proyectil
    y_0=5426 #altura del volcán sobre el nivel del mar
    temp=20 #temperatura del ambiente
    rho = (348.42*(1-(y_0*0.000105)))/(273+temp) #densidad del aire
    A = np.pi*r**2 #área del proyectil
    C = (2*m*9.81)/(rho*A*(v_0**2)) #coeficiente de arrastre
    dt = 0.10 #delta t (tiempo)
    N = 1000 #número de iteraciones
    v_0 =250   #Velocidad inicial
    theta_deg=45 #Grados

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

    [x_list, y_list, v_list, v_x_list, v_y_list, a_x_list, a_y_list, t_list] =proyectile_with_drag(v_0, theta_deg, y_0, m, D, dt, N)

    fig = plt.figure(figsize=(20,7))
    plt.plot(r_x,r_y, label="Sin Resistencia de Aire")
    plt.plot(x_list,y_list, label="Con Resistencia de Aire")
    plt.grid()
    plt.axis('scaled')
    plt.title("Trayectoria con y sin resistencia de aire")
    plt.xlim([0,9500])
    plt.ylim([0,5500])
    _ = plt.xticks(np.arange(0,9500,500))
    _ = plt.yticks(np.arange(0,5500,500))
    _ = plt.legend()
    st.pyplot(plt)