# Machine Learning - Module 1: Unsupervised Learning, Discovering Hidden Patterns

## Learning Objectives

1. Define what unsupervised learning is and understand how it differs from supervised learning
2. Understand the two different types of unsupervised learning algorithms: clustering and association rule mining
3. Explore real-world applications of clustering and association rule mining

---

## Introduction: What is Unsupervised Learning?

### Definition

**Unsupervised Learning** is a type of machine learning where the algorithm learns patterns, structure, and relationships within data **without any class labels or correct answers**.

### Key Characteristics

- **No Labels**: We do not have any class labels or correct answers (Y)
- **No Prediction Goal**: The goal is **NOT to do any prediction**
- **Knowledge Discovery**: The goal is to find **hidden structure, patterns, and relationships** within the data itself
- **Data Structure**: Only **X** (input features) is available, **no Y** (labels)

### Comparison with Supervised Learning

| Aspect | Supervised Learning | Unsupervised Learning |
|--------|-------------------|----------------------|
| **Data** | X + Y (with labels) | X only (no labels) |
| **Goal** | Prediction | Pattern discovery / Knowledge discovery |
| **Purpose** | Predict unknown values for the future | Find hidden structure and patterns in data |
| **Learning** | Learns from data and correct labels | Learns patterns from data without labels |
| **Also Known As** | Prediction methods | Descriptive methods / Knowledge discovery |

### Analogy

**Supervised Learning** is like a student learning from a textbook with answers:
- Has questions (X) and answers (Y)
- Learns to predict answers for new questions

**Unsupervised Learning** is like exploring data without any answers:
- Only has data (X)
- Discovers patterns and groups naturally present in the data
- No "correct" answer to check against

---

## Types of Unsupervised Learning

Unsupervised learning algorithms can be broadly categorized into **two primary types**:

### 1. Clustering

**Definition**: Algorithms that automatically **group similar data points together** into natural groups or clusters.

**Key Principles**:
- **Similar items** → Put into the **same group**
- **Dissimilar items** → Put into **different groups**
- **Goal**: Identify **natural groups** in the data

**Core Objective**:
- **Minimize intra-cluster distance**: Data points within the same cluster should be very similar (distance minimized, similarity maximized)
- **Maximize inter-cluster distance**: Data points in different clusters should be very dissimilar (distance maximized, similarity minimized)

**Note**: Distance and similarity are **inversely proportional**:
- High distance = Low similarity
- Low distance = High similarity

### 2. Association Rule Mining

**Definition**: Algorithms that find **interesting relationships or rules** between variables in a dataset.

**Key Principles**:
- Find **frequently occurring items together**
- Discover **dependency rules** that can predict the occurrence of one item based on another
- Identify patterns like: "If item A is bought, then item B is also likely to be bought"

**Goal**: Find relationships and patterns between items in the data

---

## Clustering: Detailed Explanation

### What is Clustering?

Given a set of data points (only **X**, no **Y**, no class labels, no correct answers), the goal of clustering algorithms is to:

1. **Find groups** such that data points in one group are **very similar to each other**
2. **Separate groups** such that data points in different groups are **very dissimilar to each other**

### Clustering Example: India State Division (1947)

**Historical Context**: After independence in 1947, India needed to decide how to organize the country - as one unit or divided into states.

**Problem**: How to divide the country into states?

**Solution Philosophy**:
- **Similar people** → Put into **one state**
- **Dissimilar people** → Put into **different states**

**Similarity Criterion**: **Language**
- If two people speak the **same language** → Put into one state
- If two people speak **different languages** → Put into different states

**Examples**:
- People speaking **Malayali** → Kerala state
- People speaking **Tamil** → Tamil Nadu state
- People speaking **Punjabi** → Punjab state
- People speaking **Gujarati** → Gujarat state
- People speaking **Marathi** → Maharashtra state
- People speaking **Bengali** → West Bengal state
- People speaking **Odiya** → Odisha state

**Key Insight**:
- This was **NOT about prediction** - it was about finding similarity
- Similar people (same language) grouped together
- Dissimilar people (different languages) separated into different groups
- **Result**: Majority of state boundaries today are based on language

**Alternative Similarity Criteria** (could have been used):
- Height of person
- Gender
- Physical attributes
- Clothing/dress (saree, salwar kurta, dhoti kurta, etc.)
- But language was chosen as the primary criterion

### Clustering Objective

The idea of any clustering algorithm is to:
- **Minimize intra-cluster distance**: Distance inside the cluster should be minimized
- **Maximize inter-cluster distance**: Distance between clusters should be maximized

**In other words**:
- **Within cluster**: Similarity should be **maximized** (distance minimized)
- **Between clusters**: Similarity should be **minimized** (distance maximized)

---

## Real-World Applications

### Clustering Applications

#### 1. Google News - Document Clustering

**Problem**: Thousands of news articles are generated every day. Presenting all articles as one bunch is not an effective way to pass information.

**Solution**: **Topic identification** using clustering
- Divide news articles into **groups based on topic**
- **Similar news articles** → Put into **one group**
- **Dissimilar news articles** → Put into **different groups**

**Result**: News articles organized by categories:
- **Finance** news articles in one group
- **Foreign** news articles in another group
- **National** news articles in another group
- **Metro** news articles in another group
- **Sports** news articles in another group

**Key Point**: Not doing any prediction - just finding similarity between news articles and grouping them.

#### 2. Stock Market Analysis

**Problem**: Analyze which groups of companies are performing well.

**Application**:
- **Oil companies** performing well → One group
- **Defense companies** performing well → Another group
- **Technology companies** performing well → Another group
- **Finance companies** performing well → Another group

**Example Scenario**:
- After budget announcement: "Technology companies are going to perform well" (because government reduced tax on technology companies)
- If oil price comes down → All companies related to oil business will see stock price increase

**Key Point**: Finding groups/clusters in the data, not doing prediction.

#### 3. Market Segmentation

**Problem**: Divide market into segments for targeted marketing.

**Application**:
- **Direct marketing**: Market to a specific group of customers
- **Example**: When launching an iPhone, don't market it to people with very low income
- **Strategy**: Identify customer segments and target marketing efforts accordingly

**Key Point**: Clustering helps identify natural customer groups for effective marketing.

### Association Rule Mining Applications

#### 1. Supermarket Shelf Management

**Problem**: How to arrange thousands of products in a supermarket effectively?

**Solution**: Use association rule mining to identify items that are **frequently bought together**.

**Strategy**:
- **Items bought together** → Arrange them in **one place**
- **Items not bought together** → Arrange them in **different places**

**Example**:
- If **samosa** is bought, there is a **high chance** that **coke** will also be bought
- Stack items that are frequently purchased together near each other

**Benefit**:
- Improves customer shopping experience
- Increases sales through strategic product placement
- Makes shopping more convenient

#### 2. Inventory Management

**Application**: Use association rules to manage inventory effectively.

**Strategy**:
- Identify items that are frequently purchased together
- Stock related items together
- Optimize inventory based on purchasing patterns

**Benefit**: Better inventory control and reduced stockouts.

#### 3. Classic Example: "Tanda" and Coca Cola

**Tagline**: "Tanda means Coca Cola"

**Concept**: This is an association rule mining example - finding association between two things:
- If one thing is happening (thirst/"tanda"), another thing will also happen (purchase of Coca Cola)
- Association rule: **Thirst → Coca Cola**

---

## Key Concepts Summary

### Clustering

- **Purpose**: Find natural groups in data
- **Input**: Only X (no labels)
- **Output**: Groups/clusters of similar data points
- **Principle**: Minimize intra-cluster distance, maximize inter-cluster distance
- **Applications**: Document clustering, stock market analysis, market segmentation

### Association Rule Mining

- **Purpose**: Find interesting relationships or rules between variables
- **Input**: Only X (no labels)
- **Output**: Dependency rules (if A, then B)
- **Principle**: Find frequently occurring items together
- **Applications**: Supermarket management, inventory management, product recommendations

---

## Summary

### Key Takeaways

1. **Unsupervised Learning**:
   - Uses **only X** (no labels, no Y)
   - Goal is **NOT prediction** - it's **knowledge discovery**
   - Finds **hidden structure, patterns, and relationships** in data
   - Also known as **descriptive methods** or **knowledge discovery**

2. **Two Types of Unsupervised Learning**:
   - **Clustering**: Groups similar data points together, finds natural groups
     - Principle: Minimize intra-cluster distance, maximize inter-cluster distance
   - **Association Rule Mining**: Finds relationships and rules between items
     - Principle: Find frequently occurring items together

3. **Clustering Applications**:
   - **Google News**: Document clustering by topic
   - **Stock Market Analysis**: Grouping companies by performance patterns
   - **Market Segmentation**: Dividing customers into groups for targeted marketing
   - **Historical Example**: India state division based on language

4. **Association Rule Mining Applications**:
   - **Supermarket Shelf Management**: Arrange items bought together
   - **Inventory Management**: Optimize stock based on purchasing patterns
   - **Product Recommendations**: Identify item associations

5. **Key Difference from Supervised Learning**:
   - **Supervised**: X + Y → Prediction
   - **Unsupervised**: X only → Pattern discovery

### Important Distinctions

| Concept | Supervised Learning | Unsupervised Learning |
|---------|-------------------|----------------------|
| **Data** | X + Y (with labels) | X only (no labels) |
| **Goal** | Prediction | Pattern discovery / Knowledge discovery |
| **Output** | Predictions for new data | Groups, patterns, relationships |
| **Examples** | Classification, Regression | Clustering, Association Rule Mining |

| Concept | Clustering | Association Rule Mining |
|---------|-----------|------------------------|
| **Focus** | Grouping similar items | Finding relationships between items |
| **Output** | Natural groups/clusters | Dependency rules (if A, then B) |
| **Question** | "What are the natural groups?" | "What items occur together?" |
| **Example** | News articles by topic | Samosa → Coke |

---

*Notes compiled from: Module 1 - Unsupervised Learning, Discovering Hidden Patterns (Dr. Hemant Rathore, Video 3)*
