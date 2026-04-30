

# Data Science Final Exam Study Guide

## Quick Facts
- **Exam Date:** Thursday, April 30, 7:00 AM
- **Format:** No code, comprehensive
- **Materials Allowed:** Calculator and pen/pencil (no notes)

---

## 1. Data Science Fundamentals

### What is Data Science?
- A field that combines statistics, mathematics, and programming to extract insights from data
- The data tells the story; the scientist doesn't tell the data what story to tell

### The Data Scientist
- **Pi-Model**: Data scientists need depth in 2-3 areas and breadth across many
- Key traits: Curiosity, Communication, Storytelling
- Transforms raw data into actionable insights

### The Machine Learning Process (CRISP-DM)
1. **Business Understanding** - Define the problem
2. **Data Understanding** - Explore and assess data quality
3. **Data Preparation** - Clean, transform, engineer features
4. **Modeling** - Select and train models
5. **Evaluation** - Assess model performance
6. **Deployment** - Put model into production

### Types of Machine Learning
- **Supervised Learning**: Train on labeled data (regression, classification)
- **Unsupervised Learning**: Train on unlabeled data (clustering)
- **Online Learning**: Model learns continuously as new data arrives
- **Batch Learning**: Model trained on entire dataset at once

---

## 2. ETL (Extract, Transform, Load)

### Extract (Loading Data)
- **CSV Files**: Reading from local files
- **Web Scraping**: Extracting data from websites
- **APIs**: Pulling data from web services

### Transform (Data Cleaning & Preparation)

#### Missing Values
- **When to drop**: When too much data is missing (>30-50% threshold varies)
- **When to fill**: When missing is random or ignorable
  - Fill with mean, median, or mode
  - Interpolate for time-series data
- **When to keep as indicator**: When the fact that data is missing is meaningful

#### Feature Engineering
- Creating new variables from existing ones
- Example: From "birth_year" create "age"
- Improves model performance by providing more relevant input

#### Data Wrangling
- **Encoding Categorical Variables**:
  - One-Hot Encoding: Convert categories to binary columns
  - Ordinal Encoding: Assign ordered numbers (good for ordered categories)
  - Label Encoding: Simple numerical mapping
  
- **Data Reshaping**:
  - Long-format: One observation per row (typically preferred)
  - Wide-format: Multiple observations per row
  - Pivot Tables: Reshape long → wide with aggregation
  - Melting: Reshape wide → long
  
- **Combining Data**:
  - Concatenation: Combine tables vertically (same columns)
  - Joins: Combine tables horizontally with a key
    - **Inner Join**: Only matching records
    - **Left Join**: All left table records + matching right
    - **Right Join**: All right table records + matching left
    - **Outer Join**: All records from both tables

---

## 3. EDA (Exploratory Data Analysis)

### Purpose
- Understand the data structure and patterns
- Identify outliers and anomalies
- Assess data quality
- Determine what models are appropriate
- Guide feature engineering decisions

### Key Activities
- Create visualizations (histograms, scatter plots, box plots, etc.)
- Calculate statistical summaries (mean, median, std dev, etc.)
- Identify relationships between variables
- Understand the distribution of target variable
- Document findings and patterns

### Role in CRISP-DM
- Bridges "Data Understanding" and "Data Preparation"
- Informs modeling choices
- Helps with evaluation interpretation

---

## 4. Statistical Learning & Machine Learning Models

### Fundamental Concept
The underlying true relationship: **y = f(x) + ε**
- f(x) = true underlying function
- ε = irreducible error (random noise, cannot be modeled)

Our estimated model: **ŷ = f̂(x)**

### Two Sources of Error
1. **Reducible Error**: |f(x) - f̂(x)| - The difference between our model and truth
2. **Irreducible Error**: ε - Random noise; trying to model this causes overfitting

### Cross-Validation
- Split data into training set (to train) and test set (to evaluate)
- Prevents overfitting by testing on unseen data
- Common split: 70/30 or 80/20

### Feature Scaling
**Why it matters**: Distance-based algorithms (kNN) are affected by variable scale
- Example: Years of experience (1-40) vs Salary ($50,000-$150,000)
  - Salary differences dominate the distance calculation

#### Normalization (Min-Max Scaling)
- Scales variables to range [0, 1]
- Formula: x_scaled = (x - min) / (max - min)
- Use when: You need bounded output or uniform distribution

#### Standardization (Z-score normalization)
- Scales to have mean=0 and std=1
- Formula: x_scaled = (x - mean) / std_dev
- Use when: Data should follow normal distribution

---

## 5. Regression

### Purpose
- **Predict a continuous numerical value**
- Input: Numerical (and/or categorical)
- Output: Numerical

### Example Use Cases
- Predicting house prices
- Forecasting sales
- Estimating temperature

### Supervised Learning
- Trained on labeled data where the numerical output is known
- Model learns the relationship between inputs and outputs

### Linear Regression
- Models relationship as a straight line: y = mx + b
- **Variance**: Measure of spread in a variable
- **Covariance**: How two variables move together (positive/negative)
- **Correlation**: Standardized measure of relationship (-1 to 1)
  - 1 = perfect positive relationship
  - 0 = no relationship
  - -1 = perfect negative relationship

### Evaluation Metrics for Regression

#### MAE (Mean Absolute Error)
- Average absolute difference between predicted and actual
- Interpretation: Average prediction error in original units
- Robust to outliers

#### SSE (Sum of Squared Errors)
- Sum of all squared differences
- Emphasizes larger errors

#### MSE (Mean Squared Error)
- Average of squared errors
- Penalizes large errors heavily

#### RMSE (Root Mean Squared Error)
- Square root of MSE
- Back in original units like MAE
- Interpretation: "Average prediction error"

#### RMSLE (Root Mean Squared Logarithmic Error)
- RMSE of log(actual) vs log(predicted)
- Good when values span different magnitudes
- Less sensitive to large outliers

---

## 6. Classification

### Purpose
- **Predict which category/class something belongs to**
- Input: Numerical and/or categorical
- Output: Categorical (discrete classes)

### Example Use Cases
- Predicting whether email is spam/not spam
- Classifying images of animals
- Predicting loan approval (yes/no)

### Supervised Learning
- Trained on labeled data where the category is known

### k-Nearest Neighbors (kNN)

#### How it works
1. For a new point, find the k nearest training points
2. Take a "vote" - the most common class among those k neighbors is the prediction

#### Distance Calculation (Norms)
- **Euclidean Distance** (L2 norm): √(Σ(differences²))
  - Most common, straight-line distance
- **Manhattan Distance** (L1 norm): Σ|differences|
  - Block distance
- Choice affects which neighbors are considered "close"

#### Choosing k
- Must be odd (to avoid ties in binary classification)
- Common heuristic: k ≈ √n (rounded to nearest prime)
- Larger k = smoother decision boundary
- Smaller k = more sensitive to individual points

### Evaluation Metrics for Classification

#### Accuracy
- (Correct Predictions) / (Total Predictions)
- Simple but misleading with imbalanced classes

#### Precision
- (True Positives) / (True Positives + False Positives)
- "Of the ones we predicted as positive, how many were correct?"
- Use when: False positives are costly

#### Recall (Sensitivity)
- (True Positives) / (True Positives + False Negatives)
- "Of the actual positives, how many did we catch?"
- Use when: False negatives are costly

#### F1-Score
- Harmonic mean of Precision and Recall: 2 × (Precision × Recall) / (Precision + Recall)
- Balances both metrics
- Good when you want a single overall score

---

## 7. Clustering

### Purpose
- **Find natural groupings in unlabeled data**
- Input: Numerical and/or categorical
- Output: Categorical (cluster assignments)
- **KEY DIFFERENCE**: Unsupervised - we don't know the categories beforehand

### Example Use Cases
- Customer segmentation
- Document grouping
- Anomaly detection

### k-Means Clustering

#### How it works
1. Choose k (number of clusters)
2. Randomly initialize k cluster centers
3. Assign each point to nearest center
4. Recalculate cluster centers as mean of assigned points
5. Repeat 3-4 until convergence

#### Distance Calculation
- Uses norms (Euclidean or Manhattan) like kNN
- Determines which cluster a point belongs to

### Evaluation Metrics for Clustering

#### WCSS (Within-Cluster Sum of Squares) / Inertia
- Sum of squared distances from each point to its cluster center
- Lower WCSS = tighter, more compact clusters
- Lower is better

#### The Elbow Method
- Plot WCSS vs number of clusters (k)
- Look for "elbow" point where WCSS stops decreasing sharply
- The elbow indicates the optimal k

---

## 8. Key Equations to Know

### Variance
Measure of spread in data around the mean

### Covariance
How much two variables change together

### Correlation
Standardized relationship between variables (-1 to 1)

### Distance Norms
- **Euclidean (L2)**: √(Σ(differences²))
- **Manhattan (L1)**: Σ|differences|

### Error Metrics
- **MAE**: Average absolute error
- **SSE**: Sum of squared errors
- **MSE**: Mean squared error
- **RMSE**: √MSE (back in original units)
- **RMSLE**: √(mean(log(predicted/actual)²))

### Classification Metrics
- **Accuracy**: (TP + TN) / Total
- **Precision**: TP / (TP + FP)
- **Recall**: TP / (TP + FN)
- **F1**: 2 × (Precision × Recall) / (Precision + Recall)

### Scaling
- **Normalization**: (x - min) / (max - min) → [0, 1]
- **Standardization**: (x - mean) / std → normal distribution

---

## Study Tips

1. **Understand the "Why"** - Know when to use each model and metric
2. **Know the Trade-offs** - Precision vs Recall, normalization vs standardization
3. **Connect to CRISP-DM** - See how each concept fits into the overall process
4. **Practice Interpretation** - Be ready to interpret what numbers mean
5. **Classification Key**: Know when to use Precision vs Recall
6. **Clustering Key**: Understand the Elbow Method for choosing k
7. **Remember**: This exam emphasizes concepts, not code - focus on understanding WHY not HOW
