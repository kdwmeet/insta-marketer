import streamlit as st
from PIL import Image
# 핵심 로직 함수만 임포트
from app.generator import generate_instagram_post

# 페이지 기본 설정
st.set_page_config(page_title="AI Insta Marketer", layout="centered")

# --- UI 헤더 ---
st.title(" AI 인스타그램 마케터")
st.divider()

# --- 이미지 업로드 섹션 ---
uploaded_file = st.file_uploader("마케팅할 제품/풍경 사진을 선택하세요", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    # 업로드된 이미지 미리보기
    image = Image.open(uploaded_file)
    st.image(image, caption='업로드된 이미지', use_container_width=True)
    
    st.divider()

    # --- 생성 버튼 및 결과 섹션 ---
    if st.button("✨ 마법의 포스팅 생성하기", type="primary", use_container_width=True):
        with st.spinner("AI 마케터가 사진의 분위기를 분석하고 글을 쓰는 중..."):
            # 백엔드 로직 호출
            result_text = generate_instagram_post(uploaded_file)
            
            st.success("작성 완료! 결과물을 확인하세요.")
            
            # 결과 출력 박스
            with st.container(border=True):
                st.markdown(result_text)
                
            # 복사 버튼 팁 (Streamlit 내장 기능 활용)
            st.caption("위 텍스트 상자 우측 상단의 '복사' 아이콘을 눌러 바로 사용하세요!")

else:
    # 이미지가 없을 때 안내 문구
    st.info("먼저 위에서 이미지 파일을 업로드해주세요.")