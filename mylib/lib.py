import pandas as pd
from pyspark.sql import SparkSession
from pyspark.sql.functions import when, col
from pyspark.sql.types import StructType, StructField, IntegerType, StringType, FloatType


LOG_FILE = "titanic_output.md"

def log(operation, output, query=None):
    with open(LOG_FILE, "a") as file:
        file.write(f"The operation is {operation}\n\n")
        if query: 
            file.write(f"The query is {query}\n\n")
        file.write("The output is: \n\n")
        file.write(output)
        file.write("\n\n")


def start_spark(appName):
    """Start Spark session."""
    spark = SparkSession.builder \
    .appName(appName) \
    .getOrCreate()
    #spark.sparkContext.setLogLevel("DEBUG")
    #print(spark.version)
    return spark

def end_spark(spark):
    """Stop Spark session."""
    spark.stop()
    return

def load_data(spark, url):
    """Load data from URL into Spark DataFrame without saving locally."""
    # Read data from URL into a pandas DataFrame
    pdf = pd.read_csv(url)
    
    # Convert pandas DataFrame to Spark DataFrame
    schema = StructType([
        StructField("Survived", IntegerType(), True),
        StructField("Pclass", IntegerType(), True),
        StructField("Name", StringType(), True),
        StructField("Sex", StringType(), True),
        StructField("Age", FloatType(), True),
        StructField("Siblings/Spouses Aboard", IntegerType(), True),
        StructField("Parents/Children Aboard", IntegerType(), True),
        StructField("Fare", FloatType(), True),
    ])
    
    df = spark.createDataFrame(pdf, schema=schema)   
    #df.show()
    log("load", df.limit(10).toPandas().to_markdown())
    return df

def query(spark, df, query, name): 
    """Run SQL query on Spark DataFrame."""
    df.createOrReplaceTempView(name)
    result = spark.sql(query)
    #print(result)
    log("query", result.limit(10).toPandas().to_markdown(), query)
    return result

def describe(df):
    """Generate and log summary statistics."""
    summary_stats_str = df.describe().toPandas().to_markdown()
    log("summary data", summary_stats_str)
    return df.describe()

def example_transform(df):
    """Apply a transformation to categorize age groups."""
    df = df.withColumn(
        "Age_Group",
        when(col("Age") < 18, "Child")
        .when((col("Age") >= 18) & (col("Age") < 60), "Adult")
        .otherwise("Senior")
    )
    log("transform", df.limit(10).toPandas().to_markdown())
    return df

