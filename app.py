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
# --- Ganho de Peso ---
elif menu == "Ganho de Peso":
    st.subheader("📈 Cálculo de Ganho de Peso")

    nome_animal = st.text_input("Nome do Animal")
    data_entrada = st.date_input("Data de Entrada", value=date.today())
    data_saida = st.date_input("Data de Saída", value=date.today())
    peso_inicial = st.number_input("Peso Inicial (kg)", min_value=0.0, step=0.1)
    peso_final = st.number_input("Peso Final (kg)", min_value=0.0, step=0.1)

    if st.button("Calcular Ganho"):
        if nome_animal.strip() == "":
            st.warning("⚠ Informe o nome do animal.")
        elif data_saida <= data_entrada:
            st.warning("⚠ A data de saída deve ser posterior à data de entrada.")
        elif peso_final <= peso_inicial:
            st.warning("⚠ O peso final deve ser maior que o peso inicial.")
        else:
            dias = (data_saida - data_entrada).days
            ganho_total = peso_final - peso_inicial
            ganho_medio = ganho_total / dias if dias > 0 else 0

            st.success(f"""
            📊 Resultado para **{nome_animal}**:
            - Dias: {dias}  
            - Ganho Total: {ganho_total:.2f} kg  
            - Ganho Médio Diário: {ganho_medio:.2f} kg/dia
            """)
# --- Editar/Remover Animal ---
elif menu == "Editar/Remover Animal":
    st.subheader("✏️ Editar ou Remover Animal")
    
    if not rebanho:
        st.info("Nenhum animal cadastrado para editar ou remover.")
    else:
        nomes_animais = [animal["nome"] for animal in rebanho]
        selecionado = st.selectbox("Selecione o animal", nomes_animais)
        
        if selecionado:
            index = nomes_animais.index(selecionado)
            animal = rebanho[index]
            
            # Campos para edição
            novo_nome = st.text_input("Nome", animal["nome"])
            nova_raca = st.text_input("Raça", animal["raca"])
            nova_idade = st.number_input("Idade (anos)", min_value=0, value=animal["idade"], step=1)
            novo_peso = st.number_input("Peso (kg)", min_value=0.0, value=animal["peso"], step=0.1)
            novo_sexo = st.selectbox("Sexo", ["Macho", "Fêmea"], index=["Macho", "Fêmea"].index(animal["sexo"]))
            
            if st.button("Salvar Alterações"):
                rebanho[index] = {
                    "nome": novo_nome,
                    "raca": nova_raca,
                    "idade": nova_idade,
                    "peso": novo_peso,
                    "sexo": novo_sexo
                }
                salvar_dados(ARQUIVO_REBANHO, rebanho)
                st.success("✅ Animal atualizado com sucesso!")
            
            if st.button("Remover Animal"):
                rebanho.pop(index)
                salvar_dados(ARQUIVO_REBANHO, rebanho)
                st.success("❌ Animal removido com sucesso!")

# --- Editar/Remover Pasto ---
elif menu == "Editar/Remover Pasto":
    st.subheader("✏️ Editar ou Remover Pasto")
    
    if not pastos:
        st.info("Nenhum pasto cadastrado para editar ou remover.")
    else:
        nomes_pastos = [pasto["nome"] for pasto in pastos]
        selecionado = st.selectbox("Selecione o pasto", nomes_pastos)
        
        if selecionado:
            index = nomes_pastos.index(selecionado)
            pasto = pastos[index]
            
            # Campos para edição
            novo_nome = st.text_input("Nome", pasto["nome"])
            nova_localizacao = st.text_input("Localização", pasto["localizacao"])
            novo_tamanho = st.number_input("Tamanho (hectares)", min_value=0.1, value=pasto["tamanho"], step=0.1)
            
            if st.button("Salvar Alterações"):
                pastos[index] = {
                    "nome": novo_nome,
                    "localizacao": nova_localizacao,
                    "tamanho": novo_tamanho
                }
                salvar_dados(ARQUIVO_PASTOS, pastos)
                st.success("✅ Pasto atualizado com sucesso!")
            
            if st.button("Remover Pasto"):
                pastos.pop(index)
                salvar_dados(ARQUIVO_PASTOS, pastos)
                st.success("❌ Pasto removido com sucesso!")
