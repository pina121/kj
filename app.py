from flask import Flask, request, send_file
import cv2
import numpy as np
from some_animegan_library import apply_ghibli_filter  # Example library

app = Flask(__name__)

@app.route("/ghibli-style", methods=["POST"])
def ghibli_style():
    file = request.files["image"]
    image = cv2.imdecode(np.frombuffer(file.read(), np.uint8), cv2.IMREAD_COLOR)
    output = apply_ghibli_filter(image)
    cv2.imwrite("output.jpg", output)
    return send_file("output.jpg", mimetype="image/jpeg")

if __name__ == "__main__":
    app.run(debug=True)
