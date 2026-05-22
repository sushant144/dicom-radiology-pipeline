import pydicom
import os
import shutil
from datetime import datetime

DOWNLOAD_DIR = "dicom_files"
DEIDENTIFIED_DIR = "dicom_deidentified"

# PHI tags to scrub based on DICOM standard
PHI_TAGS = [
    "PatientName",
    "PatientID",
    "PatientBirthDate",
    "PatientSex",
    "PatientAge",
    "AccessionNumber",
    "ReferringPhysicianName",
    "InstitutionName",
    "InstitutionAddress",
    "StationName",
]

def deidentify_file(filename, anonymous_id):
    src = os.path.join(DOWNLOAD_DIR, filename)
    os.makedirs(DEIDENTIFIED_DIR, exist_ok=True)
    dst = os.path.join(DEIDENTIFIED_DIR, filename)

    try:
        ds = pydicom.dcmread(src)

        # scrub each PHI tag
        for tag in PHI_TAGS:
            if tag in ds:
                ds.data_element(tag).value = anonymous_id

        # add de-identification note
        ds.PatientIdentityRemoved = "YES"
        ds.DeidentificationMethod = "Manual PHI scrub"

        ds.save_as(dst)
        return True
    except Exception as e:
        return False

def deidentify_all(anonymous_id="ANON001"):
    files = [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".dcm")]
    results = {"success": 0, "failed": 0}

    for filename in files:
        if deidentify_file(filename, anonymous_id):
            results["success"] += 1
        else:
            results["failed"] += 1

    return results

def get_deidentified_files():
    if not os.path.exists(DEIDENTIFIED_DIR):
        return []
    return [f for f in os.listdir(DEIDENTIFIED_DIR) if f.endswith(".dcm")]

def compare_tags(filename):
    original_path = os.path.join(DOWNLOAD_DIR, filename)
    deidentified_path = os.path.join(DEIDENTIFIED_DIR, filename)

    if not os.path.exists(deidentified_path):
        return None

    original = pydicom.dcmread(original_path)
    deidentified = pydicom.dcmread(deidentified_path)

    comparison = []
    for tag in PHI_TAGS:
        original_value = str(original.get(tag, "N/A"))
        deidentified_value = str(deidentified.get(tag, "N/A"))
        comparison.append({
            "tag": tag,
            "original": original_value,
            "deidentified": deidentified_value,
            "scrubbed": original_value != deidentified_value
        })

    return comparison