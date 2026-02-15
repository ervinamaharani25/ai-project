from app_v1.milvus_client import connect_milvus, load_collection
from app_v1.nomic_embedder import embed_text_batch, normalize
from app_v1.config import TOP_K
from typing import Any


def search_kb(query: str):
    connect_milvus()
    collection = load_collection()

    query_embedding = embed_text_batch([query])[0]
    query_embedding = normalize(query_embedding)

    search_params = {
        "metric_type": "IP",
        "params": {"nprobe": 10}
    }

    results : Any = collection.search(
        data=[query_embedding],
        anns_field="embedding",
        param=search_params,
        limit=TOP_K,
        output_fields=["troubleshoot_step"]
    )
    
    hits = []

    for hit in results[0]:
        hits.append({
            "score": hit.score,
            "content": hit.entity.get("troubleshoot_step")
        })
        print(hit.entity.get("ticket_number"))
        print(hit.entity.get("troubleshoot_step"))
        print(hit.distance)
        print("------")
    return hits