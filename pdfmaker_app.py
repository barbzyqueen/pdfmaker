import streamlit as st
import pandas as pd
from fpdf import FPDF
import os

# App Title
st.title("PDF Generator from CSV")

# File Upload
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    # Read CSV file
    df = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded File:")
    st.dataframe(df)

    # Generate PDF
    if st.button("Generate PDF"):
        # Create an instance of FPDF class
        pdf = FPDF(orientation="P", unit="mm", format="A4")
        pdf.set_auto_page_break(auto=False, margin=0)

        for index, row in df.iterrows():
            pdf.add_page()

            # Add header
            pdf.set_font(family="Times", style="B", size=24)
            pdf.set_text_color(100, 100, 100)
            pdf.cell(w=0, h=12, txt=row["Topic"], align='L', ln=1)

            # Add lines
            for y in range(20, 298, 10):
                pdf.line(10, y, 200, y)

            # Footer
            pdf.ln(277)
            pdf.set_font(family="Times", style="I", size=8)
            pdf.set_text_color(180, 180, 180)
            pdf.cell(w=0, h=10, txt=row["Topic"], align="R")

            for _ in range(row["Pages"] - 1):
                pdf.add_page()
                pdf.ln(265)
                pdf.set_font(family="Times", style="I", size=8)
                pdf.set_text_color(180, 180, 180)
                pdf.cell(w=0, h=10, txt=row["Topic"], align="R")
                for y in range(20, 298, 10):
                    pdf.line(10, y, 200, y)

        # Save PDF to a temporary file
        output_path = "generated_pdf.pdf"
        pdf.output(output_path)

        # Display Download Button
        with open(output_path, "rb") as pdf_file:
            st.download_button(label="Download PDF", 
                               data=pdf_file, 
                               file_name="output.pdf", 
                               mime="application/pdf")
