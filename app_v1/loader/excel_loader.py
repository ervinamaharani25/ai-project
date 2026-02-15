import pandas as pd

def load_excel_kb(file_path: str):

    df = pd.read_excel(file_path)
    df.columns = df.columns.str.strip()

    records = []

    for _, row in df.iterrows():

        if pd.notna(row["ticket_summary"]) and pd.notna(row["troubleshoot_step"]):

            records.append({
                "ticket_number": str(row["ticket_number"]),
                "ticket_summary": str(row["ticket_summary"]),
                "type_ticket": str(row["type_ticket"]),
                "category": str(row["category"]),
                "sub_category": str(row["sub_category"]),
                "department": str(row["department"]),
                "assign_name": str(row["assigned_name"]),
                "troubleshoot_step": str(row["troubleshoot_step"]),
            })

    print(f"Loaded {len(records)} records from Excel")
    return records