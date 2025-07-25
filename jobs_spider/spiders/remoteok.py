import scrapy, json
from datetime import datetime, timezone

class RemoteokAPISpider(scrapy.Spider):
    name = "remoteok_api"
    allowed_domains = ["remoteok.com"]
    start_urls = ["https://remoteok.com/api"]

    def parse(self, response):
        data = json.loads(response.text)
        for job in data:
            # l'API retourne un premier dict 'legal' → ignorer
            if "id" not in job:
                continue
            yield {
                "link":    job["url"],
                "title":   job["position"],
                "company": job["company"],
                "date":    datetime.fromtimestamp(job["epoch"], tz=timezone.utc).isoformat(),
                "tags":    ", ".join(job["tags"]),
            }
