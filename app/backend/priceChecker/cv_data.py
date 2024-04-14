import easyocr
import cv2
import supervision as sv
import cv2
import subprocess
import ast

def get_data(img_path):
    # Начальные переменные, необходимые для дальнейшей работы
    data_dict = {}
    image = cv2.imread(img_path)
    #print(image)

    
    result = subprocess.check_output(['inference', 'infer', '--input', img_path, '--api-key', 'hXHzHoDbAJs5k5oQlZQN', '--model_id', 'price-tag-detection-r5jlv/1']).decode("utf-8")
    result = result[(result.find('\n')):]

    result = ast.literal_eval(result)
    #print(result)
    #Названия разметки, сами разметки и два объекта классов LabelAnnotator и BoundingBoxAnnotator, которые и производят аннотацию ценников.
    labels = [item["class"] for item in result["predictions"]]
    detections = sv.Detections.from_inference(result)
    label_annotator = sv.LabelAnnotator()
    bounding_box_annotator = sv.BoundingBoxAnnotator()


    #Создание размеченной картинки.
    annotated_image = bounding_box_annotator.annotate(
        scene=image.copy(), detections=detections)
    annotated_image = label_annotator.annotate(
        scene=annotated_image.copy(), detections=detections, labels=labels)
    
    #print(annotated_image)

    #Задаем настройки считывателю текста
    reader = easyocr.Reader(['ru'])

    
    #часть, которая определяет координаты разметки, обрезает фотографию, считывает текст, записывает в data_dict и так со всеми аннотациями.
    for i, detection in enumerate(detections.xyxy):
        try:
            x_min, y_min, x_max, y_max = detection
            cropped_img = image[int(y_min):int(y_max), int(x_min):int(x_max)]


            result = reader.readtext(cropped_img, paragraph=True, detail=0)
            #print(result)
            if result:
                data_dict[i+1] = result
            else:
                print(f"Annotation {i+1}: No text detected")
        except IndexError:
            print(f"Error processing annotation {i+1}")
    

    #print(data_dict)
    return data_dict

