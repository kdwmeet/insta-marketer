import base64
from PIL import Image
from io import BytesIO

def encode_image_to_base64(uploaded_file):
    """
    Streamlit으로 업로드된 이미지 파일을 OpenAI가 이해할 수 있는 base64 문자열로 변환합니다.
    """
    try:
        # 업로드된 파일을 이미지 객체로 엶
        image = Image.open(uploaded_file)

        # 이미지를 바이트 스트림으로 저장(JPEG 형식 권장)
        buffered = BytesIO()
        # RGBA(투명 배경)인 경우 RGB로 변환 후 저장
        if image.mode in ("RGBA", "P"):
            image = image.convert("RGB")
        image.save(buffered, format="JPEG")

        # 바이트를 base64 문자열로 인코딩
        img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
        return img_str
    
    except Exception as e:
        print(f"이미지 인코딩 오류: {e}")
        return None