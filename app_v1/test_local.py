from app_v1.rag_engine import ask_ai

if __name__ == "__main__":
    ticket_no = '12312022026'
    question = "Error downloading Orange Report"
    result = ask_ai(question)
    print(result)