import streamlit as st
import requests

from utils.document_utils import format_html_preview
from utils.export_utils import (
    create_txt,
    create_docx,
    create_pdf
)


BACKEND_URL = "http://127.0.0.1:8000/generate"


st.set_page_config(
    page_title="LegalEase",
    page_icon="⚖️",
    layout="wide"
)


st.title("⚖️ LegalEase")
st.subheader("AI-Powered Legal Document Generator")

st.write(
    "Generate customizable legal documents using AI."
)

st.divider()


document_type = st.text_input(
    "Document Type",
    placeholder="Example: NDA / Employment Contract / Lease Agreement"
)

parties = st.text_area(
    "Parties Involved",
    placeholder="Example: John Doe (Employee), ABC Company (Employer)"
)

terms = st.text_area(
    "Terms & Conditions",
    placeholder=(
        "Payment terms; "
        "Confidentiality; "
        "Termination conditions"
    )
)

dates = st.text_input(
    "Effective Date",
    placeholder="Example: 30/09/2026"
)


if st.button("Generate Document", type="primary"):

    if not document_type or not parties or not terms or not dates:

        st.warning(
            "Please fill in all the required fields."
        )

    else:

        payload = {
            "document_type": document_type,
            "parties": parties,
            "terms": terms,
            "dates": dates
        }

        try:

            response = requests.post(
                BACKEND_URL,
                json=payload
            )

            if response.status_code == 200:

                result = response.json()

                st.session_state["document"] = (
                    result["document"]
                )

                st.success(
                    "Document generated successfully!"
                )

            else:

                st.error(
                    "Failed to generate document."
                )

        except requests.exceptions.ConnectionError:

            st.error(
                "Backend is not running. "
                "Please start FastAPI first."
            )


if "document" in st.session_state:

    st.divider()

    st.subheader("Document Preview")

    st.markdown(
        format_html_preview(
            st.session_state["document"]
        ),
        unsafe_allow_html=True
    )

    st.subheader("Edit Document")

    edited_document = st.text_area(
        "Edit your document here:",
        value=st.session_state["document"],
        height=400
    )

    st.session_state["document"] = edited_document

    st.subheader("Download")

    txt_data = create_txt(edited_document)

    docx_data = create_docx(
        edited_document,
        document_type
    )

    pdf_data = create_pdf(
        edited_document,
        document_type
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.download_button(
            "Download TXT",
            data=txt_data,
            file_name="LegalEase_Document.txt",
            mime="text/plain"
        )

    with col2:

        st.download_button(
            "Download DOCX",
            data=docx_data,
            file_name="LegalEase_Document.docx",
            mime=(
                "application/vnd.openxmlformats-officedocument."
                "wordprocessingml.document"
            )
        )

    with col3:

        st.download_button(
            "Download PDF",
            data=pdf_data,
            file_name="LegalEase_Document.pdf",
            mime="application/pdf"
        )
