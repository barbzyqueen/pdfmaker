# PDF Maker App with Streamlit

## Description
This app allows users to generate customized PDF files from a CSV file using a simple and interactive web interface powered by Streamlit.

## Features
- Upload a CSV file.
- Generate multi-page PDFs with formatted content.
- Download the generated PDFs directly.

## Requirements
- Python 3.x
- Install dependencies with:
  ```bash
  pip install -r requirements.txt

## Setup Instructions

Follow these steps to set up and run the project locally:

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <project-folder>
   
2. **Create and Activate a Virtual Environment**:

   On macOS/Linux:
   - python3 -m venv pdf-venv
   - source pdf-venv/bin/activate

   On Windows:
   - python -m venv pdf-venv
   - pdf-venv\Scripts\activate
     
3. **Install Dependencies**:
   
   Install the required packages from the requirements.txt file:

   pip install -r requirements.txt

4. **Run the Application**:

   Start the Streamlit application:

   streamlit run pdfmaker_app.py

5. **Open your browser**:

   The application will open automatically in your default web browser. If it doesn’t, visit:

   http://localhost:8501

7. **Use the application**:
   
   - Upload your CSV file using the interface provided.
   - Generate and download your custom PDF file.
   
**Note:** Ensure you have Python 3.7 or higher installed on your machine to run this project.
