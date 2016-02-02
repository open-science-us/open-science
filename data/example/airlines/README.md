## Airlines

The dataset to be operated on is the publicly available [airlines dataset](http://stat-computing.org/dataexpo/2009/the-data.html), which contains twenty years of flight records (from 1987 to 2008). I am interested in predicting airline arrival delay based on the flight departure delay, aircraft type, and distance traveled.

### Downloading compressed csv files
~~~
curl -O http://stat-computing.org/dataexpo/2009/1987.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1988.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1989.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1990.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1991.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1992.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1993.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1994.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1995.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1996.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1997.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1998.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/1999.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2000.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2001.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2002.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2003.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2004.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2005.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2006.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2007.csv.bz2
curl -O http://stat-computing.org/dataexpo/2009/2008.csv.bz2
~~~

### Preprocessing data with Apache Spark v1.6.0 cluster on 3 Amazon EC2 r3.large instances
~~~
bin/spark-shell --master spark://172.30.2.99:7077 --packages com.databricks:spark-csv_2.10:1.3.0 \
--executor-cores=2 --num-executors=3 --conf spark.executor.memory=8G \
--driver-memory=2G —conf spark.serializer=org.apache.spark.serializer.KryoSerializer

~~~





