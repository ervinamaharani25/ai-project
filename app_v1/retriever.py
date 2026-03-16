from app_v1.milvus_client import connect_milvus, load_collection
#nomic+llama
from app_v1.nomic_embedder import embed_text_batch, normalize
#bge+qwen
# from app_v1.bge_embedder import bge_embed_text_batch, bge_normalize
from app_v1.config import TOP_K
from typing import Any


def search_kb(query: str):
    connect_milvus()
    collection = load_collection()

    # query_embedding = bge_embed_text_batch([query])[0]
    # query_embedding = bge_normalize(query_embedding)

    query_embedding = embed_text_batch([query])[0]
    query_embedding = normalize(query_embedding)

    # 2. DEBUG HERE
    print("Query:", query)
    print("Embedding sample:", query_embedding[:10])

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