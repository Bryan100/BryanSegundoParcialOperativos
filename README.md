# BryanSegundoParcialOperativos

Estudiante | Código
--- | --- | ---
Bryan Estiben Pérez Parra| 12203030

# Tutorial de Ejecución

## Modulo 1: Configurar La Aplicación, dentro de la Maquina Virtual

#### URL Del Repositorio:
https://github.com/Bryan100/BryanSegundoParcialOperativos.git

#### URL Del Archivo README.md
https://github.com/Bryan100/BryanSegundoParcialOperativos/edit/master/README.md

#### Paso 0. Inicie sesión en su Maquina Virtual (preferiblemente con la Consola de Putty.exe), ingresando su username y password.

#### Paso 1. Verificar que la interfaz-puente de la maquina virtual esté arriba. De lo contrario, ejecute el sgte comando:
      $ ifup ethx, donde el caractér 'x' varía según el número asignado a la interface puente 
      
#### Paso 2. Ir a la carpeta /home y crear un directorio con el nombre "jenkinUser" (Ver Comandos Abajo):
 
Comando | Propósito
--- | --- | ---
$ cd /home | Ir al directorio /home
$ mkdir jenkinUser | Crear la carpeta "jenkinUser"


#### Paso 3. Ubicarse dentro de la carpeta recien creada (jenkinUser) y clonar el repositorio nombrado ánteriormente (Verificar primero que la maquina virtual tiene instalada la librería de git)

Comando | Propósito
--- | --- | ---
$ cd .../jenkinUser | Ir al directorio jenkinUser
$ git clone https://github.com/Bryan100/BryanSegundoParcialOperativos.git  | Copiar los archivos del repositorio en la carpeta
$ yum install git | Instalar la librería git, si es necesario

#### Una vez ejecutado los comandos anteriores, debieron haber quedado guardados los sgts archivos:

Comando | Propósito
--- | --- | ---
comandos.py | Contiene los algoritmos de la aplicación
test_comandos.py | Codumenta que ejecuta pruebas, por medio del framework de Pytest, para evaluar los algoritmos descritos en el archivo "comandos.py"
test_comandos.pyc | Es el archivo de compilación de "test_comandos.py"
README.md | Informe-Tutorial para ejecutar y probar la aplicación

#### Los sgtes son los servicios que provee la aplicación, configurados dentro del archivo "comandos.py" y son los algoritmos que vamos a exponer a pruebas, por medio de Pytest

Nombre Algoritmo-App | Parametros | Descripción
--- | --- | ---
darTodosArchivos | --- | Muestra todos los archivos que hay dnetro de la carpeta jenkinUser
agregarArchivo | Nombre Del Documentos, Contenido del Documento | Genera, dentro de la carpeta jenkinUser, un archivo con extensión .txt
borrarArchivo | Nombre Del Documentos + Extensión (Ej: .txt) | Elimina el archivo especificado, si existe, de la carpeta jenkinUser
        
#### A partir de aqui, se asume que las librerias necesarias, para configurar entornos virtuales, están instaladas.

#### Paso 4. Crear y Activar un entorno virtual, dentro de la carpeta "jenkinUser"
Comando | Propósito
--- | --- | ---
$ cd .../jenkinUser | Ir al directorio jenkinUser
$ virtualenv miAmbiente | Generar el Ambiente virtual
$ . miAmbiente/bin/activate | Activar el Ambiente virtual creado

#### Paso 5. Con el ambiente virtual activo, instalar la libreria Flask
      $ pip install Flask

#### Ahora dentro de la carpeta "jenkinUser" deberían estár, al menos, 3 archivos importantes

Archivo | Descripción
--- | --- | ---
comandos.py | Contiene los algoritmos de la aplicación
test_comandos.py | Codumenta que ejecuta pruebas, por medio del framework de Pytest, para evaluar los algoritmos descritos en el archivo "comandos.py"
test_comandos.pyc | Es el archivo de compilación de "test_comandos.py"
miAmbiente | Es el ambiente virtual creado, el cual me va a permitir subir los servicios, configurados en el archivo "URI.py", a la nube

#### Hasta este punto, ya están listos los archivos  con los servicios de la aplicación, los archivos con los algoritmos que permiten probar la eficacia de dichos servicios y el ambiente virtual que permite ejecutar los servicios definidos, por medio de la consola de python.

## Modulo 2: Ejecución y Prueba de La Solución

