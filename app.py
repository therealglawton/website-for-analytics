from flask import Flask, render_template
from flask_frozen import Freezer

app = Flask(__name__)
freezer = Freezer(app)

# Predefined posts (replace with your real content)
posts = [
    {'title': 'Welcome to My Blog', 'content': 'This is my first post!'},
    {'title': 'Another Blog Post', 'content': 'Here’s some more content.'}
]

@app.route('/')
def home():
    return render_template('home.html', posts=posts)

@app.route('/post/<int:post_id>')
def post(post_id):
    if 0 <= post_id < len(posts):
        return render_template('post.html', post=posts[post_id])
    return "Post not found", 404

if __name__ == '__main__':
    freezer.freeze()  # Generate static files
    app.run(debug=True)
