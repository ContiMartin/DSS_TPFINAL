from flask import Flask, request,render_template,views
from matplotlib.pyplot import get
import pandas as pd
import matplotlib.pyplot as plt
import base64
import io 

# create the Flask app
app = Flask(__name__)

@app.route('/')
def inicio(): 
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    # cantidadEquipos = int(request.form.get("cantidadEquipos"))
    # nombreTorneo = request.form.get("nombreTorneo")
    # listas = request.form.getlist("lista[]")
    # torneo= Torneo(cantidadEquipos=cantidadEquipos,nombreTorneo=nombreTorneo)
    # simu=Simulacion(torneo) 
    # datosSimulacion,datos=simu.simular(listas,cantidadEquipos,1)
    # simu.obtenerGrafico(datos)
    return render_template("index.html") #, datos = datosSimulacion)

# @app.route('/graficar')
# def graficar():
#     return render_template('graficar.html', rutas=list(rutas.values()))


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5002)