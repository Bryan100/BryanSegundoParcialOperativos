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


## mkdir miDirectorio

3. Ubiquese dentro del directorio recien creado y haga la clonación de este repositorio, de la
    siguiente manera:
    
    A) cd miDirectorio
    B) git clone https://github.com/Bryan100/EntregaParcialOperativos.git
    https://github.com/Bryan100/BryanSegundoParcialOperativos.git
Tip: Asegúrese que su maquina virtual tiene instalado la librería de Git

4. Con los comandos anteriores debieron haber quedado los archivos de ejecución que contienen
    los algoritmos de ejecución:
        *URI.py
        *comandos.py
        
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
