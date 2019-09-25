from textblob import TextBlob

def sent_test(message):
    sentiment = "positive"
    if TextBlob(message).sentiment.polarity < 0.0:
        sentiment = "negative"

    return sentiment

print(sent_test("perl is bad"))