from pymilvus import Collection
from app.core.config import settings

def search_kb(vector: list, limit: int = 3):
    try:
        collection = Collection(settings.MILVUS_COLLECTION)
        collection.load()

        results = collection.search(
            data=[vector],
            anns_field="embedding",
            param={
                "metric_type": "IP",
                "params": {"nprobe": 10}
            },
            limit=limit,
            output_fields=["troubleshoot_step"]
        )

        hits = []
        for hit in results[0]:
            hits.append({
                "content": hit.entity.get("troubleshoot_step"),
                "score": hit.score
            })

        print("🧠 KB hits:", hits)
        return hits

    except Exception as e:
        print("[KB] Milvus search error:", str(e))
        return []