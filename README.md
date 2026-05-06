#Carpooling Price Prediction — Morocco

End-to-end ML project: from data generation to a live prediction API.

## Project Structure
carpooling-price-prediction/
├── ml/
│   ├── train.ipynb           
│   └── carpooling_dataset.csv
│   └──price-model.pkl
├── api/
│   └── app.py                # FastAPI prediction server
└── requirements.txt

## Setup

### 1. Clone the repo
git clone https://github.com/your-username/carpooling-price-prediction.git
cd carpooling-price-prediction

### 2. Install dependencies
pip install -r requirements.txt

### 3. Train the model
Open and run ml/train.ipynb — this generates ml/price_model.pkl

### 4. Start the API
cd api
uvicorn app:app --reload

### 5. Test it
Open http://localhost:8000/docs

## API Usage

POST /predict
{
  "distance": 120,
  "available_seats": 2,
  "time_before_departure": 1.0
}

Response:
{
  "price": 94.5,
  "currency": "MAD"
}

## Tech Stack
- Python
- scikit-learn
- FastAPI
- pandas / numpy