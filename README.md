# OpenLibrary Book Fetcher

A Python automation tool that queries the OpenLibrary Search API to fetch, filter, and export book data into a structured CSV file.

---

## 📌 Project Overview
The script searches for books under the query keyword `"world"`, filters them according to specific criteria, sorts the records chronologically, and saves the final result.

### Core Features:
- **API Pagination Handling**: Iterates through search result pages to safely collect the exact target number of records.
- **Data Filtering**: Filters for books published after the year **2000**.
- **Data Integrity**: Safely extracts missing fields using defensive dictionary methods (`.get()`) and concatenates multiple authors cleanly.
- **Sorting**: Sorts records in **descending order** by publication year (newest to oldest).
- **CSV Export**: Outputs a UTF-8 encoded `filtered_books.csv` file without blank rows.

---

## 🛠 Tech Stack
- **Language**: Python 3
- **HTTP Client**: `requests`
- **Output Format**: CSV (via Python's built-in `csv` module)

---

## 🚀 Setup & Execution

### 1. Clone the repository
git clone https://github.com/ahmadhooshmand1/openlibrary-project.git

cd openlibrary-project

### 2. Create and activate a Virtual Environment
python3 -m venv venv

source venv/bin/activate

### 3. Install dependencies
pip install requests

### 4. Run the script
python main.py

---

## 📄 Output Format
The resulting `filtered_books.csv` contains 50 records with the following headers:
- `Title`: Book title
- `Author(s)`: Comma-separated list of contributors
- `First Publish Year`: Year of first publication 