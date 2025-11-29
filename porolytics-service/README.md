# Porolytics Service

This service provides a simple API to query League of Legends player data.

## Setup

1.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

2.  **Set up your environment variables:**
    Create a `.env` file in this directory and add your Riot Games API key:
    ```
    RIOT_API_KEY=your_riot_api_key_here
    ```
    You can get an API key from the [Riot Developer Portal](https://developer.riotgames.com/).

## Running the Service

To run the service, use uvicorn:

```bash
uvicorn app.main:app --reload --app-dir porolytics-service
```

The API will be available at `http://127.0.0.1:8000`.

### Regions

The following regions are supported:
`br`, `eune`, `euw`, `jp`, `kr`, `lan`, `las`, `na`, `oce`, `tr`, `ru`, `ph`, `sg`, `th`, `tw`, `vn`.
