import streamlit as st

def show():
    st.title("🏥 DICOM Radiology Informatics Pipeline")
    st.markdown("---")

    st.markdown("""
    A full end-to-end radiology informatics demo built with Python, 
    pydicom, Streamlit, and Orthanc PACS.
    """)

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.info("📥 **TCIA Browser**\nSearch and download real cancer imaging data")

    with col2:
        st.info("🔍 **DICOM Viewer**\nInspect metadata and view CT images")

    with col3:
        st.info("🔒 **De-identify**\nScrub PHI from DICOM files")

    with col4:
        st.info("🗄️ **PACS Dashboard**\nUpload and verify in Orthanc")

    st.markdown("---")
    st.markdown("""
    ### Radiology Informatics Flow
    `EMR` → `ORM` → `RIS` → `Modality` → `PACS` → `ORU` → `EMR`
    
    This project simulates the imaging data layer — 
    from acquisition through PACS storage and metadata verification.
    """)