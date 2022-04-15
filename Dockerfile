FROM python:3.8.13-bullseye

EXPOSE 8000

WORKDIR /app
COPY . .

RUN pip3 install -r requirements.txt

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]