# Data Sync

Resilient API sync with retry logic · exponential backoff · auto-recovery

## Stack
- Python
- Requests
- REST API
- python-dotenv

## How it works
1. Fetches data from a REST API endpoint
2. On failure, retries up to 3 times automatically
3. Wait time doubles on each retry: 1s → 2s → 4s (exponential backoff)
4. Persists response as JSON · logs every sync attempt

## How to run
1. Clone the repository
2. Install dependencies: `pip install -r requirements.txt`
3. Run: `python main.py`

## Demo

![Data Sync Demo](assets/demo.png)
![Automation Pipeline](assets/demo_2.png)