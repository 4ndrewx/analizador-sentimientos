
import streamlit as st
import nltk
from textblob import TextBlob

# Configuración de la aplicación
st.set_page_config(
    page_title="Uso de TextBlob",
    page_icon="💬",
    layout="wide"
)

# Recursos de NLTK
@st.cache_resource
def preparar_nltk():
    nltk.download("punkt", quiet=True)
    nltk.download("punkt_tab", quiet=True)

preparar_nltk()

# Barra lateral
with st.sidebar:
    st.subheader("Polaridad y Subjetividad")

    st.write("""
    **Polaridad:** indica si el sentimiento es positivo,
    negativo o neutral.

    - -1: muy negativo
    - 0: neutral
    - +1: muy positivo

    **Subjetividad:** mide cuánto expresa opiniones
    o emociones.

    - 0: objetivo
    - 1: subjetivo
    """)

# Interfaz principal
st.title("Uso de TextBlob")

st.write(
    "Por favor, escribe en el campo de texto "
    "la frase que deseas analizar."
)

texto = st.text_area(
    "Escribe tu frase:",
    value="I am sad",
    height=120
)

if st.button("Analizar sentimiento", type="primary"):

    if not texto.strip():
        st.warning("Primero debes escribir una frase.")

    else:
        # Análisis de sentimientos
        analisis = TextBlob(texto.strip())
        polaridad = analisis.sentiment.polarity
        subjetividad = analisis.sentiment.subjectivity

        # Resultados numéricos
        col1, col2 = st.columns(2)

        col1.metric("Polarity", f"{polaridad:.3f}")
        col2.metric("Subjectivity", f"{subjetividad:.3f}")

        # Clasificación e interacción
        if polaridad < -0.1:
            st.error("Es un sentimiento negativo")

            st.write(
                "El texto transmite una emoción desfavorable. "
                "¿Quieres contarme qué ocurrió?"
            )

        elif polaridad > 0.1:
            st.success("Es un sentimiento positivo")

            st.write(
                "El texto transmite una emoción favorable. "
                "¿Qué fue lo mejor de esa experiencia?"
            )

        else:
            st.info("Es un sentimiento neutral")

            st.write(
                "El texto parece neutral. "
                "¿Quieres añadir más detalles?"
            )

        # Procesamiento de lenguaje natural
        with st.expander("Detalles del procesamiento NLP"):

            tokens = nltk.word_tokenize(texto.strip())

            st.write("Texto original:", texto)
            st.write("Tokens detectados:", tokens)
            st.write("Número de tokens:", len(tokens))

        # Corrección ortográfica en inglés
        with st.expander("Corrección en inglés"):

            corregido = str(analisis.correct())

            st.write("Texto original:", texto)
            st.write("Texto corregido:", corregido)

st.divider()

st.caption(
    "Aplicación educativa de PLN con Python, TextBlob y NLTK. "
    "El análisis de sentimientos está orientado principalmente al inglés."
)
