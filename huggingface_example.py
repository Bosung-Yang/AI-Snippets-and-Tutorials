import requests
from transformers import pipeline, AutoTokenizer, AutoModel
from huggingface_hub import HfApi
from config import config

def setup_huggingface():
    """Hugging Face 설정"""
    if not config.HUGGINGFACE_API_KEY:
        print("⚠️  Hugging Face API 키가 설정되지 않았습니다. 일부 기능이 제한될 수 있습니다.")
        return False
    
    # API 키를 환경 변수로 설정
    import os
    os.environ['HUGGING_FACE_HUB_TOKEN'] = config.HUGGINGFACE_API_KEY
    print("✅ Hugging Face가 설정되었습니다.")
    return True

def get_huggingface_models():
    """사용 가능한 모델 목록 가져오기"""
    try:
        api = HfApi()
        models = api.list_models(limit=5)  # 처음 5개 모델만 가져오기
        print("📋 사용 가능한 모델들:")
        for model in models:
            print(f"   - {model.modelId}")
        return models
    except Exception as e:
        print(f"❌ 모델 목록 가져오기 실패: {e}")
        return []

def text_classification_example(text: str):
    """텍스트 분류 예시"""
    try:
        classifier = pipeline(
            "text-classification",
            model="distilbert-base-uncased-finetuned-sst-2-english",
            token=config.HUGGINGFACE_API_KEY
        )
        result = classifier(text)
        return result
    except Exception as e:
        print(f"❌ 텍스트 분류 중 오류 발생: {e}")
        return None

def sentiment_analysis_example(text: str):
    """감정 분석 예시"""
    try:
        sentiment_analyzer = pipeline(
            "sentiment-analysis",
            model="cardiffnlp/twitter-roberta-base-sentiment-l14",
            token=config.HUGGINGFACE_API_KEY
        )
        result = sentiment_analyzer(text)
        return result
    except Exception as e:
        print(f"❌ 감정 분석 중 오류 발생: {e}")
        return None

def text_generation_example(prompt: str):
    """텍스트 생성 예시"""
    try:
        generator = pipeline(
            "text-generation",
            model="gpt2",
            token=config.HUGGINGFACE_API_KEY
        )
        result = generator(prompt, max_length=100, num_return_sequences=1)
        return result
    except Exception as e:
        print(f"❌ 텍스트 생성 중 오류 발생: {e}")
        return None

def translation_example(text: str, source_lang: str = "en", target_lang: str = "ko"):
    """번역 예시"""
    try:
        translator = pipeline(
            "translation",
            model=f"Helsinki-NLP/opus-mt-{source_lang}-{target_lang}",
            token=config.HUGGINGFACE_API_KEY
        )
        result = translator(text)
        return result
    except Exception as e:
        print(f"❌ 번역 중 오류 발생: {e}")
        return None

def custom_model_example():
    """커스텀 모델 사용 예시"""
    try:
        # 토크나이저와 모델 로드
        model_name = config.HUGGINGFACE_MODEL
        tokenizer = AutoTokenizer.from_pretrained(model_name, token=config.HUGGINGFACE_API_KEY)
        model = AutoModel.from_pretrained(model_name, token=config.HUGGINGFACE_API_KEY)
        
        # 텍스트 토크나이징
        text = "Hello, how are you?"
        inputs = tokenizer(text, return_tensors="pt")
        
        # 모델 추론
        outputs = model(**inputs)
        
        print(f"✅ 커스텀 모델 '{model_name}' 사용 성공")
        print(f"   입력 텍스트: {text}")
        print(f"   출력 형태: {outputs.last_hidden_state.shape}")
        
        return outputs
    except Exception as e:
        print(f"❌ 커스텀 모델 사용 중 오류 발생: {e}")
        return None

if __name__ == "__main__":
    # 설정 확인
    config.print_config()
    
    # Hugging Face 설정
    setup_huggingface()
    
    # 모델 목록 가져오기
    print("\n🔍 모델 탐색:")
    get_huggingface_models()
    
    # 텍스트 분류 예시
    print("\n📊 텍스트 분류 예시:")
    classification_result = text_classification_example("I love this movie!")
    if classification_result:
        print(f"분류 결과: {classification_result}")
    
    # 감정 분석 예시
    print("\n😊 감정 분석 예시:")
    sentiment_result = sentiment_analysis_example("오늘은 정말 좋은 날씨네요!")
    if sentiment_result:
        print(f"감정 분석 결과: {sentiment_result}")
    
    # 텍스트 생성 예시
    print("\n✍️ 텍스트 생성 예시:")
    generation_result = text_generation_example("The future of artificial intelligence")
    if generation_result:
        print(f"생성된 텍스트: {generation_result[0]['generated_text']}")
    
    # 번역 예시
    print("\n🌐 번역 예시:")
    translation_result = translation_example("Hello, how are you today?", "en", "ko")
    if translation_result:
        print(f"번역 결과: {translation_result[0]['translation_text']}")
    
    # 커스텀 모델 예시
    print("\n🔧 커스텀 모델 예시:")
    custom_result = custom_model_example() 