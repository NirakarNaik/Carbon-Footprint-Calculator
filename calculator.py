#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#!/usr/bin/env python
# coding: utf-8
import streamlit as st

def calculate_carbon_footprint():
    """Calculate carbon footprint and provide recommendation."""
    st.title("Carbon Footprint Calculator")
    st.write("Please answer the following questions to estimate your carbon footprint.")

    try:
        num_people = st.number_input("How many people are in your household?", min_value=1, step=1)
        electricity_usage = st.number_input("What is your monthly electricity usage in kilowatt-hours (kWh)?",
                                            min_value=0.0, format="%.2f")
        km_driven = st.number_input("How many kilometers do you drive per month?", min_value=0.0, format="%.2f")
        public_transport_km = st.number_input("How many kilometers do you use public transportation per month?",
                                              min_value=0.0, format="%.2f")
        flights_taken = st.number_input("How many flights do you take per year?", min_value=0, step=1)

        if st.button("Calculate Carbon Footprint"):
            # Constants for carbon emissions
            electricity_emission_factor = 0.8  # kg CO2 per kWh
            car_emission_factor = 0.646  # kg CO2 per kilometer
            public_transport_emission_factor = 0.15  # kg CO2 per kilometer
            flight_emission_factor = 0.24  # kg CO2 per kilometer

            # Calculate carbon footprint
            electricity_emissions = electricity_usage * electricity_emission_factor
            car_emissions = km_driven * car_emission_factor
            public_transport_emissions = public_transport_km * public_transport_emission_factor
            flight_emissions = flights_taken * flight_emission_factor * 1000  # convert g CO2 to kg CO2

            total_emissions = (electricity_emissions +
                               car_emissions +
                               public_transport_emissions +
                               flight_emissions) * num_people

            # Print results
            st.write(f"Your estimated carbon footprint is: {total_emissions:.2f} kg CO2e per month")

            # Calculate number of trees needed to offset carbon footprint
            trees_needed = total_emissions / 25  # One tree absorbs approximately 25 kg of CO2 per year
            st.write(f"To offset your carbon footprint, you would need to plant {trees_needed:.2f} trees per month.")

            # Link to recommendations app with updated IP address
            st.write("\nFor personalized recommendations to reduce your carbon footprint, visit the [Recommendations App](http://192.168.29.241:8502).")

    except ValueError:
        st.error("Invalid input. Please enter numeric values where expected.")
    except Exception as e:
        st.error(f"An error occurred: {e}")

if __name__ == "__main__":
    calculate_carbon_footprint()

