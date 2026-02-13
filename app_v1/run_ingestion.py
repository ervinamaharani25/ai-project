from app_v1.ingestion import ingest_documents
from app_v1.loader.excel_loader import load_excel_kb
from app_v1.loader.db_loader import load_db_kb


if __name__ == "__main__":

    file_path = "D:\\1.VINA\\ai_project\\Issue_Recap_2025.xlsx"

    # load excel kb (initiation)
    docs = load_excel_kb(file_path)

    # load db kb (future)
    # docs = load_db_kb()

    ingest_documents(docs)