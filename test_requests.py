import requests
import time

# Flask 앱 URL
url_list = [
    "http://localhost:5000/",
    "http://localhost:5000/hello"
]

while True:
    for url in url_list:
        try:
            response = requests.get(url)
            print(f"{url} -> {response.status_code}")
        except Exception as e:
            print(f"Error: {e}")
    time.sleep(3)  
