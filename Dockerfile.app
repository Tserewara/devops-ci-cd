FROM ubuntu

WORKDIR /source

ENV POSTGRES_HOST=damarowahutu-db

ENV POSTGRES_PASSWORD=tserewara

RUN apt-get update

RUN apt-get install -y python3 && apt-get install -y python3-pip

COPY . /source

RUN pip3 install -r requirements.txt

CMD ["sh", "start.sh"]

EXPOSE 8000