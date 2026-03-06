from app_v2.ingestion import ingest_documents
from app_v2.loader.excel_loader import load_excel_kb
from app_v2.loader.db_loader import load_db_kb
from pymilvus import utility
from app_v2.milvus_client import connect_milvus

# connect_milvus()

# utility.drop_collection("apollo_kb")
# print("Collection apollo_kb deleted")

if __name__ == "__main__":

    # file_path = "D:\\1.VINA\\ai_project\\Issue_Recap_2025.xlsx"
    file_path = "C:\\dev\\db\Apollo Issue Recap 2025.xlsx"

    # load excel kb (initiation)
    docs = load_excel_kb(file_path)

    # load db kb (future)
    # docs = load_db_kb()

    ingest_documents(docs)