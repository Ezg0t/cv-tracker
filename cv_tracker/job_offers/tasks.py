from celery import shared_task
import requests
from bs4 import BeautifulSoup
from .models import JobOffer

@shared_task
def fetch_justjoin_offers(keyword="Python"):
    url = f"https://justjoin.it/job-offers/all-locations?keyword={keyword}"
    response = requests.get(url)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")

    offers_html = soup.select("a.offer-card")

    for offer in offers_html:
        try:
            href = offer.get("href")
            url_offer = f"https://justjoin.it{href}"

            title_tag = offer.select_one("h3")
            title = title_tag.get_text(strip=True) if title_tag else ""

            company_tag = offer.select_one("p.MuiTypography-root.MuiTypography-body1.mui-1jo71uz")
            company_name = company_tag.get_text(strip=True) if company_tag else ""

            location_tag = offer.select_one("span.mui-1o4wo1x")
            location = location_tag.get_text(strip=True) if location_tag else ""

            JobOffer.objects.update_or_create(
                url=url_offer,
                defaults={
                    "title": title,
                    "company_name": company_name,
                    "location": location
                }
            )
        except Exception as e:
            print(f"Błąd przy ofercie: {e}")

    print(f"Pobrano {len(offers_html)} ofert dla keyword={keyword}")
