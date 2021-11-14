import json 
import os
import glob

dataset_dir = "trash\dataset"


for subset in ["train", "val"]:
    dataset_dir_1 = os.path.join(dataset_dir, subset, f"{subset}_annons_json_full.json")
    print(dataset_dir_1)
    annotations = json.load(open(dataset_dir_1))
    print(annotations.keys()) 