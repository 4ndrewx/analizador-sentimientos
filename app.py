!pip -q install textblob nltk

import nltk

nltk.download('punkt', quiet=True)
nltk.download('punkt_tab', quiet=True)
nltk.download('brown', quiet=True)

print("Librerías instaladas correctamente.")
import nltk
import ipywidgets as widgets

from textblob import TextBlob
from IPython.display import display, HTML, clear_output

# Título y explicación
display(HTML("""
<div style="display:flex; font-family:Arial; border-radius:8px;
            overflow:hidden; border:1px solid #ddd;">

  <div style="background:#f0f2f6; padding:25px; width:240px;
              color:#333; flex-shrink:0;">
    <h3>Polaridad y Subjetividad</h3>
    <p><b>Polaridad:</b> indica si el sentimiento es positivo,
    negativo o neutral. Va de -1 a +1.</p>
    <p><b>Subjetividad:</b> mide cuánto expresa opiniones
    o emociones. Va de 0 a 1.</p>
  </div>

  <div style="padding:25px; flex:1; color:#333;">
    <h1>Uso de textblob</h1>
    <p>Escribe una frase en inglés para analizar su sentimiento.</p>
  </div>

</div>
"""))

# Entrada de texto
texto = widgets.Textarea(
    value="I am sad",
    description="Escribe:",
    layout=widgets.Layout(width="100%", height="100px")
)

boton = widgets.Button(
    description="Analizar sentimiento",
    button_style="primary",
    layout=widgets.Layout(width="220px")
)

resultado = widgets.Output()

display(texto, boton, resultado)


# Función de análisis
def analizar(b):

    with resultado:
        clear_output()

        frase = texto.value.strip()

        if not frase:
            print("Escribe una frase antes de analizar.")
            return

        # PLN: tokenización con NLTK
        palabras = nltk.word_tokenize(frase)

        # Análisis con TextBlob
        analisis = TextBlob(frase)
        polaridad = analisis.sentiment.polarity
        subjetividad = analisis.sentiment.subjectivity

        # Clasificación e interacción
        if polaridad < -0.1:
            sentimiento = "Negativo"
            color = "#dc3545"
            respuesta = (
                "El texto expresa un sentimiento negativo. "
                "¿Quieres contarme qué ocurrió?"
            )

        elif polaridad > 0.1:
            sentimiento = "Positivo"
            color = "#198754"
            respuesta = (
                "El texto expresa un sentimiento positivo. "
                "¿Qué te hizo sentir así?"
            )

        else:
            sentimiento = "Neutral"
            color = "#6c757d"
            respuesta = (
                "El texto parece neutral. "
                "¿Quieres añadir más detalles?"
            )

        # Mostrar resultados
        display(HTML(f"""
        <div style="font-family:Arial; padding:20px;
                    border:1px solid #ddd; border-radius:10px;
                    margin-top:15px; color:#333;">

            <h2 style="color:{color};">
                Sentimiento {sentimiento}
            </h2>

            <p><b>Polarity:</b> {polaridad:.3f}</p>
            <p><b>Subjectivity:</b> {subjetividad:.3f}</p>

            <hr>

            <h3>Respuesta de la aplicación</h3>
            <p>{respuesta}</p>

            <h3>Procesamiento NLP con NLTK</h3>
            <p><b>Palabras identificadas:</b> {len(palabras)}</p>
            <p><b>Tokens:</b> {palabras}</p>

        </div>
        """))


boton.on_click(analizar)
# Aplicación de análisis de sentimientos
