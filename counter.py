import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .circle {
        height: 150px;
        width: 150px;
        background-color: #ffffff;
        border-radius: 50%;
        border: 4px solid #4CAF50;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
        font-size: 40px;
        font-weight: bold;
    }
    .arrow-btn {
        font-size: 60px !important;
        padding: 0 !important;
        margin: 0 20px !important;
        border: none !important;
        background: none !important;
        color: #4CAF50 !important;
    }
    .reset-btn {
        margin: 20px auto;
        width: 100px;
        border-radius: 20px !important;
        background-color: #ff4444 !important;
        color: white !important;
    }
    .container {
        display: flex;
        justify-content: center;
        align-items: center;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'count' not in st.session_state:
    st.session_state.count = 0

# Function to update count
def update_count(change):
    new_count = st.session_state.count + change
    if new_count >= 0:  # Prevent negative numbers
        st.session_state.count = new_count

# Reset function
def reset_count():
    st.session_state.count = 0

# Main layout
col1, col2, col3 = st.columns([1, 2, 1])

with col1:
    if st.button('▼', key='down', on_click=update_count, args=(-1,)):
        pass

with col2:
    st.markdown(f"<div class='circle'>{st.session_state.count}</div>", unsafe_allow_html=True)

with col3:
    if st.button('▲', key='up', on_click=update_count, args=(1,)):
        pass

# Reset button
st.button('Reset', on_click=reset_count, key='reset', use_container_width=True)

# Mobile responsiveness
st.markdown("""
    <style>
    @media (max-width: 600px) {
        .circle {
            height: 100px;
            width: 100px;
            font-size: 30px;
        }
        .arrow-btn {
            font-size: 40px !important;
            margin: 0 10px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)