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
