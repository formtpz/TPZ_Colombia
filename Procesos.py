# ----- Librerías ---- #

import streamlit as st
import Historial, Capacitacion, Otros_Registros, Bonos, Salir, FMI, Consulta_Campo

# ----- Procesos 1 ---- #

def Procesos1(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False: 

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        procesos_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        fmi_2 = placeholder8_2.button("Folios de Matricula Inmobiliaria",key="fmi_2")

        placeholder9_2 = st.empty()
        consulta_campo_2 = placeholder9_2.button("Consultas de Campo",key="consulta_campo_2")

        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos ---- #

        elif bonos_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Ingreso= False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- FMI ---- #

        elif fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)

        # ----- Consultas de Campo ---- #

        elif consultas_campo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Consulta_Campo=True
            Consulta_Campo.Consulta_Campo(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.FMI==True:
            FMI.FMI(usuario,puesto)

        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)
            
# ----- Procesos 2 ---- #

def Procesos2(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False:

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        cc_conformacion_2 = placeholder8_2.button("Control de Calidad Conformación",key="cc_conformacion_2")

        placeholder9_2 = st.empty()
        cc_ifi_2 = placeholder9_2.button("Control de Calidad IF I",key="cc_ifi_2")

        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos ---- #

        elif bonos_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Ingreso = False
            st.session_state.Procesos=True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- Control de Calidad Conformación ---- #

        elif cc_conformacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_Conformacion=True
            Conformacion.CC_Conformacion(usuario,puesto)

        # ----- Control de Calidad IF I ---- #

        elif cc_ifi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.CC_IFI=True
            CC_IFI.CC_IFI(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.CC_Conformacion==True:
            CC_Conformacion.CC_Conformacion(usuario,puesto)

        elif st.session_state.CC_IFI==True:
            CC_IFI.CC_IFI(usuario,puesto)
        
# ----- Procesos 3 ---- #

def Procesos3(usuario,puesto):

    st.session_state.Ingreso=True

    if st.session_state.Procesos==False:

        placeholder1_2= st.sidebar.empty()
        titulo= placeholder1_2.title("Menú")

        placeholder2_2= st.sidebar.empty()
        historial_2 = placeholder2_2.button("Historial",key="historial_2")

        placeholder3_2 = st.sidebar.empty()
        capacitacion_2 = placeholder3_2.button("Capacitaciones",key="capacitacion_2")

        placeholder4_2 = st.sidebar.empty()
        otros_registros_2 = placeholder4_2.button("Otros Registros",key="otros_registros_2")

        placeholder5_2 = st.sidebar.empty()
        bonos_2 = placeholder5_2.button("Bonos",key="bonos_2")

        placeholder6_2 = st.sidebar.empty()
        salir_2 = placeholder6_2.button("Salir",key="salir_2")

        placeholder7_2 = st.empty()
        registro_2 = placeholder7_2.title("Procesos")

        placeholder8_2 = st.empty()
        fmi_2 = placeholder8_2.button("Folios de Matricula Inmobiliaria",key="fmi_2")

        placeholder9_2 = st.empty()
        consulta_campo_2 = placeholder9_2.button("Consultas de Campo",key="consulta_campo_2")

        # ----- Historial ---- #

        if historial_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Historial=True
            Historial.Historial(usuario,puesto)

        # ----- Capacitación ---- #

        elif capacitacion_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Capacitacion=True
            Capacitacion.Capacitacion(usuario,puesto)

        # ----- Otros Registros ---- #

        elif otros_registros_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Otros_Registros=True
            Otros_Registros.Otros_Registros(usuario,puesto)

        # ----- Bonos ---- #

        elif bonos_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Bonos=True
            Bonos.Bonos(usuario,puesto)

        # ----- Salir ---- #

        elif salir_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Ingreso = False
            st.session_state.Procesos = True
            st.session_state.Salir=True
            Salir.Salir()

        # ----- FMI ---- #

        elif fmi_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.FMI=True
            FMI.FMI(usuario,puesto)

        # ----- Consulta Campo ---- #

        elif consulta_campo_2:

            placeholder1_2.empty()
            placeholder2_2.empty()
            placeholder3_2.empty()
            placeholder4_2.empty()
            placeholder5_2.empty()
            placeholder6_2.empty()
            placeholder7_2.empty()
            placeholder8_2.empty()
            placeholder9_2.empty()
            st.session_state.Procesos=True
            st.session_state.Consulta_Campo=True
            Consulta_Campo.Consulta_Campo(usuario,puesto)

    elif st.session_state.Procesos==True:

        if st.session_state.Historial==True:
            Historial.Historial(usuario,puesto)       

        elif st.session_state.Capacitacion==True:
            Capacitacion.Capacitacion(usuario,puesto)

        elif st.session_state.Otros_Registros==True:
            Otros_Registros.Otros_Registros(usuario,puesto)

        elif st.session_state.Bonos==True:
            Bonos.Bonos(usuario,puesto)

        elif st.session_state.FMI==True:
            FMI.FMI(usuario,puesto)

        elif st.session_state.Consulta_Campo==True:
            Consulta_Campo.Consulta_Campo(usuario,puesto)
