sudo mkdir volumen
docker run -it --net=host --name contenedor_web -v "$PWD"/volumen:/home/volumen -h contenedor -p 8080:8080 ubuntu:24.04

apt update
apt upgrade -y
apt install python3 -y
apt install python3-pip -y
apt install python3.12-venv -y
apt install sqlite3 -y
python3 -m venv .venv
source .venv/bin/activate
pip install web.py
pip install request
pip install requests