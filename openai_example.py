import openai
from config import config

def setup_openai():
    """OpenAI 클라이언트 설정"""
    if not config.OPENAI_API_KEY:
        raise ValueError("OpenAI API 키가 설정되지 않았습니다. .env 파일을 확인해주세요.")
    
    openai.api_key = config.OPENAI_API_KEY
    print("✅ OpenAI 클라이언트가 설정되었습니다.")

def chat_with_gpt(prompt: str, model: str = None) -> str:
    """GPT 모델과 대화하는 함수"""
    if not model:
        model = config.OPENAI_MODEL
    
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[
                {"role": "user", "content": prompt}
            ],
            max_tokens=1000,
            temperature=0.7
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"❌ OpenAI API 호출 중 오류 발생: {e}")
        return None

def generate_text_with_completion(prompt: str, model: str = "text-davinci-003") -> str:
    """Completion API를 사용한 텍스트 생성"""
    try:
        response = openai.Completion.create(
            model=model,
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        print(f"❌ OpenAI Completion API 호출 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    # 설정 확인
    config.print_config()
    
    if config.validate_required_keys():
        try:
            setup_openai()
            
            # 채팅 예시
            print("\n🤖 GPT와 대화 예시:")
            response = chat_with_gpt("안녕하세요! 오늘 날씨에 대해 간단히 설명해주세요.")
            if response:
                print(f"GPT: {response}")
            
            # 텍스트 생성 예시
            print("\n📝 텍스트 생성 예시:")
            completion = generate_text_with_completion("파이썬의 장점은")
            if completion:
                print(f"생성된 텍스트: {completion}")
                
        except Exception as e:
            print(f"❌ 오류 발생: {e}")
    else:
        print("❌ 필수 API 키가 설정되지 않아 실행할 수 없습니다.") 