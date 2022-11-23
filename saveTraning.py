import joblib  

def cargarDatos():
    # Ahora supongamos que tenemos el siguiente modelo, clf_rf, ya entrenado:

    clf_rf.fit(x_train, y_train) # Entrenamiento del modelo

    # Podemos guardarlo realizando un joblib.dump():

    joblib.dump(clf_rf, 'modelo_entrenado.pkl') # Guardo el modelo.

    # El modelo se guardará en el fichero “modelo_entrenado.pkl” dentro del directorio que hayamos establecido por defecto en nuestro intérprete de Python.
    # 2. Carga del modelo entrenado

    # Cuando necesitemos cargar el modelo ya entrenado, simplemente hacemos un joblib.load():

    clf_rf = joblib.load('modelo_entrenado.pkl') # Carga del modelo.

    # Si queremos asegurarnos que el modelo se ha guardado correctamente, podemos calcular el rendimiento del modelo antes de guardarlo y al cargarlo de nuevo de la siguiente forma:

    clf_rf.score(x_train, y_train)