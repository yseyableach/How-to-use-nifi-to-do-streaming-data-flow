import psycopg2

# Update connection string information

host = "172.20.0.2"
dbname = "postgres"
user = "jay"
password = "1234"
sslmode = "allow"
# Construct connection string
conn_string = "host={0} user={1} dbname={2} password={3} sslmode={4}".format(host, user, dbname, password, sslmode)
conn = psycopg2.connect(conn_string)
print("Connection established")
