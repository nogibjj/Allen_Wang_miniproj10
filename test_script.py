from mylib.lib import (
    start_spark,
    load_data,
    query,
    describe,
    example_transform,
    end_spark
)
import os
import pandas as pd

def test_spark():
    spark= start_spark("Test")
    assert spark is not None
    end_spark(spark)


def test_load(spark):
    df = load_data(spark, url="https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
    assert df is not None
    return df

def test_describe(df):
    result = describe(df)
    assert result is None

def test_query(spark,df):
    result=query(spark, df, "SELECT Pclass, COUNT(*) as Count FROM TitanicData GROUP BY Pclass ORDER BY Pclass", "TitanicData")
    assert result is not None

def test_transform(df):
    result = example_transform(df)
    assert result is None

if __name__ == "__main__":
    test_spark()
    spark = start_spark("TitanicTest")
    df = test_load(spark)
    test_describe(df)
    test_query(spark, df)
    test_transform(df)