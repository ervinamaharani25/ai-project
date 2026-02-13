from pymilvus import (
    connections,
    FieldSchema, CollectionSchema, DataType,
    Collection, utility
)

from app_v1.config import MILVUS_HOST, MILVUS_PORT, COLLECTION_NAME, EMBEDDING_DIM


def connect_milvus():
    conn = connections.connect(
        alias="default",
        host=MILVUS_HOST,
        port=MILVUS_PORT
    )
    return conn


def create_collection():
    if utility.has_collection(COLLECTION_NAME):
        return Collection(COLLECTION_NAME)

    fields = [
        FieldSchema(name="id", dtype=DataType.INT64, is_primary=True, auto_id=True),
        FieldSchema(name="ticket_number",dtype=DataType.VARCHAR,max_length=12),
        FieldSchema(name="ticket_summary",dtype=DataType.VARCHAR,max_length=1024),
        FieldSchema(name="type_ticket",dtype=DataType.VARCHAR,max_length=64),
        FieldSchema(name="category",dtype=DataType.VARCHAR,max_length=128),
        FieldSchema(name="sub_category",dtype=DataType.VARCHAR,max_length=128),
        FieldSchema(name="department",dtype=DataType.VARCHAR,max_length=128),
        FieldSchema(name="assign_name",dtype=DataType.VARCHAR,max_length=128),
        FieldSchema(name="troubleshoot_step",dtype=DataType.VARCHAR,max_length=4096),
        FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=EMBEDDING_DIM),
    ]

    schema = CollectionSchema(fields, description="Apollo KB")

    collection = Collection(COLLECTION_NAME, schema)

    index_params = {
        "metric_type": "IP",
        "index_type": "IVF_FLAT",
        "params": {"nlist": 128},
    }

    idx = collection.create_index("embedding", index_params)

    return collection


def load_collection():
    collection = Collection(COLLECTION_NAME)
    collection.load()
    return collection