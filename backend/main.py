from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# -------------------------
# ROOT ROUTE
# -------------------------
@app.route("/")
def home():
    return jsonify({
        "status": "Backend running",
        "message": "Portfolio API is live",
        "routes": [
            "/api/about",
            "/api/skills",
            "/api/experience",
            "/api/projects",
            "/api/contact"
        ]
    })

# -------------------------
# HARDCODED DATA
# -------------------------
ABOUT = {
    "name": "Aadit Shah",
    "role": "Frontend Engineer",
    "bio": "Frontend Engineer skilled in HTML, CSS, JavaScript, and modern UI frameworks."
}

SKILLS = ["HTML5", "CSS3", "JavaScript", "React", "Git & GitHub"]

EXPERIENCE = [
    {
        "role": "Frontend Developer",
        "company": "ABC Tech Solutions",
        "duration": "2023 - Present",
        "responsibilities": [
            "Built responsive UI components",
            "Collaborated with backend teams",
            "Optimized website performance"
        ]
    }
]

PROJECTS = [
    {
        "title": "Portfolio Website",
        "description": "Personal portfolio built using HTML, CSS, and JavaScript.",
        "tech": ["HTML", "CSS", "JavaScript"]
    },
    {
        "title": "Task Manager App",
        "description": "Task management app with CRUD operations.",
        "tech": ["JavaScript"]
    }
]

CONTACT = {
    "email": "aaditshah@email.com",
    "github": "https://github.com/aaditshah",
    "linkedin": "https://linkedin.com/in/aaditshah"
}

# -------------------------
# API ROUTES
# -------------------------
@app.route("/api/about")
def about():
    return jsonify(ABOUT)

@app.route("/api/skills")
def skills():
    return jsonify(SKILLS)

@app.route("/api/experience")
def experience():
    return jsonify(EXPERIENCE)

@app.route("/api/projects")
def projects():
    return jsonify(PROJECTS)

@app.route("/api/contact")
def contact():
    return jsonify(CONTACT)

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
