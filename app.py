from flask import Flask, render_template, request
import pacparser

app = Flask(__name__)

# Initialize pacparser
pacparser.init()

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Check if the user submitted a new PAC file
        if 'file' in request.files:
            # Get the uploaded PAC file
            uploaded_file = request.files['file']
            pac_file_content = uploaded_file.read().decode('utf-8')

            # Parse the new PAC file
            pacparser.parse_pac_string(pac_file_content)

        # Get the user-provided URL
        url_to_test = request.form['url']

        # Find the proxy configuration for the URL
        proxy_config = pacparser.find_proxy(url_to_test)

        return render_template('result.html', proxy_config=proxy_config, query=url_to_test)

    return render_template('index.html')

# Results page
@app.route('/result', methods=['POST'])
def result():
    # Get the user-provided URL
    url_to_test = request.form['query']

    # Find the proxy configuration for the URL
    proxy_config = pacparser.find_proxy(url_to_test)

    return render_template('result.html', proxy_config=proxy_config, query=url_to_test)

if __name__ == '__main__':
    app.run(host='localhost', debug=True)
