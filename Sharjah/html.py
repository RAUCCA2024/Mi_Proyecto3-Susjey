def generar_html_con_enlace():
    html = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Documento HTML con enlace a Web de Sharjah</title>
    </head>
    <body>
        <header>
            <h1>¡Bienvenido a la Web de Sharjah!</h1>
        </header>
        <div class="container">
            <p>Sharjah es una ciudad fascinante en los Emiratos Árabes Unidos, llena de historia, cultura y belleza.</p>
            <p>Para obtener más información sobre Sharjah, visita su <a href="https://www.sharjah.ae/">sitio web oficial</a>.</p>
        </div>
        <footer>
            <p>© 2024 Sharjah Real State</p>
        </footer>
    </body>
    </html>
    """
    return html

# Guardar el HTML generado en un archivo
def guardar_html(html, nombre_archivo="documento_con_enlace.html"):
    with open(nombre_archivo, "w") as archivo:
        archivo.write(html)

# Generar el HTML y guardarlo en un archivo
html_generado = generar_html_con_enlace()
guardar_html(html_generado, "mi_documento_con_enlace.html")