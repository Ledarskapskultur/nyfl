import textwrap
from io import BytesIO
from datetime import datetime

import streamlit as st
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

st.set_page_config(page_title="Ladda ner PDF", page_icon="📄", layout="centered")

st.title("Exempelsida")
st.write(
    """
    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent eget velit sed
    nisl auctor consequat. Suspendisse potenti. Nullam facilisis augue at sapien laoreet,
    et aliquam eros dictum. Vivamus congue, mi vitae faucibus mattis, massa nunc aliquet
    sem, non ultrices nibh neque a augue.
    """
)

def generate_pdf() -> bytes:
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)
    pdf.setTitle("exempel.pdf")

    width, height = A4
    margin = 50

    pdf.setFont("Helvetica-Bold", 16)
    pdf.drawString(margin, height - margin, "Exempel-PDF")

    pdf.setFont("Helvetica", 10)
    datum = datetime.now().strftime("%Y-%m-%d %H:%M")
    pdf.drawString(margin, height - margin - 20, f"Genererad: {datum}")

    textobject = pdf.beginText()
    textobject.setTextOrigin(margin, height - margin - 60)
    textobject.setFont("Helvetica", 12)

    lorem = (
        "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed do eiusmod tempor "
        "incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud "
        "exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure "
        "dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. "
        "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt "
        "mollit anim id est laborum."
    )

    for line in textwrap.wrap(lorem, width=90):
        textobject.textLine(line)

    pdf.drawText(textobject)
    pdf.showPage()
    pdf.save()

    buffer.seek(0)
    return buffer.getvalue()

pdf_bytes = generate_pdf()

st.download_button(
    label="Ladda ner PDF",
    data=pdf_bytes,
    file_name="exempel.pdf",
    mime="application/pdf",
)

st.caption("Klicka på knappen ovan för att ladda ner en genererad PDF.")
