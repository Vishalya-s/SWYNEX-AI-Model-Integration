# SWYNEX AI Sentiment Analyzer

## Overview

This project is a small AI prototype developed as part of *SWYNEX Internship Task 2: Model or API Integration*.

The prototype integrates a pre-trained sentiment analysis model using the Hugging Face Transformers library. It accepts a text sentence from the user and predicts whether the sentiment is positive or negative.

## Technologies Used

- Python
- Hugging Face Transformers
- PyTorch
- Pre-trained AI sentiment analysis model

## How It Works

1. The user enters a sentence.
2. The Transformers pipeline sends the text to a pre-trained sentiment analysis model.
3. The model predicts the sentiment.
4. The program displays the predicted sentiment and confidence score.

## Example Inputs and Outputs

### Example 1

*Input:*
text
I love learning artificial intelligence!

Output:
Sentiment: POSITIVE
Confidence: 99.97%

### Example 2

Input:
I am disappointed with poor quality of this product.

Output:
Sentiment: NEGATIVE
Confidence: 99.97%

### Example 3

Input:
The meeting is scheduled for tomorrow at 10 AM.

Output:
Sentiment: POSITIVE
Confidence: 98.36%

### Example 4

Input:
I love building AI projects!

Output:
Sentiment: POSITIVE
Confidence: 99.96%

## Installation

Clone the repository and install the required dependencies:

pip install -r requirements.txt

## Run the Project

Run the following command:

python sentiment_analyzer.py

Then enter a sentence when prompted.

## AI Model Integration

This project uses the Hugging Face Transformers pipeline API to integrate a pre-trained sentiment analysis model.

No secret API keys are required for this prototype.

## Task

SWYNEX Internship — Task 2: Model or API Integration
The objective was to integrate a model, library, or public AI API into a small working prototype and demonstrate example inputs and outputs.

3. Press **Ctrl + S**.

### Your project should now contain:

text
SWYNEX-AI-Model-Integration
│
├── sentiment_analyzer.py
├── requirements.txt
├── README.md
└── venv/