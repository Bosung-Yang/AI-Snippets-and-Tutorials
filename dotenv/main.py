#!/usr/bin/env python3
"""
AI API 키 관리 및 사용 예시
dotenv를 사용하여 Hugging Face, OpenAI 등의 API 키를 안전하게 관리합니다.
"""

import os
import sys
from config import config

def print_banner():
    """프로그램 배너 출력"""
    print("=" * 60)
    print("🤖 AI API 키 관리 및 사용 예시")
    print("=" * 60)
    print("📁 현재 작업 디렉토리:", os.getcwd())
    print("🐍 Python 버전:", sys.version)
    print("=" * 60)

def check_env_file():
    """환경 변수 파일 확인"""
    env_file = ".env"
    if os.path.exists(env_file):
        print(f"✅ {env_file} 파일이 존재합니다.")
        return True
    else:
        print(f"⚠️  {env_file} 파일이 없습니다.")
        print("   env_example.txt를 참고하여 .env 파일을 생성해주세요.")
        return False

def run_openai_example():
    """OpenAI 예시 실행"""
    print("\n" + "="*40)
    print("🚀 OpenAI API 예시 실행")
    print("="*40)
    
    try:
        from openai_example import setup_openai, chat_with_gpt, generate_text_with_completion
        
        if config.validate_required_keys():
            setup_openai()
            
            # 채팅 예시
            print("\n💬 GPT와 대화:")
            response = chat_with_gpt("파이썬의 장점을 3가지 설명해주세요.")
            if response:
                print(f"답변: {response}")
            
            # 텍스트 생성 예시
            print("\n✍️ 텍스트 생성:")
            completion = generate_text_with_completion("인공지능의 미래는")
            if completion:
                print(f"생성된 텍스트: {completion}")
        else:
            print("❌ OpenAI API 키가 설정되지 않았습니다.")
            
    except ImportError as e:
        print(f"❌ OpenAI 모듈을 가져올 수 없습니다: {e}")
    except Exception as e:
        print(f"❌ OpenAI 예시 실행 중 오류: {e}")

def run_huggingface_example():
    """Hugging Face 예시 실행"""
    print("\n" + "="*40)
    print("🤗 Hugging Face API 예시 실행")
    print("="*40)
    
    try:
        from huggingface_example import (
            setup_huggingface, 
            text_classification_example,
            sentiment_analysis_example,
            text_generation_example,
            translation_example
        )
        
        setup_huggingface()
        
        # 텍스트 분류 예시
        print("\n📊 텍스트 분류:")
        result = text_classification_example("This movie is fantastic!")
        if result:
            print(f"분류 결과: {result}")
        
        # 감정 분석 예시
        print("\n😊 감정 분석:")
        sentiment = sentiment_analysis_example("오늘은 정말 행복한 하루입니다!")
        if sentiment:
            print(f"감정 분석: {sentiment}")
        
        # 텍스트 생성 예시
        print("\n✍️ 텍스트 생성:")
        generation = text_generation_example("The future of technology")
        if generation:
            print(f"생성된 텍스트: {generation[0]['generated_text']}")
        
        # 번역 예시
        print("\n🌐 번역:")
        translation = translation_example("Hello, how are you?", "en", "ko")
        if translation:
            print(f"번역 결과: {translation[0]['translation_text']}")
            
    except ImportError as e:
        print(f"❌ Hugging Face 모듈을 가져올 수 없습니다: {e}")
    except Exception as e:
        print(f"❌ Hugging Face 예시 실행 중 오류: {e}")

def show_usage_instructions():
    """사용법 안내"""
    print("\n" + "="*60)
    print("📖 사용법 안내")
    print("="*60)
    print("1. .env 파일 생성:")
    print("   cp env_example.txt .env")
    print("   # 또는 직접 .env 파일을 생성하고 API 키를 입력")
    print()
    print("2. .env 파일에 API 키 설정:")
    print("   OPENAI_API_KEY=your_openai_api_key_here")
    print("   HUGGINGFACE_API_KEY=your_huggingface_api_key_here")
    print()
    print("3. 필요한 패키지 설치:")
    print("   pip install -r requirements.txt")
    print()
    print("4. 개별 예시 실행:")
    print("   python openai_example.py")
    print("   python huggingface_example.py")
    print()
    print("5. 전체 예시 실행:")
    print("   python main.py")
    print("="*60)

def main():
    """메인 함수"""
    print_banner()
    
    # 환경 변수 파일 확인
    env_exists = check_env_file()
    
    # 설정 상태 출력
    config.print_config()
    
    if env_exists and config.validate_required_keys():
        # OpenAI 예시 실행
        run_openai_example()
        
        # Hugging Face 예시 실행
        run_huggingface_example()
        
        print("\n✅ 모든 예시가 완료되었습니다!")
    else:
        print("\n❌ API 키가 설정되지 않아 예시를 실행할 수 없습니다.")
        show_usage_instructions()

if __name__ == "__main__":
    main() 