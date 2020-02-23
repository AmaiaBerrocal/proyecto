# Proyecto pygame

# Instrucciones de instalación

1. Crear, si se desea, un entorno virtual y activarlo:

```
python3 -m venv <nombre_del_entorno>
source <nombre_del_entorno>/bin/activate
```

2. Instalar las dependencias del fichero requirements.txt

```
pip install -r requirements.txt
```

3. Crear base de datos en el directorio data:

```
sqlite3 data/database.db
```
Después: 

```
.read score_table.sql
```

4. Lanzar la aplicación

```
python main.py
```