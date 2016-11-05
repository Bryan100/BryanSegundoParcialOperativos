# BryanSegundoParcialOperativos

Estudiante | Código
--- | --- | ---
Bryan Estiben Pérez Parra| 12203030

## Tutorial de Ejecución

#### URL Del Repositorio:
https://github.com/Bryan100/BryanSegundoParcialOperativos.git

#### Paso 0. Inicie sesión en su Maquina Virtual (preferiblemente con la Consola de Putty.exe), ingresando su username y password.


#### Paso 1. Verificar que la interfaz-puente de la maquina virtual esté arriba. De lo contrario, ejecute el sgte comando:
      ifup ethx, donde el caractér 'x' varía según el número asignado a la interface puente 
      
#### Paso 2. Ir a la carpeta /home y crear un directorio con el nombre "jenkinUser" (Ver Comandos Abajo):
 
Comando | Propósito
--- | --- | ---
cd /home | Ir al directorio /home
mkdir jenkinUser | Crear la carpeta "jenkinUser"


#### Paso 3. Ubicarse dentro de la carpeta recien creada (jenkinUser) y clonar el repositorio nombrado ánteriormente (Verificar primero que la maquina virtual tiene instalado la librería de git)

Comando | Propósito
--- | --- | ---
cd .../jenkinUser | Ir al directorio jenkinUser
git clone https://github.com/Bryan100/BryanSegundoParcialOperativos.git  | Copiar los archivos del repositorio en la carpeta
yum install git | Instalar la librería git, si es necesario

#### Una vez ejecutado los comandos anteriores, debieron haber quedado guardados los sgts archivos:

Comando | Propósito
--- | --- | ---
URI.py | C
comandos.py | Contiene los algoritmos de la aplicación

Nombre Algoritmo-App | Parametros | Descripción
--- | --- | ---
darTodosArchivos | --- | Muestra todos los archivos que hay dnetro de la carpeta jenkinUser
agregarArchivo | Nombre Del Documentos, Contenido del Documento | Genera, dentro de la carpeta jenkinUser, un archivo con extensión .txt
borrarArchivo | Nombre Del Documentos + Extensión (Ej: .txt) | Elimina el archivo especificado, si existe, de la carpeta jenkinUser
darRecientes | --- | Entrega todos los archivos que hay dentro de la carpeta jenkinUser, desde el más reciente hasta el más antiguo.
        
5. Se asume que su maquina virtual tiene las librerias necesarias para configurar entornos virtuales. Cree un entorno virtual
    dentro de la carpeta "miDirectorio"
    
$ virtualenv miAmbiente

6. Active el ambiente virtual creado

$ . miAmbiente/bin/activate

Con el ambiente activo, instale la libreria Flask

$ pip install Flask

Ahora dentro de la carpeta "miDirectorio" deberían estár 3 archivos importantes (Anque pueden haber más)
    - URI.py - Aqui estan configurardas las URL que se van a ejecutar desde un navegador
    - comandos.py - Aqui se definen algunos subprocesos que son consumidos por el archivo URI.py
    - miAmbiente - Es el ambiente virtual creado, el cual me va a permitir subir los servicios configurados en URI.py a la nube

8. Dentro del archivo URI.py, está configurado el puerto 8088, para escuchar las peticiones que hará el navegador de internet. Se
    recomiendo verificar que dicho puerto esté disponible y activo.
    
8.1 Para verificar que esté activo ejecute los siguientes comandos:
## cd /etc/sysconfig
## nano iptables
Dentro del archivo "iptables" verificar que el puerto esté disponible para recibir las peticiones necesarias. En caso
contrario, configurarlo escribiendo la siguiente linea de codigo: 
-A INPUT -m state --state NEW -m tcp -p tcp --dport 8088 -j ACCEPT

En caso de que el puerto esté ocupado y por ende toque cambiarlo, se procede a modificar su numero en el archivo
    URI.py y activarlo en el archivo iptables. Recuerde reiniciar el archivo con "service iptables restart", en caso de cambios

9. Con el ambiente virtual activado, procedemos a ejecutar los siguientes comando:
#python URI.py

El servicio a esta alturas ya debería estár en la nube.

10. Para saber que servicios provee los algoritmos confirgurados y como solicitarlos desde la extension Postman de google, se recomienda
    ver el archivo "ContratoServicios.png"
    
11. Abra la extension Postman de Google Chrome y comience a jugar con los diferentes servicios.
