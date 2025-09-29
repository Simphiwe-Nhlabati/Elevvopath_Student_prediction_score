# Student Score Prediction App

![Student Success Banner](https://img.freepik.com/free-vector/education-banner-background_53876-115373.jpg) <!-- You can replace this with your own image link -->

## 📚 Overview

The **Student Score Prediction App** is a machine learning-powered web application designed to predict student exam scores based on key academic and lifestyle factors. By leveraging advanced regression models, the app helps educators, students, and parents understand how different habits and activities impact academic performance.

### 🚀 Features

- Predicts exam scores using factors like:
  - Hours Studied
  - Attendance Percentage
  - Sleep Hours
  - Tutoring Sessions
  - Physical Activity
- Interactive and user-friendly interface built with Streamlit
- Utilizes models trained on real student performance data
- Provides instant feedback and insights

## 🛠️ Technologies Used

- Python
- Streamlit
- scikit-learn
- pandas
- numpy
- joblib

## 📦 Installation & Usage

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/student_score_prediction.git
cd student_score_prediction
```

### 2. Install Dependencies with [uv](https://github.com/astral-sh/uv)

If you don't have `uv` installed, get it [here](https://github.com/astral-sh/uv).

```sh
uv pip install -r requirements.txt
```

### 3. Run the App

```sh
uv pip install streamlit
streamlit run app.py
```

Or, if you want to run with `uv` directly:

```sh
uv venv
uv pip install -r requirements.txt
uv pip install streamlit
uv run streamlit app.py
```

## 📊 How It Works

1. The app loads a trained model from `student_success_models.pkl`.
2. Users input their study hours, attendance, sleep, tutoring, and physical activity.
3. The model predicts the likely exam score and displays it instantly.

## 📝 Data

The model is trained on anonymized student data from `StudentPerformanceFactors.csv`, considering multiple academic and lifestyle features.

## 👨‍💻 Author

Developed by **Simphiwe Nhlabati**

---

> _Empowering students and educators with data-driven insights for better academic outcomes._
