# Usa l'immagine Python come base
FROM python:3.9-slim

# Crea la cartella dell'applicazione
WORKDIR /app

# Copia i file necessari
ADD . /app

# Installa i pacchetti Python richiesti
RUN pip install feedparser

# Avvia lo script Python direttamente
CMD ["python", "/app/rss_reader.py"]