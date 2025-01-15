from flask import Flask, render_template

app = Flask(__name__)

slides = [
    'slide1.html',
    'slide2.html',
    'slide3.html'
]

@app.route('/')
def index():
    return render_template('index.html', slide=slides[0])

@app.route('/slide/<int:slide_id>')
def slide(slide_id):
    if slide_id < len(slides):
        return render_template(slides[slide_id])
    else:
        return "No more slides", 404

if __name__ == '__main__':
    app.run(debug=True)
