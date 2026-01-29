FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y curl
# Copy only requirements first to use Docker cache
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Now copy backend code
COPY . /app

# Tell Flask where templates/static are (optional but safe)
ENV FLASK_APP=app.py
ENV PYTHONUNBUFFERED=1

EXPOSE 5000

CMD ["python", "app.py"]
