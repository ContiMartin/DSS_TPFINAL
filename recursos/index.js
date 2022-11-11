window.onload = () => {
    /**
     * Opciones de la red neuronal
     * dataUrl: url del archivo .json donde están nuestros datos.
     * task: Tipo de tarea a ejecutar en la red, para este ejemplo usaremos 'classification'
     * inputs: Datos de entrada, es decir, la fuente de datos usados para alimentar la red.
     * outputs: Datos de salida, es decir, la descripción de los datos de entrada.
     * debug: Define si se muestra o no la visualización del entrenamiento de la red neuronal en el html.
     */
    const options = {
      dataUrl: 'recursos/coordenadas.json',
      task: 'classification',
      inputs: ['x', 'y'],
      outputs: ['label'],
      debug: true,
    }
  
    // inicializamos la red neuronal
    const nn = ml5.neuralNetwork(options, normalize)
  
    // normalizamos los datos de esta
    function normalize () {
      nn.normalizeData()
      train()
    }
  
    // entrenamos el modelo de datos
    function train () {
      /**
       * epochs: En términos de redes neuronales, un 'epoch' se refiere a un ciclo completo sobre los datos de entrenamiento.
       * batchSize: Bloques de datos en que la información será procesada.
       * 
       * No hay una cantidad específica de epochs que se necesitan, pero se pueden hacer pruebas para encontrar la cantidad óptima de acuerdo a los resultados.
       */
      const trainigOptions = {
        epochs: 250,
        batchSize: 12,
      }
      nn.train(trainigOptions, classify)
    }
  
    // una vez entrenada nuestra red neuronal, procedemos a probar como se comporta frente a datos desconocidos.
    function classify () {
      // en este ejemplo le estamos pasando las coordenadas 300,350 las cuales corresponden al lado inferior izquierdo.
      const input = {
        x: 300,
        y: 350,
      }
      nn.classify(input, handleResults)
    }
  
    function handleResults (error, results) {
      // en caso de error, lo colocamos en consola
      if (error) {
        console.log(error)
        return
      // si todo es un éxito, podremos ver en la consola del navegador los resultados de la clasificación realizada.
      } else {
        console.log(results)
      }
    }
  } 