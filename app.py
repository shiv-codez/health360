"""Health360 - Flask web app that embeds the Tableau Public dashboard and story."""
from flask import Flask, render_template

app = Flask(__name__)

# Published Tableau Public workbook
TABLEAU_PROFILE = "https://public.tableau.com/app/profile/shivam.singh2218"
DASHBOARD_URL = f"{TABLEAU_PROFILE}/viz/Health360_17932068115940/Health360Dashboard"
STORY_URL = f"{TABLEAU_PROFILE}/viz/Health360_17932068115940/Health360Story"


@app.context_processor
def inject_links():
    return {"dashboard_url": DASHBOARD_URL, "story_url": STORY_URL}


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():
    return render_template("dashboard.html")


@app.route("/story")
def story():
    return render_template("story.html")


if __name__ == "__main__":
    app.run(debug=True)
