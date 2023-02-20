 
 
 ### Introduction
 In this lab , i will show you how to use nifi to do ETL streaming data.

### Use Docker to create your environment

- install Docker on your computer
- use the instructions to generate your environment
    ```
    docker compose up
    ```
- access to [localhost:8080/nifi](http://loaclhost:8080/nifi) and check your nifi  has been created successfully

- use any kind of your familiar database gui and connect to your postgresql database
    ```
    POSTGRES_DB: postgres
    POSTGRES_USER: jay #postgres
    POSTGRES_PASSWORD: 1234 #1234
    POSTGRES_PORT: 5432 #1234
    ```

### Start processing streaming data 

- access to [localhost:8080/nifi](http://loaclhost:8080/nifi)
- check your iris.json file in docker environment
![check file](image/check_your_iris_in_docker.png)
- go back to nifi web page and click Processor and choose **GetFile**
![check file](image/click_processor_getfile.png)
- go back to nifi web page and click Processor and choose **GetFile**
- You can use **pwd** on your nifi environment to check your iris.json path 
![check file](image/pwd_check_path.png)
- click right button on **GetFile** to and fill your **input directory** and **file filter** and click **Apply**
![check file](image/fill_to_getfile.png)
- click Processor and choose **ConverJsonToSQL**
![check file](image/click_processor_converjsontosql.png)
- click right button and set your **statement type** , **table name**(you should create the schema in database first) ,**JDBC Connection Pool**
![check file](image/configure_jdbc.png)
- click the arrow in **JDBC Connection Pool**,
set the properties on **Configure Controller Service** because of driver i have already dockerize in our environment , so you only need to import the file path.
    ```
    Database Connection URL: jdbc:postgresql://db:5432/postgres
    Database Driver Class Name : org.postgresql.Driver
    Database Driver Location(s) : /opt/nifi/nifi-current/postgresql-42.5.3.jar
    user : jay
    account : 1234
    ```

    ![check file](image/configure_processor_jdbcinfo.png)

- click Processor and choose **PutSQL**
    ![put sql](image/putSQL.png)

- set your **JDBC Connection Pool** on **PutSQL** you just set before
    ![put sql](image/setjdbcconf.png)

- use Funnel to collect your failed information and successful information
![put sql]
- Press right button and start your streaming pipeline.

### Check the data 
- go back to your familiar database GUI, if you don't have and tools, you can access localhost:8088 to use **pgadmin** to check your data is in database success or not.
- You can discover your data has already in your database, you can use the sql below to check your data
    ```
    select * from iriss
    ```
    ![put sql](image/result.png)


### Conclusion
- in this lab, i show you how to use nifi to do streaming task when the file on your file system then it will upload the result to your database 
- you also can get file from your datalake like : AWS S3 , Azure Blob and upload your result to any kind of your relational database  