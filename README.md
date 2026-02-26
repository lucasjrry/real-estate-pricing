# Hyper-Local Real Estate Valuation Engine 🏡

## Overview
A full-stack machine learning application designed to predict real estate pricing (housing and renting costs).

## Current Scope (MVP)
* **Target Metro:** Los Angeles Metro Area.
* **Data Source:** Row-level CSV ingestion (Redfin).
* **Focus:** Developing the core ingestion pipeline, spatial clustering algorithms, and prediction engine before scaling to other cities. 

## Tech Stack & Architecture
This project is built as a Monorepo, separating the interactive UI from the data-heavy machine learning backend.

### Frontend (User Interface & Mapping)
* **Framework:** Next.js (App Router) with React
* **Language:** TypeScript
* **Styling:** Tailwind CSS
* **Visualization (Planned):** Mapbox GL JS or Leaflet for side-by-side map and list comparisons.

### Backend (API & Machine Learning)
* **Framework:** FastAPI (Python)
* **Environment Management:** `uv`
* **Database:** SQLite
* **ORM:** SQLAlchemy
* **Data Pipeline:** Pandas (for cleaning and database upserting)
* **Machine Learning:** Scikit-learn (DBSCAN/K-Means for clustering), XGBoost (for price prediction)
