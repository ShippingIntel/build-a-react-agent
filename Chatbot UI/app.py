from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Serve static files (for favicon and other static assets)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/operations_dsm', methods=['POST'])
def operations_dsm():
    user_message = request.json.get('message')

    # Simulated response
    response = {
        'result': f"Bot Response to '{user_message}'",
        'html_map': None  # You can send any additional HTML content here
    }

    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5005)
