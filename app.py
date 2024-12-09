import streamlit as st
import matplotlib.pyplot as plt  # type: ignore
from math import pi

# Apply LinkedIn-like white and blue theme using custom CSS
st.markdown(
    """
    <style>
    /* Background color */
    .stApp {
        background-color: #ffffff; /* White background */
    }

    /* Title Styling */
    h1 {
        color: #0077b5; /* LinkedIn blue */
    }

    /* Button Styling */
    div.stButton button {
        background-color: #0077b5; /* LinkedIn blue */
        color: white;
        border-radius: 5px;
    }

    /* Text and widget Styling */
    .css-1dp5vir, .css-1vbkfke {
        color: #0077b5; /* LinkedIn blue */
    }

    /* Message Styling */
    .custom-message {
        color: #0077b5; /* LinkedIn blue */
        font-size: 18px;
        font-weight: bold;
        margin-bottom: 20px;
    }

    /* Dropdown Styling */
    .css-1wa3eu0 {
        background-color: #f0f0f0; /* Light grey background for dropdown */
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Predefined alumni data
alumni_data = {
    'Heni Reddy': {'CGPA': 8.5, 'Skills Count': 7, 'Experience (years)': 3, 'Won Competitions': 2},
    'Pradip': {'CGPA': 9.0, 'Skills Count': 6, 'Experience (years)': 5, 'Won Competitions': 4},
    'Chris': {'CGPA': 7.8, 'Skills Count': 8, 'Experience (years)': 4, 'Won Competitions': 5},
    'Yoga Reddy': {'CGPA': 6.5, 'Skills Count': 5, 'Experience (years)': 2, 'Won Competitions': 3},
    'John Raj': {'CGPA': 6.5, 'Skills Count': 5, 'Experience (years)': 2, 'Won Competitions': 3},
    'Hari Krishan': {'CGPA': 9.5, 'Skills Count': 5, 'Experience (years)': 2, 'Won Competitions': 5},
    'Aruna': {'CGPA': 7.5, 'Skills Count': 8, 'Experience (years)': 3, 'Won Competitions': 7},
}

# Function to plot radar chart
def plot_radar(alumni1, alumni2, categories, data1, data2):
    N = len(categories)
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]
    
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))
    
    # Plot for Alumni 1
    ax.plot(angles, data1, linewidth=2, linestyle='solid', label=alumni1)
    ax.fill(angles, data1, 'b', alpha=0.1)
    
    # Plot for Alumni 2
    ax.plot(angles, data2, linewidth=2, linestyle='solid', label=alumni2)
    ax.fill(angles, data2, 'r', alpha=0.1)
    
    plt.xticks(angles[:-1], categories)
    plt.title(f'Comparison between {alumni1} and {alumni2}', size=15, color='black', y=1.1)
    ax.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

    st.pyplot(fig)

# Streamlit App
st.title("Radar Plot: Alumni Comparison")

# Custom message for Aruna
st.markdown('<p class="custom-message">Hello Aruna, who’s profile would you like to explore alongside yours?</p>', unsafe_allow_html=True)

# "Aruna" as the fixed alumni
alumni1 = 'Aruna'

# Dropdown for selecting the other alumni
alumni2 = st.selectbox("Select Alumni to explore with Aruna", options=[alumni for alumni in alumni_data.keys() if alumni != 'Aruna'])

# Categories for radar plot
categories = ['CGPA', 'Skills Count', 'Experience (years)', 'Won Competitions']

# Get data for selected alumni
data1 = list(alumni_data[alumni1].values())
data2 = list(alumni_data[alumni2].values())

# Completing the loop for radar
data1 += data1[:1]
data2 += data2[:1]

# Plot radar chart
if st.button("Generate Radar Chart"):
    plot_radar(alumni1, alumni2, categories, data1, data2)