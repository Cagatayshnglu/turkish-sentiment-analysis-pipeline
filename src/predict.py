import pickle
import argparse

model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def predict_sentiment(text):
    vec = vectorizer.transform([text])
    pred = model.predict(vec)
    return pred[0]

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--text", type=str, required=True)
    args = parser.parse_args()
    print("Tahmin:", predict_sentiment(args.text))
