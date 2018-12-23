import json
import os
import errno
import random

r = lambda: random.randint(0,255)

# import numpy as np

dataset_id = 1
dataset = {
    "name": "Hello",
    "id": 1
}

img_path_prefix = "/data/datasets/{}/".format(dataset["name"])
export_folder = 'exports'
coco_file_path = 'segmentation_results.json'
current_directory = os.getcwd()
full_export_folder = os.path.join(current_directory, export_folder)
if not os.path.exists(full_export_folder):
    try:
        print("creating")
        os.makedirs(full_export_folder)
    except OSError as exc: # Guard against race condition
        if exc.errno != errno.EEXIST:
            raise


change_lut = {
    "images": {
        "id": "_id"
    },
    "annotations":{
        "id": "_id"
    },
    "categories":{
        "id": "_id"
    }
}

add_lut = {
    "images":{
        "deleted":False,
        "dataset_id":dataset["id"],
        "path": img_path_prefix
    },
    "annotations":{
        "dataset_id":dataset["id"],
        "iscrowd":False,
        "deleted":False,
        "paper_object": [],
        
    },
    "categories":{
        "color": "#289eb7"
    }
}
# BASE_DIR = '2018_05_09_11_58_segmentation_task_22_fruit_cucumber_BH'
# fileName = 'segmentation_results.json'
# annPath = BASE_DIR + '/' + fileName


with open(coco_file_path, "r") as coco_file:
    coco_base = json.load(coco_file)

    for title in coco_base:
        new_json = open("{}.json".format(title), "w")
        new_json = open("{}/{}.json".format(export_folder, title), "w")
        content = coco_base[title]
        if change_lut.get(title):
            for change_key, change_value in change_lut.get(title).items():
                for element in content:
                    element[change_value] = element.pop(change_key)

        # add to all titles:
        for element in content:
            # add color to annotations
            if title == "annotations":
                # add color
                element["color"] = '#%02X%02X%02X' % (r(),r(),r())
                # add width and height from image
                element_image_id = element["image_id"]
                element["width"] = coco_base["images"][element_image_id]["width"]
                element["height"] = coco_base["images"][element_image_id]["height"]
            if add_lut.get(title):
                for add_key, add_value in add_lut.get(title).items():
                    if add_key == "path":
                        add_value = add_value + element[add_key]
                        
                    element[add_key] = add_value



        json.dump(content, new_json, indent=4, sort_keys=True)
        new_json.close()
        # print(segmentation["annotations"][0])

# d = {'old_name': 1}
# d['new_name'] = d.pop('old_name')
# print(d)
