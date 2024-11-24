import streamlit as st
import pandas as pd

# Custom CSS to style the app
def add_custom_css():
    st.markdown("""
    <style>
    /* Body styling to override Streamlit's theme */
    body {
        background-color: #f9f9f9 !important;  /* Light background */
        color: #444444;                       /* Default text color */
        font-family: 'Arial', sans-serif;     /* Clean font */
    }

    /* Main content styling */
    .main {
        background-color: #ffffff;
        padding: 2rem;
        border-radius: 15px;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    /* Header styling */
    h1 {
        color: #26a69a;                       /* Modern teal color */
        text-align: center;
        font-size: 2.5rem;
        margin-bottom: 1.5rem;
    }

    h3 {
        color: #00796b;                       /* Darker teal */
        margin-top: 1.5rem;
    }

    /* File uploader styling */
    .css-19ih76x {
        background-color: #e0f7fa !important; /* Light blue background */
        border: 2px dashed #26a69a;
        border-radius: 10px;
    }

    /* Buttons */
    button {
        background-color: #26a69a;
        color: white;
        padding: 0.8rem 2rem;
        border: none;
        border-radius: 25px;
        font-size: 1rem;
        font-weight: bold;
        cursor: pointer;
        transition: all 0.3s ease-in-out;
    }
    
    button:hover {
        background-color: #00796b;
        transform: translateY(-2px);
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
    }

    /* Table styling */
    .dataframe {
        margin-top: 2rem;
        border-radius: 10px;
        overflow: hidden;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
    }

    table {
        width: 100%;
        border-collapse: collapse;
    }

    th {
        background-color: #26a69a;
        color: white;
        padding: 1rem;
    }

    td {
        padding: 1rem;
        text-align: center;
    }

    tr:nth-child(even) {
        background-color: #f9f9f9;
    }
    </style>
    """, unsafe_allow_html=True)


# Add custom CSS for styling
add_custom_css()

# Streamlit app title and description
st.markdown("<h1>📂 Modern CSV Uploader</h1>", unsafe_allow_html=True)

st.write("""
This app allows you to upload a CSV file, preview the data, and process it. 
Enjoy the modern, clean design while managing your files effortlessly!
""")

# CSV file uploader
uploaded_file = st.file_uploader("Drag & Drop a CSV File Here", type=["csv"])

if uploaded_file is not None:
    try:
        # Read and display the CSV file
        df = pd.read_csv(uploaded_file)
        st.markdown("<h3>📊 Uploaded Data Preview</h3>", unsafe_allow_html=True)
        st.dataframe(df)
        
        # Save button
        if st.button("💾 Save Data"):
            st.success("Data has been saved successfully!")
    except Exception as e:
        st.error(f"Error loading file: {e}")
else:
    st.info("Upload a CSV file to get started.")
# import streamlit as st

# # Initialize the session state for page tracking
# if "current_page" not in st.session_state:
#     st.session_state.current_page = "Page 1"

# # Function to switch pages
# def switch_page(page):
#     st.session_state.current_page = page

# # Custom CSS for active and inactive buttons
# def add_custom_css():
#     st.markdown("""
#     <style>
#     /* Navigation bar container */
#     .nav-container {
#         display: flex;
#         justify-content: center;
#         margin-bottom: 1rem;
#     }

#     /* Button styles */
#     .nav-button {
#         padding: 0.5rem 1.5rem;
#         margin: 0 0.5rem;
#         font-size: 1rem;
#         font-weight: bold;
#         color: #ffffff;
#         border: none;
#         border-radius: 25px;
#         cursor: pointer;
#         transition: all 0.3s ease-in-out;
#     }

#     /* Active button styling */
#     .nav-button.active {
#         background-color: #26a69a;
#         box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
#     }

#     /* Inactive button styling */
#     .nav-button.inactive {
#         background-color: #b2dfdb;
#     }

#     .nav-button:hover {
#         transform: scale(1.05);
#     }
#     </style>
#     """, unsafe_allow_html=True)


# # Add the custom CSS
# add_custom_css()

# # Navigation bar
# st.markdown('<div class="nav-container">', unsafe_allow_html=True)

# # Render navigation buttons
# col1, col2 = st.columns(2)
# with col1:
#     if st.button("Page 1", key="page1"):
#         switch_page("Page 1")
# with col2:
#     if st.button("Page 2", key="page2"):
#         switch_page("Page 2")

# st.markdown("</div>", unsafe_allow_html=True)

# # Dynamically render content based on the selected page
# if st.session_state.current_page == "Page 1":
#     st.markdown('<h1 style="text-align: center; color: #26a69a;">Welcome to Page 1</h1>', unsafe_allow_html=True)
#     st.write("This is the content of Page 1.")
# elif st.session_state.current_page == "Page 2":
#     st.markdown('<h1 style="text-align: center; color: #00796b;">Welcome to Page 2</h1>', unsafe_allow_html=True)
#     st.write("This is the content of Page 2.")
