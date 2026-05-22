import requests
from requests.auth import HTTPBasicAuth
import os

ORTHANC = "http://localhost:8042"
AUTH = HTTPBasicAuth("orthanc", "orthanc")
DOWNLOAD_DIR = "dicom_files"

def is_running():
    try:
        response = requests.get(f"{ORTHANC}/system", auth=AUTH, timeout=5)
        return response.status_code == 200
    except Exception:
        return False

def upload_file(filepath):
    try:
        with open(filepath, "rb") as f:
            response = requests.post(
                f"{ORTHANC}/instances",
                auth=AUTH,
                data=f.read(),
                headers={"Content-Type": "application/dicom"}
            )
        if response.status_code == 200:
            return response.json().get("ID", "")
        return None
    except Exception as e:
        return None

def upload_all():
    files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".dcm")]
    results = {"success": 0, "failed": 0, "ids": []}
    for filename in files:
        filepath = os.path.join(DOWNLOAD_DIR, filename)
        instance_id = upload_file(filepath)
        if instance_id:
            results["success"] += 1
            results["ids"].append(instance_id)
        else:
            results["failed"] += 1
    return results

def get_patients():
    response = requests.get(f"{ORTHANC}/patients", auth=AUTH)
    if response.status_code == 200:
        return response.json()
    return []

def get_studies():
    response = requests.get(f"{ORTHANC}/studies", auth=AUTH)
    if response.status_code == 200:
        return response.json()
    return []

def get_instances():
    response = requests.get(f"{ORTHANC}/instances", auth=AUTH)
    if response.status_code == 200:
        return response.json()
    return []

def get_instance_tags(instance_id):
    response = requests.get(
        f"{ORTHANC}/instances/{instance_id}/simplified-tags",
        auth=AUTH
    )
    if response.status_code == 200:
        return response.json()
    return {}