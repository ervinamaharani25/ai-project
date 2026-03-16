# from app_v1.rag_engine import ask_ai

# if __name__ == "__main__":
#     ticket_no = '12312022026'
#     question = "Error downloading Orange Report"
#     result = ask_ai(question)
#     print(result)



import requests

queries = [
    "Missing JIT"
]

for q in queries:
    response = requests.post(
        "http://127.0.0.1:8000/ai/recommendation",
        json={"query": q}
    )
    print("Query:", q)
    print("Response:", response.json())
    print("-" * 50)