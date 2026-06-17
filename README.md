# 🎬 Movie Recommendation System

A personalized Movie Recommendation System built using Collaborative Filtering and Singular Value Decomposition (SVD). The application predicts user ratings for movies and recommends films based on historical user preferences.

The recommendation engine is deployed through a Flask web application, allowing users to receive personalized movie suggestions through a simple and interactive interface.

---

## 📌 Overview

Recommendation systems are widely used by platforms such as Netflix, Amazon, Spotify, and YouTube to improve user engagement and content discovery.

This project implements a collaborative filtering recommendation engine that learns user preferences from historical rating data and predicts ratings for unseen movies. Based on these predictions, the system generates personalized movie recommendations.

---

## 🚀 Features

* Personalized movie recommendations
* Collaborative Filtering approach
* Singular Value Decomposition (SVD) model
* User rating prediction
* Movie ranking based on predicted ratings
* Flask-based web application
* Pre-trained recommendation model

---

## 📊 Dataset

The project uses the following datasets:

### movies_metadata.csv

Contains movie-related information such as:

* Movie Title
* Genres
* Overview
* Release Information
* Popularity Metrics

### ratings_small.csv

Contains:

* User IDs
* Movie IDs
* Ratings
* Timestamps

These datasets are used to train and evaluate the recommendation model.

---

## 🛠️ Technology Stack

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Machine Learning

* Surprise Library
* Singular Value Decomposition (SVD)

### Web Framework

* Flask

### Model Persistence

* Pickle

---

## ⚙️ Project Workflow

1. Load movie metadata and user ratings datasets
2. Clean and preprocess data
3. Convert rating data into Surprise dataset format
4. Train collaborative filtering model using SVD
5. Evaluate recommendation performance
6. Predict user ratings for unseen movies
7. Rank movies based on predicted ratings
8. Generate top movie recommendations
9. Deploy recommendation engine using Flask

---

## 🧠 Recommendation Algorithm

### Collaborative Filtering

The system learns user preferences from historical ratings and identifies hidden relationships between users and movies.

Instead of relying on movie content, the model recommends movies based on patterns observed in user behavior.

### Singular Value Decomposition (SVD)

The recommendation engine uses SVD from the Surprise library.

Key benefits:

* Handles sparse rating matrices effectively
* Learns latent user preferences
* Generates personalized recommendations
* Improves rating prediction accuracy

---

## 📂 Project Structure

```text
movie-recommendation-system/
│
├── datasets/
│   ├── movies_metadata.csv
│   └── ratings_small.csv
│
├── templates/
├── app.py
├── svd_model.pkl
├── requirements.txt
└── README.md
```

## ▶️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/movie-recommendation-system.git
cd movie-recommendation-system
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run Application

```bash
python app.py
```

The Flask application will start locally.

---

## 🎯 Sample Prediction

### Predicted Rating

User ID: 1

Movie ID: 31

Predicted Rating:

```text
2.21
```

### Recommended Movies

* While You Were Sleeping
* The Sicilian Clan
* The 39 Steps
* Amélie
* Nell
* Edward Scissorhands

---

## 🌟 Real-World Applications

* Movie Streaming Platforms
* OTT Recommendation Engines
* Music Recommendation Systems
* E-Commerce Product Recommendations
* Personalized Content Delivery

---

## 📈 Future Improvements

* Content-Based Recommendation System
* Hybrid Recommendation Model
* Deep Learning Recommendation Engine
* User Authentication
* Real-Time Recommendation Updates
* Cloud Deployment
* Enhanced User Interface

---

## 👩‍💻 Author

**Asvithaa K**

Data Science & Machine Learning Enthusiast

---

## ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
