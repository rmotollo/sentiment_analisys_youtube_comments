from textblob import TextBlob
# from textblob.translate import Translator

def translate_comments(comment):
    try:
        blob = TextBlob(str(comment))
        return str(blob.translate(from_lang="pt",to="en"))
    except Exception as e:
        print(f"An error occurred: {e} at {comment} \n")
        return comment

def sentiment_analysis(comments):
    sentiment = TextBlob(comments).sentiment
    return sentiment.polarity, sentiment.subjectivity