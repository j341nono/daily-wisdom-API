# Daily Wisdom API

A simple **FastAPI + SQLite** project that provides random quotes (wisdom sayings) via API.  
This project is designed as an **open-source tool** that anyone can clone, run, and extend.

## 🚀 Features

- **Random quote retrieval** - Get inspiring wisdom sayings randomly
- **Philosopher filtering** - Filter quotes by specific philosophers
- **Quote management** - Add and delete quotes via API
- **Web scraping** - Automatically collect quotes from web sources
- **SQLite database** - Lightweight and portable data storage
- **FastAPI powered** - Modern, fast API framework with automatic documentation

## 🛠 Tech Stack

### Scraping
- **requests** - HTTP library for fetching HTML data
- **BeautifulSoup4** - HTML parsing and extraction

### Database
- **SQLite3** - Lightweight relational database

### API
- **FastAPI** - Modern web framework for building APIs

## 📋 Prerequisites

- [uv](https://github.com/astral-sh/uv) package manager
- Python 3.8+

## ⚡ Quick Start

1. **Clone the repository**
```bash
git clone git@github.com:j341nono/daily-wisdom-API.git
cd daily-wisdom-API
```

2. **Scrape wisdom quotes from web sources**
```bash
./scripts/run_scraping.sh
```

3. **Import scraped data into database**
```bash
./scripts/run_database.sh
```

4. **Start the API server**
```bash
./scripts/run_api.sh
```

The API server will be available at `http://127.0.0.1:8000`

## 📖 API Documentation

### Get Random Quote
- **Endpoint**: `GET /quotes/random`
- **Description**: Retrieve a random wisdom quote
- **Query Parameters** (optional):
  - `philosopher` (string): Filter by specific philosopher

**Response Example:**
```json
{
    "philosopher": "Socrates", 
    "quote": "The unexamined life is not worth living."
}
```

### Add New Quote
- **Endpoint**: `POST /quotes`
- **Description**: Add a new quote to the database

**Request Body:**
```json
{
    "philosopher": "Plato",
    "quote": "Wise men speak because they have something to say."
}
```

### Delete Quote
- **Endpoint**: `DELETE /quotes`
- **Description**: Delete a specific quote from the database

**Query Parameters:**
- `philosopher` (string, required): The philosopher's name
- `quote` (string, required): The exact quote text

**Example:**
```
DELETE /quotes?philosopher=Plato&quote=Wise men speak because they have something to say.
```

## 🔧 Development

### Project Structure
```
daily-wisdom-API/
├── scripts/           # Shell scripts for setup and execution
├── src/              # Source code
├── database/         # SQLite database files
└── README.md
```

### Interactive API Documentation
Once the server is running, visit:
- Swagger UI: `http://127.0.0.1:8000/docs`
- ReDoc: `http://127.0.0.1:8000/redoc`

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

Built with ❤️ using FastAPI and SQLite