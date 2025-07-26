

# 🩺 Smart Disease Prediction System

A powerful and interactive Streamlit-based web application that predicts the most likely disease based on symptoms entered by a user. It also provides a personalized healthcare plan including descriptions, medications, precautions, workouts, and dietary suggestions.

---

## 📌 Table of Contents

* [🔍 Overview](#-overview)
* [⚙️ Features](#-features)
* [🛠️ Installation](#️-installation)
* [🚀 How to Run](#-how-to-run)
* [📁 Dataset and Model](#-dataset-and-model)
* [💡 Example Usage](#-example-usage)
* [🧠 Project Structure](#-project-structure)
* [📦 Dependencies](#-dependencies)


---

## 🔍 Overview

This application allows users to enter symptoms and receive predictions for the most likely disease, using a trained Support Vector Classifier (SVC) model. It also provides detailed health guidance related to the predicted disease including:

* Descriptions
* Medications
* Precautionary measures
* Recommended workouts
* Dietary suggestions

---

## ⚙️ Features

✅ Symptom Matching using fuzzy logic
✅ Disease Prediction using Machine Learning (SVC)
✅ Clean and professional user interface with Streamlit
✅ Error handling for invalid symptoms
✅ Expandable sections for organized output
✅ Easy-to-understand health advice

---

## 🛠️ Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/yourusername/disease-prediction-system.git
   cd disease-prediction-system
   ```

2. **Create and activate a virtual environment (optional but recommended)**

   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Run

```bash
streamlit run app.py
```

> ⚠️ Make sure all the required `.csv` and `.pkl` files are present in the project directory.

---

## 📁 Dataset and Model

* `svc.pkl`: Trained Support Vector Classifier model
* `symtoms_df.csv`: Master list of symptoms
* `description.csv`: Descriptions for each disease
* `precautions_df.csv`: List of precautions for each disease
* `medications.csv`: Medications per disease
* `diets.csv`: Dietary suggestions per disease
* `workout_df.csv`: Workouts per disease

---

## 💡 Example Usage

### User Input:

```
fever, headache, cough
```

### Output:

* ✅ **Matched Symptoms**: `fever`, `headache`, `cough`
* 🧾 **Predicted Disease**: Typhoid
* 🩻 **Description**: Typhoid is a bacterial infection that can lead to high fever, diarrhea, and vomiting.
* 🔐 **Precautions**: Avoid outside food, drink clean water, maintain hygiene.
* 💊 **Medications**: \[Antibiotics, Paracetamol...]
* 🏃 **Workouts**: Light walking, Avoid heavy workouts
* 🥗 **Diet**: Boiled food, fluids, and ORS

---

## 🧠 Project Structure

```
├── app.py                   # Main Streamlit app
├── requirements.txt         # Python dependencies
├── svc.pkl                  # Trained SVC model
├── symtoms_df.csv
├── description.csv
├── precautions_df.csv
├── medications.csv
├── diets.csv
├── workout_df.csv
└── README.md
```

---

## 📦 Dependencies

The application requires the following Python libraries:

* streamlit
* numpy
* pandas
* scikit-learn
* difflib
* ast
* warnings

All dependencies are listed in [`requirements.txt`](requirements.txt).

---

## 🙌 Contribution

Contributions are welcome!
If you find any issues or would like to enhance this app, feel free to:

1. Fork the repository
2. Create a new branch
3. Submit a pull request


