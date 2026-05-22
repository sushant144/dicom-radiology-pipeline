from tcia_client import download_series
from orthanc_client import is_running, upload_all

SERIES_UID = "1.3.6.1.4.1.14519.5.2.1.6834.5010.790522551686608875035017785508"

def setup():
    # check Orthanc is running
    if not is_running():
        print("❌ Orthanc is not running.")
        print("   Start it first: docker-compose up -d")
        return

    # download DICOM files
    print("Downloading sample DICOM series from TCIA...")
    files = download_series(SERIES_UID)
    print(f"✓ Downloaded {len(files)} files")

    # upload to Orthanc
    print("Uploading to Orthanc PACS...")
    results = upload_all()
    print(f"✓ Uploaded {results['success']} files")
    print(f"✓ Setup complete — ready to run the app")

if __name__ == "__main__":
    setup()