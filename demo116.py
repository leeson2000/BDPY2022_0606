from pprint import pprint

from pyspark import SparkConf, SparkContext

config = SparkConf().setAppName("Hello Python").setMaster("local")
sc = SparkContext(conf=config)
textFile = sc.textFile("data/demo54.csv")
print("sample some result", textFile.takeSample(False, 3))
print("take ordered 3", textFile.takeOrdered(3))

print("map", textFile.map(lambda s: s.split(",")).collect())
print("map", textFile.flatMap(lambda s: s.split(",")).collect())

sc.stop()

