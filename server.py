from flask import Flask, render_template, request, jsonify
from flask_cors import CORS  # Allow frontend requests

app = Flask(__name__)
CORS(app,origin='*')  # Enable CORS for frontend access

# Store the correct password in plain text
correct_password = "Inception2010!"
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/check_password', methods=['POST'])
def check_password():
    try:
        data = request.get_json()

        if not data or "password" not in data:
            return jsonify({"success": False, "message": "Missing password field!"}), 400

        user_password = data["password"]

        if user_password == correct_password:
            return jsonify({"success": True, "message": "Access Granted! 🎉"})
        else:
            return jsonify({"success": False, "message": "Incorrect password. Try again!"})

    except Exception as e:
        return jsonify({"success": False, "message": f"Error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
