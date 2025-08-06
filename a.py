import os
import streamlit as st
import requests
# Set Gemini API key from environment variable
# genai.configure(api_key="AIzaSyB9G2dNtdwZrvzfRfDTVpJT-k1zZgo-Huc")

# Load the Gemini model
# model = genai.GenerativeModel(model_name="models/gemini-1.5-pro")
API_URL = "https://generativelanguage.googleapis.com/v1/models/gemini-1.5-flash:generateContent"

headers = {
    "Content-Type": "application/json",
    "x-goog-api-key": "AIzaSyB9G2dNtdwZrvzfRfDTVpJT-k1zZgo-Huc"
}
# App UI
st.set_page_config(page_title="Legal Notice Generator")
st.title("📄 Legal Notice Generator")
st.markdown("Fill in the details below to generate a legal notice draft:")

# Form inputs
with st.form("legal_notice_form"):
    your_name = st.text_input("Your Full Name")
    opponent_name = st.text_input("Opponent's Full Name")
    issue = st.text_area("Issue Description")
    incident_date = st.date_input("Date of Incident")
    remedy = st.text_area("Remedy or Action Demanded")
    jurisdiction = st.text_input("Jurisdiction (City, Court, etc.)")
    submitted = st.form_submit_button("Generate Notice")

# Generate notice
print(submitted, "submitted")
if submitted:
    with st.spinner("Drafting legal notice..."):
        prompt = f"""
        You are a legal professional drafting a formal legal notice.

        Details:
        - From: {your_name}
        - To: {opponent_name}
        - Issue: {issue}
        - Date of Incident: {incident_date.strftime('%d %B %Y')}
        - Remedy Sought: {remedy}
        - Jurisdiction: {jurisdiction}

        Please draft a legally appropriate notice in formal tone.
        """

        data = {
            "contents": [
                {
                    "parts": [{"text": prompt}]
                }
            ]
        }

    response = requests.post(API_URL, headers=headers, json=data)
    print(response.status_code, response.text, "response status code and text")
    content = response.json()
    notice_text = content["candidates"][0]["content"]["parts"][0]["text"]

    st.success("Legal notice drafted!")
    st.markdown("### ✉️ Drafted Legal Notice")
    st.text_area("Generated Legal Notice", notice_text, height=400)
    st.download_button("📥 Download as .txt", notice_text, file_name="legal_notice.txt")

