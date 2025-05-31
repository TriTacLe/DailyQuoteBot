FROM python:3.12

ADD main.py .src

WORKDIR /

COPY requirements.txt .

RUN pip install requests  

COPY ./src ./src 

CMD ["python", "./src/main.py"]