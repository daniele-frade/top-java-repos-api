
# API - Top 5 Java Repositories ⭐

This is a **simple and educational** project built with Python and the Flask framework, designed to demonstrate how to create a REST API from scratch. The focus is on learning, serving as a guide for beginners or for explaining basic concepts in technical interviews.

## What does this project do?

This API queries the [GitHub public API](https://docs.github.com/en/rest/search?apiVersion=2022-11-28#search-repositories) and returns the **top 5 Java repositories with the most stars**. The result is a simplified JSON list containing:

- Repository name
- Owner
- Number of stars
- Repository URL

## How does it work?

1. Flask creates a local web server.
2. When accessing the `/api/top-java-repos` endpoint, the application makes a request to the GitHub API searching for the most popular Java repositories.
3. The data is processed and only the most important information is returned as JSON.

## How to run the project

1. **Clone this repository:**
   ```sh
   git clone https://github.com/your-username/top-java-repos-api.git
   cd top-java-repos-api
   ```
2. **Create a virtual environment:**
   ```sh
   python -m venv venv
   ```
3. **Activate the virtual environment:**
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
4. **Install the dependencies:**
   ```sh
   pip install -r requirements.txt
   ```
5. **Run the application:**
   ```sh
   python app.py
   ```
6. **Access in your browser:**
   [http://127.0.0.1:5000/api/top-java-repos](http://127.0.0.1:5000/api/top-java-repos)

You will see a list of the 5 most popular Java repositories on GitHub in JSON format.

## Why is this project useful for learning?

- The code is fully commented, explaining each step.
- Shows how to consume external APIs and handle responses.
- Demonstrates how to create routes and return JSON with Flask.
- Easy to run, modify, and expand.

---

Sinta-se à vontade para usar este projeto como base para estudos, entrevistas ou para criar APIs mais avançadas!
