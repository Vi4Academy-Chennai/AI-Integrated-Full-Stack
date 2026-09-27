# pip install streamlit requests
# streamlit run frontend.py
import streamlit as st
import requests

# Set the URL of your FastAPI backend
# Adjust the port if your FastAPI runs on a different port (default is usually 8000)
API_URL = "http://127.0.0.1:8000"

st.set_page_config(page_title="ML Prediction App", page_icon="🤖", layout="centered")

st.title("🤖 Secure ML Prediction Frontend")
st.markdown("This Streamlit app connects to the FastAPI backend to make predictions.")

# --- Backend Status Check ---
st.subheader("Backend Status")
if st.button("Check Backend Status"):
    try:
        # Note: If you blocked GET requests in the previous step, this will return a 405.
        # If so, you can remove this status check or change it to a POST ping.
        response = requests.get(f"{API_URL}/")
        if response.status_code == 200:
            st.success(f"Backend is online: {response.json().get('message')}")
        else:
            st.warning(f"Backend returned status code: {response.status_code}")
    except requests.exceptions.ConnectionError:
        st.error("Failed to connect to backend. Is FastAPI running?")

st.divider()

# --- Prediction Form ---
st.subheader("Make a Prediction")
st.write("Enter the required features below:")

# Create a form so the page doesn't refresh on every key press
with st.form(key="prediction_form"):
    # TODO: Replace these with the actual inputs your ML model requires!
    feature_1 = st.number_input("Feature 1 (e.g., Age)", value=0.0)
    feature_2 = st.number_input("Feature 2 (e.g., Income)", value=0.0)
    
    # Submit button for the form
    submit_button = st.form_submit_button(label="Get Prediction")

# --- Handle API Request ---
if submit_button:
    # 1. Prepare the payload matching your FastAPI Pydantic model
    payload = {
        "feature1": feature_1,
        "feature2": feature_2
    }
    
    # 2. Make the POST request to the FastAPI predictions endpoint
    # Adjust the endpoint path ("/predictions") to match your predictions.router
    predict_endpoint = f"{API_URL}/predictions" 
    
    with st.spinner("Calculating prediction..."):
        try:
            # We use a POST request here, which perfectly aligns with your CORS configuration
            response = requests.post(predict_endpoint, json=payload)
            
            # 3. Handle the response
            if response.status_code == 201:
                result = response.json()
                st.success("Prediction successful!")
                
                # Display the result beautifully
                st.json(result)
                
                # Example of fetching a specific key if your API returns {"prediction": value}
                # st.metric(label="Predicted Value", value=result.get("prediction"))
                
            else:
                st.error(f"Error {response.status_code}: {response.text}")
                
        except requests.exceptions.ConnectionError:
            st.error("Failed to connect to the backend. Make sure your FastAPI server is running.")