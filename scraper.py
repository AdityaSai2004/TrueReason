import requests
from bs4 import BeautifulSoup

def fetch_clean_content(url, word_limit=500):
    try:
        # Fetch the webpage
        response = requests.get(url, timeout=5, headers={"User-Agent": "Mozilla/5.0"})
        response.raise_for_status()

        # Parse the HTML
        soup = BeautifulSoup(response.text, "html.parser")

        # Special case: Wikipedia articles (they have structured content)
        if "wikipedia.org" in url:
            content_div = soup.find("div", {"id": "mw-content-text"})
            if not content_div:
                return "Could not extract main content."
            paragraphs = content_div.find_all("p")
        
        else:
            # General websites: Look for meaningful content
            article = soup.find("article")  # Prioritize <article> tag if present
            if article:
                paragraphs = article.find_all("p")
            else:
                # Fallback: Get the largest text-containing <div>
                divs = soup.find_all("div")
                largest_div = max(divs, key=lambda d: len(d.get_text(strip=True)), default=None)
                paragraphs = largest_div.find_all("p") if largest_div else []

        # Extract text content
        text = " ".join(p.get_text(strip=True) for p in paragraphs)

        # Get the first N words
        words = text.split()[:word_limit]
        snippet = " ".join(words)

        return snippet if snippet else "Could not extract useful content."

    except requests.RequestException as e:
        return f"Error fetching URL: {str(e)}"