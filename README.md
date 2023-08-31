# Reconocimiento de entidades nombradas con Phyton #
#### 1 - Instalar requirements.txt -> pip install -r requirements.txt ####
#### 2 - Ejecutar  python -m spacy download es_core_news_sm, para la descarga del modelo #####
#### 3 - El programa se ejecuta desde index.py -> python index.py ####
#### 4 - Usar postman o thhunder client como cliente ####
#### 5 - La ruta es 'http://127.0.0.1:5000/api/entidades'  -> method post ####
#### 6 - Ingresar una peticion con un body ejemplo #####
{
 "oraciones": [
 "Apple está buscando comprar una startup del Reino Unido por mil millones de dólares.",
 "San Francisco considera prohibir los robots de entrega en la acera."
 ]
}

