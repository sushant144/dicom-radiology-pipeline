import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
from dicom_utils import get_dicom_files, read_metadata, get_all_tags, read_pixel_array

def show():
    st.title("🔍 DICOM Viewer")
    st.markdown("Select a DICOM file to inspect metadata and view the CT image.")
    st.markdown("---")

    files = get_dicom_files()

    if not files:
        st.warning("No DICOM files found. Go to TCIA Browser and download a series first.")
        return

    selected_file = st.selectbox("Select DICOM file", sorted(files))

    if selected_file:
        col1, col2 = st.columns([1.2, 0.8])

        # left column - CT image
        with col1:
            st.subheader("CT Image")
            pixel_array = read_pixel_array(selected_file)
            if pixel_array is not None:
                fig, ax = plt.subplots()
                ax.imshow(pixel_array, cmap="gray")
                ax.axis("off")
                st.pyplot(fig)
            else:
                st.error("Could not load image")

        # right column - metadata
        with col2:
            st.subheader("Key Metadata")
            metadata = read_metadata(selected_file)
            for key, value in metadata.items():
                st.text(f"{key:<20}: {value}")

        # full tag table
        st.markdown("---")
        st.subheader("All DICOM Tags")
        tags = get_all_tags(selected_file)
        if tags:
            import pandas as pd
            df = pd.DataFrame(tags)
            st.dataframe(df, use_container_width=True)