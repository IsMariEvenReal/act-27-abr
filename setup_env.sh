#!/bin/bash
echo "Actualizando paquetes..."
#"sudo" se refiere al superusuario (el que llamaríamos Admin en Windows)
#"-y" hace, básicamente, que se diga sí a todo, sin requerir el input del usuario
sudo apt-get update -y
echo "Instalando Git..."
sudo apt install git -y
echo "Instalando Python3..."
sudo apt install python3 python3-pip -y #Este comando también instala pip, necesario para instalar librerías para Python
echo "Instalando Docker..."
#Sí,todos estos comandos son necesarios para instalar Docker en Ubuntu (o al menos eso me dice Google)
sudo apt install apt-transport-https ca-certificates curl software-properties-common
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
sudo apt update
sudo apt install docker-ce docker-ce-cli containerd.io
#Aquí ya ha terminado la instalación de Docker
echo "Entorno preparado correctamente."