import streamlit as st

st.set_page_config(
    page_title="DICOM Radiology Pipeline",
    page_icon="🏥",
    layout="wide"
)

# sidebar navigation
st.sidebar.title("🏥 Radiology Pipeline")
st.sidebar.markdown("---")

page = st.sidebar.radio(
    "Navigate",
    ["Home", "TCIA Browser", "DICOM Viewer", "PACS Dashboard"]
)

# route to pages
if page == "Home":
    from pages.home import show
    show()
elif page == "TCIA Browser":
    from pages.tcia_browser import show
    show()
elif page == "DICOM Viewer":
    from pages.dicom_viewer import show
    show()
elif page == "PACS Dashboard":
    from pages.pacs_dashboard import show
    show()