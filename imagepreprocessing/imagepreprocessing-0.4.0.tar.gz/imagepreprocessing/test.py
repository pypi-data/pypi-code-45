from imagepreprocessing import create_training_data_keras,create_training_data_yolo, create_only_path_files_yolo, make_prediction_from_directory, make_prediction_from_array, create_confusion_matrix, train_test_split


source_path = "C:\\Users\\can\\datasets\\deep_learning\\food-101\\only3"
save_path = "C:\\Users\\can\\Desktop\\food10class100sampleeach"

images_path = "C:\\Users\\can\\PythonProjects2\\deep_learning\\test_images\\food2"
model_path = "C:\\Users\\can\\PythonProjects2\\deep_learning\\saved_models\\a.h5"

class_names = ["elma","el","armut"]


# create_training_data_yolo(source_path, rename_duplicates=True, validation_split = 0.2)

# create_only_path_files_yolo(source_path, percent_to_use=1,validation_split = 0.2)


# x, y, x_val, y_val = create_training_data_keras(source_path, save_path = None, validation_split=0.2, percent_to_use=0.1)

# x, y, test_x, test_y =  train_test_split(x,y,)

# predictions = make_prediction_from_array(test_x,model_path)

# create_confusion_matrix(predictions,test_y,class_names=class_names, one_hot=True)

# pred = make_prediction_from_directory(images_path,model_path,show_images=True)


# class_names = ["elma","el","armut"]
# classes = [0,0,0,1,1,1,2,2,2]
# predictions = [0,0,1,0,1,2,2,2,2]
# create_confusion_matrix(predictions,classes,class_names=class_names)


