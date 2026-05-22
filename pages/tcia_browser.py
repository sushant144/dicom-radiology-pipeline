import streamlit as st
from tcia_client import get_collections, get_patients, get_studies, get_series, download_series

def show():
    st.title("📥 TCIA Browser")
    st.markdown("Browse and download real cancer imaging data from TCIA public archive.")
    st.markdown("---")

    # step 1 - collection
    st.subheader("Step 1 — Select Collection")
    collections = get_collections()
    selected_collection = st.selectbox("Collection", collections)

    # step 2 - patient
    if selected_collection:
        st.subheader("Step 2 — Select Patient")
        patients = get_patients(selected_collection)
        selected_patient = st.selectbox("Patient", patients)

    # step 3 - study
    if selected_patient:
        st.subheader("Step 3 — Select Study")
        studies = get_studies(selected_patient)
        study_options = {
            f"{s.get('StudyDate', 'N/A')} — {s.get('StudyDescription', 'N/A')}": s['StudyInstanceUID']
            for s in studies
        }
        selected_study_label = st.selectbox("Study", list(study_options.keys()))
        selected_study_uid = study_options[selected_study_label]

    # step 4 - series
    if selected_study_uid:
        st.subheader("Step 4 — Select Series")
        series_list = get_series(selected_study_uid)
        series_options = {
            f"{s.get('Modality', 'N/A')} — {s.get('SeriesDescription', 'N/A')} ({s.get('ImageCount', '?')} images)": s['SeriesInstanceUID']
            for s in series_list
        }
        selected_series_label = st.selectbox("Series", list(series_options.keys()))
        selected_series_uid = series_options[selected_series_label]

        st.markdown("---")
        st.info(f"Selected series has **{selected_series_label}**")

        # download button
        if st.button("⬇️ Download Series"):
            with st.spinner("Downloading DICOM files from TCIA..."):
                files = download_series(selected_series_uid)
            if files:
                st.success(f"✓ Downloaded {len(files)} DICOM files")
            else:
                st.error("Download failed. Check your connection.")