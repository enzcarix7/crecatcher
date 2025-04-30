from bs4 import BeautifulSoup
from requests import get, Response


def credential_catcher(url_path: str, words: list[str]):
    with open(url_path, 'r', errors='ignore') as urls:
        for url in urls:
            url: str = url.strip()
            if not url:
                continue
            try:
                response: Response = get(url)
                soup: BeautifulSoup = BeautifulSoup(response.text, 'html.parser')
                for word in words:
                    if word in soup.get_text():
                        print(f'Word found: {word} - URL: {url}')
            except Exception as e:
                print(f'Error accessing {url}: {str(e)}')


path: str = r'PATH_TO_URLS_FILE.txt'  # Replace with your actual file path
words: list[str] = ['admin', 'user', 'password', 'root', 'api', 'db', 'ftp', 'login', 'account']
credential_catcher(path, words)
