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

    # --- PLANTA 1 ---
    if opcion == "1. Planta 1":
        st.subheader("--- Planta 1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- PLANTA 2 ---
    elif opcion == "2. Planta 2":
        st.subheader("--- Planta 2 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- PLANTA 3 ---
    elif opcion == "3. Planta 3":
        st.subheader("--- Planta 3 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"], horizontal=True)
        
        if bomba == "Bomba 2":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- PLANTA 4 ---
    elif opcion == "4. Planta 4":
        st.subheader("--- Planta 4 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 3":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- PLANTA 5 ---
    elif opcion == "5. Planta 5":
        st.subheader("--- Planta 5 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 4":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- FMM1 ---
    elif opcion == "6. FMM1":
        st.subheader("--- FMM1 ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- ADICIÓN DE MICROMOLIDO ---
    elif opcion == "7. ADICIÓN DE MICROMOLIDO":
        st.subheader("--- ADICIÓN DE MICROMOLIDO ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4"], horizontal=True)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- CLARIFICAR ---
    elif opcion == "8. Clarificar":
        st.subheader("--- Clarificar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5"], horizontal=True)
        
        if bomba == "Bomba 2":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "C", "D", "F", "K", "L", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- MARMITA ---
    elif opcion == "9. Marmita":
        st.subheader("--- Marmita ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 3":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "C", "D", "K", "Libre 1", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- DECANTAR ---
    elif opcion == "10. Decantar":
        st.subheader("--- Decantar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        if bomba == "Bomba 4":
            st.info("PC13: Teléfono 18")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 1")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 11")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "D", "Libre 2", "CIP", "N", "E", "I", "O", "M", "P", "Q", "H"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- PASTEURIZAR ---
    elif opcion == "11. Pasteurizar":
        st.subheader("--- Pasteurizar ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        tanques_p = ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]
        tanque = st.selectbox("Seleccione el Tanque:", tanques_p)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 5")
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 6")
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 7")
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 7")
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 6")
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 5")
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- ULTRA PASTEURIZADOR ---
    elif opcion == "12. Ultra pasteurizador":
        st.subheader("--- Ultra pasteurizador ---")
        bomba = st.radio("Seleccione la Bomba:", ["Bomba 1", "Bomba 2", "Bomba 3", "Bomba 4", "Bomba 5", "Bomba 6"], horizontal=True)
        
        tanques_up = ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]
        tanque = st.selectbox("Seleccione el Tanque:", tanques_up)
        
        if bomba == "Bomba 1":
            st.info("PC13: Teléfono 10")
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "Libre 2": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 2":
            st.info("PC13: Teléfono 9")
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 3":
            st.info("PC13: Teléfono 8")
            if tanque in ["D", "Libre 2", "CIP", "C"]: res = "B3"
            elif tanque == "Libre 1": res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 4":
            st.info("PC13: Teléfono 8")
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 5":
            st.info("PC13: Teléfono 9")
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "Bomba 6":
            st.info("PC13: Teléfono 10")
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- BOMBA REPROCESO / TRASIEGO ---
    elif opcion == "13. Bomba reproceso / Trasiego":
        st.subheader("--- Bomba reproceso / Trasiego ---")
        tanque = st.selectbox("Seleccione el Tanque de Origen:", ["C", "D", "E", "N", "Otros tanques (Manguera)"])
        
        if tanque in ["C", "N"]: res_succ = "B1"
        elif tanque == "E": res_succ = "19"
        elif tanque == "D": res_succ = "20"
        else: res_succ = "Manguera"
        
        st.info(f"Succión desde tanque: Teléfono {res_succ}")
        
        destino = st.radio("Seleccione Destino desde Placa PC13:", ["Trasiego", "Marmita"], horizontal=True)
        if destino == "Trasiego":
            st.success(f"PC 22 Teléfono de succión: {res_succ} -> Envío final por Teléfono 12")
        elif destino == "Marmita":
            st.success(f"PC 22 Teléfono de succión: {res_succ} -> Envío final por Teléfono 11")

    # --- ENVÍO A PC10 ---
    elif opcion == "14. ENVÍO A PC10":
        st.subheader("--- ENVÍO A PC10 ---")
        bomba = st.radio("Seleccione la Bomba:", ["BOMBA 1", "BOMBA 2", "BOMBA 3", "BOMBA 4", "BOMBA 5", "BOMBA 6"], horizontal=True)
        
        if bomba == "BOMBA 1":
            st.info("PC13: Teléfono 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "B", "L", "F", "K", "Libre 1", "D"])
            if tanque in ["B", "F", "L", "A"]: res = "B1"
            elif tanque == "K": res = "19"
            elif tanque == "Libre 1": res = "20"
            elif tanque == "libre 2": res = "21" 
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "BOMBA 2":
            st.info("PC13: Teléfono 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["A", "K", "Libre 1", "D", "L", "Libre 2", "F", "CIP"])
            if tanque in ["A", "K", "Libre 1", "D"]: res = "B2"
            elif tanque in ["L", "Libre 2"]: res = "19"
            elif tanque in ["F", "CIP"]: res = "20"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "BOMBA 3":
            st.info("PC13: Teléfono 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["D", "Libre 2", "CIP", "C", "Libre 1", "K", "N", "L", "I"])
            if tanque in ["Libre 1"]: res = "19"
            elif tanque in ["K", "N"]: res = "20"
            elif tanque in ["L", "I"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "BOMBA 4":
            st.info("PC13: Teléfono 7")
            tanque = st.selectbox("Seleccione el Tanque:", ["C", "N", "E", "CIP", "I", "Libre 2", "O", "Libre 1", "P"])
            if tanque in ["C", "N", "E"]: res = "B4"
            elif tanque in ["CIP", "I"]: res = "19"
            elif tanque in ["Libre 2", "O"]: res = "20"
            elif tanque in ["Libre 1", "P"]: res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "BOMBA 5":
            st.info("PC13: Teléfono 6")
            tanque = st.selectbox("Seleccione el Tanque:", ["E", "M", "O", "I", "N", "P", "Q", "CIP"])
            if tanque in ["E", "M", "O", "I"]: res = "B5"
            elif tanque in ["N", "P"]: res = "19"
            elif tanque == "Q": res = "20"
            elif tanque == "CIP": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")
            
        elif bomba == "BOMBA 6":
            st.info("PC13: Teléfono 5")
            tanque = st.selectbox("Seleccione el Tanque:", ["M", "P", "Q", "H", "O", "I", "N"])
            if tanque in ["P", "M", "Q", "H"]: res = "B6"
            elif tanque == "O": res = "19"
            elif tanque == "I": res = "20"
            elif tanque == "N": res = "21"
            else: res = "Manguera"
            st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- CIP FUNDIDORES ---
    elif opcion == "15. CIP FUNDIDORES":
        st.subheader("--- CIP FUNDIDORES ---")
        planta_cip = st.selectbox("Seleccione la Planta para Lavado:", ["PLANTA 1", "PLANTA 2", "PLANTA 3", "PLANTA 4", "PLANTA 5"])
        if planta_cip == "PLANTA 1": res = "2"
        elif planta_cip == "PLANTA 2": res = "3"
        elif planta_cip == "PLANTA 3": res = "4"
        elif planta_cip == "PLANTA 4": res = "3"
        elif planta_cip == "PLANTA 5": res = "2"
        st.success(f"PC 22 Teléfono a emplear: {res}")

    # --- CIP UHT ---
    elif opcion == "16. CIP UHT":
        st.subheader("--- CIP UHT ---")
        equipo_cip = st.selectbox("Seleccione el Equipo para Lavado:", ["CLARIFICAR", "UHT", "PASTEURIZADOR", "FMM2", "MARMITA", "FMM1", "DECANTAR"])
        if equipo_cip == "CLARIFICAR": res = "14"
        elif equipo_cip == "UHT": res = "15"
        elif equipo_cip == "PASTEURIZADOR": res = "13"
        elif equipo_cip == "FMM2": res = "16"
        elif equipo_cip == "MARMITA": res = "16"
        elif equipo_cip == "FMM1": res = "17"
        elif equipo_cip == "DECANTAR": res = "17"
        st.success(f"PC 22 Teléfono a emplear: {res}")
            
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
