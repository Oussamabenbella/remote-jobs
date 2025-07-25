# Remote Jobs Scraper 🚀

Petit projet **Scrapy + SQLite + Streamlit** qui agrège les offres d’emploi « remote ».

## Fonctionnalités
- **Scrapy** extrait les jobs depuis RemoteOK (API JSON).
- Pipeline **SQLite** — stocke dans `jobs.db`, évite les doublons.
- **Streamlit** affiche un tableau de bord filtrable (techno, date).
  
<p align="center">
  <img src="C:\Users\user\remote-jobs\docs\Capture d’écran 2025-07-25 154559.png" width="600"/>
  <img src="C:\Users\user\remote-jobs\docs\Capture d’écran 2025-07-25 154646.png" width="600"/>
</p>

## Installation rapide

```bash
git clone https://github.com/<ton‑user>/remote-jobs.git
cd remote-jobs
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt

# 1) Construire/mettre à jour la base
scrapy crawl remoteok_api

# 2) Lancer le dashboard
streamlit run dashboard.py
