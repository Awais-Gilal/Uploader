from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
  return """
  <html>
  <head>Uploader</head>
  <body>
    <h1>Uploader</h1>
    <form action="/upload" method="post" enctype="multipart/form-data">
      <input type="file" name="file" />
      <input type="submit" value="Upload" />
    </form>
  </body>
</html>
"""


@app.route("/upload", methods=["POST"])
def upload():
  file = request.files["file"]
  file.save(file.filename)
  return "File uploaded successfully"

app.run(host="0.0.0.0", port=7777, debug=True)
