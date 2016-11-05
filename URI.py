from flask import Flask, abort, request
import json
from comandos import darTodosArchivos, borrarArchivo, agregarArchivo, darRecientes

app = Flask(__name__)

@app.route('/files',methods=['POST'])
def crearArchivo():
  datos = request.get_json(silent=True)
  nombre = datos['filename']
  contenido = datos['content']
  agregarArchivo(nombre,contenido)
  return "el archivo ha sido creado",201

@app.route('/files',methods=['GET'])
def darArchivos():
  list = {}
  list["Documentos:"] = darTodosArchivos()
  return json.dumps(list), 202

@app.route('/files',methods=['PUT'])
def errorSolicitud():
  abort(404)

@app.route('/files',methods=['DELETE'])
def eliminarArchivos():
  error = False
  for docActual in darTodosArchivos():
    if not borrarArchivo(docActual):
        error = True

  if error:
    return 'Algunos documentos no fueron eliminados!', 400
  else:
    return 'Carpeta Reseteada!', 200 


@app.route('/files/recently_created',methods=['POST'])
def errorPost():
  abort(404)

@app.route('/files/recently_created',methods=['GET'])
def darRecientesL():
  return darRecientes()

@app.route('/files/recently_created',methods=['PUT'])
def errorPut():
  abort(404)

@app.route('/files/recently_created',methods=['DELETE'])
def errorDelete():
  abort(404)


if __name__ == "__main__":
  app.run(host='0.0.0.0',port=8088,debug='True')