from flask import Flask, request, jsonify

app = Flask(__name__)

data = {}

@app.route('/sensor/data', methods=['POST'])
def post_data():
    distance = request.form.get('distance')
    if not distance:
        return jsonify({"error": "Data tidak valid"}), 400

    entry_id = len(data) + 1
    subData = {'distance': distance}
    data[entry_id] = subData
    print(data)
    return jsonify({"pesan": "Data diterima dengan sukses"}), 200

@app.route('/sensor/data', methods=['GET'])
def get_data():
    return jsonify(data), 200

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')
