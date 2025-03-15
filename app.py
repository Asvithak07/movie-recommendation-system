from flask import Flask, request, jsonify, render_template
import pandas as pd
import pickle
from surprise import Dataset, Reader

# Load trained SVD model
with open("svd_model.pkl", "rb") as model_file:
    svd = pickle.load(model_file)

# Load datasets
movies = pd.read_csv("movies_metadata.csv", low_memory=False)[["id", "title"]]
movies = movies.rename(columns={"id": "movieId"})
movies["movieId"] = pd.to_numeric(movies["movieId"], errors="coerce").dropna().astype(int)

# Flask app
app = Flask(__name__)

# Serve the HTML page
@app.route("/")
def home():
    return render_template("index.html")

# Recommendation function
def recommend_movies(user_id, num_recommendations=10):
    movie_ids = movies["movieId"].unique()
    predictions = [svd.predict(user_id, movie_id).est for movie_id in movie_ids]
    recommendations = pd.DataFrame({"movieId": movie_ids, "predicted_rating": predictions})
    recommendations = recommendations.sort_values(by="predicted_rating", ascending=False)
    top_recommendations = recommendations.head(num_recommendations).merge(movies, on="movieId")
    return top_recommendations[["title", "predicted_rating"]].to_dict(orient="records")

# API endpoint
@app.route("/recommend", methods=["GET"])
def recommend():
    user_id = int(request.args.get("user_id", 1))
    num_recommendations = int(request.args.get("num_recommendations", 10))
    recommendations = recommend_movies(user_id, num_recommendations)
    return jsonify(recommendations)

if __name__ == "__main__":
    app.run(debug=True)
