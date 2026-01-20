from api.index import HDHubScraper
import json
import asyncio

def test_search():
    scraper = HDHubScraper()
    print("Searching for 'avengers'...")
    search_url = f"https://4khdhub.dad/?s=avengers"
    resp = scraper.session.get(search_url)
    with open("debug_search.html", "w", encoding="utf-8") as f:
        f.write(resp.text)
    print("Saved HTML to debug_search.html")

    try:
        results = scraper.search_movies("avengers")
        print(json.dumps(results, indent=2))
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_search()
