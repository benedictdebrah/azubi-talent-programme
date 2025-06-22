# Bank Marketing Model API

This project provides a REST API for predicting whether a bank client will subscribe to a term deposit, based on the 

## Hosted API

You can test the API live at:

[https://harsh-beef-production.up.railway.app/docs](https://harsh-beef-production.up.railway.app/docs)

This link opens the interactive Swagger UI, where you can try out the endpoints directly from your browser.

## How to Use

### 1. Predict Endpoint

- **POST** `/predict/`
- Send a JSON payload with all required client data fields (see below for the full schema).
- Example request body:

```json
{
  "age": 30,
  "job": "technician",
  "marital": "single",
  "education": "tertiary",
  "default": "no",
  "balance": 1500,
  "housing": "yes",
  "loan": "no",
  "contact": "cellular",
  "day": 5,
  "month": "may",
  "duration": 200,
  "campaign": 2,
  "pdays": -1,
  "previous": 0,
  "poutcome": "unknown"
}

```

- The response will include the prediction (`yes` or `no`) and the probability.

### 2. Root Endpoint

- **GET** `/`
- Returns a welcome message.

## Notebook

The full data processing, model training, and evaluation workflow is documented in the included Jupyter notebook (`notebook.ipynb`).

## Report

Simple report on the process and findings
 
---

For more details, see the API docs linked above.
