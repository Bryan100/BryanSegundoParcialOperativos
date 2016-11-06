from subprocess import Popen, PIPE
import glob
import os

def darTodosArchivos():
  listaArchivos = Popen(["ls"], stdout=PIPE, stderr=PIPE)
  miLista = Popen(["awk",'-F',':','{print $1}'], stdin=listaArchivos.stdout, stdout=PIPE, stderr=PIPE).communicate()[0].split('\n')
  return filter(None,miLista)


def agregarArchivo(nombre,contenido):
  arc = open(nombre+'.txt','a')
  arc.write(contenido+'\n')
  arc.close()
  return "Archivo generado!",201


def borrarArchivo(nombre):
  intocables = ["comandos.py","test_comandos.py","miAmbiente","README.md"]
  if nombre in intocables:
    return "No Se Puede Borrar Este Archivo. Es Demasiado Valioso! D:"
  else:
    rp = Popen(["rm",nombre], stdout=PIPE, stderr=PIPE)
    rp.wait()
    return "El Archivo No Fue Eliminado" if nombre in darTodosArchivos() else "El Archivo Ha Sido Eliminado!"
