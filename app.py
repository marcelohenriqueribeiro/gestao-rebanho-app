# --- Cadastrar Animal ---
if menu == "Cadastrar Animal":
    st.subheader("📋 Cadastro de Animal")
    nome = st.text_input("Nome ou Identificação do Animal")
    raca = st.text_input("Raça")
    idade = st.number_input("Idade (em anos)", min_value=0, step=1)
    peso = st.number_input("Peso (kg)", min_value=0.0, step=0.1)
    sexo = st.selectbox("Sexo", ["Selecione", "Macho", "Fêmea"])

    if st.button("Salvar Animal"):
        if nome and raca and sexo != "Selecione" and peso > 0:
            rebanho.append({
                "nome": nome,
                "raca": raca,
                "idade": idade,
                "peso": peso,
                "sexo": sexo
            })
            salvar_dados(ARQUIVO_REBANHO, rebanho)
            st.success("✅ Animal cadastrado com sucesso!")
        else:
            st.warning("⚠ Preencha todos os campos corretamente.")

# --- Cadastrar Pasto ---
elif menu == "Cadastrar Pasto":
    st.subheader("🌾 Cadastro de Pasto")
    nome_pasto = st.text_input("Nome do Pasto")
    localizacao = st.text_input("Localização")
    tamanho = st.number_input("Tamanho (em hectares)", min_value=0.1, step=0.1)

    if st.button("Salvar Pasto"):
        if nome_pasto and localizacao:
            pastos.append({
                "nome": nome_pasto,
                "localizacao": localizacao,
                "tamanho": tamanho
            })
            salvar_dados(ARQUIVO_PASTOS, pastos)
            st.success("✅ Pasto cadastrado com sucesso!")
        else:
            st.warning("⚠ Preencha todos os campos corretamente.") 
# --- Visualizar Rebanho ---
elif menu == "Visualizar Rebanho":
    st.subheader("📑 Lista de Animais Cadastrados")
    if rebanho:
        for i, animal in enumerate(rebanho, start=1):
            st.markdown(f"""
            **{i}.** 🐄 **Nome:** {animal['nome']}  
            - Raça: {animal['raca']}  
            - Idade: {animal['idade']} anos  
            - Sexo: {animal['sexo']}  
            - Peso: {animal['peso']} kg  
            """)
    else:
        st.info("Nenhum animal cadastrado.")

# --- Visualizar Pastos ---
elif menu == "Visualizar Pastos":
    st.subheader("📑 Lista de Pastos Cadastrados")
    if pastos:
        for i, pasto in enumerate(pastos, start=1):
            st.markdown(f"""
            **{i}.** 🌿 **Nome:** {pasto['nome']}  
            - Localização: {pasto['localizacao']}  
            - Tamanho: {pasto['tamanho']} hectares  
            """)
    else:
        st.info("Nenhum pasto cadastrado.")
