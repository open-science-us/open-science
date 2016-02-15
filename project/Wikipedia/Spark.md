## Using Spark

~~~
bin/spark-shell --master spark://localhost:7077 \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer


import org.apache.log4j.Logger
import org.apache.log4j.Level
Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel


val rawRDD =  sc.textFile("/work/R/example/Wikipedia/pagecounts*.gz")

rawRDD.cache()

rawRDD.take(10).foreach(println)

aa %22/ar/1541%22 1 4643
aa %C4%BDudov%C3%ADt_XV 1 4658
aa %D0%86%D0%BC%D0%BF%D0%BE%D1%80%D1%82%D0%BD%D0%B0_%D0%BA%D0%B2%D0%BE%D1%82%D0%B0 1 4733
aa %D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A_%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%22/ru/%D0%9D%D0%BE%D0%B2%D0%BE%D1%82%D0%BD%D1%8B%D0%B9,_%D0%A0%D0%B5%D0%BD%D0%B5%22 1 4946
aa %D0%92%D0%B8%D0%BA%D0%B8%D0%BF%D0%B5%D0%B4%D0%B8%D1%8F:%D0%9A_%D0%BF%D0%B5%D1%80%D0%B5%D0%B8%D0%BC%D0%B5%D0%BD%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D1%8E/%22/ru/%D0%9F%D1%80%D0%B8%D0%B4%D0%BD%D0%B5%D1%81%D1%82%D1%80%D0%BE%D0%B2%D1%8C%D0%B5%22 1 4925
aa Arms_of_Ireland 1 4633
aa Henri_de_La_Tour_d%27Auvergne_(1555-1623)/fr/Henri_de_La_Tour_d%27Auvergne,_duc_de_Bouillon 1 4782
aa Indonesian_Wikipedia 1 4627
aa Kategori:308_f.Kr 1 4644
aa L%27Odyss%C3%A9e_(s%C3%A9rie_t%C3%A9l%C3%A9vis%C3%A9e_d%27animation)/fr/L%27Odyss%C3%A9e_(M6) 1 4786

rawRDD.count()
res5: Long = 19908646 




~~~
