# Student Performance Prediction Model 🎓

A comprehensive machine learning project that predicts student academic performance based on various factors including study habits, sleep patterns, and extracurricular activities.

## 🚀 Features

- **Web Application**: Interactive Django-based prediction interface
- **ML Pipeline**: Complete machine learning workflow with multiple model comparison
- **Advanced Analytics**: Feature engineering and hyperparameter tuning
- **Production Ready**: Deployed model with REST API

## 📊 Project Structure

```
├── student_ml/                    # Django web application
│   ├── performance/              # Main app
│   │   ├── templates/           # HTML templates
│   │   ├── views.py             # API endpoints
│   │   ├── models.py            # Django models
│   │   └── serializers.py       # Data serializers
│   └── manage.py                 # Django management
├── student_performance_prediction.ipynb  # ML pipeline notebook
├── requirements.txt              # Python dependencies
└── README.md                     # This file
```

## 🛠️ Technology Stack

- **Backend**: Django, Django REST Framework
- **Machine Learning**: Scikit-learn, Pandas, NumPy
- **Data Visualization**: Matplotlib, Seaborn
- **Frontend**: HTML5, CSS3, JavaScript

## 📦 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/Angek12/Student_Prediction_model.git
   cd Student_Prediction_model
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Running the Application

### Web Application

1. **Navigate to Django project**
   ```bash
   cd student_ml
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

3. **Start the server**
   ```bash
   python manage.py runserver
   ```

4. **Access the application**
   - Open your browser and go to `http://127.0.0.1:8000`

### Jupyter Notebook

1. **Start Jupyter**
   ```bash
   jupyter notebook
   ```

2. **Open the notebook**
   - Navigate to `student_performance_prediction.ipynb`

## 📈 Model Performance

The system uses an optimized machine learning pipeline with:

- **Multiple Algorithms**: Linear Regression, Random Forest, Gradient Boosting
- **Hyperparameter Tuning**: GridSearchCV for optimal performance
- **Feature Engineering**: Advanced feature creation for better predictions

**Expected Performance:**
- R² Score: ~0.95+
- MAE: ±2-3 points

## 🎯 Features

### Input Parameters
- **Hours Studied**: Daily study hours (0-24)
- **Previous Scores**: Historical academic performance (0-100)
- **Extracurricular Activities**: Participation in non-academic activities
- **Sleep Hours**: Daily sleep duration (0-24)
- **Sample Papers Practiced**: Number of practice papers completed

### Output
- **Predicted Performance Index**: Academic performance score (0-100)
- **Performance Category**: Excellent, Good, Needs Improvement, Requires Focus

## 📊 API Endpoints

### POST `/api/predict/`

**Request Body:**
```json
{
    "hours_studied": 7,
    "previous_scores": 85,
    "extracurricular": true,
    "sleep_hours": 8,
    "sample_papers": 5
}
```

**Response:**
```json
{
    "predicted_performance_index": 78,
    "category": "Good",
    "advice": "Good performance! Continue your current study habits."
}
```

## 👨‍💻 Author

**Ange Kevine**
- GitHub: [@Angek12](https://github.com/Angek12)

---

⭐ If you find this project helpful, please give it a star!
