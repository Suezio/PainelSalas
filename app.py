import streamlit as st

def main():
    # Configuração da página
    st.set_page_config(layout="wide", page_title="Painel de Salas")
    
    # Título
    st.title("Painel de Salas Ambulatório")

    # Lista das salas
    salas = [f"SALA {i:02d}" for i in range(1, 14)]

    # Inicializa o estado de cada sala
    for sala in salas:
        if sala not in st.session_state:
            st.session_state[sala] = False

    # Botões para controle em massa
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Todas em uso", use_container_width=True):
            for sala in salas:
                st.session_state[sala] = True
            st.rerun()
    with col2:
        if st.button("Todas livres", use_container_width=True):
            for sala in salas:
                st.session_state[sala] = False
            st.rerun()

    # Estilo CSS global para esconder completamente os botões
    st.markdown("""
    <style>
    /* Esconde os botões do Streamlit mas mantém sua funcionalidade */
    div[data-testid="column"] > div[data-testid="stButton"] {
        position: absolute;
        width: 1px;
        height: 1px;
        padding: 0;
        margin: -1px;
        overflow: hidden;
        clip: rect(0, 0, 0, 0);
        white-space: nowrap;
        border-width: 0;
    }
    </style>
    """, unsafe_allow_html=True)

    # Organiza as salas em grade
    num_colunas = 4
    for i in range(0, len(salas), num_colunas):
        # Cria colunas para esta linha
        cols = st.columns(num_colunas)
        
        # Para cada sala na linha atual
        for j in range(num_colunas):
            if i + j < len(salas):
                sala = salas[i + j]
                with cols[j]:
                    # Determina o estado e a cor
                    esta_em_uso = st.session_state[sala]
                    status = "Em uso" if esta_em_uso else "Livre"
                    cor = "#FF4B4B" if esta_em_uso else "#0ECB7E"  # Vermelho ou Verde
                    
                    # Cria um contêiner com ID único que podemos clicar
                    container_id = f"container_{sala.replace(' ', '_')}"
                    
                    # Cria um div colorido personalizado que pode ser clicado
                    st.markdown(
                        f"""
                        <div id="{container_id}" style="
                            background-color: {cor};
                            color: white;
                            text-align: center;
                            padding: 15px 10px;
                            border-radius: 10px;
                            font-weight: bold;
                            margin: 10px 0;
                            cursor: pointer;
                            height: 80px;
                            display: flex;
                            flex-direction: column;
                            justify-content: center;
                            align-items: center;
                            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
                            transition: transform 0.2s, box-shadow 0.2s;
                        "
                        onmouseover="this.style.transform='scale(1.02)';this.style.boxShadow='0 6px 8px rgba(0, 0, 0, 0.15)';"
                        onmouseout="this.style.transform='scale(1)';this.style.boxShadow='0 4px 6px rgba(0, 0, 0, 0.1)';"
                        onclick="document.getElementById('btn_{sala}').click();"
                        >{sala}<br>{status}</div>
                        """,
                        unsafe_allow_html=True
                    )
                    
                    # Botão invisível que captura os cliques
                    if st.button(" ", key=f"btn_{sala}"):
                        st.session_state[sala] = not st.session_state[sala]
                        st.rerun()

if __name__ == "__main__":
    main()
