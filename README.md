# Dockerd     
   
Pasos para crear un contenedor

```shell
    1  apt update
    2  apt upgrade -y
    3  apt install python3 -y
    4  apt install python3-pip -y
    5  apt install python3.12-venv -y
    6  apt install sqlite3 -y
    7  python3 -m venv .venv
   14  source .venv/bin/activate
   15  pip install web.py
   16  pip install request
   17  pip install requests
   19  cd home/volumen
   21  more hola.py
   24  python3 hola.py
```

```shell
    sudo mkdir volumen
    docker run -it --net=host --name contenedor_web -v "$PWD"/volumen:/home/volumen -h contenedor -p 8080:8080 ubuntu:24.04
    docker rmi b58bc5e797de para borrar una imagen
```

## DockerFile
1. FROM     ubuntu:24.04
2. RUN      apt update
3. COPY     web/ : /home/web/
4. CMD      ["python3","app.py"]