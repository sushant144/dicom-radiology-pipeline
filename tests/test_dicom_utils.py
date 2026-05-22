import pytest
from dicom_utils import get_dicom_files, read_metadata, get_all_tags

def test_get_dicom_files():
    files = get_dicom_files()
    assert len(files) > 0

def test_read_metadata():
    files = get_dicom_files()
    metadata = read_metadata(files[0])
    assert "patient_id" in metadata
    assert "modality" in metadata
    assert metadata["modality"] == "CT"

def test_get_all_tags():
    files = get_dicom_files()
    tags = get_all_tags(files[0])
    assert len(tags) > 0
    assert "tag" in tags[0]
    assert "name" in tags[0]