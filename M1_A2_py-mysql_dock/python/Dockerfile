FROM python:3.9

RUN pip install pandas
RUN pip install pymysql
RUN pip install SQLAlchemy
RUN pip install cryptography
WORKDIR /usr/app/src

COPY connect_mysql.py ./
