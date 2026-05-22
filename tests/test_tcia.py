import pytest
from tcia_client import get_collections, get_patients, get_studies, get_series

def test_get_collections():
    collections = get_collections()
    assert len(collections) > 0
    assert "4D-Lung" in collections

def test_get_patients():
    patients = get_patients("4D-Lung")
    assert len(patients) > 0
    assert "100_HM10395" in patients

def test_get_studies():
    studies = get_studies("100_HM10395")
    assert len(studies) > 0
    assert "StudyInstanceUID" in studies[0]

def test_get_series():
    studies = get_studies("100_HM10395")
    series = get_series(studies[0]['StudyInstanceUID'])
    assert len(series) > 0
    assert "Modality" in series[0]