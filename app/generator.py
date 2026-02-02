from openai import OpenAI
from dotenv import load_dotenv
import os
from app.config import VISION_MODEL, SYSTEM_PROMPT, USER_PROMPT_TEMPLATE
from app.utils import encode_image_to_base64

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def generate_instagram_post(uploaded_file):
    """
    이미지를 받아 인스타그램 포스팅 내용을 생성하는 핵심 함수
    """
    # 이미지 인코딩 (Utils 활용)
    base64_image = encode_image_to_base64(uploaded_file)
    if not base64_image:
        return "이미지 처리 중 오류가 발생했습니다."
    
    try:
        # OpenAI Vision API 호출
        response = client.chat.completions.create(
            model=VISION_MODEL,
            messages=[
                {
                    "role": "system", 
                    "content": SYSTEM_PROMPT
                },
                {
                    "role": "user",
                    "content": [
                        {"type": "text", "text": USER_PROMPT_TEMPLATE},
                        {
                            "type": "image_url",
                            "image_url": {
                                # 중요: base64 이미지 데이터 전달 포맷
                                "url": f"data:image/jpeg;base64,{base64_image}"
                            },
                        },
                    ],
                }
            ],
            max_completion_tokens=1000, # 넉넉하게 설정            
        )

        # 결과 반환 
        return response.choices[0].message.content
    
    except Exception as e:
        return f"AI 요청 중 오류 발생: {str(e)}"