import cv2
import os

#pre-trained car classifier
car_cascade = cv2.CascadeClassifier('haarcascade_car.xml')

def count_cars_in_folder(input_folder, output_folder):
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.lower().endswith('.jpg'):
                image_path = os.path.join(root, file)
                count_and_annotate_cars(image_path, output_folder, root)

def count_and_annotate_cars(image_path, output_folder, relative_path):
    image = cv2.imread(image_path)
    
    if image is not None:
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        
        cars = car_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(25, 25))
        
        num_cars = len(cars)
        
        print(f"Number of cars in {image_path}: {num_cars}")
        
        output_folder_path = os.path.join(output_folder, relative_path)
        os.makedirs(output_folder_path, exist_ok=True)
        
        annotation_path = os.path.join(output_folder_path, f"{os.path.splitext(os.path.basename(image_path))[0]}.txt")
        with open(annotation_path, 'w') as f:
            f.write(str(num_cars))
        

dataset_folder = '/home/pavel/dev/n-n-cars-prediction/Insight-MVT_Annotation_Train'
annotations_folder = '/home/pavel/dev/n-n-cars-prediction/annotations'

count_cars_in_folder(dataset_folder, annotations_folder)