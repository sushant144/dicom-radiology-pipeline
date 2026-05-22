import pytest
from orthanc_client import is_running, get_patients, get_studies, get_instances

def test_orthanc_is_running():
    assert is_running() == True

def test_get_patients():
    patients = get_patients()
    assert len(patients) > 0

def test_get_studies():
    studies = get_studies()
    assert len(studies) > 0

def test_get_instances():
    instances = get_instances()
    assert len(instances) > 0