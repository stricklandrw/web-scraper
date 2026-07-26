from urllib.parse import urlsplit
from bs4 import BeautifulSoup, Tag

def normalize_url(url: str) -> str:
    u = urlsplit(url)
    path = f"{u.netloc}{u.path}"
    path = path.rstrip("/")
    return path.lower()

def get_heading_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    header = ''
    if soup('h1'):
        return soup.get_text('h1')
    else:
        if soup('h2'):
            header = soup.get_text('h2')
    return header

def get_first_paragraph_from_html(html: str) -> str:
    soup = BeautifulSoup(html, 'html.parser')
    p = ''
    if soup('p') and soup.main:
        p = soup.main.find_all('p', limit=1)
        return p[0].get_text()
    else:
        if soup('p'):
            p = soup.find_all('p', limit=1)
            return p[0].get_text()
    return p