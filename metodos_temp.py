from flask import Flask
from flask import Blueprint
from flask import request
from flask import jsonify
from werkzeug.utils import secure_filename
import json
from flask_cors import CORS, cross_origin 
import numpy as np
import requests
import math
from scipy.spatial import distance

class MetodosTemp:
    ######################
    # Llamar a OpenFaceAPI y devolver el vector de características
    def callOpenFaceAPI(path):
        url = 'http://0.0.0.0:81/openfaceAPI'
        files = {'file': open(path, 'rb')}

        result = requests.post(url, files=files)
        result = result.json()

        return result

    ######################

    def savePathAsis(f):
        # Guardar temporalmente la foto para ser procesada
        filename = f.filename
        path  = "/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/foto_compare/" + filename
        f.save(path)
        return path

    def savePath(f):
        # Guardar temporalmente la foto para ser procesada
        filename = f.filename
        path  = "/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img/" + filename
        f.save(path)
        return path

    #########################

    def transformacion(entrada):
        vector = str(entrada["result"])
        vector = vector.replace('{','')
        vector = vector.replace('}','')
        vector = vector.replace('[','')
        vector = vector.replace(']','')
        vector = vector.replace("\\","")
        vector = ''.join(vector.split('\n'))
        vector = vector.strip()
        return vector
    
    def transformacion2(vector):
        vector = ", ".join(vector)
        vector = vector.replace('{','')
        vector = vector.replace('}','')
        vector = vector.replace('[','')
        vector = vector.replace(']','')
        vector = vector.replace("\\","")
        vector = ''.join(vector.split('\n'))
        vector = vector.strip()
        return vector

    def toString(string):
        result = string.replace('{','').replace('}','')
        result = list(result.split(','))
        return result
    
    @staticmethod
    def toFloat(arr):
        vector = []
        for i in arr.split(): 
            vector.append(float(i.replace(",","")))
        return vector
    
    @staticmethod
    def Euclides(vector1, vector2):
        if not vector1 or not vector2:
            return float('inf')

        vector1 = vector1.replace(' ', ',')
        vector2 = vector2.replace(' ', ',')

        lista_floats1 = [float(valor) for valor in vector1.split(',') if valor.strip()]
        lista_floats2 = [float(valor) for valor in vector2.split(',') if valor.strip()]

        resultado = distance.euclidean( lista_floats1, lista_floats2)
        """ resultado = distance.euclidean(lista_floats1[:math.floor(len(lista_floats1)/2)], lista_floats2) """
        return resultado
