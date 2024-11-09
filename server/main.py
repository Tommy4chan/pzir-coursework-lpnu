from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory storage for the temperature
temperature_data = {
    'sensor_id': 'sensor_1',
    'temperature': None
}

@app.route('/send-temperature', methods=['POST'])
def send_temperature():
    data = request.json
    temperature = data.get('temperature')

    # Save temperature in memory
    temperature_data['temperature'] = temperature
    return jsonify({"message": "Temperature saved successfully"}), 200

@app.route('/get-command', methods=['GET'])
def get_command():
    # Get the current temperature
    temperature = temperature_data['temperature']

    if temperature is None:
        return jsonify({"error": "No temperature data available"}), 400

    # Decide whether to turn on/off the heating
    if temperature < 20:  # Example condition
        command = "turn_on_heating"
    else:
        command = "turn_off_heating"

    return jsonify({"command": command}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)