import sys
import requests

def main():
    if len(sys.argv) < 2:
        print("no website provided")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("too many arguments provided")
        sys.exit(1)
    if len(sys.argv) == 2:
        base_url = sys.argv[1]
        print(f"starting crawl of: {base_url}")
        get_html(base_url)
#    print("Script name:", sys.argv[0])  # example.py
#    print("Argument:", sys.argv[1])  # 

def get_html(url):
    try:
        response = requests.get(url, headers={"User-Agent": "BootCrawler/1.0"})
        if 400 <= response.status_code < 500:
            raise print(f"Unauthorized access")
            sys.exit(1)
        if "text/html" not in response.headers.get('content-type'):
            raise print(f"Incorrect content type")
            sys.exit(1)
        print(f"{response.text}")
    except Exception as e:
        print(f"{str(e)}")

if __name__ == "__main__":
    main()
