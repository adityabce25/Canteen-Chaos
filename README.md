# 🏛️ Canteen Chaos: An Intelligent Decision Support System

**Canteen Chaos** is an AI-powered terminal application designed to solve the problem of **Time Uncertainty** for college students. By analyzing historical data and current environmental factors, the system predicts canteen wait times and acts as an advisor to help students decide whether to visit the canteen or stay in class based on their personal hunger and schedule.

---

## ✨ Features

* **Wait-Time Prediction:** Accurate estimates of queue times based on **Day**, **Hour**, **Weather**, and **Exam schedules**.
* **Rational Advisor:** A decision engine that balances your **Hunger Level** against your **Class Schedule** to give a "Go" or "Stay" recommendation.
* **Stochastic Simulation:** A custom data generator that creates realistic campus traffic datasets using probability distributions.
* **Professional Terminal UI:** A clean, color-coded CLI dashboard built with the \`Rich\` library for a modern look and feel.

---

## 🛠️ Tech Stack

* **Language:** Python 3.14
* **Machine Learning:** \`Scikit-learn\` (Random Forest Regression)
* **Data Processing:** \`Pandas\` & \`NumPy\`
* **Model Persistence:** \`Joblib\`
* **Interface:** \`Rich\` (Terminal Formatting)

---

## 📂 Project Structure

\`\`\`text
Canteen Chaos/
├── main.py              # Master Controller (The entry point)
├── data/                # Directory for the generated CSV dataset
├── models/              # Directory for the trained AI models (.pkl files)
└── scripts/
    ├── data_generator.py # Script to generate synthetic campus data
    ├── model_trainer.py  # Script to train the Machine Learning model
    └── canteen_app.py    # The User Interface & Decision Logic
\`\`\`

---

## 🚀 Installation & Setup

1.  **Navigate to the project root directory:**
    \`\`\`bash
    cd "Canteen Chaos"
    \`\`\`

2.  **Install the necessary dependencies:**
    \`\`\`bash
    python3 -m pip install pandas numpy scikit-learn rich joblib
    \`\`\`

3.  **Run the application:**
    \`\`\`bash
    python3 main.py
    \`\`\`

> **Note:** The \`main.py\` script is designed to be self-healing. If it detects that the data or the trained model is missing, it will automatically trigger the generation and training scripts before launching the application.

---