#NICHT AUF RUN!!! Im terminal eingeben: streamlit run app.py
import streamlit as st
import requests
 
API_URL = 'http://127.0.0.1:5000/items'
 
### Service fetch_items
def fetch_items():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching items : {response.status_code}")
    return []

# service fetch_item 2 by ID
def fetch_item(item_id):
    response = requests.get(f'{API_URL}/{item_id}')
    if response.status_code == 200:
        return response.json()
    st.error(f"Error fetching items : {response.status_code}")
    return None
 
### Frontend
st.title("Custom application with Backend")
 
### Fetch Items
st.subheader("Fetch Items")
if st.button("Fetch All Items"):
    items = fetch_items()
    st.write(items)

### Fetch Items
st.subheader("Fetch Item by ID")
item_id = st.number_input('Item ID', min_value=1)
if st.button("Fetch Item"):
    item = fetch_item(item_id)
    st.write(item)