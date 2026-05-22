import requests
import zipfile
import io
import os

BASE = "https://services.cancerimagingarchive.net/nbia-api/services/v1"
DOWNLOAD_DIR = "dicom_files"

def get_collections():
    response = requests.get(f"{BASE}/getCollectionValues")
    if response.status_code == 200:
        return [c['Collection'] for c in response.json()]
    return []

def get_patients(collection):
    response = requests.get(f"{BASE}/getPatient?Collection={collection}")
    if response.status_code == 200:
        return [p['PatientId'] for p in response.json()]
    return []


def get_studies(patient_id):
    response = requests.get(f"{BASE}/getPatientStudy?PatientID={patient_id}")
    if response.status_code == 200:
        return response.json()
    return []

def get_series(study_uid):
    response = requests.get(f"{BASE}/getSeries?StudyInstanceUID={study_uid}")
    if response.status_code == 200:
        return response.json()
    return []

def download_series(series_uid):
    os.makedirs(DOWNLOAD_DIR, exist_ok=True)
    response = requests.get(
        f"{BASE}/getImage?SeriesInstanceUID={series_uid}",
        stream=True
    )
    if response.status_code == 200:
        z = zipfile.ZipFile(io.BytesIO(response.content))
        z.extractall(DOWNLOAD_DIR)
        files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".dcm")]
        return files
    return []
