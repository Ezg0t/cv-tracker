# Django Job Tracker

Prosta aplikacja Django do zarządzania ofertami pracy i wysłanymi aplikacjami.

Pozwala na:

* Przeglądanie ofert pracy (`job_offers`)
* Dodawanie aplikacji (`applications`) z poziomu oferty
* Śledzenie statusów aplikacji
* Zmianę statusów ofert i aplikacji
* Obsługę Celery i Redis do pobierania ofert w tle

---

## 🔹 Docker i uruchomienie projektu

Projekt wymaga Dockera do poprawnego działania, ponieważ używa:

* **Redis** jako brokera zadań dla Celery
* **Celery** do pobierania ofert w tle (scraper)

Aby uruchomić projekt w kontenerach:

1. Sklonuj repozytorium:

```bash
git clone <repo_url>
cd <repo_folder>
```

2. Upewnij się, że masz zainstalowanego Dockera.

3. Uruchom projekt i wszystkie potrzebne usługi (Django, Redis, Celery):

```bash
docker-compose up --build
```

4. Projekt będzie dostępny pod adresem:

```
http://127.0.0.1:8000/job-offers/
```

5. Celery będzie automatycznie pobierać oferty w tle i przetwarzać zadania.

---
