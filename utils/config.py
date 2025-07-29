from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GOOGLE_CSE_ID = os.getenv("GOOGLE_CSE_ID")

if not OPENAI_API_KEY:
    raise ValueError("API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")

if not GOOGLE_API_KEY:
    print("Google API Key가 설정되지 않았습니다.")

if not GOOGLE_CSE_ID:
    raise ValueError("CSE ID가 설정되지 않았습니다.")