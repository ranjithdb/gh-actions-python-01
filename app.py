import requests

def fetch_github():
    response = requests.get("https://api.github.com")
    if response.status_code == 200:
        return "GitHub API is reachable!"
    return "Failed to reach GitHub API."

if __name__ == "__main__":
    print(fetch_github())
