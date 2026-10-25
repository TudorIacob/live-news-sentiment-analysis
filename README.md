# Live News Sentiment Analysis

A Streamlit dashboard for exploring recent English-language news headlines and their sentiment by topic. It retrieves articles from [NewsAPI](https://newsapi.org/) and uses TextBlob to estimate the polarity of each headline.

## Features

- Start with topics including Artificial Intelligence, OpenAI, NVIDIA, Google Gemini, Claude, and Cyber Security.
- Add a topic and select it from the dashboard sidebar.
- Choose how many recent articles to request (5–20).
- View positive, neutral, and negative headline counts.
- Explore sentiment distribution and polarity charts.
- Review each headline's source, publication date, sentiment, and article URL.

## Requirements

- Python 3.10 or newer
- A [NewsAPI API key](https://newsapi.org/register)

## Setup

1. Clone this repository and open its directory:

   ```powershell
   git clone https://github.com/TudorIacob/live-news-sentiment-analysis.git
   Set-Location live-news-sentiment-analysis
   ```

2. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

   On macOS or Linux, activate it with:

   ```bash
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Create a `.env` file in the project directory and add your NewsAPI key:

   ```dotenv
   NEWS_API_KEY=your_actual_newsapi_key
   ```

   You can copy `.env.example` as a starting point. Keep your real API key private; `.env` is excluded from Git.

## Run the dashboard

From the project directory with the virtual environment active, run:

```bash
streamlit run app.py
```

Streamlit will print a local URL (typically `http://localhost:8501`) to open in your browser.

## How sentiment is calculated

TextBlob analyzes each article's **headline only**, producing a polarity value from -1.0 to 1.0. This app labels values above zero as Positive, below zero as Negative, and exactly zero as Neutral. It is a lightweight, lexicon-based estimate—not a contextual or financial sentiment model—and can misinterpret sarcasm, nuance, and domain-specific language. Treat the results as exploratory rather than authoritative.

## Data and API notes

- News results come from NewsAPI's Everything endpoint and are requested in English, newest first.
- Results and availability depend on your NewsAPI plan, query, and API limits.
- The selected topic is sent to NewsAPI; article text and headlines are analyzed locally by the app.
- The dashboard displays headline, source, publication date, polarity-derived sentiment, and the article URL returned by NewsAPI.

## Project structure

```text
.
├── app.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Troubleshooting

- **No articles or API errors:** confirm `NEWS_API_KEY` is set in `.env`, check that the key is active, and review your NewsAPI plan and request limits.
- **`streamlit` is not recognized:** activate the virtual environment and install dependencies with `python -m pip install -r requirements.txt`.
- **PowerShell blocks environment activation:** you can run Streamlit directly without activation using `.venv\Scripts\python.exe -m streamlit run app.py`.

## License

No license has been specified for this project. Contact the repository owner before redistributing or reusing the code.
