from sklearn.datasets import load_iris
from sklearn import tree
import numpy

iris = load_iris() #150 datos
target=numpy.delete(iris.target,[0,50,100])
data=numpy.delete(iris.data,[0,50,100],axis=0) #Features

#nuestros valores de prueba
prueba_target=iris.target[50]
prueba_data=iris.data[120]

clasificador=tree.DecisionTreeClassifier()
clasificador=clasificador.fit(data,target)
print("Prediccion para el elemento #50")
print(clasificador.predict([prueba_data]))

#el 1 indica que la prediccion fue correcta
print(iris.target_names[1])
