import csv
import requests
from typing import List, Dict, Any

def fetch_and_filter_books(query: str = "world", min_year: int = 2000, target_count: int = 50) -> List[Dict[str, Any]]:
    """
    Fetch books from OpenLibrary API across pages until target_count books
    published after min_year are gathered, then sort descending by year.
    """
    url = "https://openlibrary.org/search.json"
    headers = {
        "User-Agent": "OpenLibraryBookFetcher/1.0 (student_assignment)"
    }

    filtered_books = []
    page = 1

    print(f"Connecting to OpenLibrary API (Target: {target_count} books published after {min_year})...")

    while len(filtered_books) < target_count:
        params = {
            "q": query,
            "page": page,
            "limit": 100
        }

        try:
            response = requests.get(url, params=params, headers=headers, timeout=15)
            response.raise_for_status()
            data = response.json()
        except requests.exceptions.RequestException as error:
            print(f"Network error occurred on page {page}: {error}")
            break

        raw_books = data.get("docs", [])
        if not raw_books:
            print("No more books available from API.")
            break

        for book in raw_books:
            publish_year = book.get("first_publish_year")

            if publish_year and publish_year > min_year:
                filtered_books.append({
                    "Title": book.get("title", "Unknown Title"),
                    "Author(s)": ", ".join(book.get("author_name", ["Unknown Author"])),
                    "First Publish Year": publish_year
                })

            if len(filtered_books) == target_count:
                break

        page += 1

    # Sort descending by publication year
    sorted_books = sorted(
        filtered_books,
        key=lambda item: item["First Publish Year"],
        reverse=True
    )

    return sorted_books

def save_to_csv(books: List[Dict[str, Any]], filename: str = "filtered_books.csv") -> None:
    """
    Save the processed records into a clean CSV file.
    """
    if not books:
        print("No valid records found to save.")
        return

    fieldnames = ["Title", "Author(s)", "First Publish Year"]

    print(f"Writing {len(books)} records to {filename}...")
    try:
        with open(filename, mode="w", encoding="utf-8", newline="") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(books)
        print("CSV file successfully generated.")
    except IOError as error:
        print(f"File writing error occurred: {error}")

if __name__ == "__main__":
    books_data = fetch_and_filter_books()
    save_to_csv(books_data)