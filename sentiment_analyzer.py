from transformers import pipeline

# Load a pre-trained sentiment analysis model
sentiment_analyzer = pipeline("sentiment-analysis")

print("=" * 45)
print("       SWYNEX AI SENTIMENT ANALYZER")
print("=" * 45)

# Get input from the user
text = input("Enter a sentence: ")

# Analyze the sentiment
result = sentiment_analyzer(text)

# Extract result
sentiment = result[0]["label"]
confidence = result[0]["score"] * 100

# Display result
print("\n--- AI Analysis Result ---")
print("Input:", text)
print("Sentiment:", sentiment)
print("Confidence:", f"{confidence:.2f}%")
print("=" * 45)