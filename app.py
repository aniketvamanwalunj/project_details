from flask import Flask, render_template

app = Flask(__name__)

# Directly display the project details page on the home route
@app.route('/')
def project_details():
    return render_template('project_details.html')

if __name__ == '__main__':
    app.run(debug=True, port=5001)  # Specify the port here
