import findspark
import pyspark
from pyspark.sql import SQLContext

findspark.init()
sc = pyspark.SparkContext()
sqlCtx = SQLContext(sc)

df = sqlCtx.read.csv("NFL_Data\BLOCK.csv", header=True, mode="DROPMALFORMED")
df.registerTempTable('block')
tables = sqlCtx.tableNames()
sqlCtx.sql('select * from block').show()
