import streamlit as st
import requests
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from io import BytesIO

API_URL = "http://127.0.0.1:8000/generate"

st.title("⚖️ LegalEase")

document_type = st.text_input("Document Type")

parties = st.text_area("Parties")

terms = st.text_area("Terms & Conditions")

effective_date = st.text_input("Effective Date")


if st.button("Generate Document"):

    payload = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "effective_date": effective_date
    }

    try:

        response = requests.post(
            API_URL,
            json=payload
        )

        if response.status_code == 200:

            document = response.json()["document"]

            st.text_area(
                "Generated Document",
                document,
                height=400
            )

            # TXT Download
            st.download_button(
                "📄 Download TXT",
                document,
                file_name="legal_document.txt",
                mime="text/plain"
            )

            # PDF Creation
            pdf_buffer = BytesIO()

            pdf = canvas.Canvas(
                pdf_buffer,
                pagesize=A4
            )

            width, height = A4

            x = 50
            y = height - 50

            pdf.setFont(
                "Helvetica",
                10
            )

            for line in document.split("\n"):

                words = line.split()
                current_line = ""

                for word in words:

                    test_line = current_line + word + " "

                    if pdf.stringWidth(
                        test_line,
                        "Helvetica",
                        10
                    ) < 500:

                        current_line = test_line

                    else:

                        pdf.drawString(
                            x,
                            y,
                            current_line
                        )

                        y -= 15

                        current_line = word + " "

                        if y < 50:

                            pdf.showPage()

                            pdf.setFont(
                                "Helvetica",
                                10
                            )

                            y = height - 50

                if current_line:

                    pdf.drawString(
                        x,
                        y,
                        current_line
                    )

                y -= 15

                if y < 50:

                    pdf.showPage()

                    pdf.setFont(
                        "Helvetica",
                        10
                    )

                    y = height - 50

            pdf.save()

            pdf_buffer.seek(0)

            # PDF Download
            st.download_button(
                "📥 Download PDF",
                data=pdf_buffer,
                file_name="legal_document.pdf",
                mime="application/pdf"
            )

        else:

            st.error(
                f"Backend Error: {response.status_code}"
            )

    except Exception as e:

        st.error(
            f"Error: {e}"
        )