import json
import requests

endpoint_url = "http://localhost:11434/api/generate"

data = {
    "model": "tinyllama",
    "prompt": "what is the capital of Uzbekistan?",
}

response = requests.post(url=endpoint_url, json=data, stream=True)


if response.status_code == 200:
    for line in response.iter_lines():
        decoded_line = line.decode('utf-8')
        result = json.loads(decoded_line)
        generated_text = result.get("response", "")
        print(generated_text, end='', flush=True)

    print()
else: 
    print(f"There was some problem in generating the response getting {response.status_code}")