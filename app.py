from flask import Flask, request
import yt_dlp

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
    <head>
        <title>Downloader</title>
        <style>
            body {
                margin: 0;
                height: 100vh;
                display: flex;
                justify-content: center;
                align-items: center;
                flex-direction: column;
                background: linear-gradient(-45deg, #0f0c29, #302b63, #24243e);
                background-size: 400% 400%;
                animation: bg 8s ease infinite;
                font-family: Arial;
                color: white;
            }

            @keyframes bg {
                0% {background-position: 0% 50%;}
                50% {background-position: 100% 50%;}
                100% {background-position: 0% 50%;}
            }

            h1 {
                font-size: 40px;
                animation: glow 2s infinite alternate;
            }

            @keyframes glow {
                from {text-shadow: 0 0 10px white;}
                to {text-shadow: 0 0 20px #00ffcc;}
            }

            input {
                padding: 12px;
                width: 300px;
                border-radius: 10px;
                border: none;
                outline: none;
            }

            button {
                padding: 12px 20px;
                margin-top: 10px;
                border: none;
                border-radius: 10px;
                background: #00ffcc;
                cursor: pointer;
                font-weight: bold;
                transition: 0.3s;
            }

            button:hover {
                transform: scale(1.1);
                background: white;
            }

            .title {
                position: absolute;
                top: 20px;
                font-size: 22px;
                font-weight: bold;
            }
        </style>
    </head>

    <body>
        <div class="title">مصطفى تاج راسك</div>

        <h1>Video Downloader</h1>

        <form method="POST" action="/download">
            <input name="url" placeholder="ضع الرابط هنا">
            <br>
            <button>تحميل</button>
        </form>
    </body>
    </html>
    """

@app.route("/download", methods=["POST"])
def download():
    url = request.form["url"]

    ydl_opts = {
        "outtmpl": "video.%(ext)s",
        "format": "best",
        "noplaylist": True
    }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])

        return "تم التحميل بنجاح ✔"

    except Exception as e:
        return f"خطأ: {e}"


if __name__ == "__main__":
    app.run(debug=True)