# Finalytics
📈 Finalytics is an AI-based cryptocurrency technical analysis application. It enables users to analyze charts based on candlestick patterns and perform sentiment analysis on scraped data from social media. Additionally, it utilizes a GPT model to provide the latest YouTube video summaries on specific cryptocurrencies. The backend is built with Python FastAPI and hosted on AWS.

## 🚀 Features
- Candlestick Pattern Analysis: Evaluate cryptocurrency charts using advanced candlestick pattern recognition.
- Sentiment Analysis: Gain insights from social media data to gauge market sentiment.
- YouTube Summaries: Get concise summaries of the latest YouTube videos on your chosen cryptocurrency using a GPT model.

## 🛠️ Tech Stack
- Backend: Python FastAPI
- Infrastructure: AWS

## 📦 Installation and setup
1. Clone the repository:
   ```
   git clone https://github.com/debankanmitra/Finalytics-backend.git
   cd Finalytics-backend
   ```
2. Set up a virtual environment:
   ```
   python3 -m venv venv
   source venv/bin/activate
   ```
4. Install the dependencies:
   ```
   pip install -r requirements.txt
   ```
6. Configure environment variables for AWS, social media scraping, and GPT model API keys.
7. Start the FastAPI server:
   ```
   uvicorn main:app --reload
   ```

📄 License
Finalytics is licensed under the MIT License.
