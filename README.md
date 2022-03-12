# PySpark / Jupyter Notebook Demo

--------
--------
clone the git repo:
git clone --branch master --single-branch --depth 1 --no-tags  https://github.com/nmfc2003/pyspark-setup-demo.git

change dir to the repo dir:
cd pyspark-setup-demo

init docker swarm:
docker swarm init

build & start the docker containers:
docker stack deploy -c stack.yml pyspark

confirm its running:
docker stack ps pyspark --no-trunc

find the container name:
docker ps | grep pyspark_pyspark.1 | awk '{print $NF}'

result, e.g.:
pyspark_pyspark.1.mglmkk1nqfcgg7ytzv3aw167b

grep the result and input into below command, e.g.:
docker logs pyspark_pyspark.1.mglmkk1nqfcgg7ytzv3aw167b

copy the url for the notebook and paste into browser, e.g.:
http://127.0.0.1:8888/lab?token=533399ce119b16200c00e7b779125c03339d87c8f8fed9ba

in the jupiter terminal install this python libs:
pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org psycopg2-binary

---------------------------------------------
invoke the etl's in each of the notebooks (dbs, users, notifications, scans)
on each notebook we first run the source table ddl file execution for creating the source and target tables
on each notebook we run the "etl" logic by executing cell after cell
---------------------------------------------

all ddl files & notebooks are located under work folder
all source csv files are located under input_files

we can connect to postgres db for direct sql queries, e.g.:
docker exec -it pyspark_postgres.1.xafqv5jc7fdyjp7ylooylxjry bash
psql -U postgres

show dbs:
\l

connect db:
\c source;

show tables:
\dt


describe table:
SELECT 
   table_name, 
   column_name, 
   data_type 
FROM 
   information_schema.columns
WHERE 
   table_name = 'users';

