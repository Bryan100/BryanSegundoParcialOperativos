from comandos import *

def test_agregar():
  nombreArchivo = "prueba"
  contenido = "..."

  lista = darTodosArchivos()
  cantidadInicial = len(lista)

  agregarArchivo(nombreArchivo,contenido)
  listaB = darTodosArchivos()

  cantidadFinal = len(listaB)
  cantidadIdeal = cantidadInicial + 1

  assert cantidadIdeal == cantidadFinal,"La Cantidad_Final de Archivos deberia ser = La Cantidad_Inicial + 1"

def test_borrar():
  nombreArchivo = "prueba.txt"

  lista = darTodosArchivos()
  cantidadInicial = len(lista)

  borrarArchivo(nombreArchivo)
  listaB = darTodosArchivos()

  cantidadFinal = len(listaB)
  cantidadIdeal = cantidadInicial - 1

  assert cantidadIdeal == cantidadFinal,"La Cantidad_Final de Archivos deberia ser = La Cantidad_Inicial - 1"

def test_darTodos():
   
   primerMuestreo = len (darTodosArchivos())
   
   agregarArchivo("Primero","...");
   agregarArchivo("Segundo","...");
   
   segundoMuestreo = len(darTodosArchivos())

   borrarArchivo("Primero.txt");
   agregarArchivo("Tercero","...");
   agregarArchivo("Cuarto","...");
   agregarArchivo("Primero","...");

   tercerMuestreo = len(darTodosArchivos());
  
   borrarArchivo("Primero.txt");
   borrarArchivo("Segundo.txt");
   borrarArchivo("Tercero.txt");
   borrarArchivo("Cuarto.txt");

   cuartoMuestreo = len (darTodosArchivos());

   assert primerMuestreo == cuartoMuestreo and primerMuestreo + 2 == segundoMuestreo and primerMuestreo + 4 == tercerMuestreo
