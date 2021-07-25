FROM python:3
RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
RUN pip install django \
&& pip install --upgrade pip \
&& pip install djangocms-installer \
&& pip install django-cassandra-engine \
&& pip install psycopg2 \
&& djangocms vlog 
RUN apt-get update \
&& apt-get install vim -y
WORKDIR /usr/src/app/vlog
COPY initializecms.py .
COPY adduser.py .
ENTRYPOINT ["python", "initializecms.py"]
CMD ["admin","admin","admin@local.org","0.0.0.0:80"]
