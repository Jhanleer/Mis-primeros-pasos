import tensorflow as tf
#el numpy es para el manejo de arreglos, matrices y vectores
import numpy as np
#el matplotlib es para graficar
import matplotlib.pyplot as plt

metro = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9], dtype=float)
pie= np.array([3.28, 6.56, 9.84, 13.12, 16.40, 19.68, 22.96, 26.24, 29.52], dtype=float)

#aqui se crea el modelo de la red neuronal
#el modelo secuencial es para que las capas de la red neuronal se vayan agregando una tras otra
#el dense es para que la neurona tenga una sola entrada y una sola salida
#el units es para que la neurona tenga una sola salida
#el input_shape es para que la neurona tenga una sola entrada
capa= tf.keras.layers.Dense(units=1, input_shape=[1])
modelo= tf.keras.Sequential([capa])


#capa= tf.keras.layers.Dense(units=1, input_shape=[1])
#modelo= tf.keras.Sequential([capa])
#oculta1= tf.keras.layers.Dense(units=3, input_shape=[1])
#oculta2= tf.keras.layers.Dense(units=3)
#salida= tf.keras.layers.Dense(units=1)
#modelo= tf.keras.Sequential([oculta1, oculta2, salida]) 

#el compile es para que la red neuronal se compile y se pueda entrenar
modelo.compile(
    optimizer= tf.keras.optimizers.Adam(0.1),
    loss= "mean_squared_error"
)

print("Entrenando...")
#el .fit es para el entrenamiento de la IA, ahi es donde se mete los valores o neuronas que van a ser entrenadas
historial= modelo.fit(metro, pie, epochs=500, verbose=False)

print("Modelo entrenado!")

plt.xlabel(" # Epoca")
plt.ylabel("Magnitud de perdida")
plt.plot(historial.history["loss"])
plt.show()

print("Let's make a prediction!")
resultado = modelo.predict([10.0])
print("El resultado es ", (resultado) , " pies")

print("Variables internas del modelo")
print(capa.get_weights())
#el get_weights es para obtener los pesos de la neurona
#print(oculta1.get_weights())
#print(oculta2.get_weights())
#print(salida.get_weights())