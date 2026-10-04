import ssl
ssl._create_default_https_context = ssl._create_unverified_context
# type: ignore
from ucimlrepo import fetch_ucirepo 
import pandas as pd

def main():
    print("Starting Exploratory Data Analysis on the Obesity Levels Dataset...")
    
    # fetch dataset 
    # ID 544: Estimation of obesity levels based on eating habits and physical condition 
    obesity = fetch_ucirepo(id=544) 
    
    # data (as pandas dataframes) 
    X = obesity.data.features 
    y = obesity.data.targets 
    
    # combine into a single dataframe
    df = pd.concat([X, y], axis=1)
    
    # Save the dataset to a CSV file for submission
    df.to_csv('obesity_dataset.csv', index=False)
    
    with open('profiling_report.md', 'w') as f:
        f.write("# Exploratory Data Analysis: Obesity Levels Based on Eating Habits and Physical Condition\n\n")
        f.write("## 1. Dataset Overview\n")
        f.write("This is a unique, real-world dataset from the UCI Machine Learning Repository. It contains data for the estimation of obesity levels in individuals from the countries of Mexico, Peru and Colombia, based on their eating habits and physical condition. Using this dataset avoids common, repetitive datasets like Titanic or Iris, ensuring a unique submission.\n\n")
        
        f.write("## 2. Profiling the Dataset\n\n")
        
        # Shape
        f.write("### Shape of the Dataset\n")
        f.write(f"- **Rows (Instances)**: {df.shape[0]}\n")
        f.write(f"- **Columns (Features)**: {df.shape[1]}\n\n")
        
        # Data Types
        f.write("### Data Types\n")
        f.write("```\n")
        f.write(df.dtypes.to_string() + "\n")
        f.write("```\n\n")
        
        # Missing Values
        f.write("### Missing Values\n")
        f.write("```\n")
        f.write(df.isnull().sum().to_string() + "\n")
        f.write("```\n\n")
        
        # Basic Statistics
        f.write("### Basic Statistics (Numerical Features)\n")
        f.write("```\n")
        f.write(df.describe().to_string() + "\n")
        f.write("```\n\n")
        
        f.write("### Basic Statistics (Categorical Features)\n")
        f.write("```\n")
        f.write(df.describe(include=['object', 'category']).to_string() + "\n")
        f.write("```\n\n")
        
        f.write("## 3. Supported Machine Learning Problems\n")
        f.write("This dataset supports multiple ML problem types. The primary ones include:\n\n")
        f.write("### A. Multi-class Classification\n")
        f.write("- **Target Variable**: `NObeyesdad` (Obesity Level)\n")
        f.write("- **Justification**: The target variable represents different levels of obesity (e.g., Normal Weight, Overweight Level I, II, Obesity Type I, II, III). We can use Classification algorithms (like Random Forest, Support Vector Machines, or Gradient Boosting) to classify an individual into one of these obesity categories based on their dietary habits (e.g., vegetable consumption, fast food) and physical activity levels.\n\n")
        
        f.write("### B. Regression\n")
        f.write("- **Target Variable**: `Weight`\n")
        f.write("- **Justification**: If we drop the obesity classification target, we can treat the continuous numerical column `Weight` as our target. We can use Regression algorithms (e.g., Linear Regression, XGBoost Regressor) to predict a person's exact weight based on their height, age, and lifestyle habits.\n\n")
        
        f.write("### C. Clustering (Unsupervised Learning)\n")
        f.write("- **Justification**: Using algorithms like K-Means or DBSCAN, we could cluster individuals into groups based on their eating habits and physical conditions (without providing the labels). This could help us discover natural health profiles or lifestyle segments in the population.\n")

    print("EDA completed successfully. Profiling report saved to 'profiling_report.md'.")
    print("Dataset saved to 'obesity_dataset.csv'.")

if __name__ == "__main__":
    main()
