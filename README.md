
### **Project: Aviva Insurance Data Analysis ~ Hypothesis Testing and Predictive Modeling**  

## **📌 Table of Contents**  
1. [Introduction](#introduction)  
2. [Data Overview & Objective](#data-overview--objective)  
3. [Data Preparation & Descriptive Statistics](#data-preparation--descriptive-statistics)  
   - 3a. Data Preparation  
     - 3a.1 Import Required Libraries  
     - 3a.2 Data Loading and Overview  
     - 3a.3 Data Cleaning and Encoding  
   - 3b. Descriptive Statistics  
     - 3b.1 Descriptive Statistics  
     - 3b.2 Correlation Matrix  
4. [Hypothesis Testing](#hypothesis-testing)  
   - 4.1 Steps in Hypothesis Testing  
   - 4.2 Hypothesis 1: BMI and Genders  
   - 4.3 Hypothesis 2: ANOVA ~ Age vs Charges  
   - 4.4 Hypothesis 3: BMI Impact on Charges  
   - 4.5 Hypothesis 4: Medical Claims of Smokers vs Non-Smokers  
   - 4.6 Hypothesis 5: ANOVA Analysis ~ BMI and Number of Children  
   - 4.7 Chi-Square Test for Smoking Proportions Across Regions  
   - 4.8 Advanced Predictive Modeling  
     - 4.8.1 Elastic Net for Linear Regression with GridSearchCV  
     - 4.8.2 Random Forest Regressor with GridSearchCV  
     - 4.8.3 Gradient Boosting Regressor with GridSearchCV for Hyperparameter Tuning  
5. [Conclusion](#conclusion)  
6. [Deployment with Streamlit](#deployment-with-streamlit)  
7. [Next Steps](#next-steps)  

---

## **📌 Introduction**  
This project provides Aviva with an in-depth analysis of the factors influencing insurance charges. It focuses on key demographic and lifestyle attributes such as **age, number of children, smoking status, and BMI**.  

We employ **Exploratory Data Analysis (EDA)**, **Hypothesis Testing** to uncover statistical relationships, and **Predictive Modeling** to forecast insurance charges. The findings aim to **enhance risk assessment and optimize underwriting strategies**.  

---

## **📌 Data Overview & Objective**  
The dataset consists of **1,338 records**, capturing key attributes such as:  

- **Age**: Customer's age in years  
- **Gender**: Male or Female  
- **BMI**: Body Mass Index, a health risk indicator based on weight and height  
- **Smoker**: Whether the customer is a smoker or non-smoker  
- **Region**: Geographic location (Northeast, Northwest, Southeast, Southwest)  
- **Charges**: The annual insurance premium charged  

### **🔹 Project Objectives**  
✅ **Exploratory Data Analysis (EDA)** – Identify trends, distributions, and relationships within the dataset  
✅ **Hypothesis Testing** – Evaluate how demographic factors impact insurance charges  
✅ **Predictive Analysis** – Develop models to forecast charges, helping Aviva make data-driven underwriting decisions  
✅ **Customer Insights** – Identify risk patterns and tailor insurance premiums accordingly  

---

## **📌 Data Preparation & Descriptive Statistics**  
### **🔹 Data Preparation**  
- **Import Required Libraries** – Load necessary Python libraries for analysis  
- **Data Loading and Overview** – Read the dataset and inspect missing values, data types, and general structure  
- **Data Cleaning and Encoding** – Handle missing values, outliers, and categorical encoding  

### **🔹 Descriptive Statistics**  
- **General Summary Statistics** – Mean, median, standard deviation, and distribution of key variables  
- **Correlation Matrix** – Understanding relationships between numeric features  

---

## **📌 Hypothesis Testing**  
### **🔹 Steps in Hypothesis Testing**  
1. Define **Null (H₀)** and **Alternative (H₁)** hypotheses  
2. Choose an appropriate **statistical test**  
3. Set a **significance level (α = 0.05)**  
4. Compute the **test statistic and p-value**  
5. Interpret the results and **accept/reject H₀**  

### **🔹 Key Hypothesis Tests**  
📌 **Hypothesis 1:** Does BMI differ significantly between males and females?  
📌 **Hypothesis 2:** Does **age** influence **insurance charges** (ANOVA Test)?  
📌 **Hypothesis 3:** Is there a correlation between **BMI** and **charges**?  
📌 **Hypothesis 4:** Do **smokers pay significantly higher premiums** than non-smokers?  
📌 **Hypothesis 5:** Does **BMI vary based on the number of children** (ANOVA Test)?  
📌 **Chi-Square Test:** Is the **proportion of smokers different across regions**?  

---

## **📌 Predictive Modeling**  
We build **three machine learning models** to predict insurance charges:  

✅ **Elastic Net Regression** – A regularized linear model combining L1 (Lasso) & L2 (Ridge) penalties  
✅ **Random Forest Regressor** – An ensemble learning model using multiple decision trees  
✅ **Gradient Boosting Regressor** – A boosting technique to improve predictive performance  

All models undergo **hyperparameter tuning** using **GridSearchCV**.  

---

## **📌 Conclusion**  
This study provides valuable insights into **factors affecting insurance charges**, statistical significance of relationships, and **predictive models** for premium estimation.  

Key takeaways include:  
✅ **Smoking has the highest impact on insurance costs**  
✅ **BMI and age significantly influence charges**  
✅ **Predictive models help forecast costs, improving risk assessment**  

---

## **📌 Deployment with Streamlit**  
The final analysis is deployed using **Streamlit**, allowing interactive exploration of the results.  

💡 **To run the app locally:**  
```bash
streamlit run app.py
```

---

## **📌 Next Steps**  
🔹 Expand the dataset to include more policyholders for improved generalization  
🔹 Incorporate additional features like **pre-existing medical conditions**  
🔹 Fine-tune predictive models with **ensemble learning and deep learning approaches**  

---

## **🚀 Get Started**  
Clone this repository and explore the notebook:  
```bash
git clone https://github.com/Tolumie/Statistics_Hypothesis_AB_Testing.git
cd Statistics_Hypothesis_AB_Testing
```

