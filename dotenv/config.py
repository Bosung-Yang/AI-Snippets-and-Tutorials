import os
from dotenv import load_dotenv
from typing import Optional

# .env 파일 로드
load_dotenv()

class Config:
    """환경 변수 설정을 관리하는 클래스"""
    
    # OpenAI 설정
    OPENAI_API_KEY: str = os.getenv('OPENAI_API_KEY', '')
    OPENAI_MODEL: str = os.getenv('OPENAI_MODEL', 'gpt-3.5-turbo')
    
    # Hugging Face 설정
    HUGGINGFACE_API_KEY: str = os.getenv('HUGGINGFACE_API_KEY', '')
    HUGGINGFACE_MODEL: str = os.getenv('HUGGINGFACE_MODEL', 'bert-base-uncased')
    
    # 기타 설정
    API_TIMEOUT: int = int(os.getenv('API_TIMEOUT', '30'))
    DATABASE_URL: Optional[str] = os.getenv('DATABASE_URL')
    
    # 다른 서비스들
    GOOGLE_API_KEY: str = os.getenv('GOOGLE_API_KEY', '')
    ANTHROPIC_API_KEY: str = os.getenv('ANTHROPIC_API_KEY', '')
    
    @classmethod
    def validate_required_keys(cls) -> bool:
        """필수 API 키들이 설정되어 있는지 확인"""
        required_keys = [
            ('OPENAI_API_KEY', cls.OPENAI_API_KEY),
            ('HUGGINGFACE_API_KEY', cls.HUGGINGFACE_API_KEY)
        ]
        
        missing_keys = []
        for key_name, key_value in required_keys:
            if not key_value:
                missing_keys.append(key_name)
        
        if missing_keys:
            print(f"⚠️  경고: 다음 API 키들이 설정되지 않았습니다: {', '.join(missing_keys)}")
            print("   .env 파일을 확인하거나 환경 변수를 설정해주세요.")
            return False
        
        return True
    
    @classmethod
    def print_config(cls):
        """현재 설정 상태를 출력 (보안을 위해 키는 마스킹)"""
        print("🔧 현재 설정:")
        print(f"   OpenAI Model: {cls.OPENAI_MODEL}")
        print(f"   Hugging Face Model: {cls.HUGGINGFACE_MODEL}")
        print(f"   API Timeout: {cls.API_TIMEOUT}초")
        print(f"   OpenAI API Key: {'✅ 설정됨' if cls.OPENAI_API_KEY else '❌ 설정되지 않음'}")
        print(f"   Hugging Face API Key: {'✅ 설정됨' if cls.HUGGINGFACE_API_KEY else '❌ 설정되지 않음'}")
        print(f"   Database URL: {'✅ 설정됨' if cls.DATABASE_URL else '❌ 설정되지 않음'}")

# 전역 설정 인스턴스
config = Config() 