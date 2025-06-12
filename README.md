# Turkish Sentiment Analysis Pipeline 🇹🇷

Bu proje, Türkçe metinlerde duygu analizi (pozitif, negatif, nötr) yapabilen bir makine öğrenmesi pipeline'ıdır.

## 🔍 Kullanılan Teknolojiler
- Python
- Scikit-learn
- Pandas
- Türkçe Duygu Veriseti ([Kaggle Dataset](https://www.kaggle.com/datasets/omerb/turkish-emotion-dataset))

## 🧪 Nasıl Çalışır?
1. `data/` klasöründeki CSV dosyası ön işleme alınır.
2. Veriler TF-IDF ile vektörleştirilir.
3. Logistic Regression ile model eğitilir.
4. `predict.py` üzerinden test yapılabilir.

## 🚀 Kurulum
```bash
git clone https://github.com/kendi-username/turkish-sentiment-analysis-pipeline.git
cd turkish-sentiment-analysis-pipeline
pip install -r requirements.txt
python src/train_model.py
python src/predict.py --text "Bugün hava çok güzel ama biraz yorgunum."
```

## 👤 Geliştirici
Çağatay - Elektrik Elektronik Mühendisliği, TOGÜ
