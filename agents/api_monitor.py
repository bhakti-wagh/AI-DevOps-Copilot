import requests
import time

def check_api(url):
    try:
        start = time.time()
        response = requests.get(url)
        end = time.time()

        response_time = round((end - start) * 1000, 2)

        return {
            "status": response.status_code,
            "response_time": response_time
        }

    except:
        return {
            "status": "Error",
            "response_time": "N/A"
        }