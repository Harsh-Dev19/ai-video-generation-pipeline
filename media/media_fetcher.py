import requests
import os
from dotenv import load_dotenv

load_dotenv()

PEXELS_API_KEY = os.getenv("PEXELS_API_KEY")

def fetch_videos(query):
    url = "https://api.pexels.com/videos/search"

    headers = {
        "Authorization": PEXELS_API_KEY
    }

    params = {
        "query": query,
        "per_page": 7
    }

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        print("Error:", response.text)
        return []

    data = response.json()

    os.makedirs("videos", exist_ok=True)

    paths = []

    for i, video in enumerate(data["videos"]):
        video_url = video["video_files"][0]["link"]
        video_response = requests.get(video_url)

        path = f"videos/clip_{i}.mp4"

        with open(path, "wb") as f:
            f.write(video_response.content)

        paths.append(path)

    return paths
