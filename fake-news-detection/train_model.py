import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
from preprocess import clean_text

# Load Fake aur True dono CSV
fake = pd.read_csv('dataset/Fake.csv')
true = pd.read_csv('dataset/True.csv')

# Label lagao
fake['label'] = 1   # 1 = FAKE
true['label'] = 0   # 0 = REAL

# Combine karo
df = pd.concat([fake, true], ignore_index=True)

# 'text' column check karo
# Kaggle dataset mein 'text' ya 'title' column hota hai
df = df[['text', 'label']].dropna()

# Baaki code same rahega...
print("Cleaning text...")
df['clean_text'] = df['text'].apply(clean_text)

X_train, X_test, y_train, y_test = train_test_split(
    df['clean_text'], df['label'],
    test_size=0.2, random_state=42
)

vectorizer = TfidfVectorizer(max_features=5000, ngram_range=(1,2))
X_train_vec = vectorizer.fit_transform(X_train)
X_test_vec  = vectorizer.transform(X_test)

print("Training model...")
model = LogisticRegression(max_iter=1000)
model.fit(X_train_vec, y_train)

y_pred = model.predict(X_test_vec)
print(f"\nAccuracy: {accuracy_score(y_test, y_pred):.4f}")
print(classification_report(y_test, y_pred,
      target_names=['REAL', 'FAKE']))

pickle.dump(model,      open('model.pkl', 'wb'))
pickle.dump(vectorizer, open('vectorizer.pkl', 'wb'))
print("\nModel saved successfully!")