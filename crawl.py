from urllib.parse import urlsplit

def normalize_url(url: str) -> str:
    u = urlsplit(url)
    path = u.path
    if path[-1] == "/":
        path = path[:-1]
    return f"{u.hostname}{path}"
