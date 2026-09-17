# 🧭 Solvent

**Cash-flow intelligence for founders and individuals.**
At this rate, when do you run out of money and what's actually driving it?

Solvent auto-categorizes transactions, flags anomalies before they become
problems, and forecasts cash flow with honest confidence intervals not a
single false-precision number. Built as a real production ML system: versioned
data and models, drift monitoring, automated retraining, served via FastAPI
with a live dashboard.

> 🚧 **Status: actively being built, in public.** This README doubles as a
> build log checkboxes below reflect what's actually done, not what's planned.
> No shortcuts: every component is read-first, hand-built, tested.

---

## Why this exists

82% of small business failures trace back to poor cash flow management, and
classical ML can improve short-term forecast accuracy by 30–50% over manual
methods, yet most tools built for this either don't exist for individuals,
or quote a fake-precise number instead of an honest range. Solvent treats
uncertainty as a first-class citizen, not an afterthought.

## What it does

- 🏷️ **Auto-categorizes transactions** from raw, messy vendor descriptions (TF-IDF + LightGBM), with low-confidence predictions flagged for review instead of silently guessed
- 🚨 **Flags anomalies**: duplicate charges, vendor amount spikes, first-time vendors — with a plain-English reason, not just a risk score (Isolation Forest)
- 📈 **Forecasts cash flow** as a calibrated range (P10/P50/P90 via quantile regression), not a single misleading number
- 🛬 **Estimates runway**: when you run out of money, given as a date range with a confidence level
- 📊 **Live dashboard**: spend breakdown, forecast chart with shaded uncertainty band, anomaly feed

## Tech stack

`Python` · `LightGBM` · `scikit-learn` · `FastAPI` · `DVC` · `MLflow` · `Docker` ·
`GitHub Actions` · `Evidently AI` · `Airflow` · `React` (frontend, later)

## Project structure

```text
solvent/
├── data/
│   ├── raw/              # Raw data — sacred, never overwritten by hand
│   └── processed/
├── src/
│   ├── config/           # Settings each component needs before running
│   ├── entity/           # Config + artifact dataclasses — the "receipts"
│   ├── components/       # Real, reusable, independently-testable logic
│   ├── pipeline/         # Sequencing only — no real logic lives here
│   └── utils/            # Shared logging + custom exceptions
├── tests/
└── notebooks/             # Exploratory only, never part of the real pipeline


---

## 🗺️ Build log / roadmap

### Phase 1: Foundations
- [x] Repo scaffold, config-driven structure
- [x] `src/utils/logging.py` — structured logging, deduped handlers, tested
- [x] `src/utils/exceptions.py` — custom exception with filename + line-number tracing, tested
- [ ] `src/entity/` — ingestion config + artifact dataclasses
- [ ] `src/components/data_ingestion.py`
- [ ] `src/pipeline/training_pipeline.py` (ingestion wired in)
- [ ] `tests/test_ingestion.py`
- [ ] Data ingestion: PaySim + synthetic transaction generator
- [ ] Cleaning: dedup, fuzzy vendor matching, outlier flagging
- [ ] DVC — data + model versioning
- [ ] Feature engineering + strict time-based train/val/test split

### Phase 2: Models
- [ ] Transaction categorizer (TF-IDF + LightGBM) + MLflow tracking
- [ ] Baseline comparison + registry promotion logic
- [ ] Anomaly detector (Isolation Forest) + reason-code generation
- [ ] Anomaly detector evaluation (precision/recall on PaySim labels)
- [ ] Cash-flow forecaster (quantile GBM, P10/P50/P90)
- [ ] Runway calculation + calibration check

### Phase 3: Serving + Ops
- [ ] FastAPI endpoints (`/categorize`, `/anomalies`, `/forecast`)
- [ ] Docker (multi-stage build)
- [ ] CI/CD (GitHub Actions — lint, test, build)
- [ ] Cloud deployment
- [ ] Monitoring (Evidently — drift detection)
- [ ] Airflow retraining DAG
- [ ] React dashboard with forecast chart + confidence band
- [ ] Model card + README polish

---

## Running it locally

```bash
git clone https://github.com/KunalAyush1/solvent
cd solvent
uv sync            # or: python -m venv .venv && pip install -r requirements.txt
pytest tests/
```



---

