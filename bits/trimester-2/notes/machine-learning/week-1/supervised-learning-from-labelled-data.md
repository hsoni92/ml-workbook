# Machine Learning - Module 1: Supervised Learning from Labeled Data

## Learning Objectives

1. Define what supervised learning is and understand its core concepts
2. Understand the two different types of supervised learning algorithms: classification and regression
3. Learn the process of training and testing a classification model
4. Explore real-world applications of classification and regression

---

## Introduction to Machine Learning Types

Machine Learning can be broadly divided into **two fundamental types of learning**:

### 1. Supervised Learning (Prediction Methods)

- **Goal**: Learn so that we can do **prediction**
- **Purpose**: Predict unknown values for the future
- **Learning Process**: Machine learns from examples where the **correct answer is known**
- **Data Required**: Original data (X) + **Correct answers/Class labels (Y)**
- **Model Function**: Builds a function **f** that finds the relationship between data (X) and correct labels (Y)
- **Example**: Weather prediction system - predict whether there will be rainfall tomorrow or not

### 2. Unsupervised Learning (Descriptive Methods)

- **Goal**: Find **interesting patterns**, human interpretable patterns and structure in the data
- **Purpose**: **NOT doing any prediction** - just finding structure and patterns
- **Learning Process**: Machine explores the data **without correct answers**
- **Data Required**: Only original data (X) - **no correct answers or class labels**
- **Focus**: Understanding whether two points are same or different, finding patterns in data

**Key Difference**:
- **Supervised Learning** = Prediction (has labels)
- **Unsupervised Learning** = Description (no labels)

---

## What is Supervised Learning?

### Definition

**Supervised Learning** is one of the most common methods in machine learning where learning is done using **labeled data** (data with correct answers/class labels).

### Key Concepts

- **Labeled Data**: Data that consists of training examples where each example is a pair of:
  - **Input features (X)**: The original data/attributes
  - **Desired output (Y)**: Also known as **label**, **target**, or **class label**

- **The Learning Model**:
  - Builds a function **f** that finds the relationship between **X** (input features) and **Y** (class labels)
  - This function **f** is called:
    - Machine learning model
    - Classification model
    - Prediction model
    - Supervised learning model

### Example Structure

**Weather Prediction System**:
- **Input Features (X)**: Temperature, Humidity
- **Class Label (Y)**: Rain (Yes/No)

| Day | Temperature | Humidity | Rain (Label) |
|-----|-------------|----------|--------------|
| 1   | ...         | ...      | Yes          |
| 2   | ...         | ...      | No           |
| 3   | ...         | ...      | Yes          |

### Analogy

**Supervised Learning** is like a **student learning from a textbook with answers**:
- **Input**: Questions (X)
- **Output**: Answers (Y)
- **Process**: Student solves questions and checks answers at the back
- **Learning**: After solving 100 questions, student learns how to solve similar questions
- **Application**: When a new question comes, student can predict the answer

Similarly, in supervised learning:
- We have data (X) and corresponding class labels (Y)
- We build a model to do prediction in the future

---

## Types of Supervised Learning

Supervised learning is further divided into **two types** based on the nature of the output:

### 1. Classification

**Definition**: Predicting **finite number of values** or **categorical/discrete values**

**Characteristics**:
- Class labels are **categorical** in nature
- Class labels are **finite** in nature
- Number of items we can predict are **fixed** and **divided into categories**
- Question type: **"Which class?"**

**Examples**:
- **Weather Prediction**: Rain or No Rain (2 classes)
- **Fraud Detection**: Fraudulent or Genuine (2 classes)
- **Cheat Detection**: Cheated or Not Cheated (2 classes)
- **Image Classification**: Dog or Cat (2 classes)
- **Churn Detection**: Stay or Leave (2 classes)
- **Direct Marketing**: Target or Not Target (2 classes)

**Note**: Classification can have 2, 3, 4, or more classes - as long as the number is **finite**

### 2. Regression

**Definition**: Predicting **continuous** or **numerical values** (infinite number of possible values)

**Characteristics**:
- Output can be **continuous** or **numerical** in nature
- Model can predict **infinite number of values**
- Question type: **"How much?"**

**Examples**:
- **Petrol Price Prediction**: Can be 100, 101, 102, 101.5, 102.3, etc. (infinite values)
- **Oil Price Prediction**: Continuous numerical values
- **Gold Price Prediction**: Continuous numerical values
- **Stock Price Prediction**: Continuous numerical values
- **House Price Prediction**: Can be 1 lakh, 50 lakh, 1 crore, etc. (infinite values)
- **Vehicle Mileage**: Can be 10, 10.5, 11, 20, 500, etc. (infinite values)
- **Sales Prediction**: Continuous numerical values
- **Temperature/Humidity Prediction**: Continuous numerical values

### Key Differences

| Aspect | Classification | Regression |
|--------|---------------|------------|
| **Output Type** | Categorical/Discrete | Continuous/Numerical |
| **Number of Values** | Finite/Fixed | Infinite |
| **Question** | "Which class?" | "How much?" |
| **Examples** | Rain/No Rain, Fraud/No Fraud | Price, Temperature, Sales |

---

## Classification Process

### Data Structure

In classification, the data consists of:

1. **Attributes (X)**: Features that describe the data point
   - Example: Attribute 1, Attribute 2, Attribute 3

2. **Class Label (Y)**: Special attribute that we want to predict
   - Also called **target** or **class label**

**Example: Cheat Detection System**

| Customer | Refund (A1) | Marital Status (A2) | Taxable Income (A3) | Cheated (Y) |
|----------|-------------|---------------------|---------------------|-------------|
| 1        | Yes         | Single              | 125                 | No          |
| 2        | No          | Married             | 100                 | No          |
| 3        | No          | Single              | 70                  | Yes         |

- **X (Input Features)**: Refund, Marital Status, Taxable Income
- **Y (Class Label)**: Cheated (Yes/No)

### Training and Testing Process

#### Step 1: Data Split

**Original Data** is divided into two parts:

1. **Training Data**: Used to **build the model**
2. **Test Data**: Used to **check the performance** of the model

**Note**: Data splitting is done using sampling (typically without replacement)

#### Step 2: Training Phase

- Use **training data** to build the classification model
- Model learns the relationship between **X** (attributes) and **Y** (class label)
- Sometimes **validation** is also performed during this phase

#### Step 3: Testing Phase

- Use **test data** to evaluate the model
- **Process**:
  1. Temporarily "forget" the class labels in test data
  2. Use the trained model to make predictions
  3. Compare model predictions with original labels
  4. If predictions match original labels → **Model is good**
  5. If predictions don't match → **Model is of poor quality**

#### Step 4: Real-World Deployment

- In production, user provides only **X** (input features)
- Model predicts **Y** (class label) based on learned relationships

**Workflow**:
```
Original Data (X + Y)
    ↓
Split into Training & Test Data
    ↓
Train Model on Training Data
    ↓
Test Model on Test Data
    ↓
Deploy Model (User provides X → Model predicts Y)
```

---

## Real-World Applications

### Classification Applications

#### 1. Credit Card Fraud Detection

- **Problem**: Detect fraudulent credit card transactions
- **Input**: Transaction details (amount, location, time, etc.)
- **Output**: Fraudulent or Genuine
- **Process**:
  - ML model sits between user and bank
  - Checks every transaction based on previous transaction patterns
  - If transaction looks fraudulent → Block transaction or request additional authentication
  - If transaction looks genuine → Allow transaction to proceed
- **Impact**: Prevents financial losses and protects customers

#### 2. Direct Marketing

- **Problem**: Predict which customers to target for marketing campaigns
- **Input**: Customer attributes (demographics, purchase history, etc.)
- **Output**: Target or Not Target
- **Benefit**: Optimize marketing spend and improve conversion rates

#### 3. Churn Detection

- **Problem**: Predict whether a customer will stay on the platform or leave
- **Input**: Customer behavior, usage patterns, etc.
- **Output**: Stay or Leave
- **Benefit**: Proactive customer retention strategies

### Regression Applications

#### 1. Sales Prediction

- **Problem**: Predict sales for next year/quarter
- **Output**: Continuous numerical value (sales amount)
- **Use Case**: Business planning, inventory management

#### 2. Temperature/Humidity Prediction

- **Problem**: Predict weather conditions
- **Output**: Continuous numerical values (temperature in °C, humidity %)
- **Use Case**: Weather forecasting, agricultural planning

#### 3. Stock Price Prediction

- **Problem**: Predict stock prices for trading decisions
- **Output**: Continuous numerical value (price per share)
- **Use Case**: Investment strategies, risk management

#### 4. House Price Prediction

- **Problem**: Predict property values
- **Output**: Continuous numerical value (price in currency)
- **Use Case**: Real estate valuation, investment decisions

---

## Performance Metrics

### Classification Metrics

Performance of classification models is measured using:

- **Accuracy**: Percentage of correct predictions
- **Precision**: Measure of exactness
- **Recall**: Measure of completeness
- **Other metrics**: F1-score, ROC-AUC, etc.

**Note**: Detailed explanation of these metrics will be covered in **Module 3**

### Regression Metrics

Performance of regression models is measured using:

- **Mean Square Error (MSE)**: Average of squared differences between predicted and actual values
- **Sum of Square Error (SSE)**: Sum of squared differences
- **Other metrics**: Mean Absolute Error (MAE), R-squared, etc.

---

## Summary

### Key Takeaways

1. **Supervised Learning**:
   - Uses **labeled data** (data with correct answers/class labels)
   - Goal is to **predict** unknown values
   - Machine learns relationship between **X** (input features) and **Y** (class labels) through function **f**

2. **Two Types of Supervised Learning**:
   - **Classification**: Predicts **finite/categorical** values → "Which class?"
   - **Regression**: Predicts **continuous/numerical** values → "How much?"

3. **Classification Process**:
   - Data split: Training data (build model) + Test data (evaluate model)
   - Training: Learn relationship between X and Y
   - Testing: Evaluate model performance by comparing predictions with actual labels

4. **Real-World Applications**:
   - **Classification**: Fraud detection, churn detection, direct marketing
   - **Regression**: Price prediction, sales forecasting, weather prediction

5. **Performance Evaluation**:
   - Classification: Accuracy, precision, recall
   - Regression: Mean square error, sum of square error

### Important Distinctions

| Concept | Supervised Learning | Unsupervised Learning |
|---------|---------------------|----------------------|
| **Data** | X + Y (with labels) | X only (no labels) |
| **Goal** | Prediction | Pattern discovery |
| **Also Called** | Prediction Methods | Descriptive Methods |

| Concept | Classification | Regression |
|---------|----------------|------------|
| **Output** | Categorical/Discrete | Continuous/Numerical |
| **Values** | Finite | Infinite |
| **Question** | Which class? | How much? |

---

*Notes compiled from: Module 1 - Supervised Learning from Labeled Data (Dr. Hemant Dattar)*
