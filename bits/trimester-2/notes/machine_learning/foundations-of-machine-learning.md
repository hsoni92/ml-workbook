# Machine Learning - Module 1: Foundations of Machine Learning

## Learning Objectives

1. Define what Machine Learning is and its relationship to Data Science and Artificial Intelligence
2. Identify the key stages of building a standard Machine Learning workflow

---

## Why Do We Need Machine Learning?

### Digital Transformation

- **Physical to Digital Conversion**: Many physical experiences have been converted into digital experiences
  - **Photography**: Physical cameras → Mobile phones with cloud storage
  - **Shopping**: Physical bookstores → Online platforms (Amazon, Flipkart)
  - **Research**: Physical libraries → Web search (Google)
  - **Trading**: Physical stock brokers → Online applications (Zerodha)
  - **Communication**: Physical visits → Social media
  - **News**: Physical newspapers → Google News

### Data Explosion

- **Storage Capability Growth**:
  - 20 years ago: 6-8 GB HDD capacity
  - Today: 128 GB phones, petabyte-scale storage
- **Data Generation Sources**:
  - Scientific simulations
  - Bioinformatics
  - Remote sensing
  - Social media
  - E-commerce transactions
  - Stock market data

### The Core Problem

> **"We are drowning in data, but starving for knowledge"**

- We have **tons of data** and can store it
- We can process data
- **BUT**: When asking relevant questions, we don't get proper answers
  - **E-commerce example**: Can't easily detect fake bookings/orders despite having transaction data
  - **Stock market example**: Can't predict which stock to buy/sell despite having tons of market data

**Solution**: Machine Learning helps extract meaningful patterns and knowledge from massive amounts of data

---

## Historical Evolution of Data Science

### 1. Empirical Science (Before 1600)
- **Approach**: Ideas based on **observation**
- **Example**: Sun rises from east, sets in west (observation-based)
- **Method**: Build models from direct observations

### 2. Theoretical Science (1600-1950s)
- **Approach**: **Mathematical models** based on observations
- **Example**: Sun rise/set times vary by season (winter vs summer)
- **Method**: Write mathematical formulations to generalize observations
- **Goal**: Generalize ideas beyond specific observations

### 3. Computational Science (1950s-1990s)
- **Approach**: Use **limited computational power** for calculations
- **Tools**: Calculators, limited computational machines
- **Method**: Run simulations, develop complex models
- **Limitation**: Limited computational resources

### 4. Data Science & Machine Learning (Present)
- **Capabilities**:
  - **Higher computational power**
  - **Higher storage capacity**
  - **Better communication** between computation and storage
- **Approach**:
  - Digitalize observations
  - Store massive amounts of data
  - Use algorithms to **mine information** and **learn patterns** from data
- **Goal**: Extract patterns automatically from massive datasets

---

## What is Machine Learning?

### Definition

**Machine Learning** is a field of study that uses computers to **learn from data without explicitly being programmed**.

### Key Characteristics

- **Automatic Learning**: Algorithms automatically learn rules/patterns without explicit programming
- **Pattern Extraction**: Extracts ideas and information from available data
- **No Manual Programming**: Don't need to tell the machine what to extract
- **Knowledge Discovery**: Automatically extracts knowledge from data

### Evolution from Data Mining

- Machine Learning evolved from **Data Mining**
- **Data Mining Focus**: Extract useful, previously unknown knowledge from larger datasets
- **Machine Learning**: Discovers meaningful patterns **automatically or semi-automatically**

### Origins

Machine Learning draws ideas from multiple disciplines:

1. **Statistics and AI**: Theory and predictions
2. **Pattern Recognition**: Identifying patterns in data
3. **Database Systems**: Managing and querying large datasets

---

## Machine Learning Pipeline

> **Important**: Machine Learning is NOT about running a single algorithm. It is a **comprehensive multi-step process**.

### General Machine Learning Pipeline

1. **Data + Questions**: Start with data and set of questions
   - Example: "Will it rain tomorrow?" + 10 years of weather data

2. **Data Selection**: Select subset of relevant data
   - Why: Processing whole data is costly, time-consuming, and might be noisy

3. **Data Preprocessing**: Clean and transform the selected data
   - Activities: Data cleaning, data transformation, noise removal

4. **Machine Learning Algorithms**: Apply ML/data mining algorithms on transformed data

5. **Evaluation**: Use interpreter and evaluation tools
   - Performance metrics
   - Quality assessment

6. **Knowledge Extraction**: Extract knowledge to answer the original question
   - **Success Criteria**: If you can answer the question you started with, the pipeline is successful
   - **Failure**: If not, revisit one or more stages (change algorithm, data selection, preprocessing, etc.)

---

## Machine Learning Workflows

### 1. KDD (Knowledge Discovery in Databases)

**KDD** = Knowledge Discovery in Databases

A 6-stage pipeline from raw data to knowledge:

#### Stage 1: Raw Data
- Gather and store data from various sources
- Example: Weather data (temperature, humidity, wind speed, wind direction) stored in databases

#### Stage 2: Data Integration and Cleaning
- **Data Integration**: Merge/combine data from various sources
  - Multiple tables combined
  - Creates a **Data Warehouse**
- **Data Preprocessing**:
  - Data cleaning
  - Outlier detection
  - Prepare data for next stage

#### Stage 3: Data Warehouse
- Contains integrated data from various sources
- **Data Selection**: Select **task-relevant data** (subset from data warehouse)

#### Stage 4: Data Mining/Machine Learning
- Apply ML/data mining algorithms
- Find patterns in task-relevant data
- Extract knowledge/patterns

#### Stage 5: Pattern Evaluation
- Identify extracted patterns
- Measure **quality of patterns**
- Assess whether patterns are good quality

#### Stage 6: Knowledge
- Extract final, actionable insights
- **Success**: If able to answer original questions → pipeline correct
- **Failure**: Rerun pipeline, change algorithm, modify data selection, redo integration/cleaning

---

### 2. CRISP-DM (Cross-Industry Standard Process for Data Mining)

**CRISP-DM** = Popular industry framework for building ML projects

A 5-stage pipeline:

#### Stage 1: Business Understanding
- Start with: **Data + Prior Knowledge + Questions**
- Include domain expertise
- Define set of questions to answer

#### Stage 2: Data Preparation
- Integrate data from various sources
- Prepare final dataset
- Activities:
  - Data integration
  - Data cleaning
  - Data transformation

#### Stage 3: Modeling
- **Select and apply** machine learning algorithms
- Build the model using prepared data

#### Stage 4: Evaluation
- Apply built model on **newer data** (test data)
- Evaluate model performance
- Check if performance is good

#### Stage 5: Deployment/Knowledge Extraction
- If model performs well: Extract knowledge
- Check if original questions can be answered
- **Success**: Questions answered → Pipeline successful
- **Failure**: Pipeline broken, need to revisit stages

---

### 3. Business Intelligence View

A 5-stage pipeline:

1. **Data Sources**: Start with various data sources

2. **Data Preprocessing**:
   - Data integration
   - Create data warehousing

3. **Data Exploration**: Explore and understand the data

4. **Machine Learning & Data Mining**: Apply algorithms

5. **Data Presentation & Decision Making**:
   - Present results
   - Make decisions based on insights

---

## Data Types in Machine Learning

### 1. Structured Data
- **Definition**: Data arranged and stored in a structured way
- **Examples**:
  - Tabular data (spreadsheets, databases)
  - Graphical data
- **Usage**: Can directly apply ML algorithms

### 2. Unstructured/Semi-Structured Data
- **Definition**: Data without proper structure
- **Examples**:
  - News articles
  - Web pages
- **Usage Options**:
  - Apply ML algorithms directly, OR
  - Convert to structured data first, then apply ML algorithms
- **Note**: Both approaches are used in real-world applications

### 3. Time Series Data
- **Definition**: Time-dependent data
- **Characteristics**: Data points collected over time
- **Usage**: Specialized ML algorithms for temporal patterns

### 4. Advanced Data Types

- **Stream Data / Sensor Data**:
  - Real-time data from IoT devices
  - Data flowing continuously
- **Socio-Temporal Data**: Social data with temporal components
- **World Wide Data**: Global-scale datasets

---

## Summary

### Key Concepts Covered

1. **Machine Learning Definition**: Field that uses computers to learn from data without explicit programming

2. **Why ML is Needed**:
   - Digital transformation → Data explosion
   - "Drowning in data, starving for knowledge"
   - Need to extract patterns from massive datasets

3. **Historical Evolution**:
   - Empirical → Theoretical → Computational → Data Science & ML

4. **ML Workflows**:
   - General Pipeline (6 steps)
   - KDD (6 stages)
   - CRISP-DM (5 stages)
   - Business Intelligence View (5 stages)

5. **Data Types**:
   - Structured
   - Unstructured/Semi-structured
   - Time series
   - Advanced types (stream, sensor, socio-temporal)

### Important Notes

- Machine Learning is a **comprehensive multi-step process**, not just running a single algorithm
- All workflows emphasize: **Data → Processing → Modeling → Evaluation → Knowledge**
- Success is measured by whether the original questions can be answered
- If pipeline fails, iterate and refine: change algorithms, data selection, or preprocessing steps

---

*Notes compiled from: Module 1 - Foundations of Machine Learning (Dr. Hemant Rathor)*
