# from ydata_profiling import ProfileReport
from mylib.lib import (
    start_spark,
    load_data,
    query,
    describe,
    example_transform,
    end_spark,
)


def main():
    # Workflow for Titanic Dataset
    # Start Spark session
    spark = start_spark("TitanicData")

    # Load data into Spark DataFrame
    df = load_data(
        spark,
        url="https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv",
    )
    # Run a sample SQL query
    query(
        spark,
        df,
        "SELECT Pclass, COUNT(*) as Count FROM TitanicData GROUP BY Pclass ORDER BY Pclass",
        "TitanicData",
    )
    # Describe the data
    describe(df)

    # Perform example transformation
    example_transform(df)

    # Stop Spark session
    end_spark(spark)


if __name__ == "__main__":
    main()
