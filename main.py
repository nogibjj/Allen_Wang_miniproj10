#from ydata_profiling import ProfileReport
from mylib.lib import (
    create_save_visualization,
    read_dataset,
    generate_summary_statistics,
)


def df_describe(file_path):
    df = read_dataset(file_path)
    return df.describe()


def statistics_for_column(file_path, column):
    df = read_dataset(file_path)
    _, mean_values, median_values, std_dev = generate_summary_statistics(df)
    return mean_values[column], median_values[column], std_dev[column]


def create_save_visualization_for_all(file_path):
    df = read_dataset(file_path)
    for column in df.columns:
        column_name = column.replace("/", "_")
        create_save_visualization(df, column, "output/"+ column_name + "_distribution.png")


def generate_md_report(file_path, title):
    df = read_dataset(file_path)
    #profile = ProfileReport(df, title=title, explorative=True)
    #profile.to_file(title + ".html")
    summary_stats, mean_values, median_values, std_dev = generate_summary_statistics(df)
    with open(title + ".md", "w", encoding="utf-8") as file:
        file.write("Summary:\n")
        file.write(summary_stats.to_markdown() + "\n\n")
        file.write("Mean:\n")
        file.write(mean_values.to_markdown() + "\n\n")
        file.write("Median:\n")
        file.write(median_values.to_markdown() + "\n\n")
        file.write("Standard Deviation:\n")
        file.write(std_dev.to_markdown() + "\n\n")
        file.write("![image1](output/Age_distribution.png)\n")
        file.write("\n\n")
        file.write("![image2](output/Fare_distribution.png)\n")
        file.write("\n\n")
        file.write("![image3](output/Pclass_distribution.png)\n")
