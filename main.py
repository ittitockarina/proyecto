from flask import Flask
from flask import request
from flask import jsonify
import requests

app = Flask(__name__) #instancia

@app.route('/openface', methods=['POST']) #wrap (decorator)
def openface(): 
    if request.method == 'POST':
        f = request.files['file']
        
        # si queremos guardar la foto
        filename = f.filename
        
        path = "/home/karolyto/Documentos/2023/softare_construction/proyecto/backend/img/"+ filename

        f.save(path)       
           
   
        # llamando al archivo  openfaceAPI creado en docker mediante su URL 
        url = 'http://0.0.0.0:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        #files = {'file': f}

        result = requests.post(url, files=files)
        print(result.json())

    return "hecho"

if __name__ == '__main__':
    app.run(debug=True, port=5000) 