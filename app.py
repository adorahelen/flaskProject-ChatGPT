from flask import Flask, request, jsonify, render_template
import requests
import os
from dotenv import load_dotenv
import logging

app = Flask(__name__)

# .env 파일에서 API 키 불러오기
load_dotenv()
API_KEY = os.getenv("OPENAI_API_KEY")

# 로깅 설정 (콘솔에 에러 메시지를 출력)
logging.basicConfig(level=logging.INFO)

@app.route('/')
def index():
    return render_template('index.html')
# app.py <= 특정 디렉토리 안으로 옮기면, templates 디렉토리도 그안에 위치시켜야 찾을 수있음

@app.route('/chat', methods=['POST'])
def chat_with_gpt():
    try:
        # 프론트에서 받은 메시지 가져오기
        user_input = request.json.get('message')
        if not user_input:
            return jsonify({"error": "메시지를 입력해 주세요."}), 400

        # ChatGPT API 요청 설정
        api_url = "https://api.openai.com/v1/chat/completions"
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "gpt-3.5-turbo",
            "messages": [{"role": "user", "content": user_input}]
        }

        # API 요청 보내기
        response = requests.post(api_url, headers=headers, json=payload)
        response.raise_for_status()  # 응답 오류가 있는 경우 예외 발생
        reply = response.json()['choices'][0]['message']['content']
        return jsonify({"reply": reply})

    except requests.exceptions.RequestException as e:
        logging.error(f"API 요청 중 오류 발생: {e}")
        return jsonify({"error": "ChatGPT API 요청 실패"}), 500

    except KeyError:
        logging.error("API 응답에서 필요한 데이터가 없습니다.")
        return jsonify({"error": "API 응답에 문제가 있습니다."}), 500

    except Exception as e:
        logging.error(f"예상치 못한 오류 발생: {e}")
        return jsonify({"error": "서버에서 오류가 발생했습니다."}), 500

if __name__ == '__main__':
    app.run(debug=True)