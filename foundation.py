import os, requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Set environment variables for API keys
os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')

def foundation(query: str, openai_model: str):
    api_endpoint = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {os.environ['OPENAI_API_KEY']}",
    }
    payload = {
        "model": openai_model,
        "messages": [{"role": "user", "content": query}],
    }
    try:
        response = requests.post(api_endpoint, headers=headers, json=payload)
        if response.status_code == 200:
            response_data = response.json()
            return response_data['choices'][0]['message']['content'].strip()
        else:
            return None
    except requests.exceptions.RequestException as e:
        return None
    except Exception as e:
        return None

query ='As a maritime professional, how should I respond to someone calling my ship a boat.'
model= 'gpt-3.5-turbo'
print(foundation(query, model))