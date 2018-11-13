

```python
import pandas as pd
```


```python
data=pd.read_csv("/home/mayito/Escritorio/PYTHON/prebes.csv")
```


```python
data.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Prebe</th>
      <th>Nombre</th>
      <th>Sexo</th>
      <th>Carrera</th>
      <th>Edad</th>
      <th>Estatura</th>
      <th>No.Cuenta</th>
      <th>Peso</th>
      <th>Calificacion</th>
      <th>CursoInter</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>18</td>
      <td>Ana</td>
      <td>f</td>
      <td>Industrial</td>
      <td>20</td>
      <td>1.65</td>
      <td>31484533</td>
      <td>56</td>
      <td>10</td>
      <td>Web</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1</td>
      <td>Michelle</td>
      <td>f</td>
      <td>civil</td>
      <td>21</td>
      <td>1.54</td>
      <td>314184534</td>
      <td>45</td>
      <td>9</td>
      <td>Redes</td>
    </tr>
    <tr>
      <th>2</th>
      <td>2</td>
      <td>Diego</td>
      <td>m</td>
      <td>Industrial</td>
      <td>20</td>
      <td>1.65</td>
      <td>31484535</td>
      <td>56</td>
      <td>10</td>
      <td>Web</td>
    </tr>
    <tr>
      <th>3</th>
      <td>3</td>
      <td>Arely</td>
      <td>f</td>
      <td>Industrial</td>
      <td>20</td>
      <td>1.65</td>
      <td>31484556</td>
      <td>56</td>
      <td>10</td>
      <td>Web</td>
    </tr>
    <tr>
      <th>4</th>
      <td>3</td>
      <td>Isabel</td>
      <td>f</td>
      <td>Industrial</td>
      <td>20</td>
      <td>1.65</td>
      <td>31484573</td>
      <td>56</td>
      <td>10</td>
      <td>Web</td>
    </tr>
  </tbody>
</table>
</div>




```python
data.columns.values
```




    array(['Prebe', 'Nombre', 'Sexo', 'Carrera', 'Edad', 'Estatura',
           'No.Cuenta', 'Peso', 'Calificacion', 'CursoInter'], dtype=object)




```python
data.dtypes
```




    Prebe             int64
    Nombre           object
    Sexo             object
    Carrera          object
    Edad              int64
    Estatura        float64
    No.Cuenta         int64
    Peso              int64
    Calificacion      int64
    CursoInter       object
    dtype: object




```python
datos2=open("/home/mayito/Escritorio/PYTHON/prebes.csv","r")
```


```python
columnas=datos2.readline().strip().split(",")
columnas
```




    ['18', 'Ana', 'f', 'Industrial', '20', '1.65', '31484533', '56', '10', 'Web']




```python
num_columnas=len(columnas)
contador=0
diccionario={}
for c in columnas:
    diccionario[c]=[]
diccionario
```




    {'1.65': [],
     '10': [],
     '18': [],
     '20': [],
     '31484533': [],
     '56': [],
     'Ana': [],
     'Industrial': [],
     'Web': [],
     'f': []}




```python
for linea in datos2:
    valores=linea.strip().split(",")
    for i in range(num_columnas):
        diccionario[columnas[i]].append(valores[i])
    contador += 1
print("El dataset tiene %d filas y %d columnas"%(contador,num_columnas))
```

    El dataset tiene 17 fias y 10 columnas



```python
dataframe=pd.DataFrame(diccionario)
dataframe.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>1.65</th>
      <th>10</th>
      <th>18</th>
      <th>20</th>
      <th>31484533</th>
      <th>56</th>
      <th>Ana</th>
      <th>Industrial</th>
      <th>Web</th>
      <th>f</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>1.65</td>
      <td>10</td>
      <td>3</td>
      <td>20</td>
      <td>31484556</td>
      <td>56</td>
      <td>Arely</td>
      <td>Industrial</td>
      <td>Web</td>
      <td>f</td>
    </tr>
    <tr>
      <th>1</th>
      <td>1.65</td>
      <td>10</td>
      <td>3</td>
      <td>20</td>
      <td>31484573</td>
      <td>56</td>
      <td>Isabel</td>
      <td>Industrial</td>
      <td>Web</td>
      <td>f</td>
    </tr>
    <tr>
      <th>2</th>
      <td>1.65</td>
      <td>10</td>
      <td>5</td>
      <td>20</td>
      <td>31484537</td>
      <td>56</td>
      <td>Dalia</td>
      <td>Industrial</td>
      <td>Web</td>
      <td>f</td>
    </tr>
    <tr>
      <th>3</th>
      <td>1.65</td>
      <td>10</td>
      <td>6</td>
      <td>20</td>
      <td>31484543</td>
      <td>56</td>
      <td>Karina</td>
      <td>Industrial</td>
      <td>Web</td>
      <td>f</td>
    </tr>
    <tr>
      <th>4</th>
      <td>1.65</td>
      <td>10</td>
      <td>7</td>
      <td>20</td>
      <td>31484536</td>
      <td>56</td>
      <td>Diana</td>
      <td>Industrial</td>
      <td>Web</td>
      <td>f</td>
    </tr>
  </tbody>
</table>
</div>




```python

```
