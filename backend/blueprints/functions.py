import numpy as np
import requests

# Convertir Diccionario a Cadena
# Devuelve la lista de cadenas
def toString(dic):
    res = []
    result = dic['result'].replace("\n", "").replace("  ", " ").replace("[", "").replace("]", "") 
    result = list(result.split(' ')) 

    for i in result:
        if i == '':
            pass
        else:
            res.append(i)

    return res


# Convertir lista de cadenas en lista flotante
# Lista flotante de retorno
def stringToFloat(arr):
    vector = []
    for i in arr:
        vector.append(float(i))

    return vector


# Calcular la distancia euclidiana
# Return Float
def distanciaEuclidiana(vector1, vector2):
    dist = np.sqrt(np.sum(np.square(vector1 - vector2)))
    return dist


def savePath(f):
    # si queremos guardar la foto
    filename = f.filename
    path = "/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img/"+ filename
    f.save(path)

    return path


def callOpenFaceAPI(path):
    url =  'http://0.0.0.0:81/openfaceAPI'
    files = {'file': open(path, 'rb')}

    result = requests.post(url, files=files)
    result = result.json()

    return result