🚗 Pincode Distance API - FastAPI, Google Maps & Redis Caching
A blazing-fast, REST-compliant API built with FastAPI to fetch distance and travel duration between Indian pin codes. Integrates Google Maps Distance Matrix API, uses Redis for caching, and PostgreSQL for persistent storage—perfect for high-efficiency requests without the redundant API costs.

Features
REST API: Fully REST-compliant, no UI. Easily testable with Postman.
Google Maps Integration: Fetches real-time route info (distance & duration) based on pin codes.
Caching with Redis: Avoid redundant calls to Google Maps API; cache results for 1 hour.
PostgreSQL Storage: Persist all route information and save latitude/longitude data for pin codes.
Asynchronous FastAPI: Leveraging FastAPI’s async power for fast responses and concurrency.
Test-Driven Development (TDD): Pytest-ready with structured unit tests to ensure reliability.
Get Started
Clone the repo
Set up dependencies (requirements.txt)
Configure your .env with Google API key, Redis, and PostgreSQL credentials
Run the app, and you're ready to hit endpoints 🚀
