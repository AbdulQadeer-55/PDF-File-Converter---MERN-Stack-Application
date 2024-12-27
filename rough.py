import streamlit as st
import pandas as pd
import camelot
from io import BytesIO

# Function to extract and format data from the PDF
def extract_and_format_data(pdf_file):
    try:
        tables = camelot.read_pdf(pdf_file, pages="all", flavor="stream")
        formatted_data = {
            "Day": [],
            "Date": [],
            "USD": []
        }
        
        for table in tables:
            df = table.df
            for _, row in df.iterrows():
                formatted_data["Day"].append(row[0])  # Replace based on PDF structure
                formatted_data["Date"].append(row[1])  # Replace based on PDF structure
                formatted_data["USD"].append(row[2])  # Replace based on PDF structure

        final_df = pd.DataFrame(formatted_data)
        return final_df
    except Exception as e:
        st.error(f"Error processing the PDF: {e}")
        return None

# UI: Streamlit App
def main():
    # Page settings
    st.set_page_config(
        page_title="PDF to Excel Converter",
        page_icon="📄",
        layout="wide",
        initial_sidebar_state="expanded",
    )
    
    # Custom CSS for modern design
    st.markdown("""
        <style>
            body {
                font-family: 'Segoe UI', sans-serif;
                color: #444;
                background-color: #f4f4f9;
            }
            header {
                font-size: 24px;
                font-weight: bold;
                color: #4a4e69;
                text-align: center;
                margin: 20px 0;
            }
            .stButton>button {
                background-color: #3a86ff;
                color: white;
                font-size: 16px;
                border-radius: 8px;
                border: none;
                padding: 10px 20px;
            }
            .stButton>button:hover {
                background-color: #8338ec;
            }
        </style>
    """, unsafe_allow_html=True)

    # Page Header
    st.markdown("<header>📄 PDF to Excel Converter</header>", unsafe_allow_html=True)

    # File Upload
    uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

    if uploaded_file:
        st.success("File uploaded successfully! Processing...")
        with st.spinner("Extracting data..."):
            extracted_data = extract_and_format_data(uploaded_file)

        if extracted_data is not None:
            st.success("Data extracted successfully!")
            st.dataframe(extracted_data)

            # Download button
            output = BytesIO()
            with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
                extracted_data.to_excel(writer, index=False, sheet_name="Data")
            output.seek(0)

            st.download_button(
                label="Download Excel File",
                data=output,
                file_name="formatted_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            )
        else:
            st.error("Unable to process the PDF file. Please ensure it's formatted correctly.")

    # Sidebar
    with st.sidebar:
        st.markdown("### About the App")
        st.markdown("""
        This app converts data from PDF files into structured Excel sheets
        with modern and elegant design principles.
        """)
        st.markdown("**Developed by:** [Your Name]")
        st.markdown("**Version:** 1.0")

# Run the app
if __name__ == "__main__":
    main()
