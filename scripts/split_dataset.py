import json
import os
import errno
import random
import numpy as np
from shutil import copyfile

# Split dataset to training set and test set
dataset_dir = "/home/simon/Documents/cucumber/dataset/fruits"
dataset_file_name = dataset_dir + '/' + 'fruits.json'
subsets = ['train', 'valid', 'test']
subsets_percent = [75, 15, 10]
subset_json_file_name = 'annotations'

# train_test_ration = 10.0 / 15.0

# current_directory = os.getcwd()

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
    dataset_size = len(coco_base["images"])

    permutation = np.random.permutation(dataset_size).tolist()
    cursor = 0
    all_subsets_indices = []
    for i, subset in enumerate(subsets):
        subset_size = int(subsets_percent[i] / 100.0 * dataset_size)
        subset_indices = permutation[cursor:cursor + subset_size]
        cursor += subset_size
       
        #Simon: remove lise if not necessary
        all_subsets_indices.append(subset_indices)
        ##################
        
        subset_dir = os.path.join(dataset_dir, subset) 
        make_dir(subset_dir)
        subset_file = open("{}/{}.json".format(subset_dir, subset_json_file_name), "w")
    
        subset_dictionary =  {}
        subset_dictionary["categories"] = coco_base["categories"]
        # train_subset["info"] = coco_base["info"]
        subset_dictionary["images"] = [ coco_base["images"][j] for j in subset_indices ]
        subset_dictionary["annotations"] = []

        # copy image to train directory
        for image in subset_dictionary["images"]:
            print("copying {} to {}".format(dataset_dir + "/" + image["file_name"], subset_dir + "/" + image["file_name"]))
            copyfile(dataset_dir + "/" + image["file_name"], subset_dir + "/" + image["file_name"])

        # copy only relevent annotations
        subset_image_ids = [image["id"] for image in subset_dictionary["images"]]
        for annotation in coco_base["annotations"]:
            if annotation["image_id"] in subset_image_ids:
                subset_dictionary["annotations"].append(annotation)

        json.dump(subset_dictionary, subset_file, indent=4, sort_keys=True)
        subset_file.close()


    # # test subset
    # test_dir = os.path.join(current_directory, "test") 
    # make_dir(test_dir)
    # test_file = open("{}/{}.json".format(test_dir, subset_json_file_name), "w")
    
    # test_subset =  {}
    # test_subset["categories"] = coco_base["categories"]
    # # test_subset["info"] = coco_base["info"]
    # test_subset["images"] = [ coco_base["images"][i] for i in test_indices ]
    # test_subset["annotations"] = []

    # # copy image to train directory
    # for image in test_subset["images"]:
    #     copyfile(dataset_dir + "/" + image["file_name"], test_dir +"/"+ image["file_name"])

    # # copy test annotations
    # test_image_ids = [image["id"] for image in test_subset["images"]]
    # for annotation in coco_base["annotations"]:
    #     if annotation["image_id"] in test_image_ids:
    #         test_subset["annotations"].append(annotation)


    # json.dump(test_subset, test_file, indent=4, sort_keys=True)
    # test_file.close()
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
