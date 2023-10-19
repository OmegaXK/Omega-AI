from flask import Flask, render_template

app = Flask(__name__, template_folder='html_templates',
            static_folder='static_files')

@app.route('/')
def home():
    """This is the home page."""
    return render_template('home.html')

@app.route('/about')
def about():
    """This is the about page."""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """This is the contact page."""
    return render_template('contact.html')

@app.route('/play')
def play():
    """This is the play page."""
    return render_template('play.html')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5001)