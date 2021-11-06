from flask import Flask, render_template

app = Flask(__name__,  template_folder='templates') #reference this file

@app.route('/') # maps url to the following function
def index():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)