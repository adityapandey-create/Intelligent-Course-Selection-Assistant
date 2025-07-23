# Coursera Course Recommendation System
[](https://www.python.org/downloads/)
[](https://streamlit.io)
[](https://opensource.org/licenses/MIT)

A web application that suggests Coursera courses based on user interests, built with Python and Streamlit. This project leverages content-based filtering to recommend courses from a dataset of over 3,000 options.

## 🎬 Demo Video

https://github.com/user-attachments/assets/123a6485-a511-437f-8f16-78445a27239f

## 📖 About The Project

Finding the right online course can be overwhelming given the vast number of choices available. This project aims to simplify that process by providing personalized course recommendations on Coursera.

A user selects a course they like, and the system uses a content-based filtering algorithm to find and display a list of the most similar courses. The front end is a user-friendly web app built with Streamlit, featuring a modern UI with custom styling.

**This project was created by Group 3.**

## ✨ Key Features

  * **Interactive UI:** A clean and modern web interface built with Streamlit.
  * **Massive Course Selection:** Search from a dataset of over 3,000 courses from Coursera.
  * **Content-Based Filtering:** Recommendations are based on the content of the courses (like tags, description, etc.), ensuring relevance.
  * **Real-time Recommendations:** Get instant suggestions after selecting a course.
  * **Visually Appealing:** Features custom-styled cards, gradient text, and a uniform layout for a better user experience.

## 🛠️ Built With

This project utilizes the following technologies and libraries:

  * **Backend & Logic:**
      * [Python](https://www.python.org/)
      * [Pandas](https://pandas.pydata.org/) for data manipulation.
      * [NumPy](https://numpy.org/) for numerical operations.
      * [Scikit-learn](https://scikit-learn.org/) for calculating similarity.
  * **Frontend:**
      * [Streamlit](https://streamlit.io/) for creating the interactive web application.
  * **Data:**
      * [Pickle](https://docs.python.org/3/library/pickle.html) for loading the pre-processed dataset and similarity matrix.

## ⚙️ How It Works: The Recommendation Engine

The core of this project is a **Content-Based Filtering** model. Here’s a brief overview of the methodology:

1.  **Data Collection & Preprocessing:**

      * Course data (name, description, tags, etc.) was scraped or collected from Coursera.
      * The textual data for each course was combined and cleaned to create a "content corpus."

2.  **Feature Extraction (Vectorization):**

      * The textual corpus for each course was transformed into a numerical vector using a technique like **TF-IDF (Term Frequency-Inverse Document Frequency)**. This process converts text into a meaningful numerical representation where important words are given more weight.

3.  **Similarity Calculation:**

      * **Cosine Similarity** was used to calculate the similarity between every pair of course vectors. Cosine similarity measures the cosine of the angle between two vectors, with a value closer to 1 indicating higher similarity.
      * The result is a large similarity matrix (`similarity.pkl`), where each cell `(i, j)` stores the similarity score between course `i` and course `j`.

4.  **Making a Recommendation:**

      * When a user selects a course, the system looks up that course's index in the similarity matrix.
      * It then retrieves the similarity scores of that course with all other courses and sorts them in descending order.
      * The top 6 courses with the highest similarity scores (excluding the input course itself) are returned as recommendations.

## 🚀 Getting Started

To get a local copy up and running, follow these simple steps.

### Prerequisites

  * Python 3.9 or higher installed on your machine.
  * `pip` package manager.

### Installation

1.  **Clone the repository:**

    ```sh
    git clone https://github.com/your-username/your-repository-name.git
    ```

2.  **Navigate to the project directory:**

    ```sh
    cd your-repository-name
    ```

3.  **Create a `requirements.txt` file** with the following content:

    ```
    streamlit
    pandas
    numpy
    scikit-learn
    ```

4.  **Install the required packages:**

    ```sh
    pip install -r requirements.txt
    ```

5.  **Place your data files** (`courses.pkl` and `similarity.pkl`) in the root of the project directory.

6.  **Run the Streamlit app:**

    ```sh
    streamlit run main.py
    ```

    *(Make sure your main Python script is named `app.py` or change the command accordingly.)*

## ⚖️ License

Distributed under the MIT License. See `LICENSE` file for more information.

-----
