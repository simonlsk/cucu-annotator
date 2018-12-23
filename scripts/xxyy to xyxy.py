import json
# import numpy as np

BASE_DIR = '../dataset/2018_05_09_11_58_segmentation_task_22_fruit_cucumber_BH'
fileName = 'segmentation_results.json'
annPath = BASE_DIR + '/' + fileName

new_json = open("new_json.json", "w")

with open(annPath, "r") as segmentation_file:
    segmentation = json.load(segmentation_file)
    annotations = segmentation["annotations"]
    new_annotations = []
    for id in range(len(annotations)):

        # turn xyxy... to [xxx][yyy]
        # x = annotations[id]["segmentation"][0][::2]
        # y = annotations[id]["segmentation"][0][1::2]
        x = annotations[id]["segmentation"][0]
        y = annotations[id]["segmentation"][1]

        # new version
        new_annotations.append(annotations[id])

        # turn to [xxx][yyy]
        # new_annotations[id]["segmentation"] = [x,y]
        new_annotations[id]["segmentation"] = [None]
        new_annotations[id]["segmentation"][0] = [None] * (len(x) + len(y))
        new_annotations[id]["segmentation"][0][::2] = x
        annotations[id]["segmentation"][0][1::2] = y

    segmentation["annotations"] = new_annotations
    json.dump(segmentation, new_json, indent=4, sort_keys=True)
    # print(segmentation["annotations"][0])
