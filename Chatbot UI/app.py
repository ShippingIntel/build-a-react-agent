from flask import Flask, render_template, request, jsonify
import logging

app = Flask(__name__)

# Serve static files (for favicon and other static assets)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

# Set up logging
logging.basicConfig(level=logging.DEBUG)

@app.route('/')
def home():
    app.logger.debug('Rendering home page')
    return render_template('index.html')

@app.route('/operations_dsm', methods=['POST'])
def operations_dsm():
    user_message = request.json.get('message')
    app.logger.debug(f'Received message: {user_message}')

    # Simulated response
    response = {
        'result': f"Bot Response to '{user_message}'",
        'html_map': None  # You can send any additional HTML content here
    }

    app.logger.debug(f'Sending response: {response}')
    return jsonify(response)

if __name__ == '__main__':
    app.run(port=5005)
