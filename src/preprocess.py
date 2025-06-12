import pandas as pd
import re

def clean_text(text):
    text = re.sub(r"[^a-zA-ZçÇğĞıİöÖşŞüÜ\s]", "", text)
    text = text.lower()
    return text

def load_and_clean(path):
    df = pd.read_csv(path)
    df['text'] = df['text'].apply(clean_text)
    return df
