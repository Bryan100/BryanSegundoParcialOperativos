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
  intocables = ["comandos.py","URI.py","miAmbiente","README.md"]
  if nombre in intocables:
    return True
  else:
    rp = Popen(["rm",nombre], stdout=PIPE, stderr=PIPE)
    rp.wait()
    return False if nombre in darTodosArchivos() else True

def darRecientes():
  files = darTodosArchivos()
  files.sort(key=lambda x: os.path.getmtime(x), reverse=True)
  files = [str(x) for x in files]
  return "Archivos del Mas Reciente al Mas Antiguo- ", filter(None,files)