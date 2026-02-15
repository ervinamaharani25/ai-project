from app_v1.milvus_client import connect_milvus, create_collection
from app_v1.nomic_embedder import embed_text_batch, normalize


def ingest_documents(records: list[dict]):

    connect_milvus()
    collection = create_collection()

    # ✅ Gabungkan text untuk embedding
    texts = [
        f"{r['ticket_summary']} {r['troubleshoot_step']}"
        for r in records
    ]

    # ✅ Embed SEKALI saja
    embeddings = embed_text_batch(texts)
    embeddings = [normalize(v) for v in embeddings]

    # ✅ Pisahkan setiap field
    ticket_number = [r["ticket_number"] for r in records]
    ticket_summary = [r["ticket_summary"] for r in records]
    type_ticket = [r["type_ticket"] for r in records]
    category = [r["category"] for r in records]
    sub_category = [r["sub_category"] for r in records]
    department = [r["department"] for r in records]
    assign_name = [r["assign_name"] for r in records]
    troubleshoot_step = [r["troubleshoot_step"] for r in records]


    #Check data
    print("ticket_number:", len(ticket_number))
    print("ticket_summary:", len(ticket_summary))
    print("type_ticket:", len(type_ticket))
    print("category:", len(category))
    print("sub_category:", len(sub_category))
    print("department:", len(department))
    print("assign_name:", len(assign_name))
    print("troubleshoot_step:", len(troubleshoot_step))
    print("embeddings:", len(embeddings))
    # ✅ Insert ke Milvus (urutan harus sama dengan schema)
    collection.insert([
        ticket_number,
        ticket_summary,
        type_ticket,
        category,
        sub_category,
        department,
        assign_name,
        troubleshoot_step,
        embeddings
    ])

    collection.flush()

    print("Total entities in Milvus:", collection.num_entities)