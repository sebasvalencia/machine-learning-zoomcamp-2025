import pickle

def load_pipeline(filename='pipeline_v1.bin'):
    with open(filename, 'rb') as f:
        pipeline = pickle.load(f)
    return pipeline

def score_record(pipeline, record):
    records = [record]
    probabilities = pipeline.predict_proba(records)
    return probabilities[0][1]

if __name__ == "__main__":
    pipeline = load_pipeline()
    
    record = {
        "lead_source": "paid_ads",
        "number_of_courses_viewed": 2,
        "annual_income": 79276.0
    }
    print(f"Scoring record: {record}")
    
    probability = score_record(pipeline, record)
    print(f"Probability that this lead will convert: {probability:.3f}")
