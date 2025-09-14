# Carbon-Footprint-Calculator

A capstone project that calculates an individual’s carbon footprint and recommends ways to reduce it using Natural Language Processing (NLP).

- Project Overview:
This tool aims to promote sustainability by making carbon footprint tracking simple and interactive.
Users answer a few questions about their lifestyle.
The system calculates their footprint using constants and official government data.
On the Recommendation Page (I have used chatgpt to get recommendations on different keywords) , users can ask any query (NLP-powered) to get personalized suggestions for reducing their emissions.

- Tech Stack:
Python
NLP (Natural Language Processing)
Streamlit for the web app
Pandas for data handling

- Dataset:
Data sourced from official government websites.
Challenge: Emission data was available based on vehicle CC (engine capacity) instead of direct usage.
Solution: Averaged values for estimation → achieved 97–98% accuracy after cross-checking with an established calculator.

- Features:
Calculates carbon footprint based on user inputs
Interactive Q&A for emission-reduction recommendations
Easy-to-use web interface (Streamlit)
High accuracy despite dataset limitations

- Potential Impact:
Individuals: Raise awareness & provide actionable steps to reduce emissions.
Companies & Policymakers: Can scale up to track footprints and guide greener strategies.
