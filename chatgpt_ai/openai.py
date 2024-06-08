from dotenv import load_dotenv
import openai
import os

os.chdir(r"C:\Users\emily\OneDrive\桌面\PBC1122")
# print(os.getcwd())


load_dotenv(r"C:\Users\emily\OneDrive\桌面\PBC1122\token.env")

openai.api_key = os.getenv("CHATGPT_API_KEY")

# 串gpt-3.5-turbo的api
def chatgpt_response(prompt):
    response = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {
            "role": "user",
            "content": prompt,
        }
        ],
        temperature=1,
        max_tokens=100
    )
    
    response_dict = response.get("choices")
    
    if response_dict and len(response_dict) > 0:
        prompt_response = response_dict[0]["message"]["content"]
    
    return prompt_response