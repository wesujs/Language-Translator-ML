from textblob import TextBlob

def analyze_sentiment(text: str) -> str:
    analysis = TextBlob(text)
    
    if analysis.sentiment.polarity > 0:
        return 'positive'
    elif analysis.sentiment.polarity == 0:
        return 'neutral'
    else:
        return 'negative'