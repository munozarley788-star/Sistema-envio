import streamlit as st

# --- TUS DATOS DE REFERENCIA ---
cip_fundidores = {"1": 2, "2": 3, "3": 4, "4": 3, "5": 2}
cip_uht = {"CLARIFICAR": 10, "UHT": 11, "PASTEURIZADOR": 12, "FMM2": 13, "MARMITA": 13, "FMM1": 14}

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Sistema de Envío", page_icon="🥛")
st.title("🚜 SISTEMA DE ENVÍO")

# Menú lateral
seleccion_envio = st.sidebar.radio("MENÚ PRINCIPAL", ["Envío 1", "Envío 2", "Salir"])

if seleccion_envio == "Salir":
    st.write("¡Buen turno! Recarga la página para volver a empezar.")

elif seleccion_envio == "Envío 1":
    st.title("🚀 Sistema de Control - Envío 1")
    st.markdown("Seleccione detalladamente el destino, equipo o proceso para calcular los teléfonos de marcado automáticos.")

    # --- 1. MENÚ DE SELECCIÓN PRINCIPAL DE DESTINO ---
    destino_e1 = st.selectbox(
        "📍 Seleccione el Destino Principal (Envío 1):",
        [
            "Seleccionar...",
            "Plantas (1 al 5)",
            "FMM1",
            "FMM2",
            "Clarificar",
            "Marmita",
            "Decantar",
            "Pasteurizar",
            "Ultra pasteurizador",
            "Bomba reproceso / Trasiego",
            "Envío a PC10",
            "CIP Fundidores",
            "CIP UHT"
        ]
    )

    st.markdown("---")

    if destino_e1 != "Seleccionar...":
        
        # ==========================================
        # LÓGICA A: PLANTAS (1 AL 5)
        # ==========================================
        if destino_e1 == "Plantas (1 al 5)":
            st.subheader("🏢 Configuración para Envío a Plantas")
            planta = st.radio("¿A qué planta vas a enviar?", ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5"], horizontal=True)
            
            # Filtro dinámico de bombas según las capacidades físicas de cada planta
            b_opciones = []
            if planta == "Planta 1": b_opciones = ["Bomba 1", "Bomba 2", "Bomba 3"]
            elif planta == "Planta 2": b_opciones = ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4"]
            elif planta in ["Planta 3", "Planta 4"]: b_opciones = ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"]
            elif planta == "Planta 5": b_opciones = ["Bomba 4", "Bomba 5", "Bomba 6"]
            
            bomba_e1 = st.selectbox(f"Seleccione la bomba para {planta}:", ["Seleccionar..."] + b_opciones)
            
            if bomba_e1 != "Seleccionar...":
                # Lógica para determinar el teléfono de la línea según la Planta y la Bomba elegida
                tel_linea = ""
                if planta == "Planta 1":
                    tel_linea = "18" if bomba_e1 == "Bomba 3" else "1"
                elif planta == "Planta 2":
                    tel_linea = "18" if bomba_e1 in ["Bomba 1", "Bomba 4"] else "1"
                elif planta == "Planta 3":
                    tel_linea = "18" if bomba_e1 in ["Bomba 2", "Bomba 5"] else "1"
                elif planta == "Planta 4":
                    tel_linea = "18" if bomba_e1 in ["Bomba 3", "Bomba 6"] else "1"
                elif planta == "Planta 5":
                    tel_linea = "18" if bomba_e1 == "Bomba 4" else "1"
                
                st.info(f"📞 **Línea de Envío:** Para conectar {planta} usando la {bomba_e1}, marque el **Teléfono {tel_linea}**.")
                
                # Selector de Tanques origen
                tanque_e1 = st.selectbox("¿Desde qué tanque vas a succionar?", ["Seleccionar...", "A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"])
                
                if tanque_e1 != "Seleccionar...":
                    st.markdown("### 📱 Resultado de la Marcación de Succión:")
                    
                    # Matriz completa de succión común para plantas
                    if bomba_e1 == "Bomba 1":
                        if tanque_e1 in ["B", "F", "L", "A"]: st.success("👉 Teléfono a marcar: **B1**")
                        elif tanque_e1 == "K": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "D": st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango o requiere manguera para Bomba 1.")
                    
                    elif bomba_e1 == "Bomba 2":
                        if tanque_e1 in ["A", "K", "Libre 1", "D"]: st.success("👉 Teléfono a marcar: **B2**")
                        elif tanque_e1 in ["L", "Libre 2"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["F", "CIP"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["B", "C"]: st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango para Bomba 2.")
                        
                    elif bomba_e1 == "Bomba 3":
                        if tanque_e1 in ["D", "Libre 2", "CIP", "C"]: st.success("👉 Teléfono a marcar: **B3**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["K", "N"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["E", "A"]: st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango para Bomba 3.")
                        
                    elif bomba_e1 == "Bomba 4":
                        if tanque_e1 in ["C", "N", "E"]: st.success("👉 Teléfono a marcar: **B4**")
                        elif tanque_e1 in ["CIP", "I"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["Libre 2", "O"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["D", "M"]: st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango para Bomba 4.")
                        
                    elif bomba_e1 == "Bomba 5":
                        if tanque_e1 in ["E", "M", "O", "I"]: st.success("👉 Teléfono a marcar: **B5**")
                        elif tanque_e1 in ["N", "P"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Q": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["H", "C"]: st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango para Bomba 5.")
                        
                    elif bomba_e1 == "Bomba 6":
                        if tanque_e1 in ["P", "M", "Q", "H"]: st.success("👉 Teléfono a marcar: **B6**")
                        elif tanque_e1 == "O": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "I": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "E": st.success("👉 Teléfono a marcar: **21**")
                        else: st.warning("⚠️ Tanque fuera de rango para Bomba 6.")

        # ==========================================
        # LÓGICA B: MAQUINARIA (FMM1, FMM2, CLARIFICAR, MARMITA, DECANTAR)
        # ==========================================
        elif destino_e1 in ["FMM1", "FMM2", "Clarificar", "Marmita", "Decantar"]:
            st.subheader(f"⚙️ Procesamiento en {destino_e1}")
            
            # Asignación estricta de bombas permitidas por el equipo de destino
            b_opciones = []
            if destino_e1 == "FMM1": b_opciones = ["Bomba 1", "Bomba 2", "Bomba 3"]
            elif destino_e1 == "FMM2": b_opciones = ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4"]
            elif destino_e1 in ["Clarificar", "Marmita"]: b_opciones = ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"]
            elif destino_e1 == "Decantar": b_opciones = ["Bomba 4", "Bomba 5", "Bomba 6"]
            
            bomba_e1 = st.selectbox("Seleccione la bomba a utilizar:", ["Seleccionar..."] + b_opciones)
            
            if bomba_e1 != "Seleccionar...":
                # Lógica del teléfono de envío para la línea de equipos
                tel_linea = ""
                if destino_e1 == "FMM1": tel_linea = "18" if bomba_e1 == "Bomba 3" else "1"
                elif destino_e1 == "FMM2": tel_linea = "18" if bomba_e1 in ["Bomba 1", "Bomba 4"] else "1"
                elif destino_e1 == "Clarificar": tel_linea = "18" if bomba_e1 in ["Bomba 2", "Bomba 5"] else "1"
                elif destino_e1 == "Marmita": tel_linea = "18" if bomba_e1 in ["Bomba 3", "Bomba 6"] else "1"
                elif destino_e1 == "Decantar": 
                    if bomba_e1 == "Bomba 4": tel_linea = "18"
                    elif bomba_e1 == "Bomba 5": tel_linea = "1"
                    elif bomba_e1 == "Bomba 6": tel_linea = "11" # Decantar Bomba 6 usa el Teléfono 11
                
                st.info(f"📞 **Línea de Envío:** Para enviar a {destino_e1} por la {bomba_e1}, usar **Teléfono {tel_linea}**.")
                
                tanque_e1 = st.selectbox("¿Desde qué tanque se succionará?", ["Seleccionar...", "A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"])
                
                if tanque_e1 != "Seleccionar...":
                    st.markdown("### 📱 Resultado de la Marcación de Succión:")
                    if bomba_e1 == "Bomba 1":
                        if tanque_e1 in ["B", "F", "L", "A"]: st.success("👉 Teléfono a marcar: **B1**")
                        elif tanque_e1 == "K": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "D": st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 2":
                        if tanque_e1 in ["A", "K", "Libre 1", "D"]: st.success("👉 Teléfono a marcar: **B2**")
                        elif tanque_e1 in ["L", "Libre 2"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["F", "CIP"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["B", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 3":
                        if tanque_e1 in ["D", "Libre 2", "CIP", "C"]: st.success("👉 Teléfono a marcar: **B3**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["K", "N"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["E", "A"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 4":
                        if tanque_e1 in ["C", "N", "E"]: st.success("👉 Teléfono a marcar: **B4**")
                        elif tanque_e1 in ["CIP", "I"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["Libre 2", "O"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["D", "M"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 5":
                        if tanque_e1 in ["E", "M", "O", "I"]: st.success("👉 Teléfono a marcar: **B5**")
                        elif tanque_e1 in ["N", "P"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Q": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["H", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 6":
                        if tanque_e1 in ["P", "M", "Q", "H"]: st.success("👉 Teléfono a marcar: **B6**")
                        elif tanque_e1 == "O": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "I": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "E": st.success("👉 Teléfono a marcar: **21**")

        # ==========================================
        # LÓGICA C: PASTEURIZADORES (PASTEURIZAR / ULTRA PASTEURIZADOR)
        # ==========================================
        elif destino_e1 in ["Pasteurizar", "Ultra pasteurizador"]:
            st.subheader(f"🌡️ Tratamiento Térmico: {destino_e1}")
            bomba_e1 = st.selectbox("Seleccione la bomba a emplear (1 al 6):", 
                                 ["Seleccionar...", "Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"])
            
            if bomba_e1 != "Seleccionar...":
                tel_linea = ""
                # Variación de líneas de envío térmico cruzado
                if destino_e1 == "Pasteurizar":
                    if bomba_e1 in ["Bomba 1", "Bomba 6"]: tel_linea = "5"
                    elif bomba_e1 in ["Bomba 2", "Bomba 5"]: tel_linea = "6"
                    elif bomba_e1 in ["Bomba 3", "Bomba 4"]: tel_linea = "7"
                else: # Ultra pasteurizador
                    if bomba_e1 in ["Bomba 1", "Bomba 6"]: tel_linea = "10"
                    elif bomba_e1 in ["Bomba 2", "Bomba 5"]: tel_linea = "9"
                    elif bomba_e1 in ["Bomba 3", "Bomba 4"]: tel_linea = "8"
                
                st.info(f"📞 **Línea de Envío:** Para {destino_e1} por la {bomba_e1}, marque el **Teléfono {tel_linea}**.")
                
                tanque_e1 = st.selectbox("Seleccione el tanque de origen del producto:", ["Seleccionar...", "A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"])
                
                if tanque_e1 != "Seleccionar...":
                    st.markdown("### 📱 Resultado de la Marcación de Succión:")
                    if bomba_e1 == "Bomba 1":
                        if tanque_e1 in ["B", "F", "L", "A"]: st.success("👉 Teléfono a marcar: **B1**")
                        elif tanque_e1 == "K": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "D": st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 2":
                        if tanque_e1 in ["A", "K", "Libre 1", "D"]: st.success("👉 Teléfono a marcar: **B2**")
                        elif tanque_e1 in ["L", "Libre 2"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["F", "CIP"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["B", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 3":
                        if tanque_e1 in ["D", "Libre 2", "CIP", "C"]: st.success("👉 Teléfono a marcar: **B3**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["K", "N"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["E", "A"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 4":
                        if tanque_e1 in ["C", "N", "E"]: st.success("👉 Teléfono a marcar: **B4**")
                        elif tanque_e1 in ["CIP", "I"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["Libre 2", "O"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["D", "M"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 5":
                        if tanque_e1 in ["E", "M", "O", "I"]: st.success("👉 Teléfono a marcar: **B5**")
                        elif tanque_e1 in ["N", "P"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Q": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["H", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 6":
                        if tanque_e1 in ["P", "M", "Q", "H"]: st.success("👉 Teléfono a marcar: **B6**")
                        elif tanque_e1 == "O": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "I": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "E": st.success("👉 Teléfono a marcar: **21**")

        # ==========================================
        # LÓGICA D: BOMBA DE REPROCESO / TRASIEGO / PLACA PC13
        # ==========================================
        elif destino_e1 == "Bomba reproceso / Trasiego":
            st.subheader("🔄 Operación con Bomba de Reproceso")
            tanque_e1 = st.selectbox("Seleccione el tanque de succión:", ["Seleccionar...", "C", "N", "D", "E", "Otros tanques"])
            
            if tanque_e1 != "Seleccionar...":
                if tanque_e1 in ["C", "N"]:
                    st.success("👉 Teléfono a emplear para la succión: **B1**")
                elif tanque_e1 == "D":
                    st.success("👉 Teléfono a emplear para la succión: **19**")
                elif tanque_e1 == "E":
                    st.success("👉 Teléfono a emplear para la succión: **20**")
                elif tanque_e1 == "Otros tanques":
                    st.info("ℹ️ Nota operativa: Los demás tanques se deben conectar mediante manguera física.")
                
                st.markdown("### 📍 Trayectoria de Salida (Desde Placa PC13):")
                opc_pc13 = st.radio("¿Hacia dónde se transfiere el producto desde PC13?", ["Trasiego", "Marmita"], horizontal=True)
                if opc_pc13 == "Trasiego":
                    st.warning("📞 Envío hacia **Trasiego**: Marcar **Teléfono 12**.")
                else:
                    st.warning("📞 Envío hacia **Marmita**: Marcar **Teléfono 11**.")

        # ==========================================
        # LÓGICA E: ENVÍO COMPLETO A PLACA PC10
        # ==========================================
        elif destino_e1 == "Envío a PC10":
            st.subheader("🔌 Distribución hacia Placa PC10")
            bomba_e1 = st.selectbox("Seleccione la bomba que impulsará a PC10:", 
                                 ["Seleccionar...", "Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"])
            
            if bomba_e1 != "Seleccionar...":
                tel_pc10 = ""
                if bomba_e1 in ["Bomba 1", "Bomba 6"]: tel_pc10 = "5"
                elif bomba_e1 in ["Bomba 2", "Bomba 5"]: tel_pc10 = "6"
                elif bomba_e1 in ["Bomba 3", "Bomba 4"]: tel_pc10 = "7"
                
                st.info(f"📞 **Configuración de Línea:** Para la {bomba_e1} hacia PC10, marcar **Teléfono {tel_pc10}**.")
                
                tanque_e1 = st.selectbox("Seleccione el tanque de origen:", ["Seleccionar...", "A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"])
                
                if tanque_e1 != "Seleccionar...":
                    st.markdown("### 📱 Resultado de Succión para PC10:")
                    if bomba_e1 == "Bomba 1":
                        if tanque_e1 in ["B", "F", "L", "A"]: st.success("👉 Teléfono a marcar: **B1**")
                        elif tanque_e1 == "K": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "D": st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 2":
                        if tanque_e1 in ["A", "K", "Libre 1", "D"]: st.success("👉 Teléfono a marcar: **B2**")
                        elif tanque_e1 in ["L", "Libre 2"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["F", "CIP"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["B", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 3":
                        if tanque_e1 in ["D", "Libre 2", "CIP", "C"]: st.success("👉 Teléfono a marcar: **B3**")
                        elif tanque_e1 == "Libre 1": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["K", "N"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["E", "A"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 4":
                        if tanque_e1 in ["C", "N", "E"]: st.success("👉 Teléfono a marcar: **B4**")
                        elif tanque_e1 in ["CIP", "I"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 in ["Libre 2", "O"]: st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["D", "M"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 5":
                        if tanque_e1 in ["E", "M", "O", "I"]: st.success("👉 Teléfono a marcar: **B5**")
                        elif tanque_e1 in ["N", "P"]: st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "Q": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 in ["H", "C"]: st.success("👉 Teléfono a marcar: **21**")
                    elif bomba_e1 == "Bomba 6":
                        if tanque_e1 in ["P", "M", "Q", "H"]: st.success("👉 Teléfono a marcar: **B6**")
                        elif tanque_e1 == "O": st.success("👉 Teléfono a marcar: **19**")
                        elif tanque_e1 == "I": st.success("👉 Teléfono a marcar: **20**")
                        elif tanque_e1 == "E": st.success("👉 Teléfono a marcar: **21**")

        # ==========================================
        # LÓGICA F: SISTEMAS DE LAVADO (CIP FUNDIDORES Y CIP UHT)
        # ==========================================
        elif destino_e1 == "CIP Fundidores":
            st.subheader("🧽 Lavado - CIP Fundidores")
            planta_cip = st.selectbox("¿A qué planta se le aplicará el CIP?", ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5"])
            tels_fundidores = {"Planta 1": "2", "Planta 2": "3", "Planta 3": "4", "Planta 4": "3", "Planta 5": "2"}
            st.success(f"🧼 **Configuración de Lavado:** Para limpiar la {planta_cip}, marque el **Teléfono {tels_fundidores[planta_cip]}**.")

        elif destino_e1 == "CIP UHT":
            st.subheader("🧽 Lavado - CIP UHT")
            equipo_cip = st.selectbox("¿Qué módulo de equipo va a entrar en lavado?", ["Clarificar", "UHT", "Pasteurizador", "FMM2", "Marmita", "FMM1", "Decantar"])
            tels_uht = {
                "Clarificar": "14", "UHT": "15", "Pasteurizador": "13", 
                "FMM2": "16", "Marmita": "16", "FMM1": "17", "Decantar": "17"
            }
            st.success(f"🧼 **Configuración de Lavado:** Para limpiar el equipo {equipo_cip}, marque el **Teléfono {tels_uht[equipo_cip]}**.")
elif seleccion_envio == "Envío 2":
    st.header("📍 Selección de destino")
    opcion = st.selectbox("¿Hacia dónde vas a enviar?", 
                          ["Seleccionar...", "1. Planta (1 al 5)", "2. FMM1", "3. FMM2", "4. Clarificar", 
                           "5. Marmita", "6. Pasteurizar", "7. Ultrapasteurizador", "8. PC11", 
                           "9. CIP Fundidores", "10. CIP UHT"])

    # --- 1. PLANTAS ---
    if "1. Planta" in opcion:
        p = st.selectbox("¿A qué planta vas a enviar?", ["1", "2", "3", "4", "5"])
        st.subheader(f"--- Configuración planta {p} ---")
        
        if p == "1":
            bomba = st.radio("Bomba:", ["9", "10"], horizontal=True)
            st.info("PC12: Teléfono 1" if bomba == "10" else "PC12: Teléfono 5")
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            res = "B9" if (bomba == "9" and tanque in ["R", "U"]) else ("B10" if (bomba == "10" and tanque in ["U", "S"]) else "B9-B10")
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "2":
            bomba = st.radio("Bomba:", ["8", "9", "10"], horizontal=True)
            st.info("PC12: Teléfono 1" if bomba in ["9", "10"] else "PC12: Teléfono 5")
            if bomba == "8":
                tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
                res = "B8" if tanque in ["T", "W"] else "B7-B8"
            else:
                tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
                if bomba == "9" and tanque in ["R", "U"]: res = "B9"
                elif bomba == "10" and tanque in ["U", "S"]: res = "B10"
                else: res = "B9-B10"
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "3":
            bomba = st.radio("Bomba:", ["7", "8", "9", "10"], horizontal=True)
            st.info("PC12: Teléfono 5" if bomba == "10" else "PC12: Teléfono 1")
            if bomba in ["7", "8"]:
                tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
                if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
                else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
            else:
                tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
                if bomba == "9" and tanque in ["R", "U"]: res = "B9"
                elif bomba == "10" and tanque in ["U", "S"]: res = "B10"
                else: res = "B9-B10"
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "4":
            bomba = st.radio("Bomba:", ["7", "8", "9"], horizontal=True)
            st.info("PC12: Teléfono 1" if bomba in ["9", "7"] else "PC12: Teléfono 5")
            if bomba == "9":
                tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
                res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else:
                tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
                if bomba == "7" and tanque in ["X", "W"]: res = "B7"
                elif bomba == "8" and tanque in ["T", "W"]: res = "B8"
                else: res = "B7-B8"
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "5":
            bomba = st.radio("Bomba:", ["7", "8"], horizontal=True)
            st.info("PC12: Teléfono 1" if bomba == "7" else "PC12: Teléfono 5")
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            res = "B7" if (bomba == "7" and tanque in ["X", "W"]) else ("B8" if (bomba == "8" and tanque in ["T", "W"]) else "B7-B8")
            st.success(f">> Teléfono a emplear: {res}")

    # --- 2. FMM1 ---
    elif "2. FMM1" in opcion:
        bomba = st.radio("Bomba:", ["9", "10"], horizontal=True)
        st.info("PC12: Teléfono 1" if bomba == "10" else "PC12: Teléfono 5")
        tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
        res = "B10" if (bomba == "10" and tanque in ["S", "U"]) else ("B9" if (bomba == "9" and tanque in ["R", "U"]) else "B9-B10")
        st.success(f">> Teléfono a emplear: {res}")

    # --- 3. FMM2 ---
    elif "3. FMM2" in opcion:
        bomba = st.radio("Bomba:", ["8", "9", "10"], horizontal=True)
        st.info("PC12: Teléfono 1" if bomba in ["10", "9"] else "PC12: Teléfono 5")
        if bomba == "8":
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            res = "B8" if tanque in ["T", "W"] else "B7-B8"
        else:
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            res = "B10" if (bomba == "10" and tanque in ["S", "U"]) else ("B9" if (bomba == "9" and tanque in ["R", "U"]) else "B9-B10")
        st.success(f">> Teléfono a emplear: {res}")

    # --- 4. CLARIFICAR ---
    elif "4. Clarificar" in opcion:
        bomba = st.radio("Bomba:", ["7", "8", "9", "10"], horizontal=True)
        st.info("PC12: Teléfono 5" if bomba == "10" else "PC12: Teléfono 1")
        if bomba in ["7", "8"]:
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
        else:
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            if bomba == "9": res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else: res = "B10" if tanque in ["U", "S"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 5. MARMITA ---
    elif "5. Marmita" in opcion:
        bomba = st.radio("Bomba:", ["7", "8", "9"], horizontal=True)
        st.info("PC12: Teléfono 5" if bomba == "8" else "PC12: Teléfono 1")
        if bomba == "9":
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            res = "B9" if tanque in ["R", "U"] else "B9-B10"
        else:
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 6. PASTEURIZAR ---
    elif "6. Pasteurizar" in opcion:
        bomba = st.radio("Bomba:", ["7", "8", "9", "10"], horizontal=True)
        st.info("PC12: Teléfono 6" if bomba in ["7", "10"] else "PC12: Teléfono 7")
        if bomba in ["7", "8"]:
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
        else:
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            if bomba == "9": res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else: res = "B10" if tanque in ["U", "S"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 7. ULTRAPASTEURIZADOR ---
    elif "7. Ultrapasteurizador" in opcion:
        bomba = st.radio("Bomba:", ["7", "8", "9", "10"], horizontal=True)
        st.info("PC12: Teléfono 9" if bomba in ["7", "10"] else "PC12: Teléfono 8")
        if bomba in ["7", "8"]:
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
        else:
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            if bomba == "9": res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else: res = "B10" if tanque in ["U", "S"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 8. PC11 ---
    elif "8. PC11" in opcion:
        bomba = st.radio("Bomba:", ["7", "8", "9", "10"], horizontal=True)
        st.info("PC12: Teléfono 6" if bomba in ["7", "10"] else "PC12: Teléfono 7")
        if bomba in ["7", "8"]:
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            if bomba == "7": res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else: res = "B8" if tanque in ["T", "W"] else "B7-B8"
        else:
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            if bomba == "9": res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else: res = "B10" if tanque in ["U", "S"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 9. CIP FUNDIDORES ---
    elif "9. CIP Fundidores" in opcion:
        pl = st.selectbox("Planta:", ["1", "2", "3", "4", "5"])
        st.success(f">> Teléfono a emplear: {cip_fundidores[pl]}")

    # --- 10. CIP UHT ---
    elif "10. CIP UHT" in opcion:
        eq = st.selectbox("Equipo:", ["CLARIFICAR", "UHT", "PASTEURIZADOR", "FMM2", "MARMITA", "FMM1"])
        st.success(f">> Teléfono a emplear: {cip_uht[eq]}")
    
        st.warning("Configurando lógica de flujo para este equipo...")
        # (Aquí se repite la lógica de bombas/tanques exacta de tu archivo)
