# dotenv를 사용한 API 키 관리 예시

이 폴더는 dotenv를 사용해서 Hugging Face와 OpenAI API 키를 안전하게 관리하는 방법에 대한 예시와 튜토리얼을 포함합니다.

## 🚀 주요 기능

- **dotenv를 사용한 API 키 관리**: 환경 변수를 통해 API 키를 안전하게 관리
- **OpenAI API 예시**: GPT 모델과의 대화 및 텍스트 생성
- **Hugging Face API 예시**: 다양한 NLP 작업 (분류, 감정 분석, 번역 등)
- **설정 검증**: API 키 설정 상태 확인 및 오류 처리

## 📁 파일 구조

```
dotenv/
├── README.md                 # 프로젝트 설명
├── requirements.txt          # 필요한 패키지 목록
├── config.py                # 환경 변수 설정 관리
├── main.py                  # 메인 실행 파일
├── openai_example.py        # OpenAI API 사용 예시
├── huggingface_example.py   # Hugging Face API 사용 예시
└── env_example.txt          # 환경 변수 예시 파일
```

## 🛠️ 설치 및 설정

### 1. 가상환경 생성 및 활성화
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 2. 패키지 설치
```bash
pip install -r requirements.txt
```

### 3. 환경 변수 설정
```bash
# env_example.txt를 참고하여 .env 파일 생성
cp env_example.txt .env
```

`.env` 파일에 API 키를 설정하세요:
```env
OPENAI_API_KEY=your_openai_api_key_here
HUGGINGFACE_API_KEY=your_huggingface_api_key_here
OPENAI_MODEL=gpt-3.5-turbo
HUGGINGFACE_MODEL=bert-base-uncased
API_TIMEOUT=30
```

## 🎯 사용법

### 전체 예시 실행
```bash
python main.py
```

### 개별 예시 실행
```bash
# OpenAI 예시만 실행
python openai_example.py

# Hugging Face 예시만 실행
python huggingface_example.py
```

## 🔧 주요 컴포넌트

### Config 클래스 (`config.py`)
- 환경 변수 로드 및 관리
- API 키 유효성 검사
- 설정 상태 출력

### OpenAI 예시 (`openai_example.py`)
- GPT 모델과의 채팅
- 텍스트 생성 (Completion API)
- 오류 처리 및 로깅

### Hugging Face 예시 (`huggingface_example.py`)
- 텍스트 분류
- 감정 분석
- 텍스트 생성
- 번역
- 커스텀 모델 사용

## 🔒 보안 고려사항

- `.env` 파일은 `.gitignore`에 포함되어 Git에 커밋되지 않습니다
- API 키는 환경 변수로만 관리됩니다
- 실제 API 키는 절대 코드에 하드코딩하지 마세요

## 📝 API 키 획득 방법

### OpenAI API 키
1. [OpenAI 웹사이트](https://platform.openai.com/)에 가입
2. API Keys 섹션에서 새 키 생성
3. 생성된 키를 `.env` 파일에 설정

### Hugging Face API 키
1. [Hugging Face 웹사이트](https://huggingface.co/)에 가입
2. Settings > Access Tokens에서 새 토큰 생성
3. 생성된 토큰을 `.env` 파일에 설정

## 🐛 문제 해결

### API 키 오류
- `.env` 파일이 올바른 위치에 있는지 확인
- API 키가 올바르게 설정되었는지 확인
- API 키의 유효성을 확인

### 패키지 설치 오류
- Python 버전이 3.7 이상인지 확인
- 가상환경이 활성화되어 있는지 확인
- `pip install -r requirements.txt` 재실행

## 📚 추가 리소스

- [python-dotenv 문서](https://github.com/theskumar/python-dotenv)
- [OpenAI API 문서](https://platform.openai.com/docs)
- [Hugging Face Transformers 문서](https://huggingface.co/docs/transformers) 