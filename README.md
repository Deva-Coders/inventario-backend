## BackEnd Inventory System

## Steps to run locally

### 1. Clone the repository
```bash
git clone https://github.com/Deva-Coders/inventario-backend.git
```

### 2. Access the cloned folder
```bash
cd inventario-backend
```

### 3. Create the virtual environment
```bash
python -m venv zaiko-env
```

### 4. Activate the virtual environment
```bash
source zaiko-env/bin/activate
```

### 5. Install packages
```bash
pip install -r requirements.txt
```

### 6. Generate docker image
```bash
docker build -t zaiko . 
``` 

### 7. Start container
```bash
docker-compose up -d
```
    
> [!TIP]
Run dockr-compose
3 services are present in file `docker-compose.yml`:
> - zaiko: backend (fastapi)
> - db: database
> - adminer: database manager