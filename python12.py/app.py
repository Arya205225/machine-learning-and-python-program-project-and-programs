from flask import Flask, render_template, request, jsonify, Response
from services.gemini_service import GeminiService
from services.subtitle_service import SubtitleService
from services.stt_service import STTService
from services.game_service import GameService
from config import Config
import cv2

app = Flask(__name__, template_folder="templates")
app.config.from_object(Config)

# --- Initialize services ---
gemini = GeminiService()
subtitle = SubtitleService()
stt = STTService()
games = GameService()

# --- Camera setup (OpenCV) ---
camera = cv2.VideoCapture(0)

def generate_frames():
    while True:
        success, frame = camera.read()
        if not success:
            break
        else:
            # Encode frame as JPEG
            ret, buffer = cv2.imencode('.jpg', frame)
            frame = buffer.tobytes()
            
            yield (b'--frame\r\n'
                   b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

# --- Pages ---
@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/lessons")
def lessons_page():
    return render_template("lesson.html")

@app.route("/game")
def game_page():
    return render_template("game.html")


# --- Webcam feed ---
@app.route("/video_feed")
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# --- APIs ---
@app.route("/api/chat", methods=["POST"])
def api_chat():
    data = request.get_json(force=True)
    message = data.get("message","")
    lang = data.get("lang","en")
    reply = gemini.chat(message, lang=lang)
    return jsonify({"reply": reply})

@app.route("/api/subtitles", methods=["POST"])
def api_subtitles():
    data = request.get_json(force=True)
    text = data.get("text","")
    roman = subtitle.to_roman_urdu(text)
    return jsonify({"original": text, "roman_urdu": roman})

@app.route("/api/stt", methods=["POST"])
def api_stt():
    if "audio" not in request.files:
        return jsonify({"error": "audio file missing"}), 400
    audio = request.files["audio"]
    transcript = stt.transcribe_audio(audio.read())
    return jsonify({"transcript": transcript})

@app.route("/api/games/vocab")
def api_vocab_quiz():
    items = games.get_vocab_quiz()
    return jsonify(items)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)