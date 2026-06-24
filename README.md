# Amazon Product Segmentation and Value Analysis using Unsupervised Learning

<p align="center">
  <img src="image/project_diagram.png" alt="Project Pipeline" width="100%">
</p>

---

## 📌 Project Overview

This project demonstrates an end-to-end Data Science and Machine Learning workflow by collecting real-world Amazon product data through web scraping and transforming it into meaningful business insights.

The project covers the complete pipeline from data acquisition and preprocessing to exploratory data analysis, feature engineering, unsupervised machine learning, and business-driven interpretation. Using K-Means clustering, products are automatically grouped into meaningful segments based on pricing and customer ratings, enabling analysis of product positioning and value.

Rather than simply applying a machine learning algorithm, this project focuses on solving a practical e-commerce problem by identifying product segments and supporting data-driven decision making.

---

## 🎯 Project Objective

The objective of this project is to develop an automated product segmentation system for e-commerce products using unsupervised machine learning techniques.

The project aims to:

* Collect real-world Amazon product data through web scraping.
* Clean and preprocess the collected dataset.
* Explore pricing and customer rating patterns using Exploratory Data Analysis (EDA).
* Engineer meaningful features such as Log Price and Value Score.
* Group similar products using K-Means clustering.
* Evaluate clustering performance using the Elbow Method and Silhouette Score.
* Interpret product segments and generate business insights that can support pricing strategies, inventory planning, and recommendation systems.

Ultimately, this project demonstrates how machine learning can transform raw e-commerce data into actionable business intelligence.

---

## 🛠️ Tools & Technologies

| Category                        | Tools / Technologies           | Purpose                                                                                 |
| ------------------------------- | ------------------------------ | --------------------------------------------------------------------------------------- |
| Programming Language            | Python                         | Core programming language used throughout the project                                   |
| Web Scraping                    | Scrapy                         | Extracted Amazon product information from web pages                                     |
| Data Manipulation               | Pandas, NumPy                  | Data cleaning, preprocessing, transformation, and numerical operations                  |
| Data Cleaning                   | Pandas                         | Handling missing values, removing duplicates, converting data types, validating records |
| Exploratory Data Analysis (EDA) | Matplotlib, Seaborn            | Visualizing data distributions, relationships, and outliers                             |
| Feature Engineering             | NumPy, Pandas                  | Generated new features such as **Log Price** and **Value Score**                        |
| Feature Scaling                 | StandardScaler (Scikit-learn)  | Standardized numerical features before clustering                                       |
| Machine Learning                | Scikit-learn                   | Implemented the K-Means clustering algorithm                                            |
| Cluster Evaluation              | Elbow Method, Silhouette Score | Determined the optimal number of clusters and evaluated clustering quality              |
| Development Environment         | Jupyter Notebook, VS Code      | Data analysis, experimentation, and development                                         |
| Version Control                 | Git & GitHub                   | Project version control and portfolio hosting                                           |

---

## 🤖 Machine Learning Implementation

This project applies **Unsupervised Machine Learning** using the **K-Means Clustering** algorithm.

Unlike supervised learning, the dataset does not contain predefined labels such as *Budget*, *Mid-range*, or *Premium*. The objective is to automatically discover hidden patterns by grouping similar products based on their characteristics.

The clustering process was performed using engineered numerical features derived from the original dataset, allowing products with similar pricing and customer rating characteristics to be placed into the same segment.

---

## 📐 Feature Engineering

To improve clustering performance and generate more meaningful product segments, additional numerical features were created.

### 1. Value Score

The Value Score estimates how much customer satisfaction is obtained relative to the product price.

[
\text{Value Score}=\frac{\text{Rating}}{\text{Price}}
]

A higher Value Score generally indicates products that offer better customer ratings at a relatively lower price.

---

### 2. Log Price Transformation

Product prices often span a very large range, causing highly priced products to dominate distance calculations during clustering.

To reduce this effect, a logarithmic transformation is applied.

[
\text{Log Price}=\log(\text{Price})
]

This transformation compresses extreme price values while preserving their relative ordering, leading to more balanced clustering.

---

## 📏 Feature Scaling

Since K-Means relies on Euclidean distance, numerical features with larger values can dominate the clustering process.

To ensure every feature contributes equally, StandardScaler was applied.

The standardization formula is

[
z=\frac{x-\mu}{\sigma}
]

where

* (x) = original feature value
* (\mu) = mean of the feature
* (\sigma) = standard deviation

After scaling, each feature has approximately:

* Mean = 0
* Standard Deviation = 1

---

## 🧠 K-Means Clustering

K-Means partitions the dataset into **K** groups by minimizing the distance between each observation and the centroid of its assigned cluster.

The optimization objective is

[
J=\sum_{i=1}^{K}\sum_{x\in C_i}\left|x-\mu_i\right|^2
]

where

* (K) = number of clusters
* (C_i) = observations belonging to cluster (i)
* (\mu_i) = centroid of cluster (i)

The algorithm follows these steps:

1. Initialize K cluster centroids.
2. Assign each product to its nearest centroid.
3. Recalculate centroid locations.
4. Repeat until cluster assignments no longer change.

---

## 📊 Cluster Evaluation

Two evaluation techniques were used.

### Elbow Method

The Elbow Method helps determine the optimal number of clusters.

For each value of (K), the **Within-Cluster Sum of Squares (WCSS)** is calculated.

[
WCSS=\sum_{i=1}^{K}\sum_{x\in C_i}\left|x-\mu_i\right|^2
]

The point where adding more clusters produces only marginal improvement (the "elbow") is selected as the optimal number of clusters.

---

### Silhouette Score

The Silhouette Score evaluates how well each observation fits within its assigned cluster.

[
s=\frac{b-a}{\max(a,b)}
]

where

* (a) = average distance to points within the same cluster
* (b) = average distance to the nearest neighboring cluster

Interpretation:

* **1** → Excellent separation
* **0** → Overlapping clusters
* **Negative** → Poor clustering

---

## 💼 Business Value

The generated product segments can support several e-commerce decisions:

* Product segmentation into budget, mid-range, and premium groups.
* Identification of high-value products.
* Detection of potentially overpriced products.
* Pricing strategy analysis.
* Product recommendation systems.
* Inventory planning and marketing campaign optimization.

