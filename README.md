# 🚀 Loan Approval Prediction: End-to-End ML Case Study

[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)](https://scikit-learn.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

## 📌 Project Overview
This repository contains a comprehensive Machine Learning analysis of a **Loan Approval Dataset** consisting of 50,000 records. The primary objective is to build a predictive model that accurately classifies loan applications as 'Approved' or 'Refused' based on financial and demographic data.

In credit risk assessment, the cost of a "False Negative" (approving a high-risk borrower) is significantly higher than a "False Positive," making this a classic challenge in **imbalanced classification**.

## 📊 Dataset Specifications
*   **Observations:** 50,000
*   **Target:** `loan_status` (Binary)
*   **Imbalance:** ~80% Approved / 20% Refused
*   **Key Features:** Annual Income, Credit Score, Debt-to-Income (DTI) ratio, Loan Intent, and Historical Defaults.

## 🛠️ Technical Implementation

### 1. Exploratory Data Analysis (EDA)
Detailed visualization of feature distributions and their relationship with the target variable. We utilize heatmaps to identify multicollinearity and box plots to detect outliers in financial variables like income and loan amount.

### 2. Data Preprocessing
*   **Missing Value Imputation:** Handling nulls using median/mode strategies to preserve data integrity.
*   **Categorical Encoding:** One-Hot and Ordinal encoding for features like 'Employment Type' and 'Home Ownership'.
*   **Class Imbalance (SMOTE):** Since the dataset is skewed, we implemented **Synthetic Minority Over-sampling Technique (SMOTE)** to generate synthetic samples for the 'Refused' class, ensuring the model doesn't become biased toward the majority class.

### 3. Feature Selection (RFECV)
To optimize performance and reduce computational overhead, we utilized **Recursive Feature Elimination with Cross-Validation (RFECV)**. This allowed us to identify the "Golden Features" that contribute most to the model's predictive power while dropping noise.

### 4. Model Training & Evaluation
We benchmarked several models to find the optimal balance of Precision and Recall:
*   **Logistic Regression**
*   **Decision Trees**
*   **Random Forest** (Best Performing)

**Evaluation Metrics:**
*   **F1-Score:** Our primary metric for the imbalanced classes.
*   **ROC-AUC:** To measure the model's ability to distinguish between classes.
*   **Confusion Matrix:** To visualize the trade-off between Type I and Type II errors.

## 🚀 Getting Started

1.  **Clone the Repo:**
    ```bash
    git clone https://github.com/your-username/loan-approval-ml.git
    ```
2.  **Install Dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Analysis:**
    Open `Credit_Risk_Analysis.ipynb` in your preferred IDE to view the step-by-step executionHere is the complete, professional Markdown code for your GitHub repository. I've structured this to showcase a sophisticated machine learning workflow, including the handling of class imbalances and feature selection.
