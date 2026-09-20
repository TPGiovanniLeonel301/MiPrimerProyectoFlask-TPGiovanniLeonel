import os
from flask import Flask, render_template
from dotenv import load_dotenv

# Cargar variables del archivo .env
load_dotenv()

# Crear aplicación Flask
app = Flask(__name__)

# Configuración
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

# Variables del proyecto
NOMBRE_PROYECTO = os.getenv(
    "APP_NAME",
    "Proyecto Flask"
)

@app.route("/")
def inicio():
    return render_template(
        "index.html",
        proyecto=NOMBRE_PROYECTO
    )

@app.route("/acerca")
def acerca():
    return render_template(
        "acerca.html",
        proyecto=NOMBRE_PROYECTO
    )

@app.route("/contacto")
def contacto():
    return render_template(
        "contacto.html",
        proyecto=NOMBRE_PROYECTO
    )

if __name__ == "__main__":
    app.run(debug=True)
    