 # Step 1: Import the necessary libraries
# - Flask to create our web server
# - jsonify to format our response as JSON
# - requests to make the call to the GitHub API
from flask import Flask, jsonify
import requests

 # Step 2: Create the main Flask app instance
app = Flask(__name__)

# Step 3: Define the route (endpoint) that will return the repositories
# The route will be '/api/top-java-repos' and will only accept GET requests
@app.route('/api/top-java-repos', methods=['GET'])
def get_top_java_repos():
    # This is the main body of our logic

    # Step 4.1: Define the base URL for the GitHub search API
    GITHUB_API_URL = 'https://api.github.com/search/repositories'

    # Step 4.2: Define the search parameters
    # - q: the search query (Java language)
    # - sort: the sorting criteria (stars)
    # - order: the order (descending)
    params = {
        'q': 'language:java',
        'sort': 'stars',
        'order': 'desc'
    }

    # Step 4.3: Make the GET request to GitHub
    response = requests.get(GITHUB_API_URL, params=params)

    # Step 5.1: Get the response data in JSON format
    data = response.json()

    # Step 5.2: Access the list of repositories, which is in the 'items' key
    repositories = data.get('items', [])

    # Step 5.3: Create an empty list to store our simplified results
    top_repos = []

    # Step 6.1: Loop through the first 5 results to simplify
    for repo in repositories[:5]:
    # Step 6.2: For each repo, create a dictionary with the information we want
        repo_info = {
            'name': repo['name'],
            'owner': repo['owner']['login'],
            'stars': repo['stargazers_count'],
            'url': repo['html_url']
        }
    # Step 6.3: Add the dictionary to our results list
        top_repos.append(repo_info)

    # Step 7: Return the list of simplified repositories in JSON format
    return jsonify(top_repos)

 # Step 8: Code block to run the app when the script is executed directly
if __name__ == '__main__':
    app.run(debug=True)
