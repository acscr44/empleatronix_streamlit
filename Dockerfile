FROM python:3.8

# instalación de librerías streamlit (solo en docker):
RUN pip install numpy pandas streamlit seaborn matplotlib

# se copia desde el ámbito local al ámbito del contenedor (solo en docker):
COPY src/* /app/
COPY data/* /app/data/

EXPOSE 8501

WORKDIR /app

ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]