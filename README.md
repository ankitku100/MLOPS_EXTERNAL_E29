
# Ceramic Pottery Kiln Energy Prediction Using MLOps

## Project Description
This project predicts electricity consumption (kWh)
for ceramic pottery kiln firing batches.

## Technologies
- Python
- Pandas and NumPy
- Scikit-learn
- MLflow
- FastAPI
- GitHub Actions

## Dataset
- Version 1: New kiln
- Version 2: Older kiln

## Machine Learning Models
1. Linear Regression
2. Random Forest Regression

## Features
- Dataset version management
- Data preprocessing
- Feature engineering
- MLflow model registry
- Automated testing
- FastAPI prediction API

## Run Project

Install dependencies:

pip install -r requirements.txt

Run API:

uvicorn app:app --reload

Open:

http://127.0.0.1:8000/docs

## Output
Predicts electricity consumption in kWh.
