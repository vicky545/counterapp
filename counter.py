import streamlit as st

# Custom CSS for styling
st.markdown("""
    <style>
    .circle {
        height: 150px;
        width: 150px;
        background-color: transparent;
        border-radius: 50%;
        border: 4px solid #4CAF50;
        display: flex;
        align-items: center;
        justify-content: center;
        margin: 20px auto;
        font-size: 40px;
        font-weight: bold;
        color: #4CAF50;
    }
    .button-container {
        display: flex;
        justify-content: center;
        gap: 20px;
        margin-top: 20px;
    }
    .arrow-btn {
        height: 150px !important;
        width: 150px !important;
        font-size: 80px !important;
        padding: 0 !important;
        border: none !important;
        background: none !important;
        color: #4CAF50 !important;
        border-radius: 50% !important;
        display: flex !important;
        align-items: center;
        justify-content: center;
    }
    .reset-btn {
        margin: 30px auto;
        width: 100px;
        border-radius: 20px !important;
        background-color: #ff4444 !important;
        color: white !important;
    }
    
    /* Dark mode adjustments */
    [data-testid="stAppViewContainer"] .stDark .circle {
        color: orange !important;
        border-color: orange !important;
    }
    [data-testid="stAppViewContainer"] .stDark .arrow-btn {
        color: orange !important;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize session state
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'input_count' not in st.session_state:
    st.session_state.input_count = 0

# Function to update count
def update_count(change):
    new_count = st.session_state.count + change
    if new_count >= 0:
        st.session_state.count = new_count

# Reset function
def reset_count():
    st.session_state.count = 0

# Main layout
st.markdown('<div class="container">', unsafe_allow_html=True)

# User input for setting count
col1, col2 = st.columns([3, 1])
with col1:
    st.number_input(
        "Set counter value", 
        value=st.session_state.input_count, 
        step=1, 
        key='input_count'
    )
with col2:
    if st.button("Set", use_container_width=True):
        st.session_state.count = st.session_state.input_count

# Circle display
st.markdown(f"<div class='circle'>{st.session_state.count}</div>", unsafe_allow_html=True)

# Arrow buttons container
st.markdown('<div class="button-container">', unsafe_allow_html=True)
col_up, col_down = st.columns(2)
with col_up:
    st.button('▲', key='up', on_click=update_count, args=(1,), use_container_width=True)
with col_down:
    st.button('▼', key='down', on_click=update_count, args=(-1,), use_container_width=True)
st.markdown('</div>', unsafe_allow_html=True)

# Reset button
st.button('Reset', on_click=reset_count, key='reset', use_container_width=True)

st.markdown('</div>', unsafe_allow_html=True)

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
            height: 100px !important;
            width: 100px !important;
            font-size: 50px !important;
        }
    }
    </style>
""", unsafe_allow_html=True)