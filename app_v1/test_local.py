from app_v1.rag_engine import ask_ai

if __name__ == "__main__":
    ticket_no = '12312022026'
    question = "I forgot my Apollo password"
    result = ask_ai(ticket_no, question)
    print(result)