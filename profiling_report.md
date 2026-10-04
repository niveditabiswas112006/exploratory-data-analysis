# Exploratory Data Analysis: Obesity Levels Based on Eating Habits and Physical Condition

## 1. Dataset Overview
This is a unique, real-world dataset from the UCI Machine Learning Repository. It contains data for the estimation of obesity levels in individuals from the countries of Mexico, Peru and Colombia, based on their eating habits and physical condition. Using this dataset avoids common, repetitive datasets like Titanic or Iris, ensuring a unique submission.

## 2. Profiling the Dataset

### Shape of the Dataset
- **Rows (Instances)**: 2111
- **Columns (Features)**: 17

### Data Types
```
Gender                                str
Age                               float64
Height                            float64
Weight                            float64
family_history_with_overweight        str
FAVC                                  str
FCVC                              float64
NCP                               float64
CAEC                                  str
SMOKE                                 str
CH2O                              float64
SCC                                   str
FAF                               float64
TUE                               float64
CALC                                  str
MTRANS                                str
NObeyesdad                            str
```

### Missing Values
```
Gender                            0
Age                               0
Height                            0
Weight                            0
family_history_with_overweight    0
FAVC                              0
FCVC                              0
NCP                               0
CAEC                              0
SMOKE                             0
CH2O                              0
SCC                               0
FAF                               0
TUE                               0
CALC                              0
MTRANS                            0
NObeyesdad                        0
```

### Basic Statistics (Numerical Features)
```
               Age       Height       Weight         FCVC          NCP         CH2O          FAF          TUE
count  2111.000000  2111.000000  2111.000000  2111.000000  2111.000000  2111.000000  2111.000000  2111.000000
mean     24.312600     1.701677    86.586058     2.419043     2.685628     2.008011     1.010298     0.657866
std       6.345968     0.093305    26.191172     0.533927     0.778039     0.612953     0.850592     0.608927
min      14.000000     1.450000    39.000000     1.000000     1.000000     1.000000     0.000000     0.000000
25%      19.947192     1.630000    65.473343     2.000000     2.658738     1.584812     0.124505     0.000000
50%      22.777890     1.700499    83.000000     2.385502     3.000000     2.000000     1.000000     0.625350
75%      26.000000     1.768464   107.430682     3.000000     3.000000     2.477420     1.666678     1.000000
max      61.000000     1.980000   173.000000     3.000000     4.000000     3.000000     3.000000     2.000000
```

### Basic Statistics (Categorical Features)
```
       Gender family_history_with_overweight  FAVC       CAEC SMOKE   SCC       CALC                 MTRANS      NObeyesdad
count    2111                           2111  2111       2111  2111  2111       2111                   2111            2111
unique      2                              2     2          4     2     2          4                      5               7
top      Male                            yes   yes  Sometimes    no    no  Sometimes  Public_Transportation  Obesity_Type_I
freq     1068                           1726  1866       1765  2067  2015       1401                   1580             351
```

## 3. Supported Machine Learning Problems
This dataset supports multiple ML problem types. The primary ones include:

### A. Multi-class Classification
- **Target Variable**: `NObeyesdad` (Obesity Level)
- **Justification**: The target variable represents different levels of obesity (e.g., Normal Weight, Overweight Level I, II, Obesity Type I, II, III). We can use Classification algorithms (like Random Forest, Support Vector Machines, or Gradient Boosting) to classify an individual into one of these obesity categories based on their dietary habits (e.g., vegetable consumption, fast food) and physical activity levels.

### B. Regression
- **Target Variable**: `Weight`
- **Justification**: If we drop the obesity classification target, we can treat the continuous numerical column `Weight` as our target. We can use Regression algorithms (e.g., Linear Regression, XGBoost Regressor) to predict a person's exact weight based on their height, age, and lifestyle habits.

### C. Clustering (Unsupervised Learning)
- **Justification**: Using algorithms like K-Means or DBSCAN, we could cluster individuals into groups based on their eating habits and physical conditions (without providing the labels). This could help us discover natural health profiles or lifestyle segments in the population.
