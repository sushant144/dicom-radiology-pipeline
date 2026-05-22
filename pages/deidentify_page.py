import streamlit as st
import pandas as pd
from deidentify import deidentify_all, get_deidentified_files, compare_tags
from dicom_utils import get_dicom_files

def show():
    st.title("🔒 De-identification")
    st.markdown("Scrub PHI from DICOM files before sending to research or external systems.")
    st.markdown("---")

    files = get_dicom_files()

    if not files:
        st.warning("No DICOM files found. Download a series first.")
        return

    st.info(f"Found **{len(files)}** DICOM files ready for de-identification")

    anonymous_id = st.text_input(
        "Anonymous Patient ID",
        value="ANON001",
        help="This value replaces all PHI tags"
    )

    if st.button("🔒 De-identify All Files"):
        with st.spinner("Scrubbing PHI tags..."):
            results = deidentify_all(anonymous_id)
        st.success(f"✓ De-identified {results['success']} files")
        if results['failed'] > 0:
            st.error(f"✗ Failed: {results['failed']} files")

    # before/after comparison
    deidentified = get_deidentified_files()
    if deidentified:
        st.markdown("---")
        st.subheader("Before / After Comparison")
        selected = st.selectbox("Select file to compare", sorted(deidentified))

        if selected:
            comparison = compare_tags(selected)
            if comparison:
                df = pd.DataFrame(comparison)
                st.dataframe(
                    df.style.map(
                        lambda v: "background-color: #d4edda" if v == True else "",
                        subset=["scrubbed"]
                    ),
                    use_container_width=True
                )