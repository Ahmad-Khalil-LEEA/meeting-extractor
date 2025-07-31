# Meeting Extractor (Audio → Text → LLM)

Transcribe calls, extract decisions, action items, and generate follow-up emails using Whisper + LLM.

## Features

- **Audio Transcription:** Converts meeting audio files to text using OpenAI Whisper.
- **LLM Post-Processing:** Uses a Large Language Model (e.g., OpenAI GPT-4) to:
  - Extract decisions
  - Identify action items
  - Generate follow-up emails
- **Dockerized:** Easily deployable with Docker.
- **REST API:** Simple HTTP API for submitting audio files and retrieving results.

## Quick Start

### 1. Clone the repository

```bash
git clone https://github.com/Ahmad-Khalil-LEEA/meeting-extractor.git
cd meeting-extractor
```

### 2. Add your API keys

- Whisper is run locally (no key needed).
- For the LLM (e.g., OpenAI GPT-4), create a `.env` file:

```
OPENAI_API_KEY=your_openai_api_key
```

### 3. Build and run with Docker

```bash
docker build -t meeting-extractor .
docker run --env-file .env -p 8000:8000 meeting-extractor
```

### 4. Usage

Send a POST request with an audio file:

```bash
curl -F "file=@meeting.mp3" http://localhost:8000/extract
```

Response will include:
- Transcribed text
- Extracted decisions
- Action items
- Draft follow-up email

## API

### `POST /extract`

- **file**: (form-data) Audio file (`.mp3`, `.wav`, etc.)

**Response JSON:**
```json
{
  "transcript": "...",
  "decisions": [...],
  "action_items": [...],
  "follow_up_email": "..."
}
```

## Requirements

- Docker
- OpenAI API key (for LLM tasks)

## Project Structure

```
meeting-extractor/
├── app/
│   ├── main.py
│   ├── whisper_utils.py
│   ├── llm_utils.py
│   └── email_utils.py
├── requirements.txt
├── Dockerfile
├── .env.example
└── README.md
```

## License

MIT License
