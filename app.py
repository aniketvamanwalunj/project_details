from flask import Flask, render_template

app = Flask(__name__)

# Directly display the project details page on the home route
@app.route('/')
def project_details():
    return render_template('project_details.html')

if __name__ == '__main__':
    # Directly specify the port here
    app.run(debug=True, host='0.0.0.0', port=5001)
