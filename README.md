# BryanSegundoParcialOperativos

Estudiante | Código
--- | --- | ---
Bryan Estiben Pérez Parra| 12203030

# Tutorial de Ejecución

## Modulo 1: Configurar La Aplicación, dentro de la Maquina Virtual

#### URL Del Repositorio:
https://github.com/Bryan100/BryanSegundoParcialOperativos.git

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
URI.py | Contiene la configuración de las URI's que permiten consumir los servicios de la aplicación, desde un navegador.

#### Los sgtes son los servicios que provee la aplicación, configurados dentro del archivo "comandos.py"

Nombre Algoritmo-App | Parametros | Descripción
--- | --- | ---
darTodosArchivos | --- | Muestra todos los archivos que hay dnetro de la carpeta jenkinUser
agregarArchivo | Nombre Del Documentos, Contenido del Documento | Genera, dentro de la carpeta jenkinUser, un archivo con extensión .txt
borrarArchivo | Nombre Del Documentos + Extensión (Ej: .txt) | Elimina el archivo especificado, si existe, de la carpeta jenkinUser
darRecientes | --- | Entrega todos los archivos que hay dentro de la carpeta jenkinUser, desde el más reciente hasta el más antiguo.
        
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
URI.py | Contiene la configuración de las URI's que permiten consumir los servicios de la aplicación, desde un navegador.
miAmbiente | Es el ambiente virtual creado, el cual me va a permitir subir los servicios, configurados en el archivo "URI.py", a la nube

#### Paso 6. Dentro del archivo "URI.py", está configurado el puerto 8088 para escuchar las peticiones que hará el navegador de internet. Se recomienda verificar que dicho puerto está disponible y activo, para esto usar los sgts comandos:
    
Comando | Propósito
--- | --- | ---
$ cd /etc/sysconfig | Ir a la carpeta sysconfig, donde se encuentra el archivo para configurar los puertos
$ nano iptables | Entrar al editor de texto, para modificar la configuración de los puertos
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8088 -j ACCEPT | Dentro del archivo "iptables", escribir esta linea para activar el puerto 8088, en caso de no estarlo. Si dicho puerto ya está siendo utilizado, escribir el nombre de otro que sí esté disponible y modificar el archivo URI.py, escribiendo el puerto nuevo a utilizar.
service iptables restart | Restaurar el archivo iptables, para que acepte y asimile los cambios

#### Paso 7. Con el ambiente virtual activado, procedemos a subir los servicios configurados a la nube:
      $ python URI.py

## Modulo 2: Ejecución y Prueba de La Solución
