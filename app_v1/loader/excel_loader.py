import pandas as pd


def load_excel_kb(file_path: str) -> list[str]:

    df = pd.read_excel(file_path)

    documents = []

    for _, row in df.iterrows():

        description = str(row.get("Ticket Summary", "")).strip()
        action_taken = str(row.get("Troubleshoot Step", "")).strip()


        text = f"""

        Description:
        {description}

        Resolution:
        {action_taken}
        """.strip()

        if description and action_taken:
            documents.append(text)

    print(f"Loaded {len(documents)} documents from Excel")

    return documents