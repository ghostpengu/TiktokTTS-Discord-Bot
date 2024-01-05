from flask import Flask, send_file , request

app = Flask(__name__)

@app.route('/download')
def download_file():
    

    # Get the value of the 'age' parameter from the URL
    file = request.args.get('file')

    # Use Flask's send_file function to send the file to the client
    return send_file(file, as_attachment=True)

def run():
  
    app.run(debug=False)

