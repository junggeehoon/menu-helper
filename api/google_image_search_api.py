import requests
import os
from utils.config import GOOGLE_API_KEY, GOOGLE_CSE_ID

def search_image_urls(query, num_results=1):
    """
    Google Custom Search API를 사용하여 이미지 URL을 검색합니다.
    """
    search_url = "https://www.googleapis.com/customsearch/v1"
    params = {
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_CSE_ID,
        'q': query,
        'searchType': 'image',  # 이미지 검색
        'num': num_results      # 가져올 이미지 개수
    }

    headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
                'Referer': 'https://www.google.com/'
            }

    try:
        response = requests.get(search_url, headers=headers, params=params)
        response.raise_for_status()
        search_results = response.json()

        image_urls = []
        if 'items' in search_results:
            for item in search_results['items']:
                if 'link' in item:
                    image_urls.append(item['link'])
        return image_urls
    except requests.exceptions.RequestException as e:
        print(f"Google 이미지 검색 중 오류 발생: {e}")
        return []
    except Exception as e:
        print(f"이미지 검색 결과 처리 중 오류 발생: {e}")
        return []

