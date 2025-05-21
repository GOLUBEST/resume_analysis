import streamlit as st

import pandas as pd

# Load the data
data = pd.read_csv("questionDS.csv")

data['role'] = data['role'].str.strip().str.lower()  # Normalize

# Function to get random Q&A
def get_random_qa(role_input, n=10):
    role_input = role_input.strip().lower()
    filtered = data[data['role'] == role_input]

    if filtered.empty:
        return None

    return filtered.sample(n=min(n, len(filtered)))

# Streamlit UI
st.title(" Interview Questions & Answers by Role")

# Dropdown to select role
roles = sorted(data['role'].unique())
selected_role = st.selectbox("Select a role:", roles)

# Slider to select number of Q&A
num_items = st.slider("How many questions do you want to ask?", 1, 20, 10)

# Show button
if st.button("Show Questions and Answers"):
    results_df = get_random_qa(selected_role, num_items)

    if results_df is not None:
        st.subheader(f" Top {len(results_df)} Q&A for: {selected_role.title()}")

        # Loop through Q&A and display
        cnt=1
        for i, row in results_df.iterrows():
            st.markdown(f"**{cnt}. Q: {row['question']}**")
            st.markdown(f" *A: {row['answer']}*\n")
            st.markdown("---")
            cnt=cnt+1
    else:
        st.warning(" No data found for that role.")                       
