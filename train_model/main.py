import pandas as pd
import numpy as np
import time
import pickle
import os
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder

# Start timing
start_time = time.time()

# Load full dataset
dataset = pd.read_csv('phishing_site_urls.csv')

# Separate classes
bad_urls = dataset[dataset['Label'].str.lower() == 'bad']
good_urls = dataset[dataset['Label'].str.lower() == 'good']

# Check minimum count to balance
min_count = min(len(bad_urls), len(good_urls))
print(f"Balancing classes to {min_count} samples each.")

# Sample equally from both classes
bad_sample = bad_urls.sample(min_count, random_state=42)
good_sample = good_urls.sample(min_count, random_state=42)

# Combine and shuffle
balanced_data = pd.concat([bad_sample, good_sample]).sample(frac=1, random_state=42).reset_index(drop=True)

# Features and labels
x = balanced_data.iloc[:, 0].values  # URLs
y = balanced_data.iloc[:, 1].values  # Labels

# Encode labels: Good -> 0, Bad -> 1
le = LabelEncoder()
y = le.fit_transform(y)
print(f"Label Mapping: {dict(zip(le.classes_, le.transform(le.classes_)))}")

# Convert URLs to features
cv = CountVectorizer()
x = cv.fit_transform(x)

# Split data
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# Train model
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(x_train, y_train)

# End timing
end_time = time.time()
print(f"\n✅ Training completed in {end_time - start_time:.2f} seconds.")

# Save model and vectorizer
model_path = os.path.join(os.getcwd(), 'phishing_model.pkl')
with open(model_path, 'wb') as f:
    pickle.dump((clf, cv), f)

print(f"✅ Model saved to {model_path}")
