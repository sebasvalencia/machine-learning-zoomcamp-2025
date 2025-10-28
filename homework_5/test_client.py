import requests
import json

def test_fastapi_service():
    url = "http://localhost:8000/predict"
    client = {
        "lead_source": "organic_search",
        "number_of_courses_viewed": 4,
        "annual_income": 80304.0
    }
    
    print(f"Testing client data: {client}")
    print(f"Making request to: {url}")
    
    try:
        response = requests.post(url, json=client)
        if response.status_code == 200:
            result = response.json()
            probability = result['probability']
            
            print(f"✅ Request successful!")
            print(f"Response: {json.dumps(result, indent=2)}")
            print(f"Probability: {probability:.6f}")
            
            return probability
        else:
            print(f"❌ Request failed with status code: {response.status_code}")
            print(f"Response: {response.text}")
            return None
            
    except requests.exceptions.ConnectionError:
        print("❌ Could not connect to the service. Make sure the FastAPI server is running.")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

if __name__ == "__main__":
    test_fastapi_service()