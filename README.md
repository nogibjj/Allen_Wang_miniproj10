# Allen_Wang_miniproj_10

[![CI](https://github.com/nogibjj/Allen_Wang_miniproj_10/actions/workflows/badge.svg)](https://github.com/nogibjj/Allen_Wang_miniproj_10/actions)

## Overview

This project uses **PySpark** to perform data processing on the **Titanic dataset**. It includes:

- A **Spark SQL** query to analyze the data.
- A **data transformation** that categorizes passengers by age group.
- Results are logged in markdown format for analysis and reporting.
- The project also includes a CI/CD pipeline for automated testing and deployment.

## Features

- **Data Processing with PySpark**:
  - **Spark SQL Queries**: Executes SQL queries on the dataset to derive insights.
  - **Data Transformation**: Adds new columns to the dataset by applying transformations, such as age categorization.

- **Descriptive Statistics**:
  - Generates summary statistics (mean, median, standard deviation) for numeric columns.
  - Creates visualizations (e.g., histograms) to aid in data analysis.

- **Automated Testing**:
  - Includes unit tests for both the Python scripts and the Jupyter notebook using `pytest` with the `nbval` plugin for notebook validation.

- **CI/CD Pipeline**:
  - **GitHub Actions**: Runs all Makefile commands with badges displayed in the README for continuous integration and deployment.
  - The pipeline includes:
    - Testing: Runs unit tests to ensure code correctness.
    - Code Formatting: Automatically formats the code using **Black**.
    - Linting: Ensures clean code using **Ruff**.
    - Package Installation: Automatically installs project dependencies.

## Project Structure

- **Titanic Data Processing Script (`main.py`)**:
  - Contains the main code for data processing and analysis using PySpark.
  - Executes descriptive statistics and transformations using either **Pandas** or **Polars**.

- **Makefile**:
  - Contains the following commands to manage the project:
    - `make install`: Installs project dependencies via `pip`.
    - `make format`: Formats the code with **Black**.
    - `make lint`: Lints the code using **Ruff**.
    - `make test`: Runs all unit tests for the Python scripts and Jupyter notebooks.

## Setup

1. **Clone the repository:**

    ```bash
    git clone https://github.com/nogibjj/Allen_Wang_miniproj_10.git
    cd Allen_Wang_miniproj_10
    ```

2. **Install dependencies:**

    ```bash
    make install
    ```

3. **Format code:**

    ```bash
    make format
    ```

4. **Lint code:**

    ```bash
    make lint
    ```

5. **Test code:**

    ```bash
    make test
    ```

## How to Run the Script

1. To run the **Titanic data processing script** (`main.py`), simply execute:

    ```bash
    python main.py
    ```

2. This will load the Titanic dataset, perform the transformation and analysis, and log the results in `titanic_output.md`.
    


