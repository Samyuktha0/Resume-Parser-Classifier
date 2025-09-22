import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import pickle

def train_model():
    df = pd.read_csv('data/labeled_dataset.csv')
    X = df['text']
    y = df['label']
    vec = TfidfVectorizer()
    X_vec = vec.fit_transform(X)
    clf = LogisticRegression()
    clf.fit(X_vec, y)
    with open('model/resume_classifier.pkl', 'wb') as f:
        pickle.dump((vec, clf), f)

def predict_resume(text):
    with open('model/resume_classifier.pkl', 'rb') as f:
        vec, clf = pickle.load(f)
    X_vec = vec.transform([text])
    return clf.predict(X_vec)[0]
