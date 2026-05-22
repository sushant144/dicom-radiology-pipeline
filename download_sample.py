from tcia_client import download_series

SERIES_UID = "1.3.6.1.4.1.14519.5.2.1.6834.5010.790522551686608875035017785508"

print("Downloading sample DICOM series...")
files = download_series(SERIES_UID)
print(f"Downloaded {len(files)} files")