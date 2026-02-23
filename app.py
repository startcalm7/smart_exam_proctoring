import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename
from src.object_detector_with_face import run_detection

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"
ALLOWED_EXTENSIONS = {"mp4", "avi", "mov", "mkv"}

os.makedirs(UPLOAD_FOLDER, exist_ok=True)


# ===============================
# CHECK ALLOWED FILE TYPE
# ===============================
def allowed_file(filename):
    return "." in filename and \
           filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        if "video" not in request.files:
            return render_template("error.html", error="No file uploaded.")

        file = request.files["video"]

        if file.filename == "":
            return render_template("error.html", error="No selected file.")

        if not allowed_file(file.filename):
            return render_template("error.html", error="Invalid file type. Upload a video file.")

        # Secure filename
        filename = secure_filename(file.filename)
        video_path = os.path.join(UPLOAD_FOLDER, filename)

        # Save file
        try:
            file.save(video_path)
        except Exception as e:
            return render_template("error.html", error=f"File save failed: {str(e)}")

        mode = request.form.get("mode", "CLASSROOM")

        # Run detection
        report = run_detection(video_path, mode)

        if "error" in report:
            return render_template("error.html", error=report["error"])

        return render_template("result.html", report=report)

    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
