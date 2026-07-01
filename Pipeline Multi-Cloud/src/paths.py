from pathlib import Path 

base_path = Path(__file__).resolve().parent.parent
data_raw_path = base_path/"data"/"raw"
data_clean_path = base_path/"data"/"cleaned"
data_gold_path = base_path/"data"/"gold"