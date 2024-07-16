from flask import Flask, render_template, request, redirect, url_for
import os
import yt_dlp as youtube_dl

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    quality = request.form.get('quality')
    download_path = os.path.join(app.root_path, 'static', 'downloads')
    
    if not os.path.exists(download_path):
        os.makedirs(download_path)
    
    quality_map = {
        'high': 'best',
        'good': 'best[height<=720]',
        'average': 'best[height<=480]',
        'low': 'best[height<=360]',
        'audio': 'bestaudio/best'
    }

    ydl_opts = {
        'format': quality_map.get(quality, 'best'),
        'outtmpl': os.path.join(download_path, '%(title)s.%(ext)s'),
    }
    
    try:
        with youtube_dl.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
        print("Download realizado com sucesso.")
        return redirect(url_for('success'))
    except Exception as e:
        print(f"Erro durante o download: {e}")
        return render_template('index.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
