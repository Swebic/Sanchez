'''html inptu to flask

'''


from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello_world():
    if request.method == 'GET':
        return '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset = "UTF-8">
        <meta name "viewport" content="width=device-width, initial-scale=1.0">
        <title>IT DL</title>
    </head>
    <body>
        <h1> Youtube Downloader </h1>
        <form action = "" method="POST">
            <label for="url"> Video URL</label>
            <input type= "text" name="url">
            <input type="submit" value="Download">
        </formm>
    </body>
    </html>

'''
    elif request.method == 'POST':
        url = request.form.get ('url')
        print(url)
        yt = YouTube(url), on_progress_callback = on_progress)

        print(yt.title)
        ys = yt.stream.filter(progressive=True).get_highest_resolution()
        return "ok"