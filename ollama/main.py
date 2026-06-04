import requests
import json
def get_response(prompt):
    api_url = "http://localhost:11434/api/generate"
    request_data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": True
    }
    result = requests.post(api_url, json=request_data,stream=True)
    
    full_response = ""
    for line in result.iter_lines():
        if line:
            chunk = json.loads(line.decode())
            print(chunk.get("response",""),end="")
            full_response += chunk.get("response", "")
    print()
    return full_response

prompt = ""
while prompt != "exit":
    prompt = input(">>>")

    res = get_response(prompt)
    
