# Credential Catcher 🕵️‍♂️

This Python script scans a list of URLs and checks if any given sensitive words (like `admin`, `password`, `login`, etc.) appear in the HTML content of those pages.

## 🔍 What It Does

- Reads URLs from a text file (one URL per line)
- Sends a GET request to each URL
- Parses the HTML content with BeautifulSoup
- Looks for matches with words commonly associated with credentials
- Prints any matches along with the URL where they were found

## 🛠️ Usage

1. Install dependencies (if not already installed):

```
pip install requests beautifulsoup4
```

2. Replace PATH_TO_URLS_FILE.txt in the script with the path to your own .txt file containing URLs.
3. Run the script:
```
python credential_catcher.py
```

### Notes
•	Make sure your URL list is clean (no extra spaces or empty lines).
•	Use responsibly. This script is for educational and ethical testing purposes only.
