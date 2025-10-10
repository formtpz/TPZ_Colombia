# ----- Librerías ---- #
import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
from urllib.parse import urlparse

import pytz

import Procesos,Historial,Capacitacion,Bonos_Extras,Salir

def Otros_Registros(usuario,puesto):

  # ----- Conexión, Botones y Memoria ---- #

  uri=st.secrets.db_credentials.URI
  result = urlparse(uri)
  hostname = result.hostname
  database = result.path[1:]
  username = result.username
  pwd = result.password
  port_id = result.port
  con = psycopg2.connect(host=hostname,dbname= database,user= username,password=pwd,port= port_id)

  placeholder1_13= st.sidebar.empty()
  titulo= placeholder1_13.title("Menú")

  placeholder2_13 = st.sidebar.empty()
  procesos_13 = placeholder2_13.button("Procesos",key="procesos_13")

  placeholder3_13 = st.sidebar.empty()
  historial_13 = placeholder3_13.button("Historial",key="historial_13")

  placeholder4_13 = st.sidebar.empty()
  capacitacion_13 = placeholder4_13.button("Capacitaciones",key="capacitacion_13")

  placeholder5_13 = st.sidebar.empty()
  bonos_extras_13 = placeholder5_13.button("Bonos y Horas Extra",key="bonos-extras_13")

  placeholder6_13 = st.sidebar.empty()
  salir_13 = placeholder6_13.button("Salir",key="salir_13")

  placeholder7_13 = st.empty()
  otros_registros_13 = placeholder7_13.title("Otros Registros")

  if puesto== "Coordinador" or puesto=="Técnico SIG":

    nombre_13= pd.read_sql(f"select nombre from usuarios where usuario='{usuario}'",uri)
    nombre_13 = nombre_13.loc[0,'nombre']

    placeholder8_13 = st.empty()
    otros_registros_registro_13 = placeholder8_13.subheader("Registro")

    data_personal_13 = pd.read_sql(f"select nombre from usuarios where estado='Activo'", con)
    placeholder9_13 = st.empty()
    personal_13= placeholder9_13.multiselect("Personal",data_personal_13,key="personal_13")

    default_date_13=datetime.now(pytz.timezone('America/Guatemala'))

    placeholder10_13= st.empty()
    fecha_13= placeholder10_13.date_input("Fecha",value=default_date_13,key="fecha_13")
    
    placeholder11_13= st.empty()
    motivo_13= placeholder11_13.selectbox("Motivo", options=("Reposición de tiempo","Cita CCSS","Entregas","Incapacidad","Control de Calidad Informalidades Especiales", "Informalidades Especiales","Fallos en Aplicativo o Conexión","Horas Extras","Licencia por Fallecimiento de Familiar","Licencia por Maternidad, Paternidad o Lactancia","Paneo de Omisiones y Comisiones", "Reunión", "Supervisión","Ubicación","Vacaciones","Horas Ordinarias de apoyo a Proyecto Externo","Horas Extra apoyo a Proyecto Externo","Otros"),key="motivo_13")
        
    placeholder12_13= st.empty()
    horas_13= placeholder12_13.number_input("Cantidad de Horas Individuales",min_value=0.0,key="horas_13")

    placeholder13_13 = st.empty()
    observaciones_13 = placeholder13_13.text_input("Observaciones",max_chars=60,key="observaciones_13")

    placeholder14_13 = st.empty()
    reporte_13 = placeholder14_13.button("Generar Reporte",key="reporte_13")

    placeholder15_13= st.empty()
    separador_13 = placeholder15_13.markdown("_____")

    placeholder16_13 = st.empty()
    otros_registros_historial_13 = placeholder16_13.subheader("Historial")

    placeholder17_13 = st.empty()
    fecha_de__inicio_13 = placeholder17_13.date_input("Fecha de Inicio",value=default_date_13,key="fecha_de_inicio_13")

    placeholder18_13 = st.empty()
    fecha_de__finalizacion_13 = placeholder18_13.date_input("Fecha de Finalización",value=default_date_13,key="fecha_de_finalizacion_13")
      
    placeholder19_13 = st.empty()
    filtro_13 = placeholder19_13.selectbox("Filtro", options=("Todos","Operarios","Profesional Jurídico","Propio","Personal Asignado","Reportados"), key="filtro_13")

    if filtro_13=="Todos":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Operarios":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)
    
    elif filtro_13=="Profesional Jurídico":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where puesto='Profesional Jurídico' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)
  
    elif filtro_13=="Propio" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Personal Asignado" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where supervisor='{nombre_13}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Reportados" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where reporte='{nombre_13}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

  elif puesto=="Supervisor":   
    
    nombre_13= pd.read_sql(f"select nombre from usuarios where usuario ='{usuario}'",uri)
    nombre_13 = nombre_13.loc[0,'nombre']   

    placeholder8_13 = st.empty()
    otros_registros_registro_13 = placeholder8_13.subheader("Registro")

    data_personal_13 = pd.read_sql(f"select nombre from usuarios where estado='Activo' and supervisor='{nombre_13}' or usuario='{usuario}'", con)
    placeholder9_13 = st.empty()
    personal_13= placeholder9_13.multiselect("Personal",data_personal_13,key="personal_13")

    default_date_13=datetime.now(pytz.timezone('America/Guatemala'))

    placeholder10_13= st.empty()
    fecha_13= placeholder10_13.date_input("Fecha",value=default_date_13,key="fecha_13")

    placeholder11_13= st.empty()
    motivo_13= placeholder11_13.selectbox("Motivo", options=("Reposición de tiempo","Cita CCSS","Entregas","Incapacidad","Control de Calidad Informalidades Especiales", "Informalidades Especiales","Fallos en Aplicativo o Conexión","Licencia por Fallecimiento de Familiar","Licencia por Maternidad, Paternidad o Lactancia", "Reunión","Paneo de Omisiones y Comisiones", "Supervisión","Ubicación","Horas Extra","Vacaciones", "Otros"),key="motivo_13")
        
    placeholder12_13= st.empty()
    horas_13= placeholder12_13.number_input("Cantidad de Horas Individuales",min_value=0.0,key="horas_13")

    placeholder13_13 = st.empty()
    observaciones_13 = placeholder13_13.text_input("Observaciones",max_chars=60,key="observaciones_13")

    placeholder14_13 = st.empty()
    reporte_13 = placeholder14_13.button("Generar Reporte",key="reporte_13")

    placeholder15_13= st.empty()
    separador_13 = placeholder15_13.markdown("_____")

    placeholder16_13 = st.empty()
    otros_registros_historial_13 = placeholder16_13.subheader("Historial")

    placeholder17_13 = st.empty()
    fecha_de__inicio_13 = placeholder17_13.date_input("Fecha de Inicio",value=default_date_13,key="fecha_de_inicio_13")

    placeholder18_13 = st.empty()
    fecha_de__finalizacion_13 = placeholder18_13.date_input("Fecha de Finalización",value=default_date_13,key="fecha_de_finalizacion_13")
      
    placeholder19_13 = st.empty()
    filtro_13 = placeholder19_13.selectbox("Filtro", options=("Todos","Operarios","Profesional Jurídico","Propio","Personal Asignado","Reportados"), key="filtro_13")

    if filtro_13=="Todos":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Operarios":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where puesto='Operario Catastral' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)
    
    elif filtro_13=="Profesional Jurídico":
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where puesto='Profesional Jurídico' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)
      
    elif filtro_13=="Propio" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Personal Asignado" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where supervisor='{nombre_13}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

    elif filtro_13=="Reportados" :
      data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where reporte='{nombre_13}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)

  elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      

    placeholder20_13 = st.empty()
    otros_registros_historial_13 = placeholder20_13.subheader("Historial")

    default_date_13 = datetime.now(pytz.timezone('America/Guatemala'))

    placeholder21_13 = st.empty()
    fecha_de__inicio_13 = placeholder21_13.date_input("Fecha de Inicio",value=default_date_13,key="fecha_de_inicio_13")

    placeholder22_13 = st.empty()
    fecha_de__finalizacion_13 = placeholder22_13.date_input("Fecha de Finalización",value=default_date_13,key="fecha_de_finalizacion_13")
      
    data = pd.read_sql(f"select cast(id as integer),marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte from otros_registros where usuario='{usuario}' and fecha>='{fecha_de__inicio_13}' and fecha<='{fecha_de__finalizacion_13}'", con)
    


  placeholder23_13 = st.empty()
  histo_13= placeholder23_13.dataframe(data=data)

  # ----- Contador de tiempo ----------------------------------------------------------------------------
    
  import time

  st.subheader("⏱ Registro de tiempo trabajado")

  # Inicializar variables de sesión
  if "inicio_tiempo" not in st.session_state:
      st.session_state.inicio_tiempo = None
  if "corriendo_tiempo" not in st.session_state:
      st.session_state.corriendo_tiempo = False
  if "tiempo_total_seg" not in st.session_state:
      st.session_state.tiempo_total_seg = 0.0
  if "ultimo_update" not in st.session_state:
      st.session_state.ultimo_update = time.time()

  col_t1, col_t2, col_t3 = st.columns(3)

    # Funciones
  def iniciar_tiempo():
      if not st.session_state.corriendo_tiempo:
          st.session_state.inicio_tiempo = time.time()
          st.session_state.corriendo_tiempo = True

  def detener_tiempo():
      if st.session_state.corriendo_tiempo:
          tiempo_actual = time.time() - st.session_state.inicio_tiempo
          st.session_state.tiempo_total_seg += tiempo_actual
          st.session_state.corriendo_tiempo = False

  with col_t1:
      st.button("▶️ Iniciar", on_click=iniciar_tiempo)
  with col_t2:
      st.button("⏹ Detener", on_click=detener_tiempo)

    # Calcular tiempo transcurrido
  if st.session_state.corriendo_tiempo:
      tiempo_transcurrido = time.time() - st.session_state.inicio_tiempo + st.session_state.tiempo_total_seg
        # Refrescar cada 1 segundo manualmente
      if time.time() - st.session_state.ultimo_update >= 1:
          st.session_state.ultimo_update = time.time()
          st.rerun()
  else:
      tiempo_transcurrido = st.session_state.tiempo_total_seg

    # Mostrar tiempo
  horas = int(tiempo_transcurrido // 3600)
  minutos = int((tiempo_transcurrido % 3600) // 60)
  segundos = int(tiempo_transcurrido % 60)
  st.metric("Tiempo transcurrido", f"{horas:02d}:{minutos:02d}:{segundos:02d}")

  tiempo_en_horas = round(tiempo_transcurrido / 3600, 2)
  st.write(f"**Tiempo total en horas decimales:** {tiempo_en_horas} h")

    # Generar reporte
  with col_t3:
      generar_reporte_tiempo = st.button("📝 Generar Reporte")

  if generar_reporte_tiempo:
      nombre_13 = pd.read_sql(f"select nombre from usuarios where usuario='{usuario}'", con)
      nombre_13 = nombre_13.loc[0, 'nombre']

      puesto_13 = pd.read_sql(f"select puesto from usuarios where usuario='{usuario}'", con)
      puesto_13 = puesto_13.loc[0, 'puesto']

      supervisor_13 = pd.read_sql(f"select supervisor from usuarios where usuario='{usuario}'", con)
      supervisor_13 = supervisor_13.loc[0, 'supervisor']

      marca_13 = datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")
      fecha_13 = datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d")

      cursor01 = con.cursor()
      cursor01.execute(f"""
          INSERT INTO otros_registros 
          (marca, usuario, nombre, puesto, supervisor, fecha, motivo, horas, observaciones, reporte, horas_bi) VALUES ('{marca_13}', '{usuario}', '{nombre_13}', '{puesto_13}', '{supervisor_13}', '{fecha_13}', 'Horas cronometradas', '{tiempo_en_horas}', 'Registro automático desde contador', '{nombre_13}', '{tiempo_en_horas}')
        """)
      con.commit()
      st.success("✅ Reporte generado correctamente.")

        # Reiniciar contador
      st.session_state.inicio_tiempo = None
      st.session_state.corriendo_tiempo = False
      st.session_state.tiempo_total_seg = 0.0


    #fin contador--------------------------------------------------------------------------------------------------------
    

  # ----- Registro ---- #
    
  if procesos_13:
    placeholder1_13.empty()
    placeholder2_13.empty()
    placeholder3_13.empty()
    placeholder4_13.empty()
    placeholder5_13.empty()   
    placeholder6_13.empty()
    placeholder7_13.empty()
    if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":
      placeholder8_13.empty()
      placeholder9_13.empty()
      placeholder10_13.empty()
      placeholder11_13.empty()
      placeholder12_13.empty()
      placeholder13_13.empty()
      placeholder14_13.empty()
      placeholder15_13.empty()
      placeholder16_13.empty()
      placeholder17_13.empty()  
      placeholder18_13.empty()
      placeholder19_13.empty()
    elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      placeholder20_13.empty()
      placeholder21_13.empty()
      placeholder22_13.empty()
    placeholder23_13.empty()
    st.session_state.Procesos=False
    st.session_state.Otros_Registros=False

    perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
    perfil= perfil.loc[0,'perfil']

    if perfil=="1":        
                    
      Procesos.Procesos1(usuario,puesto)
                
    elif perfil=="2":        
                    
      Procesos.Procesos2(usuario,puesto)   

    elif perfil=="3":  

      Procesos.Procesos3(usuario,puesto)       

  # ----- Historial ---- #
    
  elif historial_13:
    placeholder1_13.empty()
    placeholder2_13.empty()
    placeholder3_13.empty()
    placeholder4_13.empty()
    placeholder5_13.empty()   
    placeholder6_13.empty()
    placeholder7_13.empty()
    if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":
      placeholder8_13.empty()
      placeholder9_13.empty()
      placeholder10_13.empty()
      placeholder11_13.empty()
      placeholder12_13.empty()
      placeholder13_13.empty()
      placeholder14_13.empty()
      placeholder15_13.empty()
      placeholder16_13.empty()
      placeholder17_13.empty()  
      placeholder18_13.empty()
      placeholder19_13.empty()
    elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      placeholder20_13.empty()
      placeholder21_13.empty()
      placeholder22_13.empty()
    placeholder23_13.empty()
    st.session_state.Otros_Registros=False
    st.session_state.Historial=True
    Historial.Historial(usuario,puesto)

  # ----- Capacitación ---- #
    
  elif capacitacion_13:
    placeholder1_13.empty()
    placeholder2_13.empty()
    placeholder3_13.empty()
    placeholder4_13.empty()
    placeholder5_13.empty()   
    placeholder6_13.empty()
    placeholder7_13.empty()
    if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":
      placeholder8_13.empty()
      placeholder9_13.empty()
      placeholder10_13.empty()
      placeholder11_13.empty()
      placeholder12_13.empty()
      placeholder13_13.empty()
      placeholder14_13.empty()
      placeholder15_13.empty()
      placeholder16_13.empty()
      placeholder17_13.empty()  
      placeholder18_13.empty()
      placeholder19_13.empty()
    elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      placeholder20_13.empty()
      placeholder21_13.empty()
      placeholder22_13.empty()
    placeholder23_13.empty()
    st.session_state.Otros_Registros=False
    st.session_state.Capacitacion=True
    Capacitacion.Capacitacion(usuario,puesto)

  # ----- Bonos y Horas Extras ---- #

  elif bonos_extras_13:
    placeholder1_13.empty()
    placeholder2_13.empty()
    placeholder3_13.empty()
    placeholder4_13.empty()
    placeholder5_13.empty()   
    placeholder6_13.empty()
    placeholder7_13.empty()
    if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":
      placeholder8_13.empty()
      placeholder9_13.empty()
      placeholder10_13.empty()
      placeholder11_13.empty()
      placeholder12_13.empty()
      placeholder13_13.empty()
      placeholder14_13.empty()
      placeholder15_13.empty()
      placeholder16_13.empty()
      placeholder17_13.empty()  
      placeholder18_13.empty()
      placeholder19_13.empty()
    elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      placeholder20_13.empty()
      placeholder21_13.empty()
      placeholder22_13.empty()
    placeholder23_13.empty()
    st.session_state.Otros_Registros=False
    st.session_state.Bonos_Extras=True
    Bonos_Extras.Bonos_Extras(usuario,puesto)
    
  # ----- Salir ---- #
    
  elif salir_13:
    placeholder1_13.empty()
    placeholder2_13.empty()
    placeholder3_13.empty()
    placeholder4_13.empty()
    placeholder5_13.empty()   
    placeholder6_13.empty()
    placeholder7_13.empty()
    if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":
      placeholder8_13.empty()
      placeholder9_13.empty()
      placeholder10_13.empty()
      placeholder11_13.empty()
      placeholder12_13.empty()
      placeholder13_13.empty()
      placeholder14_13.empty()
      placeholder15_13.empty()
      placeholder16_13.empty()
      placeholder17_13.empty()  
      placeholder18_13.empty()
      placeholder19_13.empty()
    elif puesto=="Operario Catastral" or puesto=="QC" or puesto=="Entregas" or puesto=="Validación" or puesto=="Profesional Jurídico":
      placeholder20_13.empty()
      placeholder21_13.empty()
      placeholder22_13.empty()
      placeholder23_13.empty()
    st.session_state.Ingreso = False
    st.session_state.Otros_Registros=False
    st.session_state.Salir=True
    Salir.Salir()

  # ----- Reporte ---- #

  if puesto=="Supervisor" or puesto=="Técnico SIG" or puesto=="Coordinador":

    if reporte_13:

      if personal_13 =='':
        
        st.error('Favor ingresar el nombre de alguna persona')

      else:
        uri=st.secrets.db_credentials.URI
        for nombre in personal_13:
          cursor01=con.cursor()
          
          marca_13= datetime.now(pytz.timezone('America/Guatemala')).strftime("%Y-%m-%d %H:%M:%S")

          usuario_13= pd.read_sql(f"select usuario from usuarios where nombre ='{nombre}'",uri)
          usuario_13 = usuario_13.loc[0,'usuario']

          puesto_13= pd.read_sql(f"select puesto from usuarios where nombre ='{nombre}'",uri)
          puesto_13 = puesto_13.loc[0,'puesto']

          supervisor_13= pd.read_sql(f"select supervisor from usuarios where nombre ='{nombre}'",uri)
          supervisor_13 = supervisor_13.loc[0,'supervisor']

          horas_bi = float(horas_13)
          cursor01.execute(f"INSERT INTO otros_registros (marca,usuario,nombre,puesto,supervisor,fecha,motivo,horas,observaciones,reporte,horas_bi)VALUES('{marca_13}','{usuario_13}','{nombre}','{puesto_13}','{supervisor_13}','{fecha_13}','{motivo_13}','{horas_13}','{observaciones_13}','{nombre_13}','{horas_bi}')")
          con.commit()                                                                                            
        st.success('Registro enviado correctamente')
