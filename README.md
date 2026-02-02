# AI Instagram Marketer

## 1. 프로젝트 개요

본 프로젝트는 Vision AI 기술을 활용하여 인스타그램 마케팅 콘텐츠를 자동으로 생성하는 솔루션입니다. 사용자가 제품이나 풍경 이미지를 업로드하면, AI가 시각적 요소를 분석하여 해당 이미지에 최적화된 마케팅 카피, 감성적인 본문, 그리고 유입을 유도하는 해시태그를 자동으로 작성합니다.

핵심 엔진으로는 OpenAI의 최신 경량화 멀티모달 모델인 **gpt-5-mini**를 채택하여, 낮은 지연 시간(Low Latency)과 비용 효율성을 확보하면서도 정교한 이미지 분석 능력을 구현하였습니다.

### 주요 기능
* **이미지 분석:** 업로드된 이미지의 피사체, 색감, 조명, 분위기 등을 심층 분석.
* **마케팅 카피라이팅:** 분석된 데이터를 바탕으로 타겟 오디언스에 맞춘 매력적인 헤드라인 및 본문 작성.
* **해시태그 자동 생성:** 게시물의 노출 도달률을 높이기 위한 최적의 해시태그 추천.
* **모듈화된 아키텍처:** 설정, 유틸리티, 핵심 로직, UI가 분리된 유지보수 용이한 구조.

## 2. 시스템 아키텍처

본 시스템은 Streamlit 기반의 프론트엔드와 OpenAI API 기반의 백엔드 로직으로 구성된 모듈형 아키텍처를 따릅니다.

1.  **User Interface:** 사용자가 이미지를 업로드하고 생성을 요청.
2.  **Preprocessing:** `Pillow` 및 `io` 라이브러리를 통해 이미지를 최적화하고 Base64 포맷으로 인코딩.
3.  **Core Logic:** 인코딩된 이미지와 시스템 프롬프트를 결합하여 `gpt-5-mini` 모델에 요청 전송.
4.  **Response Handling:** 모델이 생성한 텍스트 데이터를 파싱하여 화면에 출력.

## 3. 기술 스택

* **Language:** Python 3.10 이상
* **AI Model:** OpenAI gpt-5-mini (Vision capabilities)
* **Framework:** Streamlit (UI/UX)
* **Image Processing:** Pillow (PIL)
* **Environment Management:** python-dotenv

## 4. 프로젝트 구조

실무 수준의 유지보수성과 확장성을 고려하여 기능 단위로 패키지를 분리하였습니다.

```text
insta-marketer/
├── .env                  # 환경 변수 (API Key)
├── requirements.txt      # 의존성 패키지 목록
├── main.py               # 애플리케이션 진입점 (UI)
└── app/                  # 백엔드 핵심 모듈
    ├── __init__.py
    ├── config.py         # 모델 설정 및 프롬프트 관리
    ├── utils.py          # 이미지 전처리 및 인코딩 헬퍼 함수
    └── generator.py      # OpenAI API 통신 및 콘텐츠 생성 로직
```

## 5. 설치 및 실행 가이드
### 5.1. 사전 준비
Python이 설치된 환경에서 아래 명령어를 통해 프로젝트를 복제하고 가상 환경을 설정하십시오.

```Bash
git clone [레포지토리 주소]
cd insta-marketer
```
### 5.2. 의존성 패키지 설치
필요한 라이브러리를 설치합니다.

```Bash
pip install -r requirements.txt
```
### 5.3. 환경 변수 설정
프로젝트 루트 디렉토리에 .env 파일을 생성하고 OpenAI API 키를 설정하십시오. 본 프로젝트는 gpt-5-mini 모델 접근 권한이 필요합니다.

```Ini, TOML
OPENAI_API_KEY=sk-your-api-key-here
```
### 5.4. 애플리케이션 실행
Streamlit 서버를 구동합니다.

```Bash
streamlit run main.py
```
## 6. 구성 요소 상세 (Modules)
**app/config.py**

시스템 프롬프트와 모델 파라미터를 관리합니다. 마케팅 톤앤매너를 수정하거나 모델 버전을 변경할 때 이 파일만 수정하면 됩니다.

**app/utils.py**

이미지 파일을 API 전송 가능한 형태(Base64)로 변환하는 전처리 로직을 담당합니다. 메모리 누수를 방지하기 위해 BytesIO 스트림 처리를 구현하였습니다.

**app/generator.py**

OpenAI 클라이언트를 초기화하고 실제 API 호출을 수행합니다. 예외 처리가 구현되어 있어 API 호출 실패 시 에러 메시지를 반환합니다.