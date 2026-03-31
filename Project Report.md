
# 🏛️ PROJECT REPORT: CANTEEN CHAOS
**An Intelligent Decision Support System using Machine Learning and Rational Agent Logic**

**NAME:** Aditya Choudhary 

**REG NO.:** 25BCE11161

**COURSE:** CSE2001 Fundamentals in AI ML
 

---

## 1. Executive Summary
The "Canteen Chaos" project is a terminal-based Intelligent Agent designed to mitigate the uncertainty of campus dining wait times. By utilizing a **Random Forest Regressor** trained on synthetically generated stochastic data, the system provides real-time wait estimates and a "Go/No-Go" advisor. The project successfully demonstrates the integration of statistical distributions (Poisson/Gaussian) and Supervised Learning to solve a common logistical problem.

---

## 2. Problem Statement
College students often face a "Time-Utility Tradeoff" between attending classes and visiting the canteen. High variability in queue lengths leads to:
1. **Punctuality Issues:** Students arriving late to lectures due to unforeseen delays.
2. **Health Issues:** Students skipping meals to avoid potential lateness.
The objective of this project is to build an agent that predicts these delays with high accuracy and offers rational advice based on user-specific constraints.

---

## 3. System Architecture & Methodology
The system follows a modular 3-stage pipeline:

### 3.1 Data Generation (The Environment)
To simulate a realistic campus environment, the dataset was generated using two primary statistical models:
* **Arrival Rate:** Modeled using a **Poisson Distribution** to represent random student arrivals over a fixed interval.
* **Stochastic Noise:** A **Gaussian (Normal) Distribution** was used to simulate random "chaos" factors (e.g., equipment failure, slow service).

### 3.2 Machine Learning (The Brain)
A **Random Forest Regressor** was selected as the primary estimator. This model was chosen for its ability to handle non-linear relationships between variables like Weather, Exam Week, and Time of Day. 
* **Train/Test Split:** 80/20 ratio to ensure model generalization.
* **Preprocessing:** Label Encoding was used to convert categorical features into numerical vectors.

### 3.3 Rational Agent Logic (The Interface)
The agent operates on a **Utility-based decision model**. It calculates the benefit of eating vs. the cost of being late:
**Utility = (Hunger × Benefit_Weight) - (WaitTime × Time_Weight) - (Lateness_Penalty)**

---

## 4. Implementation Details

### Tech Stack:
* **Language:** Python 3.14
* **Libraries:** Scikit-learn(ML), Pandas(Data Manipulation), Rich (CLI UI), Joblib(Model Persistence).

### Code Organization:
* data_generator.py: Generates the "World" dataset (1,500+ records).
* model_trainer.py: Trains the "Brain" and validates accuracy.
* canteen_app.py: The user-facing "Agent" that provides advice.

---

## 5. Results and Discussion
The final model achieved a high accuracy score, indicating that factors like "Lunch Hour" and "Weather" are strong predictors of wait time. The "Rational Advisor" successfully identifies scenarios where high hunger justifies a slight risk of being late, mimicking human decision-making but backed by data.

### Sample Interaction:
* **Input:** Monday, 12:00 PM, Rainy.  
* **AI Prediction:** 22.5 Minutes.  
* **User Input:** Hunger 9/10, Time Left 20 mins.  
* **Agent Decision:** \`⚠️ RISKY GO\` (Utility remains high due to extreme hunger).

---

## 6. Conclusion
"Canteen Chaos" demonstrates that even simple terminal-based applications can solve complex human problems when powered by robust Machine Learning models. The project successfully bridges the gap between theoretical probability and practical AI application.

---

## 7. References
1. *Artificial Intelligence: A Modern Approach* - Russell & Norvig.
2. *Scikit-learn Documentation* (Random Forest Regression).
3. *Numpy Documentation* (Random Sampling & Distributions).
   
