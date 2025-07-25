import requests, pandas as pd
from bs4 import BeautifulSoup

URL = "https://remoteok.com/remote-python-jobs"
resp = requests.get(URL, headers={"User-Agent": "Mozilla/5.0"})
soup = BeautifulSoup(resp.text, "html.parser")

jobs = []
for card in soup.select("tr.job"):
    jobs.append({
        "title":   card.select_one("h2").get_text(strip=True),
        "company": card.select_one("h3").get_text(strip=True),
        "date":    card.select_one("time")["datetime"],
        "link":    "https://remoteok.com" + card["data-href"],
        "tags":    ", ".join(t.get_text(strip=True) for t in card.select("td.tags a")),
    })

pd.DataFrame(jobs).to_csv("remoteok.csv", index=False)
print(f"{len(jobs)} offres enregistrées dans remoteok.csv")
