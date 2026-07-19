import streamlit as st

# --- TUS DATOS DE REFERENCIA ---
cip_fundidores = {"1": 2, "2": 3, "3": 4, "4": 3, "5": 2}
cip_uht = {"CLARIFICAR": 10, "UHT": 11, "PASTEURIZADOR": 12, "FMM2": 13, "MARMITA": 13, "FMM1": 14}

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="Sistema de Envío", page_icon="🥛")
st.title("🚜 SISTEMA DE ENVÍO")

# Menú lateral
seleccion_envio = st.sidebar.radio("MENÚ PRINCIPAL", ["Envío 1", "Inventario Envío 1", "Envío 2", "Salir"])

if seleccion_envio == "Salir":
    st.write("¡Buen turno! Recarga la página para volver a empezar.")

elif seleccion_envio == "Envío 1":
    st.header("📍 Envío 1 - Destinos")
    
    opcion = st.selectbox(
        "¿Hacia dónde vas a enviar?", 
        [
            "Seleccionar...", 
            "1. Planta 1", 
            "2. Planta 2", 
            "3. Planta 3", 
            "4. Planta 4", 
            "5. Planta 5", 
            "6. FMM1", 
            "7. ADICIÓN DE MICROMOLIDO", 
            "8. Clarificar", 
            "9. Marmita", 
            "10. Decantar", 
            "11. Pasteurizar", 
            "12. Ultra pasteurizador", 
            "13. Bomba reproceso / Trasiego", 
            "14. ENVÍO A PC10", 
            "15. CIP FUNDIDORES", 
            "16. CIP UHT"
        ]
    )

    # ==========================================
    # 1. PLANTA 1
    # ==========================================
    if opcion == "1. Planta 1":
        st.subheader("--- Planta 1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "F", "L", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 2. PLANTA 2
    # ==========================================
    elif opcion == "2. Planta 2":
        st.subheader("--- Planta 2 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 3. PLANTA 3
    # ==========================================
    elif opcion == "3. Planta 3":
        st.subheader("--- Planta 3 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"], horizontal=True)
        
        if bomba == "Bomba 2":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 4. PLANTA 4
    # ==========================================
    elif opcion == "4. Planta 4":
        st.subheader("--- Planta 4 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 3":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 5. PLANTA 5
    # ==========================================
    elif opcion == "5. Planta 5":
        st.subheader("--- Planta 5 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 4":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 6. FMM1
    # ==========================================
    elif opcion == "6. FMM1":
        st.subheader("--- FMM1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 7. ADICIÓN DE MICROMOLIDO
    # ==========================================
    elif opcion == "7. ADICIÓN DE MICROMOLIDO":
        st.subheader("--- Adición de Micromolido ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: Articulado")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "I", "O", "M", "N", "P", "Q", "CIP"])
            if tanque in ["E", "I", "O", "M"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 8. CLARIFICAR
    # ==========================================
    elif opcion == "8. Clarificar":
        st.subheader("--- Clarificar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"], horizontal=True)
        
        if bomba == "Bomba 2":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 9. MARMITA
    # ==========================================
    elif opcion == "9. Marmita":
        st.subheader("--- Marmita ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 3":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 10. DECANTAR
    # ==========================================
    elif opcion == "10. Decantar":
        st.subheader("--- Decantar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 4":
            st.info("PC13 Teléfono: 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 11")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 11. PASTEURIZAR
    # ==========================================
    elif opcion == "11. Pasteurizar":
        st.subheader("--- Pasteurizar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 12. ULTRA PASTEURIZADOR
    # ==========================================
    elif opcion == "12. Ultra pasteurizador":
        st.subheader("--- Ultra pasteurizador ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13 Teléfono: 10")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13 Teléfono: 9")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13 Teléfono: 8")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13 Teléfono: 8")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13 Teléfono: 9")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13 Teléfono: 10")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 13. BOMBA REPROCESO / TRASIEGO
    # ==========================================
    elif opcion == "13. Bomba reproceso / Trasiego":
        st.subheader("--- Bomba Reproceso y Trasiego ---")
        tanque = st.selectbox("Seleccione el Tanque o Método de Succión:", ["C", "N", "E", "D", "Manguera (Otros Tanques)"])
        
        if tanque in ["C", "N"]:
            st.success("PC 22 Teléfono a emplear: B1")
        elif tanque == "E":
            st.success("PC 22 Teléfono a emplear: 19")
        elif tanque == "D":
            st.success("PC 22 Teléfono a emplear: 20")
        elif tanque == "Manguera (Otros Tanques)":
            st.info("Se debe emplear manguera para los tanques restantes.")

        st.info("Llega a la placa PC13. De ahí se puede enviar a:\n* **Trasiego** con el Teléfono 12\n* **Marmita** con el Teléfono 11.")

    # ==========================================
    # 14. ENVÍO A PC10
    # ==========================================
    elif opcion == "14. ENVÍO A PC10":
        st.subheader("--- Envío a PC10 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("Teléfono de Bomba: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["B", "F", "L", "A", "K", "Libre 1", "Libre 2"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("Teléfono de Bomba: 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("Teléfono de Bomba: 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["Libre 1", "K", "N", "L", "I"])
            if tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("Teléfono de Bomba: 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("Teléfono de Bomba: 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("Teléfono de Bomba: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["P", "M", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # ==========================================
    # 15. CIP FUNDIDORES
    # ==========================================
    elif opcion == "15. CIP FUNDIDORES":
        st.subheader("--- CIP Fundidores ---")
        planta_cip = st.selectbox("Seleccione la Planta para Lavado:", ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5"])
        if planta_cip == "Planta 1": res_cip = "2"
        elif planta_cip == "Planta 2": res_cip = "3"
        elif planta_cip == "Planta 3": res_cip = "4"
        elif planta_cip == "Planta 4": res_cip = "3"
        elif planta_cip == "Planta 5": res_cip = "2"
        st.success(f"Teléfono CIP a emplear: {res_cip}")

    # ==========================================
    # 16. CIP UHT
    # ==========================================
    elif opcion == "16. CIP UHT":
        st.subheader("--- CIP UHT ---")
        sector_uht = st.selectbox(
            "Seleccione el Sector a Lavar:", 
            ["Clarificar", "UHT", "Pasteurizador", "FMM2", "Marmita", "FMM1", "Decantar"]
        )
        if sector_uht == "Clarificar": res_uht = "14"
        elif sector_uht == "UHT": res_uht = "15"
        elif sector_uht == "Pasteurizador": res_uht = "13"
        elif sector_uht in ["FMM2", "Marmita"]: res_uht = "16"
        elif sector_uht in ["FMM1", "Decantar"]: res_uht = "17"
        st.success(f"Teléfono CIP UHT a emplear: {res_uht}")

elif seleccion_envio == "Inventario Envío 1":
    st.header("📦 Inventario Envío 1")
    st.write("A continuación se detalla la cantidad de accesorios por placa para este envío:")
    
    # --- DATOS DE LA PLACA PC22 ---
    st.subheader("🔹 Placa PC22")
    inventario_pc22 = {
        "Descripción del Accesorio": [
            "Teléfono B1", "Teléfono B2", "Teléfono B3", 
            "Teléfono B4", "Teléfono B5", "Teléfono B6", 
            "Teléfono 19", "Teléfono 20", "Teléfono 21"
        ],
        "Cantidad (Unidades)": [1, 1, 1, 1, 1, 1, 2, 2, 2]
    }
    st.table(inventario_pc22)
    total_pc22 = sum(inventario_pc22["Cantidad (Unidades)"])
    st.markdown(f"**Subtotal Placa PC22:** {total_pc22} unidades")
    
    st.markdown("---")
    
    # --- DATOS DE LA PLACA PC13 ---
    st.subheader("🔹 Placa PC13")
    inventario_pc13 = {
        "Descripción del Accesorio": [
            "Teléfono 1", "Teléfono 2", "Teléfono 3", "Teléfono 4", 
            "Teléfono 5", "Teléfono 6", "Teléfono 7", "Teléfono 8", 
            "Teléfono 9", "Teléfono 10", "Teléfono 11", "Teléfono 12", 
            "Teléfono 13", "Teléfono 14", "Teléfono 15", "Teléfono 16", 
            "Teléfono 17", "Teléfono 18"
        ],
        "Cantidad (Unidades)": [6, 1, 1, 1, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2]
    }
    st.table(inventario_pc13)
    total_pc13 = sum(inventario_pc13["Cantidad (Unidades)"])
    st.markdown(f"**Subtotal Placa PC13:** {total_pc13} unidades")
    
    st.markdown("---")
    
    # --- TOTAL GENERAL DEL ENVÍO ---
    total_general = total_pc22 + total_pc13
    
    col1, col2 = st.columns([2, 1])
    with col2:
        st.metric(label="📊 CANTIDAD TOTAL ENVÍO 1", value=f"{total_general} uds") 

            
elif seleccion_envio == "Envío 2":
    st.header("📍 Envío 2 - Destinos")
    
    opcion = st.selectbox(
        "¿Hacia dónde vas a enviar?", 
        [
            "Seleccionar...", 
            "1. Planta 1", 
            "2. Planta 2", 
            "3. Planta 3", 
            "4. Planta 4", 
            "5. Planta 5", 
            "6. FMM1", 
            "7. FMM2",
            "8. Clarificar", 
            "9. Marmita", 
            "10. Pasteurizar", 
            "11. Ultra pasteurizador", 
            "12. ENVÍO A PC11", 
            "13. CIP FUNDIDORES", 
            "14. CIP UHT"
        ]
    )

    # ==========================================
    # 1. PLANTA 1
    # ==========================================
    if opcion == "1. Planta 1":
        st.subheader("--- Planta 1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 9":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 2. PLANTA 2
    # ==========================================
    elif opcion == "2. Planta 2":
        st.subheader("--- Planta 2 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 8":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 3. PLANTA 3
    # ==========================================
    elif opcion == "3. Planta 3":
        st.subheader("--- Planta 3 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 4. PLANTA 4
    # ==========================================
    elif opcion == "4. Planta 4":
        st.subheader("--- Planta 4 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 5. PLANTA 5
    # ==========================================
    elif opcion == "5. Planta 5":
        st.subheader("--- Planta 5 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 6. FMM1
    # ==========================================
    elif opcion == "6. FMM1":
        st.subheader("--- FMM1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 9":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 7. FMM2
    # ==========================================
    elif opcion == "7. FMM2":
        st.subheader("--- FMM2 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 8":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 8. CLARIFICAR
    # ==========================================
    elif opcion == "8. Clarificar":
        st.subheader("--- Clarificar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 9. MARMITA
    # ==========================================
    elif opcion == "9. Marmita":
        st.subheader("--- Marmita ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 5")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 1")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 10. PASTEURIZAR
    # ==========================================
    elif opcion == "10. Pasteurizar":
        st.subheader("--- Pasteurizar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 6")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 7")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 7")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 6")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 11. ULTRA PASTEURIZADOR
    # ==========================================
    elif opcion == "11. Ultra pasteurizador":
        st.subheader("--- Ultrapasteurizador ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("PC12 Teléfono: 9")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("PC12 Teléfono: 8")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("PC12 Teléfono: 8")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("PC12 Teléfono: 9")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 12. ENVÍO A PC11
    # ==========================================
    elif opcion == "12. ENVÍO A PC11":
        st.subheader("--- Envío a PC11 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 7", "Bomba 8", "Bomba 9", "Bomba 10"], horizontal=True)
        
        if bomba == "Bomba 7":
            st.info("Teléfono de Bomba: 6")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "X", "T"])
            if tanque in ["W", "X"]:
                res = "B7"
            elif tanque == "T":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 8":
            st.info("Teléfono de Bomba: 7")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de X, W, T):", ["W", "T", "X"])
            if tanque in ["W", "T"]:
                res = "B8"
            elif tanque == "X":
                res = "B7-B8"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 9":
            st.info("Teléfono de Bomba: 7")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["R", "U", "S"])
            if tanque in ["R", "U"]:
                res = "B9"
            elif tanque == "S":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 10":
            st.info("Teléfono de Bomba: 6")
            tanque = st.selectbox("Seleccione el Tanque (Succiona de R, U, S):", ["S", "U", "R"])
            if tanque in ["S", "U"]:
                res = "B10"
            elif tanque == "R":
                res = "B9-B10"
            st.success(f"PC 23 Teléfono a emplear: {res}")

    # ==========================================
    # 13. CIP FUNDIDORES
    # ==========================================
    elif opcion == "13. CIP FUNDIDORES":
        st.subheader("--- CIP Fundidores ---")
        planta_cip = st.selectbox("Seleccione la Planta para Lavado:", ["Planta 1", "Planta 2", "Planta 3", "Planta 4", "Planta 5"])
        if planta_cip == "Planta 1": res_cip = "2"
        elif planta_cip == "Planta 2": res_cip = "3"
        elif planta_cip == "Planta 3": res_cip = "4"
        elif planta_cip == "Planta 4": res_cip = "3"
        elif planta_cip == "Planta 5": res_cip = "2"
        st.success(f"Teléfono CIP a emplear: {res_cip}")

    # ==========================================
    # 14. CIP UHT
    # ==========================================
    elif opcion == "14. CIP UHT":
        st.subheader("--- CIP UHT ---")
        sector_uht = st.selectbox("Seleccione el Sector a Lavar:", ["Clarificar", "UHT", "Pasteurizador", "FMM2", "Marmita", "FMM1"])
        if sector_uht == "Clarificar": res_uht = "10"
        elif sector_uht == "UHT": res_uht = "11"
        elif sector_uht == "Pasteurizador": res_uht = "12"
        elif sector_uht == "FMM2": res_uht = "13"
        elif sector_uht == "Marmita": res_uht = "13"
        elif sector_uht == "FMM1": res_uht = "14"
        st.success(f"Teléfono CIP UHT a emplear: {res_uht}")
    
        st.warning("Configurando lógica de flujo para este equipo...")
        # (Aquí se repite la lógica de bombas/tanques exacta de tu archivo)
