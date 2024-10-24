from flask import Flask, render_template
import requests

url = "https://zenquotes.io/api/random"

app = Flask(__name__)

@app.route('/')
def index():
    #######################################just checking in
    try:
    # Hacer la solicitud GET a la API
        response = requests.get(url)

        # Verificar que la respuesta sea exitosa (código 200)
        if response.status_code == 200:
            # Obtener los datos de la respuesta en formato JSON
            data = response.json()
            # Extraer la frase y el autor
            quote = data[0]['q']
            author = data[0]['a']

            # Imprimir la frase motivacional
            resultado = f'"{quote}" - {author}'
        else:
            resultado =  f"Error: Unable to fetch data, status code: {response.status_code}"
    except Exception as e:
        resultado = f"An error occurred: {e}"


    ######################################

    # Resultado de Python que deseas enviar al HTML
    return render_template('index.html', resultado=resultado)

if __name__ == '__main__':
    app.run(debug=True)
