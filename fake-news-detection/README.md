# Fake News Detection System

A machine learning project that detects whether a news article is REAL or FAKE.

## Tech Stack
- Python, Scikit-learn, NLTK
- TF-IDF Vectorization
- Logistic Regression
- Streamlit (Web UI)

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Download dataset from Kaggle (link below)
3. Train model: `python train_model.py`
4. Run app: `streamlit run app.py`

## Dataset
Download from Kaggle: https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset

## Results
- Accuracy: ~95%
- Model: Logistic Regression with TF-IDF features