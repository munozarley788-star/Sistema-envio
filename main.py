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
    t.header("📍 Selección de destino")
    opcion = st.selectbox("¿Hacia dónde vas a enviar?", 
                          ["Seleccionar...", "1. Planta (1 al 5)", "2. FMM1", "3. FMM2", "4. Clarificar", 
                           "5. Marmita", "6. Decantar", "7. Pasteurizar", "8. Ultrapasteurizador", 
                           "9. Bomba reproceso / Trasiego", "10. Envío a PC10", "11. CIP Fundidores", "12. CIP UHT"])

    # --- FUNCTION AUXILIAR PARA LA MATRIZ DE SUCCIÓN COMÚN DEL ENVÍO 1 ---
    def obtener_succion_e1(bomba, tanque):
        if bomba == "1":
            return "B1" if tanque in ["B", "F", "L", "A"] else ("19" if tanque == "K" else ("20" if tanque == "LIBRE 1" else ("21" if tanque == "D" else "Manguera")))
        elif bomba == "2":
            return "B2" if tanque in ["A", "K", "LIBRE 1", "D"] else ("19" if tanque in ["L", "LIBRE 2"] else ("20" if tanque in ["F", "CIP"] else ("21" if tanque in ["B", "C"] else "Manguera")))
        elif bomba == "3":
            return "B3" if tanque in ["D", "LIBRE 2", "CIP", "C"] else ("19" if tanque == "LIBRE 1" else ("20" if tanque in ["K", "N"] else ("21" if tanque in ["E", "A"] else "Manguera")))
        elif bomba == "4":
            return "B4" if tanque in ["C", "N", "E"] else ("19" if tanque in ["CIP", "I"] else ("20" if tanque in ["LIBRE 2", "O"] else ("21" if tanque in ["D", "M"] else "Manguera")))
        elif bomba == "5":
            return "B5" if tanque in ["E", "M", "O", "I"] else ("19" if tanque in ["N", "P"] else ("20" if tanque == "Q" else ("21" if tanque in ["H", "C"] else "Manguera")))
        elif bomba == "6":
            return "B6" if tanque in ["P", "M", "Q", "H"] else ("19" if tanque == "O" else ("20" if tanque == "I" else ("21" if tanque == "E" else "Manguera")))
        return "No configurado"

    # --- 1. PLANTAS ---
    if "1. Planta" in opcion:
        p = st.selectbox("¿A qué planta vas a enviar?", ["1", "2", "3", "4", "5"])
        st.subheader(f"--- Configuración planta {p} ---")
        
        if p == "1":
            bomba = st.radio("Bomba:", ["1", "2", "3"], horizontal=True)
            st.info("Línea: Teléfono 18" if bomba == "3" else "Línea: Teléfono 1")
            tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "K", "L", "N", "Libre 1", "Libre 2", "CIP"]).upper()
            res = obtener_succion_e1(bomba, tanque)
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "2":
            bomba = st.radio("Bomba:", ["1", "2", "3", "4"], horizontal=True)
            st.info("Línea: Teléfono 18" if bomba in ["1", "4"] else "Línea: Teléfono 1")
            tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "I", "K", "L", "M", "N", "O", "Libre 1", "Libre 2", "CIP"]).upper()
            res = obtener_succion_e1(bomba, tanque)
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "3" or p == "4":
            bomba = st.radio("Bomba:", ["2", "3", "4", "5"], horizontal=True)
            if p == "3":
                st.info("Línea: Teléfono 18" if bomba in ["2", "5"] else "Línea: Teléfono 1")
                t_list = ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]
            else:
                st.info("Línea: Teléfono 18" if bomba in ["3", "6"] else "Línea: Teléfono 1")
                t_list = ["A", "C", "D", "E", "H", "I", "K", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]
            tanque = st.selectbox("Tanque:", t_list).upper()
            res = obtener_succion_e1(bomba, tanque)
            st.success(f">> Teléfono a emplear: {res}")

        elif p == "5":
            bomba = st.radio("Bomba:", ["4", "5", "6"], horizontal=True)
            st.info("Línea: Teléfono 18" if bomba == "4" else "Línea: Teléfono 1")
            tanque = st.selectbox("Tanque:", ["C", "D", "E", "H", "I", "M", "N", "O", "P", "Q", "Libre 2", "CIP"]).upper()
            res = obtener_succion_e1(bomba, tanque)
            st.success(f">> Teléfono a emplear: {res}")

    # --- 2. FMM1 ---
    elif "2. FMM1" in opcion:
        st.subheader("--- Configuración FMM1 ---")
        bomba = st.radio("Bomba:", ["1", "2", "3"], horizontal=True)
        st.info("Línea: Teléfono 18" if bomba == "3" else "Línea: Teléfono 1")
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "K", "L", "N", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 3. FMM2 ---
    elif "3. FMM2" in opcion:
        st.subheader("--- Configuración FMM2 ---")
        bomba = st.radio("Bomba:", ["1", "2", "3", "4"], horizontal=True)
        st.info("Línea: Teléfono 18" if bomba in ["1", "4"] else "Línea: Teléfono 1")
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "I", "K", "L", "M", "N", "O", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 4. CLARIFICAR ---
    elif "4. Clarificar" in opcion:
        st.subheader("--- Configuración Clarificar ---")
        bomba = st.radio("Bomba:", ["2", "3", "4", "5"], horizontal=True)
        st.info("Línea: Teléfono 18" if bomba in ["2", "5"] else "Línea: Teléfono 1")
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 5. MARMITA ---
    elif "5. Marmita" in opcion:
        st.subheader("--- Configuración Marmita ---")
        bomba = st.radio("Bomba:", ["3", "4", "5", "6"], horizontal=True)
        st.info("Línea: Teléfono 18" if bomba in ["3", "6"] else "Línea: Teléfono 1")
        tanque = st.selectbox("Tanque:", ["A", "C", "D", "E", "H", "I", "K", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 6. DECANTAR ---
    elif "6. Decantar" in opcion:
        st.subheader("--- Configuración Decantar ---")
        bomba = st.radio("Bomba:", ["4", "5", "6"], horizontal=True)
        if bomba == "4": st.info("Línea: Teléfono 18")
        elif bomba == "5": st.info("Línea: Teléfono 1")
        elif bomba == "6": st.info("Línea: Teléfono 11")
        tanque = st.selectbox("Tanque:", ["C", "D", "E", "H", "I", "M", "N", "O", "P", "Q", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 7. PASTEURIZAR ---
    elif "7. Pasteurizar" in opcion:
        st.subheader("--- Configuración Pasteurizar ---")
        bomba = st.radio("Bomba:", ["1", "2", "3", "4", "5", "6"], horizontal=True)
        st.info("Línea: Teléfono 5" if bomba in ["1", "6"] else ("Línea: Teléfono 6" if bomba in ["2", "5"] else "Línea: Teléfono 7"))
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 8. ULTRAPASTEURIZADOR ---
    elif "8. Ultrapasteurizador" in opcion:
        st.subheader("--- Configuración Ultra pasteurizador ---")
        bomba = st.radio("Bomba:", ["1", "2", "3", "4", "5", "6"], horizontal=True)
        st.info("Línea: Teléfono 10" if bomba in ["1", "6"] else ("Línea: Teléfono 9" if bomba in ["2", "5"] else "Línea: Teléfono 8"))
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 9. BOMBA REPROCESO / TRASIEGO ---
    elif "9. Bomba reproceso / Trasiego" in opcion:
        st.subheader("--- Configuración Reproceso / Trasiego ---")
        tanque = st.selectbox("Tanque de Origen:", ["C", "N", "D", "E", "Otros tanques (Manguera)"]).upper()
        if tanque in ["C", "N"]: st.info("Succión: Teléfono B1")
        elif tanque == "D": st.info("Succión: Teléfono 19")
        elif tanque == "E": st.info("Succión: Teléfono 20")
        else: st.info("Succión: Emplear Manguera")
        
        destino_pc13 = st.radio("Destino desde PC13:", ["Trasiego", "Marmita"], horizontal=True)
        res_tel = "12" if destino_pc13 == "Trasiego" else "11"
        st.success(f">> Teléfono a emplear (Línea): {res_tel}")

    # --- 10. ENVÍO A PC10 ---
    elif "10. Envío a PC10" in opcion:
        st.subheader("--- Configuración Envío a PC10 ---")
        bomba = st.radio("Bomba:", ["1", "2", "3", "4", "5", "6"], horizontal=True)
        st.info("PC10: Teléfono 5" if bomba in ["1", "6"] else ("PC10: Teléfono 6" if bomba in ["2", "5"] else "PC10: Teléfono 7"))
        tanque = st.selectbox("Tanque:", ["A", "B", "C", "D", "E", "F", "H", "I", "K", "L", "M", "N", "O", "P", "Q", "Libre 1", "Libre 2", "CIP"]).upper()
        res = obtener_succion_e1(bomba, tanque)
        st.success(f">> Teléfono a emplear: {res}")

    # --- 11. CIP FUNDIDORES ---
    elif "11. CIP Fundidores" in opcion:
        st.subheader("--- CIP Fundidores ---")
        pl = st.selectbox("Planta:", ["1", "2", "3", "4", "5"])
        tels_f = {"1": "2", "2": "3", "3": "4", "4": "3", "5": "2"}
        st.success(f">> Teléfono a emplear: {tels_f[pl]}")

    # --- 12. CIP UHT ---
    elif "12. CIP UHT" in opcion:
        st.subheader("--- CIP UHT ---")
        eq = st.selectbox("Equipo:", ["CLARIFICAR", "UHT", "PASTEURIZADOR", "FMM2", "MARMITA", "FMM1", "DECANTAR"])
        tels_u = {"CLARIFICAR": "14", "UHT": "15", "PASTEURIZADOR": "13", "FMM2": "16", "MARMITA": "16", "FMM1": "17", "DECANTAR": "17"}
        st.success(f">> Teléfono a emplear: {tels_u[eq]}")
    
            
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
