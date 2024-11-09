from main import (
    df_describe,
    statistics_for_column,
    create_save_visualization_for_all,
    generate_md_report,
)
import os
import pandas as pd


def test_generate_report():
    file_path = (
        "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    )
    generate_md_report(file_path, "Titanic Profiling Report")
    assert os.path.isfile("Titanic Profiling Report.md")


def test_statistics_report():
    file_path = (
        "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    )
    describe = df_describe(file_path)
    assert type(describe) is pd.DataFrame
    for column in describe.columns:
        mean_values, _ , std_dev = statistics_for_column(file_path, column)
        assert describe.loc["mean", column] == mean_values
        # assert describe.loc["median", column] == median_values
        assert describe.loc["std", column] == std_dev


def test_visualization():
    file_path = (
        "https://web.stanford.edu/class/archive/cs/cs109/cs109.1166/stuff/titanic.csv"
    )
    create_save_visualization_for_all(file_path)
    describe = df_describe(file_path)
    for column in describe.columns:
        column_name = column.replace("/", "_")
        assert os.path.isfile("output/"+ column_name + "_distribution.png")


if __name__ == "__main__":
    test_statistics_report()
    test_generate_report()
    test_visualization()
