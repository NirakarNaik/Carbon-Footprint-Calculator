#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
import streamlit as st
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Define extended recommendations
recommendation = {
    'reduce_energy_use': [
        "Turn off lights and electronics when not in use.",
        "Use energy-efficient appliances and LED bulbs.",
        "Insulate your home to reduce heating and cooling needs.",
        "Consider installing solar panels to generate renewable energy.",
        "Use programmable thermostats to optimize heating and cooling."
    ],
    'use_sustainable_transport': [
        "Opt for public transportation or carpooling.",
        "Consider biking or walking for short distances.",
        "Use electric or hybrid vehicles if possible.",
        "Plan and combine trips to reduce overall travel.",
        "Maintain your vehicle regularly to improve fuel efficiency."
    ],
    'reduce_waste': [
        "Recycle and compost waste to minimize landfill use.",
        "Avoid single-use plastics and opt for reusable items.",
        "Purchase products with minimal or eco-friendly packaging.",
        "Donate items you no longer need instead of throwing them away.",
        "Implement a zero-waste lifestyle by reducing, reusing, and recycling."
    ],
    'save_water': [
        "Fix leaks in taps and toilets to prevent water wastage.",
        "Use water-saving fixtures and appliances.",
        "Take shorter showers and turn off the tap while brushing your teeth.",
        "Collect rainwater for gardening and other non-potable uses.",
        "Water your garden early in the morning or late in the evening to minimize evaporation."
    ],
    'conserve_resources': [
        "Opt for digital documents instead of printing.",
        "Use energy-efficient appliances and reduce water usage.",
        "Support and buy products made from sustainable materials.",
        "Avoid excessive use of disposable products.",
        "Participate in or support conservation efforts in your community."
    ]
}

# Define stopwords and punctuation
stop_words = set(stopwords.words('english'))
punctuation = set(string.punctuation)

def preprocess_text(text):
    """Tokenize and remove stopwords and punctuation from the text."""
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word not in stop_words and word not in punctuation]
    return filtered_tokens

def match_keywords(tokens):
    """Match tokens with predefined keywords and return relevant categories."""
    keywords = {
        'energy': 'reduce_energy_use',
        'transport': 'use_sustainable_transport',
        'waste': 'reduce_waste',
        'recycle': 'reduce_waste',
        'plastic': 'reduce_waste',
        'car': 'use_sustainable_transport',
        'bike': 'use_sustainable_transport',
        'water': 'save_water',
        'leak': 'save_water',
        'appliance': 'conserve_resources',
        'resources': 'conserve_resources',
        'sustainable': 'conserve_resources'
    }

    matched_categories = set()

    for token in tokens:
        if token in keywords:
            matched_categories.add(keywords[token])

    return matched_categories

def get_recommendation(user_input):
    """Generate recommendation based on user input."""
    tokens = preprocess_text(user_input)

    matched_categories = match_keywords(tokens)

    if not matched_categories:
        return ["I'm sorry, I couldn't find specific recommendations. Try asking about energy, transport, "
                "waste reduction, water conservation, or resource conservation."]

    results = []
    for category in matched_categories:
        results.append(f"To {category.replace('_', ' ')}:")
        results.extend(recommendation[category])

    return results

def show_recommendations():
    """Show recommendations based on user input."""
    st.title("Recommendations to Reduce Your Carbon Footprint")
    st.write("Enter your query below to get personalized recommendations.")

    user_input = st.text_input("Enter your query about reducing your carbon footprint (e.g., 'How can I reduce energy use?'):")
    if user_input:
        recommendations = get_recommendation(user_input)
        st.write("\n".join(recommendations))

if __name__ == "__main__":
    show_recommendations()

