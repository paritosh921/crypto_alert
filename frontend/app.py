import streamlit as st
import requests

API_URL = "http://backend:8000/api/alerts/"

st.title("Cryptocurrency Price Alert Application")

st.header("Create Price Alert")
coin = st.text_input("Coin (e.g., BTC)")
target_price = st.number_input("Target Price", min_value=0.0)
user_email = st.text_input("Your Email")

if st.button("Create Alert"):
    response = requests.post(API_URL + "create/", json={
        "coin": coin,
        "target_price": target_price,
        "user": user_email
    })
    if response.status_code == 201:
        st.success("Alert created successfully!")
    else:
        st.error("Failed to create alert.")


st.header("Existing Alerts")
response = requests.get(API_URL)
if response.status_code == 200:
    alerts = response.json()
    for alert in alerts:
        st.write(f"{alert['coin']} - ${alert['target_price']} - Status: {alert['status']}")
else:
    st.write("No alerts created.")