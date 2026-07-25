from urllib.parse import urlsplit

def normalize_url(url: str) -> str:
    u = urlsplit(url)
    path = f"{u.netloc}{u.path}"
    path = path.rstrip("/")
    return path.lower()
