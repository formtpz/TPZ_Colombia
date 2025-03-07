# ----- Librerías ---- #

import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
from datetime import date
import pytz
from urllib.parse import urlparse
import Procesos,Historial,Capacitacion,Otros_Registros,Bonos_Extras,Salir

def FMI(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_3= st.sidebar.empty()
  titulo= placeholder1_3.title("Menú")

  placeholder2_3 = st.sidebar.empty()
  procesos_3 = placeholder2_3.button("Procesos",key="procesos_3")

  placeholder3_3 = st.sidebar.empty()
  historial_3 = placeholder3_3.button("Historial",key="historial_3")

  placeholder4_3 = st.sidebar.empty()
  capacitacion_3 = placeholder4_3.button("Capacitaciones",key="capacitacion_3")

  placeholder5_3 = st.sidebar.empty()
  otros_registros_3 = placeholder5_3.button("Otros Registros",key="otros_registros_3")

  placeholder6_3 = st.sidebar.empty()
  bonos_extras_3 = placeholder6_3.button("Bonos y Horas Extra",key="bonos_extra_3")

  placeholder7_3 = st.sidebar.empty()
  salir_3 = placeholder7_3.button("Salir",key="salir_3")

  placeholder8_3 = st.empty()
  informacion_final_i_3 = placeholder8_3.title("Folios de Matricula Inmobiliaria")

  default_date_3 = datetime.now(pytz.timezone('America/Bogota'))

  placeholder9_3= st.empty()
  fecha_3= placeholder9_3.date_input("Fecha",value=default_date_3,key="fecha_3")

  placeholder10_3= st.empty()
  municipio_3= placeholder10_3.selectbox("Municipio", options=("Cabuyaro","Chalán","Colombia","Cuítiva","Iza","Los Palmitos","Morroa","Trinidad","San Estanislao","San Luis de Cubarral","Zambrano"), key="municipio_3")
  
  placeholder11_3= st.empty()
  unidad_inter_3=placeholder11_3.selectbox("Unidad de Intervención", options=("UITR-1","UITR-2","UITR-3","UITR-4","UITR-5","UITR-6","UITR-7","UITR-8","UITR-9","UITR-10","UITR-11","UITR-12","UITR-13","UITR-14","UITR-15","UITR-16","UITR-17","UITR-18","UITR-19","UITR-20","UITR-21","UITR-22","UITR-22","UITR-23","UITR-24","UITR-25","UITU-1","UITU-2","UITU-3","UITU-4","UITU-5","UITU-6","UITU-7","UITU-8","UITU-9","UITU-10","UITU-11","UITU-12","UITU-13","UITU-14","UITU-15","UTU-16","UITU-17","UITU- 18","UITU-19","UITU-20","UITU-21","UITU-22","UITU-22","UITU-23","UITU-24","UITU-25","Sin Geometría"), key="unidad_inter_3")

  placeholder12_3= st.empty()
  tipo_3= placeholder12_3.selectbox("Tipo", options=("Ordinario","Corrección"), key="tipo_3")
                  
  placeholder13_3= st.empty()
  produccion_3= placeholder13_3.number_input("Cantidad de Folios Revisados",min_value=0,step=1,key="produccion_3")

  placeholder14_3 = st.empty()
  reporte_3 = placeholder14_3.button("Generar Reporte",key="reporte_3")

  # ----- Procesos ---- #
    
  if procesos_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.Procesos=False
    st.session_state.FMI=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       


  #----- Historial ---- #
    
  elif historial_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.FMI=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)   

  # ----- Capacitación ---- #
    
  elif capacitacion_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.FMI=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Otros Registros ---- #
    
  elif otros_registros_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.FMI=False
    st.session_state.Otros_Registros=True
    Otros_Registros.Otros_Registros(usuario,puesto)

  # ----- Bonos y Horas Extras ---- #
    
  elif bonos_extras_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.FMI=False
    st.session_state.Bonos_Extras=True
    Bonos_Extras.Bonos_Extras(usuario,puesto)    

    # ----- Salir ---- #
    
  elif salir_3:
    placeholder1_3.empty()
    placeholder2_3.empty()
    placeholder3_3.empty()
    placeholder4_3.empty()
    placeholder5_3.empty()
    placeholder6_3.empty()
    placeholder7_3.empty()
    placeholder8_3.empty()
    placeholder9_3.empty()
    placeholder10_3.empty()
    placeholder11_3.empty()
    placeholder12_3.empty()
    placeholder13_3.empty()
    placeholder14_3.empty()
    st.session_state.Ingreso = False
    st.session_state.FMI=False
    st.session_state.Salir=True
    Salir.Salir()

  elif reporte_3:

    cursor01=con.cursor()

    marca_3= datetime.now(pytz.timezone('America/Bogota')).strftime("%Y-%m-%d %H:%M:%S")
    
    nombre_3= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_3 = nombre_3.loc[0,'nombre']
      
    supervisor_3= pd.read_sql(f"select supervisor from usuarios where usuario ='{usuario}'",uri)
    supervisor_3 = supervisor_3.loc[0,'supervisor']
    
    semana_3 = fecha_3.isocalendar()[1]

    año_3 = fecha_3.isocalendar()[0]

    unidad_3=municipio_3+'-'+unidad_inter_3

    cursor01.execute(f"INSERT INTO registro (marca,usuario,nombre,puesto,supervisor,proceso,fecha,semana,año,unidad_asignacion,tipo,produccion,aprobados,rechazados,horas)VALUES('{marca_3}','{usuario}','{nombre_3}','{puesto}','{supervisor_3}','Folios de Matricula Inmobiliaria','{fecha_3}','{semana_3}','{año_3}','{unidad_3}','{tipo_3}','{produccion_3}','0','0','0')")
    con.commit()                                                                                                                                 
    st.success('Reporte enviado correctamente')
