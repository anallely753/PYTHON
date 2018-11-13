from sklearn import tree

""""
(Features)

"""

features=[[150,0],[170,0],[140,1],[130,1]]
labels=['Naranja','Naranja','Manzana','Manzana']


#Arbol de decision
clasificador=tree.DecisionTreeClassifier()

#fit ->el algoritmo de aprendizaje incluido 
clasificador=clasificador.fit(features, labels)

print(clasificador.predict([[150,0]]))