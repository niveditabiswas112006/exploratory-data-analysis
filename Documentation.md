# Project Documentation: Exploratory Data Analysis (EDA)

## 1. Project Overview
This project is an Exploratory Data Analysis (EDA) assignment aimed at understanding the fundamental characteristics of a real-world dataset before jumping into Machine Learning models. The objective was to select a unique, faculty-approved dataset, profile its structure, identify missing values, compute basic statistics, and determine which Machine Learning problems the dataset can support.

## 2. Dataset Used
**Name:** Estimation of Obesity Levels Based on Eating Habits and Physical Condition  
**Source:** UCI Machine Learning Repository (Dataset ID: 544)  
**Description:** This dataset contains data from individuals from Mexico, Peru, and Colombia. It includes 17 attributes related to eating habits (e.g., frequent consumption of high caloric food, vegetable consumption) and physical condition (e.g., physical activity frequency, time using technology devices) to estimate their obesity levels.

We specifically chose this dataset because it is unique and less common than introductory datasets like Titanic or Iris, reducing any chances of overlapping submissions with classmates.

## 3. Libraries and Technologies Used
The following Python libraries were utilized in this project:
- **`pandas`**: Used for data manipulation, generating descriptive statistics (`df.describe()`), checking for missing values (`df.isnull().sum()`), and exporting the combined dataset to a CSV file.
- **`ucimlrepo`**: A specialized Python package provided by the UCI Machine Learning Repository. We used the `fetch_ucirepo` function to directly fetch the dataset via its ID (544) over the internet, saving us from manual downloads and parsing.
- **`ssl`**: Used to bypass secure socket layer (SSL) certificate verification issues that sometimes occur in local Python environments when fetching datasets over HTTPS.

## 4. How the Code Works (`eda.py`)
The main script `eda.py` automates the entire EDA process:
1. **Fetching the Data**: It connects to the UCI database using `fetch_ucirepo(id=544)`.
2. **Data Preparation**: It separates the dataset into features (`X`) and targets (`y`), and then combines them into a single pandas DataFrame (`df = pd.concat([X, y], axis=1)`).
3. **Exporting**: It saves this complete DataFrame locally as `obesity_dataset.csv`.
4. **Profiling & Reporting**: It extracts the shape, data types, missing values, and descriptive statistics of the dataset, and programmatically writes these findings into a neatly formatted markdown file called `profiling_report.md`.

## 5. Potential Machine Learning Applications
Based on our EDA, this dataset is well-suited for:
- **Multi-class Classification:** Predicting the exact category of obesity (Normal Weight, Overweight, Obesity Type I/II/III) using the `NObeyesdad` target variable.
- **Regression:** Predicting a continuous value like the individual's `Weight` based on their lifestyle and physical attributes.
- **Clustering:** Grouping individuals with similar lifestyle and dietary habits to find patterns in the data without using predefined labels.
