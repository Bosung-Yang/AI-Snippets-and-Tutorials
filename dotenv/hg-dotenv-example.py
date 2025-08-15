
#%%import os
from dotenv import load_dotenv
from huggingface_hub import login
from transformers import AutoTokenizer, AutoModelForCausalLM

# .env 파일 로드
load_dotenv()

# 환경변수에서 Hugging Face 토큰 가져오기
hf_token = os.getenv("HUGGINGFACE_TOKEN")

if hf_token:
    # Hugging Face에 로그인
    login(token=hf_token)
    print("Hugging Face에 성공적으로 로그인했습니다.")
    
    # LLaMA2 모델 로드
    model_name = "meta-llama/Llama-2-7b-chat-hf"  # 또는 다른 LLaMA2 변형
    
    try:
        # 토크나이저와 모델 로드
        tokenizer = AutoTokenizer.from_pretrained(model_name)
        model = AutoModelForCausalLM.from_pretrained(
            model_name,
            torch_dtype="auto",
            device_map="auto"
        )
        
        print(f"LLaMA2 모델 '{model_name}'이 성공적으로 로드되었습니다.")
        
    except Exception as e:
        print(f"모델 로드 중 오류가 발생했습니다: {e}")
        
else:
    print("HUGGINGFACE_TOKEN이 .env 파일에 설정되지 않았습니다.")
    print(".env 파일에 다음과 같이 추가하세요:")
    print("HUGGINGFACE_TOKEN=your_token_here")
