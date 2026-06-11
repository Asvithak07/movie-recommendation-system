Movie Recommendation System

Overview:
This project is a movie recommendation system built using collaborative filtering and Singular Value Decomposition (SVD). 
The model predicts user ratings for movies and generates personalized movie recommendations based on historical rating data.
The application is deployed using Flask and allows users to receive movie recommendations through a simple web interface.

Dataset:
The project uses the following datasets:
* movies_metadata.csv
* ratings_small.csv
These datasets contain movie information and user ratings used for training and evaluation.

Features:
* Data cleaning and preprocessing
* Collaborative filtering-based recommendation system
* SVD model training using the Surprise library
* User rating prediction
* Top movie recommendation generation
* Flask-based web application

Technologies Used:
* Python
* Pandas
* NumPy
* Surprise (SVD Algorithm)
* Flask

Project Workflow:
1. Load movie metadata and user ratings datasets.
2. Perform data cleaning and preprocessing.
3. Convert rating data into Surprise library format.
4. Train the SVD collaborative filtering model.
5. Evaluate model performance.
6. Generate rating predictions for users.
7. Recommend movies based on predicted ratings.
8. Deploy the application using Flask.

Project Structure:
movie-recommendation-system/
├── app.py
├── requirements.txt
├── svd_model.pkl
├── datasets/
└── templates/

Sample Output:
Predicted Rating
Predicted rating for User 1 and Movie 31: 2.21

Top Recommended Movies:
* While You Were Sleeping
* The Sicilian Clan
* The 39 Steps
* Amélie
* Nell
* Edward Scissorhands

Future Improvements:
* Content-based recommendation system
* Hybrid recommendation model
* Improved user interface
* Real-time recommendation updates

Author:
Asvithaa K
Data Analyst | Power BI Developer | Python Developer
