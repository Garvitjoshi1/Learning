from flask import Flask, render_template

app = Flask(__name__)
post = [
    {
        "author": "Garvit Joshi",
        'title': 'First Blog',
        'content': "Blog's upcoming",
        'date_posted': 'June 6, 2026'
    },
    {
        "author": "Garvit Joshi",
        'title': 'Second Blog',
        'content': "Blog is here",
        'date_posted': 'June 9, 2026'
    }
]

@app.route("/")
def hello():
    return "<H1>Hello World</H1>"

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/home")
def home():
    return render_template('home.html', posts=post)

if __name__ == "__main__":
    app.run(debug=True)
