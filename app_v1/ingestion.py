from app_v1.milvus_client import connect_milvus, create_collection
from app_v1.nomic_embedder import embed_text


def ingest_documents(documents: list[str]):

    connect_milvus()

    collection = create_collection()

    texts = []
    embeddings = []

    for doc in documents:

        embedding = embed_text(doc)

        texts.append(doc)
        embeddings.append(embedding)

    collection.insert([texts, embeddings])

    collection.flush()

    print("Total entities in Milvus:", collection.num_entities)