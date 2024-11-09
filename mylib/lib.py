import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def create_save_visualization(df, column_name, save_filename=None, show=False):
    sns.set_theme(style="whitegrid")
    plt.figure(figsize=(8, 6), dpi=100)
    sns.histplot(df[column_name], kde=True, color="skyblue", bins=30)
    plt.title(f"{column_name} Distribution", fontsize=16)
    plt.xlabel(column_name, fontsize=12)
    plt.ylabel("Frequency", fontsize=12)
    if save_filename:
        plt.savefig(save_filename, bbox_inches="tight")
    if show:
        plt.show()


def read_dataset(file_path):
    df = None
    if file_path.endswith(".csv"):
        df = pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        df = pd.read_excel(file_path)
    return df

def generate_summary_statistics(df):
    summary_stats = df.describe()
    mean_values = df.mean(numeric_only=True)
    median_values = df.median(numeric_only=True)
    std_dev = df.std(numeric_only=True)
    # print(mean_values)
    return summary_stats, mean_values, median_values, std_dev