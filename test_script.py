import pytest
from mylib.lib import (
    start_spark,
    load_data,
    query,
    describe,
    example_transform,
    end_spark
)

# Fixture to start and stop Spark session
@pytest.fixture(scope="module")
def spark():
    spark = start_spark("Test")
    yield spark
    end_spark(spark)

# Fixture to load DataFrame
@pytest.fixture(scope="module")
def df(spark):
    df = load_data(spark, url="https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv")
    return df

# Test Spark session
def test_spark(spark):
    assert spark is not None

# Test loading data
def test_load(df):
    assert df is not None

# Test describe function
def test_describe(df):
    result = describe(df)
    assert result is not None

# Test query function
def test_query(spark, df):
    result = query(spark, df, "SELECT Pclass, COUNT(*) as Count FROM TitanicData GROUP BY Pclass ORDER BY Pclass", "TitanicData")
    assert result is not None

# Test transformation
def test_transform(df):
    result = example_transform(df)
    assert result is not None
