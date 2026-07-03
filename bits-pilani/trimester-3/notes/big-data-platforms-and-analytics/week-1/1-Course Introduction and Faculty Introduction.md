# Course Introduction and Faculty Introduction – Big Data Platforms and Analytics (Module 1)

## Learning Objectives

By the end of this video you will:

1. **Understand** the instructor's background and expertise in data engineering and generative AI.
2. **Recognize** the real-world engineering challenges that will be covered in this course.
3. **Describe** the overall course structure and key topics for each module.
4. **Explain** why big data is fundamentally an infrastructure problem, not just a size problem.
5. **Identify** the key technologies and frameworks that will be covered (MapReduce, Spark, Kafka, etc.).

---

## Instructor Background

### Watsal Mishra
- **Current Role**: Leads data engineering and generative AI initiatives at Google
- **Experience**: 6+ years at Google, transitioning from technical solutions consultant to senior data engineer
- **Expertise**: Scaling complex data infrastructure at world's most data-driven organizations
- **Previous Experience**:
  - Senior data platform development engineer at Urban Company (erstwhile Urban Clap)
  - Big data engineer at ZS, handling large-scale commercial data for pharmaceutical industry
- **Technical Toolkit**: Python, Spark, Kafka, SQL, Java, Spring framework
- **Education**: Bachelor of Technology in Electronics and Communications Engineering from TripleIT Allahabad

### Career Journey
- Management consulting → High growth startups → Google (data engineering and generative AI)
- Passion for transforming raw data into actionable intelligence and insights
- Focus on maintaining data platforms powered by Kafka and Spark
- Experience with Snowflake data warehouses and business intelligence tools (Redash, Jupiter Hub)

---

## Course Philosophy

### Real-World Focus
- **Not just theory**: This course shares real-world engineering challenges and solutions
- **Industry experience**: Lessons learned from some of the world's most data-driven organizations
- **Practical approach**: Designed to prepare for real-world challenges of data engineering

### Course Goal
- **Master the platforms** that power the future of analytics
- **Understand the architecture and strategy** behind modern data systems
- **Learn through practical examples** and engineering challenges

---

## Course Overview

### Module Structure

#### **Weeks 1-2: Big Data Constraints and Scaling**
- **Focus**: The three V's (Volume, Velocity, Variety)
- **Key Question**: Why can't regular computers handle big data?
- **Topics**:
  - Hardware limitations and vertical scaling
  - Shift to horizontal scaling using commodity hardware
  - CAP Theorem fundamentals

#### **Weeks 3-6: Processing Engines**
- **Week 3**: MapReduce Architecture
- **Weeks 4-6**: Spark Revolution (in-memory computing, RDDs, DAG, lazy evaluation)
- **Key Difference**: Spark is 100x faster than MapReduce due to in-memory processing

#### **Weeks 7-8: Resilience**
- **Focus**: System recovery and fault tolerance
- **Topics**:
  - Spark lineage and recovery strategies
  - Checkpointing to prevent 24-hour jobs from restarting
  - High availability and data redundancy

#### **Weeks 9-10: Data Partitioning**
- **Focus**: Solving data skew problems
- **Topics**:
  - Advanced optimization techniques
  - Salting and broadcasting
  - Avoiding hot spots that can paralyze pipelines

#### **Weeks 11-12: Distributed Machine Learning**
- **Focus**: Training models too big for single machines
- **Topics**:
  - TensorFlow distributed strategies
  - Ring all-reduce method
  - Model and data parallelism

#### **Week 13: Real-time Intelligence**
- **Focus**: Stream processing and real-time analytics
- **Topics**:
  - Kafka and Storm integration
  - Fraud detection and dynamic pricing systems
  - Systems where every millisecond counts

---

## Big Data: Size vs Infrastructure

### The Secret
- **Big data isn't just a size problem**
- **It's an infrastructure problem**
- **Shift in thinking**: From "how to store more data" to "how to process data at scale"

### Key Challenges
1. **Volume**: Data that doesn't fit on single machines
2. **Velocity**: Data coming too fast for single processors
3. **Variety**: Different data types requiring different processing approaches

### The Solution Architecture
- **From bigger boxes to more boxes**
- **Commodity hardware clusters**
- **Distributed processing and storage**

---

## Real-World Examples

### Netflix
- **Challenge**: Streaming to 200+ million users simultaneously
- **Solution**: Thousands of distributed servers across the globe
- **Benefit**: Load distribution and fault tolerance

### Uber
- **Challenge**: Real-time price calculation based on traffic, drivers, weather
- **Solution**: Parallel processing with Apache Spark
- **Benefit**: Real-time decision making

### Amazon
- **Challenge**: Processing millions of clicks and transactions per second
- **Solution**: Distributed storage and processing
- **Benefit**: Scalability and reliability

---

## Course Technology Stack

### Core Technologies
- **Processing Engines**: MapReduce, Apache Spark
- **Streaming**: Kafka, Storm
- **Distributed ML**: TensorFlow, ring all-reduce
- **Storage**: HDFS, Snowflake
- **Tools**: Redash, Jupiter Hub

### Key Concepts
- **Resilient Distributed Datasets (RDDs)**
- **Directed Acyclic Graphs (DAG)**
- **Lazy evaluation**
- **Data partitioning and skew handling**
- **Fault tolerance and recovery**

---

## Summary

- **Instructor expertise**: Real-world experience with Google, Urban Company, and ZS
- **Course focus**: Practical engineering challenges and solutions
- **Big data reality**: Infrastructure problem requiring distributed systems
- **Learning path**: From constraints to processing engines to resilience to optimization
- **Goal**: Master the platforms powering modern analytics

This course provides the foundation for understanding why big data requires fundamentally different approaches to computing and how modern data platforms are designed to handle these challenges.