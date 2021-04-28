# Mini Curso
## R, Python, MySQL para el analisis de Datos

### Requetimientos

1. Linux (server,desktop, o subsistema de Windows) Ubuntu 20.04 LTS.

```bash
# Opcional: Editor in-terminal
sudo apt install neovim
```

2. Herramientas de desarrollo Python. Ejecutar desde el terminal linux:

```bash
$ sudo apt-get install python3-dev python3-pip python3-venv
$ python3 -m pip install --upgrade pip
```

3. Instalacion R:

```bash
$ sudo apt-get install r-base
```

4. Instalacion Rstudio Server

```bash
$ sudo apt-get install gdebi-core
$ wget https://download2.rstudio.org/server/bionic/amd64/rstudio-server-1.4.1106-amd64.deb
$ sudo gdebi rstudio-server-1.4.1106-amd64.deb
```

Hecho esto se muestra un mensaje notificando que `rstudio-server.service` se encuentra activo. Se puede corroborar que se encuentra correctamente instaldo abriendo en el navegador, en el localhost, puerto 8787:

http://localhost:8787/auth-sign-in?appUri=%2F

Se mostrara una pantalla de login de Rstudio. Las credenciales de acceso coinciden con su usuario de linux. Una vez ingresadas las credenciales se abre el IDE de Rstudio.

5. Instalacion de MySQL:

```bash
$ sudo apt update
$ sudo apt install mysql-server
$ sudo mysql_secure_installation
```

Nos aparacera un mensaje al que respondemos con "y" (o "s" si nuestra instalación de Ubuntu esta en español).

Luego, nos pide elegir el nivel de seguridad del mecanismo de autenticación, solo para este ejemplo escribimos "0" (cero) para establecer una seguridad baja, si desea puede establecerla en "2" para alta, pero necesitara ingresar un mecanismo alterno de seguridad como una frase o un archivo KEY. 

Luego, se nos pedirá definir una clave de acceso para el usuario root de MySQL, para este ejemplo establecemos la misma clave de acceso de nuestro usuario linux ubuntu. Y en los mensajes subsiguientes respondemos con "y", hasta que al final nos aparezca el mensaje `All done!`

Para corroborar que la instalación se realizó correctamente ejecutamos:

```bash
sudo mysql
```

Y se nos muestra el Shell de MySQL, este terminal admite comandos SQL, por ejemplo podemos ejecutar:

```MySQL
mysql> SELECT user FROM mysql.user;
mysql> exit
```

Y se nos mostrara la lista de usuarios de MySQL, donde se encuentra el usuario root, con el que nos logeamos a MySQL.


### Carpeta de trabajo

Una vez instalados los paquetes, pude descargar la carpeta de trabajo del curso usando GIT (repositorio de GitHub), para este ejemplo creamos una carpeta llamada `ProyectoSEE` donde se almacenara la carpeta del este curso con todo el codigo que usaremos:


```bash
$ cd ~
$ mkdir ProyectoSEE
$ git clone https://github.com/CristianPachacama/Mini_Curso_Python_R_MYSQL

```

Hecho esto se crea la carpeta Mini_Curso_Python_R_MYSQL dentro del directorio ProyectoSEE, con todo lo que necesitaremos a continuación.


### Ambiente trabajo Python

Para poder desarrollar cualquier proyecto con codigo python es aconsejable (con miras a la puesta en producción de nuestro código en un servidor) crear un ambiente de trabajo. Para ello, nos dirijimos a nuestra carpeta de trabajo, y ejecutamos lo siguiente:

```bash
$ cd Mini_Curso_Python_R_MYSQL
$ python3 -m venv env
```

Hecho esto se crea un carpeta llamada `env/` que va a almacenar todos los paquetes y el interprete que nos permitirá ejecutar nuestro código python.

## Datos

A modo de ejemplo supongamos que queremos analizar datos de clientes de una entidad financiera que se encuentran en un archivo csv. Puede verlos en la carpeta `data/` que se encuentra en la carpeta de trabajo. 


## Limpieza

Una primera etapa y obvia es la limpieza de estos datos. Entonces usaremos las herramientas de python con ese objetivo. Para ello usaremos la interfaz de Rstudio. Es decir, abrimos en nuestro navegador:

http://localhost:8787/auth-sign-in?appUri=%2F


Si Rstudio Server se encuentra ejecutandose en un servidor remoto, se debe reemplazar `localhost` por el IP del servidor.

Una vez en esta página y logeado con sus credenciales (ubuntu), se muestra el IDE de Rstudio.

En el panel "Files" que se encuentra en el lado inferior derecho. podemos ver nuestro directorio de trabajo. Por defecto, la carpeta que muestra es el directorio `/home/` de nuestro usuario ubuntu.

Buscamos el directorio donde descargamos nuestro repositorio Git, en este caso: `ProyectoSEE/Mini_Curso_Python_R_MYSQL/`

Una vez en el directorio, nos dirigimos al icomo:
 ⚙️ More => Set as working directory

 Así quedara seteada nuestra carpeta de trabajo en esta locación.


### Notebook

Pues bien, ahora podemos crear nuestro primer notebook de trabajo. Para ello vamos a la esquina superior izquerda de la interfaz y clicamos en el icono de ✅🗒️ (New File), debajo del boton `File`, aquí eleginos la opción `R Notebook`. La primera vez una ventana nos pide instalar unos paquetes adiciones, damos clic en aceptar y esperamos a que termine la instalacion en la Consola.

Hecho esto se crea un archivo de Demo con codigo preparado, que podemos ejecutar, aunque primero es necesario guardar este archivo en nuestro directorio de trabajo. Una vez guardado ver el resultado del notebook clicando el icono celeste `Preview`,


