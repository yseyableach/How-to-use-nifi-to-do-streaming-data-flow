
From python:3.8.16-buster


COPY . ./
# upgrade pip
RUN pip install --upgrade pip

# install selenium
RUN pip install psycopg2

CMD [ "python","./test_connection.py" ]