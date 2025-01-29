import paramiko

# Configuración del cliente SSH
hostname = "example.com"
username = "usuario"
password = "contraseña"

# Crear cliente SSH
ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname, username=username, password=password)

# Ejecutar un comando en el servidor remoto
stdin, stdout, stderr = ssh.exec_command("ls -l")
print(stdout.read().decode())

# Cerrar la conexión
ssh.close()