import streamlit as st

## -- Textos -- ##
st.title('Elementos Textuais-Teste')

# Title
st.title('Olá isto é um título!')

# Header
st.header('Sou um título 2')

# Subheader
st.subheader('sou um título 3 / subtítulo')

# Text
var = 10
st.text(f'Isto é um texto: Eu S2 Python!{var}')

# Markdown
st.markdown("""
    # Título 1
    ## Título 2
    ### Subtítulo
    
    - texto normal
    - **negrito**
    - *itálico*  
    :smile:         
""")
code = '''def hello():
    print("Hello, Streamlit!")'''
st.code(code, language='python')



