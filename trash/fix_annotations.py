import json 
import os
import glob

dataset_dir = "trash\dataset"

base_keys= {"train": {"_via_settings": {"ui": {
                            "annotation_editor_height": 25,
                            "annotation_editor_fontsize": 0.8,
                            "leftsidebar_width": 18,
                            "image_grid": {
                                "img_height": 80,
                                "rshape_fill": "none",
                                "rshape_fill_opacity": 0.3,
                                "rshape_stroke": "yellow",
                                "rshape_stroke_width": 2,
                                "show_region_shape": True,
                                "show_image_policy": "all"
                                },
                            "image": {
                                "region_label": "__via_region_id__",
                                "region_label_font": "10px Sans",
                                "on_image_annotation_editor_placement": "NEAR_REGION",
                                "region_color":"__via_default_region_color__"
                                }
                            },
                        "core": {
                            "buffer_size": 18,
                            "filepath": {},
                            "default_filepath": ""
                            },
                        "project": {
                            "name": "train_annons_json_full"
                        }
                    }, 
                    "_via_img_metadata": {},
                    "_via_attributes": {"region":{},
                                        "file":{}
                                    }
                },
            "val": {"_via_settings": {"ui": {
                            "annotation_editor_height": 25,
                            "annotation_editor_fontsize": 0.8,
                            "leftsidebar_width": 18,
                            "image_grid": {
                                "img_height": 80,
                                "rshape_fill": "none",
                                "rshape_fill_opacity": 0.3,
                                "rshape_stroke": "yellow",
                                "rshape_stroke_width": 2,
                                "show_region_shape": True,
                                "show_image_policy": "all"
                                },
                            "image": {
                                "region_label": "__via_region_id__",
                                "region_label_font": "10px Sans",
                                "on_image_annotation_editor_placement": "NEAR_REGION",
                                "region_color":"__via_default_region_color__"
                                }
                            },
                        "core": {
                            "buffer_size": 18,
                            "filepath": {},
                            "default_filepath": ""
                            },
                        "project": {
                            "name": "val_annons_json_full"
                        }
                    }, 
                    "_via_img_metadata": {},
                    "_via_attributes": {"region":{},
                                        "file":{}
                                    }
                }
        }

for subset in ["train", "val"]:
    dataset_dir_1 = os.path.join(dataset_dir, subset)
    all_jsons = glob.glob("{}/*.json".format(dataset_dir_1))
    for json_file in all_jsons:
        print("\n>>>>"+json_file)
        annotations = json.load(open(json_file)) 
        annotations = annotations["_via_img_metadata"]
    
        for key_file in annotations:
            image_file = annotations[key_file]
            try:
                image_path = os.path.join(dataset_dir, image_file.get('filename'))
                base_keys[subset]["_via_img_metadata"][key_file] = image_file
                print(image_path)
    
            except Exception as e: 
                print(e)   
                print("---")

    with open(f'{dataset_dir_1}\{subset}_annons_json_full.json', 'w') as f:
        json.dump(base_keys[subset], f)