# App Base FastApi

# Create venv with conda
virtualenv venv --python=/home/josericardo/anaconda3/envs/python39/bin/python 

# construir Dockerfile 
sudo docker build .

# listar imagenes
sudo docker images

# acceder al container

sudo docker run -it [ID CONTAINER] bash


# eliminar container
sudo docker rm [ID CONTAINER]


# eliminar todos los recursos
sudo docker images

# construir y subir contauiner
sudo docker-compose up --build

# bajar container
sudo docker-compose down
