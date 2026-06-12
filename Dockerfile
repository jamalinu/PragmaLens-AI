# Usa una imagen oficial de Python ligera
FROM python:3.10-slim

# Establece el directorio de trabajo en el contenedor
WORKDIR /code

# Copia el archivo de requisitos e instala las dependencias
COPY ./requirements.txt /code/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copia todo el código del proyecto al contenedor
COPY . .

# Expone el puerto por defecto de Hugging Face Spaces (7860)
EXPOSE 7860

# Comando para ejecutar la app FastAPI apuntando al puerto correcto
CMD ["uvicorn", "pragmalens_app:app", "--host", "0.0.0.0", "--port", "7860"]
