FROM apache/nifi:1.12.0
ADD iris.csv ./
ADD iris.json ./
ADD postgresql-42.5.3.jar ./
