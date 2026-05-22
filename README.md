# DICOM Radiology Informatics Pipeline
# 1 - start PACS
docker-compose up -d

# 2 - install dependencies
uv venv && source .venv/bin/activate && uv sync

# 3 - load sample data
python setup_sample_data.py

# 4 - run app
streamlit run app.py