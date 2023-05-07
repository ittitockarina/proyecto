from flask import request, jsonify, Blueprint

openface = Blueprint('openface', __name__)

@openface.route('openface', request=['POST'])
def openface(): 
    if request.method == 'POST':
        f = request.files['file']
        
        # si queremos guardar la foto
        filename = f.filename
        path = "/Documentos/2023/softare_construction/proyecto/backend/img" + filename
        f.save(path)       
           
   
        # call openfaceAPI ##################################
        url = 'http://0.0.0.0:81/openfaceAPI'
        files = {'file': open(path, 'rb')}
        #files = {'file': f}

        result = request.post(url, files=files)

        print(result.json())
        ######################################################

    return jsonify(result.json())