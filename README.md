# Sistema Inventario BackEnd


### create environment
>   python-m venv zaiko-env
    

### access environment
>   source zaiko-env/bin/activate

### install libs
>   pip install -r requirements.txt 
    
### generate image
>   docker build -t zaiko .

## Run dockr-compose
3 services are present in file `docker-compose.yml`:
- zaiko: backend (fastapi)
- db: database
- adminer: database manager

### run container by...
>   docker-compose up -d 
