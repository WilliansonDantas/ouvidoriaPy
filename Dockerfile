FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app
COPY src/wait-for-it.sh /app/wait-for-it.sh

RUN chmod +x /app/wait-for-it.sh

ENV PYTHONPATH="${PYTHONPATH}:/app"

CMD ["./wait-for-it.sh", "db", "5432", "--", "python", "src/main.py"]
