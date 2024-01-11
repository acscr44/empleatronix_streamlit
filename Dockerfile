FROM python:3.8

# instalación de librerías streamlit:
RUN pip install streamlit

# se copia desde el ámbito local al ámbito del contenedor:
COPY src/* /app/

EXPOSE 8501

WORKDIR /app

ENTRYPOINT [ "streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0" ]