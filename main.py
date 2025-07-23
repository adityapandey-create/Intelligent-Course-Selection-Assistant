# <==== Importing Dependencies ====>
import os
import pickle
import streamlit as st
import numpy as np
import pandas as pd

# <==== Page Configuration ====>
# Set page configuration for a wider layout and a more professional look.
st.set_page_config(
    page_title="Coursera Course Recommender",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="auto"
)

# <==== Custom CSS for Styling ====>
# Inject custom CSS for uniform card sizes.
st.markdown("""
<style>
    /* General Styles */
    .stApp {
        background-color: #f0f2f6;
    }

    /* Gradient Title */
    .title {
        font-size: 2.8rem;
        font-weight: bold;
        text-align: center;
        padding-top: 20px;
        background: -webkit-linear-gradient(45deg, #0056d2, #4A90E2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
    }

    /* Gradient Subtitle */
    .subtitle {
        font-size: 1.2rem;
        text-align: center;
        margin-bottom: 30px;
        background: -webkit-linear-gradient(45deg, #006400, #50C878);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        font-weight: 500;
    }

    /* Visible "Courses similar to..." heading */
    h3 {
        color: #1e1e1e !important;
        text-align: center;
    }

    /* --- CHANGED FOR UNIFORM CARD SIZE --- */
    .course-card {
        background-color: #ffffff;
        border-radius: 10px;
        padding: 20px;
        margin: 10px 0;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
        transition: all 0.3s ease-in-out;
        display: flex;
        flex-direction: column;
        justify-content: space-between;
        min-height: 160px; /* This is the key change! */
    }
    .course-card:hover {
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        transform: translateY(-5px);
    }
    .course-title {
        font-size: 1.2rem;
        font-weight: bold;
        color: #333333;
        margin-bottom: 10px;
    }
    .course-link {
        display: inline-block;
        background-color: #0056d2;
        color: #ffffff;
        padding: 10px 20px;
        border-radius: 5px;
        text-decoration: none;
        font-weight: bold;
        text-align: center;
        margin-top: 15px;
    }
    .course-link:hover {
        background-color: #0041a8;
        color: #ffffff;
    }

    /* Footer */
    .footer {
        text-align: center;
        padding: 20px 0;
        margin-top: 40px;
        color: #4f4f4f;
        font-size: 0.9rem;
    }
</style>
""", unsafe_allow_html=True)
# <==== Load Data ====>
# Load the course data and similarity matrix.
# It's good practice to cache data loading for performance.
@st.cache_data
def load_data():
    try:
        courses_df = pd.read_pickle('courses.pkl')
        similarity_matrix = pd.read_pickle('similarity.pkl')
        return courses_df, similarity_matrix
    except FileNotFoundError:
        st.error("Data files (courses.pkl, similarity.pkl) not found. Please ensure they are in the correct directory.")
        return None, None

courses_list, similarity = load_data()

# <==== Recommendation Function ====>
def recommend(course):
    """
    Recommends courses similar to the selected course.
    Returns a list of dictionaries, each containing the name and URL of a recommended course.
    """
    try:
        index = courses_list[courses_list['course_name'] == course].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])

        recommended_courses = []
        for i in distances[1:7]:  # Get the top 6 similar courses
            course_name = courses_list.iloc[i[0]]['course_name']
            course_url = courses_list.iloc[i[0]]['course_url']
            recommended_courses.append({'name': course_name, 'url': course_url})
        return recommended_courses
    except IndexError:
        return [] # Return empty list if course not found

# <==== Main Application ====>
if courses_list is not None and similarity is not None:
    # Page Title and Introduction
    st.markdown("<h1 class='title'>Coursera Course Recommender</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>Discover new courses based on your interests. Built by Group 3.</p>", unsafe_allow_html=True)

    # --- Main Content Area ---
    main_container = st.container()
    with main_container:
        col1, col2, col3 = st.columns([1,2,1]) # Center the selection box
        with col2:
            # Course Selection
            course_list_names = courses_list['course_name'].values
            selected_course = st.selectbox(
                "**Select a course you've enjoyed:**",
                course_list_names,
                index=0, # Default selection
                help="Start typing to search for a course from our dataset of over 3,000 courses."
            )

            # Recommendation Button
            if st.button('✨ Find Similar Courses'):
                if selected_course:
                    st.write("---") # Separator
                    st.markdown(f"### Courses similar to **{selected_course}**:")

                    recommended_courses = recommend(selected_course)

                    if recommended_courses:
                        # Display recommendations in a 3-column grid
                        cols = st.columns(3)
                        for i, course in enumerate(recommended_courses):
                            with cols[i % 3]:
                                st.markdown(f"""
                                <div class="course-card">
                                    <div class="course-title">{course['name']}</div>
                                    <a href="{course['url']}" target="_blank" class="course-link">Go to Course</a>
                                </div>
                                """, unsafe_allow_html=True)
                    else:
                        st.warning("Could not find any recommendations for this course.")
                else:
                    st.error("Please select a course first.")

    # --- Footer ---
    st.markdown("""
    <div class="footer">
        <p>Copyright © Coursera and Respective Course Owners</p>
    </div>
    """, unsafe_allow_html=True)