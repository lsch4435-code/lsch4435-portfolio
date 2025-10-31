
import google.generativeai as genai

genai.configure(api_key="여기에_발급받은_API_키_입력")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("안녕, 제미나이!")
print(response.text)

