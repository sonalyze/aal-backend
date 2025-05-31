from pathlib import Path
import pandas as pd

current_dir = Path(__file__).parent
file_path = current_dir / "materialsTable.xlsx"

df = pd.read_excel(file_path, engine='openpyxl')


def get_material_json(name: str):
    row = df[df['description'].str.contains(name, case=False, na=False)]
    if row.empty:
        raise ValueError(f"Material '{name}' nicht gefunden.")
    row = row.iloc[0]
    absorption = [
        row.get(125, 0),
        row.get(250, 0),
        row.get(500, 0),
        row.get(1000, 0),
        row.get(2000, 0),
        row.get(4000, 0),
    ]

    return {
        "absorption": absorption
    }

