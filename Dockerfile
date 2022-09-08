FROM python:3

COPY . .

RUN pip install -r requirements.txt

EXPOSE 7000

ENTRYPOINT ["python","Serv.py"]