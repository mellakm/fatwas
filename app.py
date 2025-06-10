from flask import Flask, jsonify, request, send_from_directory
from flask_cors import CORS
import os

app = Flask(__name__, static_folder="static", static_url_path="")
CORS(app)

fatawa = [
    {
        "question": "ما حكم التصوير؟",
        "answer": "التصوير الفوتوغرافي لا يجوز إلا للضرورة - ابن باز",
        "scholar": "ابن باز",
        "type": "text"
    },
    {
        "question": "هل يجوز صيام الست من شوال متفرقة؟",
        "answer": "نعم يجوز ذلك - العثيمين",
        "scholar": "العثيمين",
        "type": "audio"
    },
    {
        "question": "حكم لبس الساعة في اليد اليمنى",
        "answer": "يجوز ولا حرج في ذلك - الفوزان",
        "scholar": "الفوزان",
        "type": "video"
    }
]

@app.route("/api/fatawa")
def get_fatawa():
    query = request.args.get("query", "").lower()
    scholar = request.args.get("scholar", "all")
    content_type = request.args.get("type", "all")

    results = []
    for item in fatawa:
        if (scholar == "all" or item["scholar"] == scholar) and            (content_type == "all" or item["type"] == content_type) and            (query in item["question"].lower() or query in item["answer"].lower()):
            results.append(item)

    return jsonify(results)

@app.route("/")
def serve_index():
    return send_from_directory(app.static_folder, "index.html")

if  __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)=8000)