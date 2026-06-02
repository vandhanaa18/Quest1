import requests
def get_response(prompt):
    api_url = "http://localhost:11434/api/generate"
    request_data = {
        "model": "llama3.2",
        "prompt": prompt,
        "stream": False
    }
    result = requests.post(api_url, json=request_data)
    
    return result.json()["response"]
prompt = ""
while prompt != "exit":
    prompt = input(">>>")

    res = get_response(prompt)
    print(res)
