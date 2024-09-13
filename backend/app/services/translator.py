from googletrans import Translator
from app.services.language_detector import detect_language
from app.services.sentiment_analyzer import analyze_sentiment

translator = Translator()

async def translate_text(text: str, target_language: str):
    source_language = detect_language(text)
    translation = translator.translate(text, dest=target_language, src=source_language)
    sentiment = analyze_sentiment(translation.text)
    
    return {
        'text': translation.text,
        'src': source_language,
        'sentiment': sentiment
    }