# Instrucciones para ejecutar este proyecto

- Clonar el proyecto y cambiar de rama
```bash
git clone https://github.com/nicolas197197/Entrega1_Nicolas_Grandich.git

cd Mi_primer_MVT

```

- Crear y activar entorno virtual (Windows)
```bash
C:\>python -m venv c:\ruta\al\entorno\virtual
C:\>c:\ruta\al\entorno\virtual\scripts\activate.bat
```

- Crear y activar entorno virtual (Linux)
```bash
python3 -m venv venv
source venv/bin/activate
```
- Instalar Django
```bash
pip install Django
```

- Crear base de datos con los Modelos (hacer migraciones y migrar)
```bash
python manage.py makemigrations app_coder

python manage.py migrate
```

- Crear super-usuario
```bash
python manage.py createsuperuser
```

- Ejecutar proyecto
```bash
python manage.py runserver
```
