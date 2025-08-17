import google.generativeai as genai
import os
from dotenv import load_dotenv

load_dotenv()
api_key=os.getenv("GENAI_API_KEY")
genai.configure(api_key=api_key)

#gemai configuration
configuration = {
    "temperature": 1,
    "top_p": 0.95,
    "top_k": 40,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain"
}

model = genai.GenerativeModel(
    model_name = 'gemini-2.5-flash',
    generation_config=configuration
)

def analyse_resume_genai(resume_content, job_description):
    prompt = f"""
    You are a professional resume analyzer. Your task is to analyze the following resume content and provide feedback based on the given job description.

    Resume Content:
    {resume_content}

    Job Description:
    {job_description}

    Task:
    - Analyze the resume against the job description.
    - Give a matching score out of 100, based on the relevance of the resume content to the job description.
    - Highlight the missing skills or experiences in the resume that are mentioned in the job description.
    - Suggest improvements to the resume to better align it with the job description.
    
    Return the result in structured formate
    Match score : XX/100
    Missing Skills :
    - ...
    Suggestions:
    - ...
    Summary:
    - ...
    """
    
    response = model.generate_content(prompt)

    return response.text
