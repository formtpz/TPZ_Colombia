import streamlit as st
import pandas as pd
import psycopg2
from datetime import datetime
import pytz
from urllib.parse import urlparse
import Procesos


def Correcciones(usuario, puesto):

    # ----- Conexión a la BD ----- #
    uri = st.secrets.db_credentials.URI
    result = urlparse(uri)
    hostname = result.hostname
    database = result.path[1:]
    username = result.username
    pwd = result.password
    port_id = result.port

    con = psycopg2.connect(
        host=hostname,
        dbname=database,
        user=username,
        password=pwd,
        port=port_id
    )
    cursor = con.cursor() 
    # ----- Procesos ---- #
    placeholder1_3= st.sidebar.empty()
    titulo= placeholder1_3.title("Menú")


    placeholder2_3 = st.sidebar.empty()
    procesos_3 = placeholder2_3.button("Regresar", key="procesos_3")
    if puesto != "Coordinador":
        page = st.empty()
        with page.container():
        
            st.title("Corrección de Reportes")

            st.write("""Aquí puedes visualizar tus reportes, filtrar por fecha y solicitar correcciones
            o eliminaciones si encuentras errores.""")

            # ----- Filtro de fechas ----- #
            st.subheader("Filtrar reportes por fecha")

            col1, col2 = st.columns(2)

            with col1:
                fecha_inicio = st.date_input("Fecha inicio")
            with col2:
                fecha_fin = st.date_input("Fecha fin")

            if fecha_inicio > fecha_fin:
                st.error("La fecha de inicio no puede ser mayor que la fecha final.")
     

            # ----- Obtener nombre del usuario ----- #
            df_nombre = pd.read_sql(f"SELECT nombre FROM usuarios WHERE usuario = '{usuario}'", con)
            nombre = df_nombre.loc[0, "nombre"]

        # ----- Consultar reportes del usuario ----- #
            query = f"""
                SELECT id, marca, usuario, nombre, fecha, tipo, produccion, aprobados, rechazados, horas, uit, hito, lote, area, efes, informales, paquete, observaciones, zona, tipo_calidad, operador_cc, tipo_de_errores, conteo_de_errores
                FROM registro
                WHERE usuario = '{usuario}'
                  AND fecha BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
                ORDER BY fecha DESC;
            """

            queryotros = f"""
                SELECT id, marca, usuario, nombre, fecha, motivo, horas, observaciones, reporte
                FROM otros_registros
                WHERE usuario = '{usuario}'
                  AND fecha BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
                ORDER BY fecha DESC;
            """

            querycapacita = f"""
                SELECT id, marca, usuario, nombre, fecha, tema, horas, observaciones, reporte
                FROM capacitaciones
                WHERE usuario = '{usuario}'
                  AND fecha BETWEEN '{fecha_inicio}' AND '{fecha_fin}'
                ORDER BY fecha DESC;
            """

            df = pd.read_sql(query, con)

            st.subheader("Reportes encontrados")
            st.dataframe(df, use_container_width=True)
    
   

            dfo = pd.read_sql(queryotros, con)

            st.subheader("Otros Registros encontrados")
            st.dataframe(dfo, use_container_width=True)
    
    

            dfc = pd.read_sql(querycapacita, con)

            st.subheader("Capacitaciones encontradas")
            st.dataframe(dfc, use_container_width=True)
    
   


        

        # ----- Seleccionar ID para corregir o eliminar ----- #
            st.subheader("Solicitar corrección o eliminación")

            id_reporte = st.text_input("Ingrese el ID del Reporte")
    

            tipo_correccion = st.radio(
                "Tipo de corrección:",
                ("Modificar valor", "Eliminar reporte"))
    
            tabla = st.radio("Tabla:", ("registros", "otros_registros", "capacitaciones"
            ))

            nuevo_valor = None

            if tipo_correccion == "Modificar valor":
        
                descripcion1 = st.radio("Motivo:", ("Estado Incorrecto", "Fecha Incorrecta","Hora Incorrecta", "Predios Incorrectos","Caracteres Especiales", "Paquete Incorrecto","Usuario Incorrecto","Tipo Incorrecto", "Unidad de Asignación Incorrecto"))
                columna = st.text_input(
                    "indique la columna que deseas corregir"
                )

                nuevo_valor = st.text_input("Ingresa el nuevo valor")
    
            elif tipo_correccion == "Eliminar reporte":
                descripcion1 = st.radio("Motivo:", ("Reporte Duplicado", "Reporte Incorrecto","Reporte de Prueba", "Proceso Incorrecto", "Municipio Incorrecto"))
                columna = 'N/A'
                nuevo_valor = '0'

            # ----- Enviar solicitud ----- #
            if st.button("Enviar Solicitud"):

                cursor = con.cursor()

                marca = datetime.now(pytz.timezone("America/Guatemala")).strftime("%Y-%m-%d %H:%M:%S")

                if tipo_correccion == "Modificar valor":
                    descripcion=descripcion1
                    solicitud = "Modificar"

                else:
                    descripcion=descripcion1
                    solicitud = "Eliminar"

                insert_query = f"""
                    INSERT INTO correcciones (usuario, nombre, tipo_error, id_asociado, fecha, solucion, tabla, columna, nuevo_valor, estado)
                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
                """

                cursor.execute(insert_query, (
                    usuario,
                    nombre,
                    descripcion,
                    id_reporte,
                    marca,
                    solicitud,
                    tabla,
                    columna,
                    nuevo_valor,
                    "Pendiente"
                ))

                con.commit()

                st.success("Solicitud registrada correctamente 🎉")

                if tipo_correccion == "Modificar valor":
                    st.info(f"Corrección solicitada: cambiar **{columna}** → **{nuevo_valor}**")
                else:
                    st.info("Solicitud de eliminación registrada.")
    
        pass #fin del placeholder global
    elif puesto == "Coordinador":
        page = st.empty()
        with page.container():
            
            # =====================================================
            # 1) TABLA: CORRECCIONES (EDITABLE)
            # =====================================================
        
            st.header("Correcciones Pendientes")
        
            filtro = st.selectbox("Mostrar:", ["Todos", "Pendiente"])
        
            query_corr = """
                SELECT id, usuario, nombre, tipo_error, id_asociado, fecha, solucion,
                       tabla, columna, nuevo_valor, estado
                FROM correcciones
            """
        
            if filtro == "Pendiente":
                query_corr += " WHERE estado = 'Pendiente'"
        
            df_corr_original = pd.read_sql(query_corr, con)
        
            df_corr_editado = st.data_editor(
                df_corr_original,
                use_container_width=True,
                num_rows="fixed"
            )
        
            # =====================================================
            # 2) GUARDAR CAMBIOS
            # =====================================================
        
            if st.button("Guardar cambios"):
        
                cambios_corr = df_corr_editado.compare(df_corr_original)
        
                if cambios_corr.empty:
                    st.info("No hay cambios para guardar.")
                    return
        
                for idx in cambios_corr.index.get_level_values(0).unique():
        
                    fila = df_corr_editado.loc[idx]
        
                    # Detectar columnas con cambios
                    columnas_cambiadas = [
                        col for col in df_corr_original.columns
                        if fila[col] != df_corr_original.loc[idx][col]
                    ]
        
                    set_clause = ", ".join([f"{col} = %s" for col in columnas_cambiadas])
        
                    # Convertir valores numpy → python
                    valores = [
                        fila[col].item() if hasattr(fila[col], "item") else fila[col]
                        for col in columnas_cambiadas
                    ]
        
                    # Convertir ID a tipo Python
                    id_python = fila["id"].item() if hasattr(fila["id"], "item") else fila["id"]
        
                    sql = f"""
                        UPDATE correcciones
                        SET {set_clause}
                        WHERE id = %s
                    """
        
                    cursor.execute(sql, valores + [id_python])
        
                con.commit()
                st.success("Cambios guardados correctamente 🎉")
        pass
    
    if procesos_3:
    # Limpiar la pantalla actual
      placeholder1_3.empty()
      placeholder2_3.empty()
      if puesto != "Coordinador":
          page.empty()
          st.empty()
      elif puesto == "Coordinador":
          page.empty()
          st.empty()
      st.session_state.Procesos = False
      st.session_state.Correcciones = False  # tu estado actual
      

      perfil=pd.read_sql(f"select perfil from usuarios where usuario ='{usuario}'",uri)
      perfil= perfil.loc[0,'perfil']

      if perfil=="1":        
                    
        Procesos.Procesos1(usuario,puesto)
                
      elif perfil=="2":        
                    
        Procesos.Procesos2(usuario,puesto)   

      elif perfil=="3":  

        Procesos.Procesos3(usuario,puesto)         
#----------------fin----------------------------------------------------------------------------------------------------------------------------------------------------------------------
   
