import pydicom
import os

DOWNLOAD_DIR = "dicom_files"

def get_dicom_files():
    if not os.path.exists(DOWNLOAD_DIR):
        return []
    return [f for f in os.listdir(DOWNLOAD_DIR) if f.endswith(".dcm")]

def read_metadata(filename):
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    try:
        ds = pydicom.dcmread(filepath)
        return {
            "patient_id"    : str(ds.get("PatientID", "")),
            "patient_name"  : str(ds.get("PatientName", "")),
            "modality"      : str(ds.get("Modality", "")),
            "study_date"    : str(ds.get("StudyDate", "")),
            "series_desc"   : str(ds.get("SeriesDescription", "")),
            "accession"     : str(ds.get("AccessionNumber", "")),
            "slice_location": str(ds.get("SliceLocation", "")),
            "rows"          : str(ds.get("Rows", "")),
            "columns"       : str(ds.get("Columns", "")),
        }
    except Exception as e:
        return {"error": str(e)}

def read_pixel_array(filename):
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    try:
        ds = pydicom.dcmread(filepath)
        return ds.pixel_array
    except Exception as e:
        return None

def get_all_tags(filename):
    filepath = os.path.join(DOWNLOAD_DIR, filename)
    try:
        ds = pydicom.dcmread(filepath)
        tags = []
        for elem in ds:
            tags.append({
                "tag"  : str(elem.tag),
                "name" : elem.name,
                "value": str(elem.value)[:100]
            })
        return tags
    except Exception as e:
        return []