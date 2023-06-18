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
    #call openfaceAPI, return vector de   caracteristicas 
    def callOpenFaceAPI(path):
        url = 'http://0.0.0.0:81/openfaceAPI'
        files = {'file': open(path, 'rb')}

        result = requests.post(url, files=files) # abriendo un archivo binario
        result = result.json()
    #print(result)

        return result

######################


    def savePathAsis(f):
    # Para guardar momentaneamente la foto para ser procesada
        filename = f.filename
        path  = "/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/foto_compare/" + filename
        f.save(path)
        return path

    def savePath(f):
    # Para guardar momentaneamente la foto para ser procesada
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
        #lista_floats = [float(valor) for valor in vector.split()]
        #tupla_floats = tuple(lista_floats)
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
        #lista_floats = [float(valor) for valor in vector.split()]
        #tupla_floats = tuple(lista_floats)
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
    
    def Euclides(vector1,vector2):
        """         lista_floats1 = [float(valor) for valor in vector1.split()]
        tupla_floats1 = tuple(lista_floats1)
        lista_floats2 = [float(valor) for valor in vector2.split()]
        tupla_floats2 = tuple(lista_floats2) """
        lista_floats1 = MetodosTemp.toFloat(vector1)
        tupla_floats1 = tuple(lista_floats1)
        lista_floats2 = MetodosTemp.toFloat(vector2)
        tupla_floats2 = tuple(lista_floats2)
        resultado = distance.euclidean(tupla_floats1, tupla_floats2)
        return resultado











