# https://github.com/biankatpas/Cracks-and-Potholes-in-Road-Images-Dataset

import os

import numpy as np
import supervisely as sly
from tqdm import tqdm

project_name = "Cracks and Potholes in Road"
dataset_path = "/Users/almaz/Downloads/v1"
ds_name = "ds0"
batch_size = 30


def convert_and_upload_project(api, workspace_id):
    def _create_ann(folder_name):
        labels = []

        lane_path = os.path.join(dataset_path, folder_name, folder_name + "_LANE.png")
        crack_path = os.path.join(dataset_path, folder_name, folder_name + "_CRACK.png")
        pothole_path = os.path.join(dataset_path, folder_name, folder_name + "_POTHOLE.png")

        for idx, curr_path in enumerate([lane_path, crack_path, pothole_path]):
            image_np = sly.imaging.image.read(curr_path)[:, :, 0]
            if len(np.unique(image_np)) != 1:
                mask = image_np == 255
                curr_bitmap = sly.Bitmap(mask)
                curr_label = sly.Label(curr_bitmap, idx_to_obj_class[idx])
                labels.append(curr_label)

        return sly.Annotation(img_size=(image_np.shape[0], image_np.shape[1]), labels=labels)


    obj_class_road = sly.ObjClass("road", sly.Bitmap)
    obj_class_crack = sly.ObjClass("cracks", sly.Bitmap)
    obj_class_pothole = sly.ObjClass("pothole", sly.Bitmap)
    obj_class_collection = sly.ObjClassCollection([obj_class_road, obj_class_crack, obj_class_pothole])
    idx_to_obj_class = {0: obj_class_road, 1: obj_class_crack, 2: obj_class_pothole}


    project_info = api.project.create(workspace_id, project_name)
    meta = sly.ProjectMeta(obj_classes=obj_class_collection)
    api.project.update_meta(project_info.id, meta.to_json())

    dataset = api.dataset.create(project_info.id, ds_name, change_name_if_conflict=True)


    folders_list = os.listdir(dataset_path)

    progress = tqdm(desc="Create dataset {}".format(ds_name), total=len(folders_list))

    for folders_batch in sly.batched(folders_list, batch_size=batch_size):
        images_names_batch = []
        img_pathes_batch = []
        anns_batch = []

        for folder_name in folders_batch:
            image_name = folder_name + "_RAW.jpg"
            images_names_batch.append(image_name)
            img_pathes_batch.append(os.path.join(dataset_path, folder_name, image_name))
            ann = _create_ann(folder_name)
            anns_batch.append(ann)

        img_infos = api.image.upload_paths(dataset.id, images_names_batch, img_pathes_batch)
        img_ids = [im_info.id for im_info in img_infos]

        api.annotation.upload_anns(img_ids, anns_batch)

        progress.update(len(images_names_batch))

    return project_info