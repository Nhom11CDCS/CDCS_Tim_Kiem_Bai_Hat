from flask import Flask, request, render_template, redirect, url_for

app = Flask(__name__)

songs_db = {
    "minh a sao doi ta": "sau loi tu khuoc",
    # Thêm dữ liệu khác ở đây 
    # Test thử dữ liệu cơ bản 
}

@app.route('/', methods=['GET', 'POST'])
def search_song():
    if request.method == 'POST':
        lyrics = request.form['lyrics']
        result = songs_db.get(lyrics)
        if result:
            return render_template('main.html', lyrics=lyrics, result=result)
        else:
            return redirect(url_for('upload'))
    return render_template('main.html')

@app.route('/upload')
def upload():
    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
