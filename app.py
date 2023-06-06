from flask import Flask, render_template, request
import pacparser

app = Flask(__name__)

# Home page
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the uploaded PAC file
        uploaded_file = request.files['file']
        pac_file_content = uploaded_file.read().decode('utf-8')

        # Get the user-provided URL
        url_to_test = request.form['url']

        # Initialize pacparser and parse the PAC file
        pacparser.init()
        pacparser.parse_pac_string(pac_file_content)

        # Find the proxy configuration for the URL
        proxy_config = pacparser.find_proxy(url_to_test)

        return render_template('result.html', proxy_config=proxy_config)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='localhost',debug=True)
