# import fitz # PyMuPDF manipulating pdf files
# import google.generativeai as genai
# import os 
# from dotenv import load_dotenv
# from analyse_pdf import analyse_resume_genai

# #function to extract text from pdf files
# def extract_text_from_pdf(pdf_path):
#     doc = fitz.open(pdf_path)
#     text = ""
#     for page in doc:
#         text += page.get_text()
#     return text

# pdf_path = "./VishweshResume.pdf"
# resume_content = extract_text_from_pdf(pdf_path)
# # print(extract_text_from_pdf(pdf_path))

# job_description = """
# We are hiring a Python Fullstack Developer with experience in building scalable web applications.
# - Proficiency in Python and Django/Flask
# - Experience with RESTful APIs
# - Familiarity with cloud platforms (AWS, GCP, Azure)
# - Strong understanding of database systems (SQL and NoSQL)

# """

# result = analyse_resume_genai(resume_content, job_description)
# print("Resume Analyser: \n")
# print(result)


from flask import Flask, request, jsonify, render_template
import fitz  # PyMuPDF
import os
from dotenv import load_dotenv
from analyse_pdf import analyse_resume_genai

# Load environment variables
load_dotenv()

app = Flask(__name__)

# Function to extract text from PDF
def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/analyze", methods=["POST"])
def analyze_resume():
    """
    Endpoint to analyze resume vs job description
    """
    if "resume" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400
    
    resume_file = request.files["resume"]
    job_description = request.form.get("job_description")

    if not job_description:
        return jsonify({"error": "Job description is required"}), 400

    # Save PDF temporarily
    pdf_path = "./temp_resume.pdf"
    resume_file.save(pdf_path)

    # Extract text from PDF
    resume_content = extract_text_from_pdf(pdf_path)

    # Analyze using your function
    result = analyse_resume_genai(resume_content, job_description)

    return jsonify({"analysis_result": result})


if __name__ == "__main__":
    app.run(debug=True)
