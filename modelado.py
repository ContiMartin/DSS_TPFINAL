from flask import Flask, request,render_template,views
from matplotlib.pyplot import get
import pandas as pd
import joblib
from tp_final_ import modelado


# create the Flask app
app = Flask(__name__)

@app.route('/')
def inicio(): 
    return render_template('formulario.html')

@app.route('/procesar', methods=['POST'])
def procesar():
    print("datos")
    persona= []
    persona.append(request.form.get("edad"))
    persona.append(request.form.get("ingresoAnual"))
    persona.append(request.form.get("situacion"))
    persona.append(request.form.get("antiguedadEmpleoActual"))
    persona.append(request.form.get("objetivoPrestamo"))
    persona.append(request.form.get("gradoPrestamo"))
    persona.append(request.form.get("montoPrestamo"))
    persona.append(request.form.get("tasaInteres"))
    persona.append(request.form.get("ingresoSobreSueldo"))
    persona.append(request.form.get("mora"))
    persona.append(request.form.get("AñosHistorialCred")) 
    #persona.append(0)
    persona = [float(x) for x in persona]
    pr = modelado()
    pr.cargaDeDatos()
    pr.mapeoDatos()
    pr.eliminarVacios()
    pr.credit = pr.credit.drop('Estado_préstamo',axis=1)
    persona2 = (persona - pr.credit.min())/(pr.credit.max()- pr.credit.min())  
    modelo = joblib.load('rfc.pkl') # Carga del modelos.
    #modelo = joblib.load('svc.pkl')
    #modelo.prediccion(persona)
    result = modelo.predict([persona2])[0]
    print("prediccion",result)
    if result == 1:
        result="El usuario no te va a pagar"
        imagen = "./static/rechazado.jpg"
    else:
        result= "El usuario es confiable"
        imagen = "./static/aceptado.jpg"

    return render_template(("index.html") , result=result,name= request.form.get("nombre"),image = imagen)


if __name__ == '__main__':
    # run app in debug mode on port 5000
    app.run(debug=True, port=5000)