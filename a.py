import os
import streamlit as st
import google.generativeai as genai

# Set Gemini API key from environment variable
genai.configure(api_key="AIzaSyB9G2dNtdwZrvzfRfDTVpJT-k1zZgo-Huc")

# Load the Gemini model
model = genai.GenerativeModel("gemini-pro")

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

        response = model.generate_content(prompt)
        notice_text = response.text

    st.success("Legal notice drafted!")
    st.markdown("### ✉️ Drafted Legal Notice")
    st.text_area("Generated Legal Notice", notice_text, height=400)
    st.download_button("📥 Download as .txt", notice_text, file_name="legal_notice.txt")

