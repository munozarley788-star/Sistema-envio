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
    st.info("Has seleccionado Envío 1 (Lógica pendiente de carga).")

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
            if bomba == "9":
                res = "B9" if tanque in ["R", "U"] else "B9-B10"
            else:
                res = "B10" if tanque in ["U", "S"] else "B9-B10"
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
            if bomba == "7":
                tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
                res = "B7" if tanque in ["X", "W"] else "B7-B8"
            elif bomba == "8":
                tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
                res = "B8" if tanque in ["T", "W"] else "B7-B8"
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
            if bomba == "7":
                res = "B7" if tanque in ["X", "W"] else "B7-B8"
            else:
                res = "B8" if tanque in ["T", "W"] else "B7-B8"
            st.success(f">> Teléfono a emplear: {res}")

    # --- 2. FMM1 ---
    elif "2. FMM1" in opcion:
        bomba = st.radio("Bomba:", ["9", "10"], horizontal=True)
        st.info("PC12: Teléfono 1" if bomba == "10" else "PC12: Teléfono 5")
        tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
        if bomba == "10":
            res = "B10" if tanque in ["S", "U"] else "B9-B10"
        else:
            res = "B9" if tanque in ["R", "U"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

    # --- 3. FMM2 ---
    elif "3. FMM2" in opcion:
        bomba = st.radio("Bomba:", ["8", "9", "10"], horizontal=True)
        if bomba in ["10", "9"]: st.info("PC12: Teléfono 1")
        else: st.info("PC12: Teléfono 5")
        
        if bomba == "8":
            tanque = st.selectbox("Tanque:", ["X", "W", "T"]).upper()
            res = "B8" if tanque in ["T", "W"] else "B7-B8"
        elif bomba == "10":
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            res = "B10" if tanque in ["S", "U"] else "B9-B10"
        else: # Bomba 9
            tanque = st.selectbox("Tanque:", ["R", "U", "S"]).upper()
            res = "B9" if tanque in ["R", "U"] else "B9-B10"
        st.success(f">> Teléfono a emplear: {res}")

     # --- 4: CLARIFICAR ---
        elif opcion == "4":
            print("\n--- CONFIGURACIÓN PARA CLARIFICAR ---")
            # Selección de Bomba
            bomba = input("¿Qué bomba vas a utilizar? Disponibles (7, 8, 9, 10): ")
            
            # Lógica PC12 (Mensajes de teléfonos según la bomba)
            if bomba == "10":
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 5.")
            elif bomba in ["7", "8", "9"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 1.")
            else:
                print("Bomba no válida para Clarificar.")
                continue 

            # Lógica según el grupo de tanques (7-8 -> X,W,T | 9-10 -> R,U,S)
            if bomba in ["7", "8"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (X, W, T): ").upper()
                if bomba == "7":
                    if tanque in ["X", "W"]: print(">> Teléfono a emplear: B7")
                    elif tanque == "T": print(">> Teléfono a emplear: B7-B8")
                    else: print("Tanque no válido para la bomba 7.")
                
                elif bomba == "8":
                    if tanque in ["T", "W"]: print(">> Teléfono a emplear: B8")
                    elif tanque == "X": print(">> Teléfono a emplear: B7-B8")
                    else: print("Tanque no válido para la bomba 8.")
            
            elif bomba in ["9", "10"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (R, U, S): ").upper()
                if bomba == "9":
                    if tanque in ["R", "U"]: print(">> Teléfono a emplear: B9")
                    elif tanque == "S": print(">> Teléfono a emplear: B9-B10")
                    else: print("Tanque no válido para la bomba 9.")
                
                elif bomba == "10":
                    if tanque in ["U", "S"]: print(">> Teléfono a emplear: B10")
                    elif tanque == "R": print(">> Teléfono a emplear: B9-B10")
                    else: print("Tanque no válido para la bomba 10.")
                                         

        # --- OPCIÓN 5: MARMITA ---
        elif opcion == "5":
            print("\n--- CONFIGURACIÓN PARA MARMITA ---")
            # Selección de Bomba
            bomba = input("¿Qué bomba vas a utilizar? Disponibles (7, 8, 9): ")
            
            # Lógica PC12 (Mensajes de teléfonos según la bomba)
            if bomba == "8":
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 5.")
            elif bomba in ["7", "9"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 1.")
            else:
                print("Bomba no válida para Marmita.")
                continue 

            # Lógica según el grupo de tanques (9 -> R,U,S | 7-8 -> X,W,T)
            if bomba == "9":
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (R, U, S): ").upper()
                if tanque in ["R", "U"]:
                    print(">> Teléfono a emplear: B9")
                elif tanque == "S":
                    print(">> Teléfono a emplear: B9-B10")
                else:
                    print("Tanque no válido para la bomba 9.")
            
            elif bomba in ["7", "8"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (X, W, T): ").upper()
                if bomba == "7":
                    if tanque in ["X", "W"]:
                        print(">> Teléfono a emplear: B7")
                    elif tanque == "T":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 7.")
                
                elif bomba == "8":
                    if tanque in ["T", "W"]:
                        print(">> Teléfono a emplear: B8")
                    elif tanque == "X":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 8.")

        # --- OPCIÓN 6: PASTEURIZAR ---
        elif opcion == "6":
            print("\n--- CONFIGURACIÓN PARA PASTEURIZAR ---")
            # Selección de Bomba
            bomba = input("¿Qué bomba vas a utilizar? Disponibles (7, 8, 9, 10): ")
            
            # Lógica PC12 (Teléfonos 6 y 7)
            if bomba in ["8", "9"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 7.")
            elif bomba in ["7", "10"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 6.")
            else:
                print("Bomba no válida para Pasteurizar.")
                continue 

            # Lógica de Tanques (7-8 -> X,W,T | 9-10 -> R,U,S)
            if bomba in ["7", "8"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (X, W, T): ").upper()
                if bomba == "7":
                    if tanque in ["X", "W"]:
                        print(">> Teléfono a emplear: B7")
                    elif tanque == "T":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 7.")
                
                elif bomba == "8":
                    if tanque in ["T", "W"]:
                        print(">> Teléfono a emplear: B8")
                    elif tanque == "X":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 8.")
            
            elif bomba in ["9", "10"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (R, U, S): ").upper()
                if bomba == "9":
                    if tanque in ["R", "U"]:
                        print(">> Teléfono a emplear: B9")
                    elif tanque == "S":
                        print(">> Teléfono a emplear: B9-B10")
                    else:
                        print("Tanque no válido para la bomba 9.")
                
                elif bomba == "10":
                    if tanque in ["U", "S"]:
                        print(">> Teléfono a emplear: B10")
                    elif tanque == "R":
                        print(">> Teléfono a emplear: B9-B10")
                    else:
                        print("Tanque no válido para la bomba 10.") 

        # --- OPCIÓN 7: ULTRAPASTEURIZADOR ---
        elif opcion == "7":
            print("\n--- CONFIGURACIÓN PARA ULTRAPASTEURIZADOR ---")
            # Selección de Bomba
            bomba = input("¿Qué bomba vas a utilizar? Disponibles (7, 8, 9, 10): ")
            
            # Lógica PC12 (Teléfonos 8 y 9)
            if bomba in ["8", "9"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 8.")
            elif bomba in ["7", "10"]:
                print("[INFO] Desde la placa PC12 puede utilizar el teléfono 9.")
            else:
                print("Bomba no válida para Ultrapasteurizador.")
                continue 

            # Lógica de Tanques (7-8 -> X,W,T | 9-10 -> R,U,S)
            if bomba in ["7", "8"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (X, W, T): ").upper()
                if bomba == "7":
                    if tanque in ["X", "W"]:
                        print(">> Teléfono a emplear: B7")
                    elif tanque == "T":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 7.")
                
                elif bomba == "8":
                    if tanque in ["T", "W"]:
                        print(">> Teléfono a emplear: B8")
                    elif tanque == "X":
                        print(">> Teléfono a emplear: B7-B8")
                    else:
                        print("Tanque no válido para la bomba 8.")
            
            elif bomba in ["9", "10"]:
                tanque = input("¿Desde qué tanque vas a enviar? Disponibles (R, U, S): ").upper()
                if bomba == "9":
                    if tanque in ["R", "U"]:
                        print(">> Teléfono a emplear: B9")
                    elif tanque == "S":
                        print(">> Teléfono a emplear: B9-B10")
                    else:
                        print("Tanque no válido para la bomba 9.")
                
                elif bomba == "10":
                    if tanque in ["U", "S"]:
                        print(">> Teléfono a emplear: B10")
                    elif tanque == "R":
                        print(">> Teléfono a emplear: B9-B10")
                    else:
                        print("Tanque no válido para la bomba 10.")  

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
