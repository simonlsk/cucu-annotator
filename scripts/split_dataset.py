import json
import os
import errno
import random
import numpy as np
from shutil import copyfile

# Split dataset to training set and test set

dataset_dir = "."
subsets = ['train', 'test']
dataset_file_name = 'segmentation_results.json'
subset_json_file_name = 'annotations'

train_test_ration = 0.5

current_directory = os.getcwd()

def make_dir(full_export_folder):
    if not os.path.exists(full_export_folder):
        try:
            print("creating")
            os.makedirs(full_export_folder)
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise



with open(dataset_file_name, "r") as coco_file:
    coco_base = json.load(coco_file)
    # dataset_size = len(coco_base["images"])
    dataset_size = 2

    permutation = np.random.permutation(dataset_size)
    train_size = int (train_test_ration * dataset_size)
    train_indices = permutation[:train_size].tolist()
    test_indices = permutation[train_size:].tolist()

    # train subset
    train_dir = os.path.join(current_directory, "train") 
    make_dir(train_dir)
    train_file = open("{}/{}.json".format(train_dir, subset_json_file_name), "w")
    
    train_subset =  {}
    train_subset["categories"] = coco_base["categories"]
    train_subset["info"] = coco_base["info"]
    train_subset["images"] = [ coco_base["images"][i] for i in train_indices ]
    train_subset["annotations"] = []

    # copy image to train directory
    for image in train_subset["images"]:
        copyfile(image["file_name"], train_dir +"/"+ image["file_name"])

    # copy only relevent annotations
    train_image_ids = [image["id"] for image in train_subset["images"]]
    for annotation in coco_base["annotations"]:
        if annotation["image_id"] in train_image_ids:
            train_subset["annotations"].append(annotation)

    json.dump(train_subset, train_file, indent=4, sort_keys=True)
    train_file.close()


    # test subset
    test_dir = os.path.join(current_directory, "test") 
    make_dir(test_dir)
    test_file = open("{}/{}.json".format(test_dir, subset_json_file_name), "w")
    
    test_subset =  {}
    test_subset["categories"] = coco_base["categories"]
    test_subset["info"] = coco_base["info"]
    test_subset["images"] = [ coco_base["images"][i] for i in test_indices ]
    test_subset["annotations"] = []

    # copy image to train directory
    for image in test_subset["images"]:
        copyfile(image["file_name"], test_dir +"/"+ image["file_name"])

    # copy test annotations
    test_image_ids = [image["id"] for image in test_subset["images"]]
    for annotation in coco_base["annotations"]:
        if annotation["image_id"] in test_image_ids:
            test_subset["annotations"].append(annotation)


    json.dump(test_subset, test_file, indent=4, sort_keys=True)
    test_file.close()
    # 
    
def in_bound_segments(segments, width, heigh):
    x = segments[::2]
    y = segments[1::2]
    for x_segment in x:
        if x_segment >= width:
            return


# d = {'old_name': 1}
# d['new_name'] = d.pop('old_name')
# print(d)
