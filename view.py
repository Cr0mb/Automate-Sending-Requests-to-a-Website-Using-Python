import requests
import random
import time
from colorama import init, Fore, Style

init(autoreset=True)

def load_proxies(file_path='proxies.txt'):
    with open(file_path, 'r') as file:
        proxies = file.read().splitlines()
    return proxies

def view_video_with_proxy(video_url, proxy, duration):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Referer': 'https://www.youtube.com/'
    }

    proxy_type = None
    if proxy.startswith('http://'):
        proxy_type = 'http'
    elif proxy.startswith('https://'):
        proxy_type = 'https'
    elif proxy.startswith('socks5://'):
        proxy_type = 'socks5'
    elif proxy.startswith('socks4://'):
        proxy_type = 'socks4'

    proxy_dict = {proxy_type: proxy} if proxy_type else {'http': proxy, 'https': proxy}

    try:
        start_time = time.time()
        response = requests.get(video_url, headers=headers, proxies=proxy_dict, timeout=10)
        response.raise_for_status()
        elapsed_time = time.time() - start_time
        print(Fore.GREEN + f"Viewed video with proxy: {proxy}")
        print(Fore.GREEN + f"Proxy Type: {proxy_type.upper()}")
        print(Fore.GREEN + f"Status Code: {response.status_code}")
        print(Fore.GREEN + f"Elapsed Time: {elapsed_time:.2f} seconds\n")
        time.sleep(duration)
    except requests.RequestException as e:
        print(Fore.RED + f"Failed to view video with proxy: {proxy}")
        print(Fore.RED + f"Proxy Type: {proxy_type.upper() if proxy_type else 'Unknown'}")
        print(Fore.RED + f"Error: {e}\n")

def main():
    video_url = 'https://www.youtube.com/watch?v=gR-AhoWpbaI'
    proxies = load_proxies()
    session_duration = random.randint(5, 5)
    print(Fore.YELLOW + Style.BRIGHT + f"Starting to view the video using proxies for {session_duration} seconds each...\n")

    for _ in range(len(proxies)):
        proxy = random.choice(proxies)
        view_video_with_proxy(video_url, proxy, session_duration)

    print(Fore.CYAN + Style.BRIGHT + f"\nFinished viewing the video with all proxies for {session_duration} seconds each.")

if __name__ == "__main__":
    main()
