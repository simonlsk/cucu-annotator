import json
# import numpy as np

BASE_DIR = '/home/nomios/Documents/Projects/deep/cucumber/dataset/fruit'
fileName = 'segmentation_results.json'
annPath = BASE_DIR + '/' + fileName
sample_value = 30
new_json = open("new_json.json", "w")

with open(annPath, "r") as segmentation_file:
    segmentation_json = json.load(segmentation_file)
    annotations = segmentation_json["annotations"]
    new_annotations = []

    for id in range(len(annotations)):
        
        segmentation = annotations[id]["segmentation"][0]
        new_segmentation = []
        sample_ratio = int(len(segmentation) / 2 / sample_value)
        sample_ratio = sample_ratio if sample_ratio > 0 else 1
        counter = 0

        # add first x,y
        new_segmentation += segmentation[0:2]
        for i in range(2, len(segmentation) - 2, 2):
            if counter % sample_ratio == 0:
                # add x value
                new_segmentation.append(segmentation[i])
                # add y value
                new_segmentation.append(segmentation[i + 1])
            counter += 1

        # add last x,y
        new_segmentation += segmentation[-2:]
        annotations[id]["segmentation"] = [new_segmentation]           
        new_annotations.append(annotations[id])

    segmentation_json["annotations"] = new_annotations
    json.dump(segmentation_json, new_json, indent=4, sort_keys=True)
    # print(segmentation["annotations"][0])

new_json.close()
