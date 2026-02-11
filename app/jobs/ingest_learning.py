from pymilvus import Collection
from app.services.embedding_service import embed_text
from app.core.config import settings

collection = Collection(settings.MILVUS_COLLECTION)

def ingest(texts: list):
    vectors = [embed_text(t) for t in texts]
    collection.insert([
        list(range(len(texts))),
        texts,
        vectors
    ])
    collection.flush()