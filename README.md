# 🏥 DICOM Radiology Informatics Pipeline

A full end-to-end radiology informatics demo built with Python, pydicom, Streamlit, and Orthanc PACS — simulating real-world clinical imaging workflows.

## Overview

This project demonstrates the core data flow in radiology informatics:

```
EMR → ORM → RIS → Modality → PACS → ORU → EMR
```

From imaging data acquisition through PACS storage, PHI de-identification, and metadata verification — all visualized through an interactive Streamlit dashboard.

---

## Features

- 📥 **TCIA Browser** — Search and download real cancer imaging data from the NIH Cancer Imaging Archive
- 🔍 **DICOM Viewer** — Inspect DICOM metadata and visualize CT images slice by slice
- 🔒 **PHI De-identification** — Scrub patient identifiers from DICOM files with before/after comparison
- 🗄️ **PACS Dashboard** — Upload de-identified studies to a local Orthanc PACS and verify stored metadata

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Language | Python 3.13 |
| UI | Streamlit |
| DICOM | pydicom |
| Data | pandas |
| PACS | Orthanc (Docker) |
| Imaging Data | TCIA Public API |
| Package Manager | uv |
| Tests | pytest |

---

## Architecture

```
TCIA API
   ↓
tcia_client.py       — collection, patient, study, series, download
   ↓
dicom_utils.py       — read tags, pixel array, all DICOM metadata
   ↓
deidentify.py        — scrub PHI tags, save de-identified files
   ↓
orthanc_client.py    — upload to PACS, query patients/studies/instances
   ↓
Streamlit UI         — interactive dashboard across all 4 modules
```

---

## Prerequisites

- Python 3.11+
- Docker Desktop
- uv package manager

Install uv:

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

---

## Quick Start

### 1 — Clone the repo

```bash
git clone https://github.com/sushant144/dicom-radiology-pipeline.git
cd dicom-radiology-pipeline
```

### 2 — Start Orthanc PACS

```bash
docker-compose up -d
```

Orthanc UI available at http://localhost:8042
Login: `orthanc` / `orthanc`

### 3 — Install dependencies

```bash
uv venv
source .venv/bin/activate
uv sync
```

### 4 — Load sample DICOM data

```bash
python setup_sample_data.py
```

Downloads a 4D-Lung CT series from TCIA and uploads to your local Orthanc instance.

### 5 — Run the app

```bash
streamlit run app.py
```

---

## Running Tests

```bash
pytest tests/ -v
```

Tests automatically download and upload sample data if not already present. No manual setup required.

---

## Project Structure

```
dicom-radiology-pipeline/
├── app.py                     # Streamlit main app and navigation
├── tcia_client.py             # TCIA public API client
├── dicom_utils.py             # pydicom metadata extraction
├── deidentify.py              # PHI de-identification
├── orthanc_client.py          # Orthanc REST API wrapper
├── setup_sample_data.py       # One-command data setup
├── docker-compose.yml         # Orthanc PACS container
├── pages/
│   ├── home.py                # Project overview
│   ├── tcia_browser.py        # TCIA search and download
│   ├── dicom_viewer.py        # CT image and metadata viewer
│   ├── deidentify_page.py     # PHI scrubbing UI
│   └── pacs_dashboard.py      # PACS upload and verification
├── tests/
│   ├── conftest.py            # Auto test data setup
│   ├── test_tcia.py           # TCIA API tests
│   ├── test_dicom_utils.py    # pydicom utility tests
│   └── test_orthanc_client.py # Orthanc client tests
└── pyproject.toml             # Project dependencies
```

---

## Clinical Context

This project simulates the imaging data layer of a real radiology informatics workflow:

- **ORM messages** — EMR sends imaging orders to RIS when a physician orders a scan
- **DICOM Modality Worklist** — RIS feeds patient context to the scanner before imaging
- **C-STORE protocol** — Scanner sends DICOM images to PACS after acquisition
- **De-identification** — PHI must be scrubbed before research data leaves the institution
- **ORU messages** — RIS sends structured results back to the EMR after radiologist reads

---

## Screenshots

> Add screenshots here after first run:
> - Home page with radiology flow diagram
> - TCIA Browser with collection selector
> - DICOM Viewer showing CT image and metadata
> - De-identification before/after comparison
> - PACS Dashboard with patient/study/instance counts

---

## About

Built as a hands-on learning project to demonstrate radiology informatics concepts — DICOM, PACS integration, PHI governance, and clinical data pipelines — using real public cancer imaging data from the NIH TCIA archive.

---

*Sample data sourced from the 4D-Lung collection via the [Cancer Imaging Archive](https://www.cancerimagingarchive.net/) — a public, de-identified research dataset.*