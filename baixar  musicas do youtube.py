import yt_dlp

url = 'cole aqui a url da musica'

ydl_opts = {
    'format': 'bestaudio/best',  # baixar o melhor áudio disponível
    'postprocessors': [{          # converter o áudio para mp3 depois do download
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',  # qualidade do MP3
    }],
    'ffmpeg_location': r'aqui vc tera que colocar o caminho do ffmpeg.exe',  # seu caminho do ffmpeg
    'outtmpl': 'downloads/%(title)s.%(ext)s',  # pasta e nome do arquivo de saída
}

with yt_dlp.YoutubeDL(ydl_opts) as ydl:
    ydl.download([url])
