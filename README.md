# flask, 인공지능 프로젝트 

## 시현 및 비교
<img width="1280" alt="image" src="https://github.com/user-attachments/assets/0a31e9e2-8de2-4d49-9e20-4b698a14bb0e">

## 디렉토리 구조
<img width="331" alt="image" src="https://github.com/user-attachments/assets/f1a110ad-e5b2-4972-ab0d-29a40f23fc4c">

## api 키 발급
<img width="331" alt="image" src="https://github.com/user-attachments/assets/b81d29c8-8b7c-44df-a12d-b4ae4d07fd29">

## api 사용을 위한 결제 
<img width="331" alt="image" src="https://github.com/user-attachments/assets/6f740ed0-385f-4766-8f17-e4c4e5c27f57">
<img width="882" alt="image" src="https://github.com/user-attachments/assets/89abab49-c8d2-4cae-83f3-417470ec4a93">
<img width="882" alt="image" src="https://github.com/user-attachments/assets/91fdd91a-ef2f-454d-88df-3a23af6b676f">
<img width="882" alt="image" src="https://github.com/user-attachments/assets/5a2cdb94-e741-4190-a9de-f7d0544fdd3d">
<img width="882" alt="image" src="https://github.com/user-attachments/assets/9f294816-7fdc-4b3f-a0df-ae7c88c63a99">

## 공부한 내용 
GitHub에서 보기 좋은 Markdown 형식으로 작성(gpt)

Flask 보안 및 컨텍스트 개념

1. 보안 문제 가능성

해당 코드에서 보안상 문제가 될 수 있는 부분은 .env 파일에 저장된 API_KEY입니다. .env 파일이나 API 키가 실수로 GitHub에 업로드되면, 누구나 이 API 키를 사용해 OpenAI API에 접근할 수 있습니다. 이를 방지하기 위해 다음을 유의해야 합니다:

	•	.gitignore 설정
.gitignore 파일에 .env를 추가하여, .env 파일이 GitHub에 업로드되지 않도록 설정합니다. 이를 통해 .env 파일에 저장된 민감 정보가 외부에 노출되지 않게 할 수 있습니다.
	•	API 키 재발급
만약 GitHub에 실수로 API 키가 업로드되었다면, API 키를 즉시 재발급하고 .gitignore 설정 후 다시 커밋해야 합니다.

	📌 Tip: 초기 커밋 시 절대 .env 파일을 업로드하지 않도록 주의하세요.

2. 코드 기능 검토

이 코드의 주요 기능은 ChatGPT API로 질문을 전송하고 응답을 받아 화면에 출력하는 역할을 수행합니다. 구체적인 동작은 다음과 같습니다:

	•	/chat 경로에서 POST 요청을 받아 사용자가 입력한 질문(message 필드)을 ChatGPT API로 전송합니다.
	•	ChatGPT API에서 받은 응답을 JSON 형식으로 가공하여 프론트엔드에 전달하고, 프론트엔드는 이를 화면에 표시합니다.

따라서 이 코드는 입력된 질문에 대해 ChatGPT의 답변을 받아 화면에 출력하는 구조로 잘 동작할 것입니다.

3. Flask의 컨텍스트

Flask에서는 두 가지 주요 컨텍스트가 사용됩니다: 애플리케이션 컨텍스트와 요청 컨텍스트입니다.

애플리케이션 컨텍스트

	•	요청을 통해 앱 레벨의 데이터를 사용할 수 있도록 합니다.
	•	사용 예: current_app, g
	•	current_app: 플라스크 애플리케이션의 인스턴스에 직접 접근하지 않고도 접근할 수 있습니다.
	•	g: 요청이 처리되는 동안 유효한 임시 데이터를 저장할 수 있습니다.

	비교: Spring Boot의 ApplicationContext와 유사하며, 모든 빈을 관리합니다.

요청 컨텍스트

	•	요청이 있는 동안 요청 레벨의 데이터를 사용할 수 있도록 합니다.
	•	사용 예: request, session
	•	request: 현재 HTTP 요청에 대한 정보를 포함합니다.
	•	session: 사용자 세션 데이터를 관리합니다.

	비교: Spring Boot의 RequestScope와 유사하며, HTTP 관련 정보를 다룹니다.







