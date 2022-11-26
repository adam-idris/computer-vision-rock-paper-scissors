import random
import cv2
from keras.models import load_model
import numpy as np
import time

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    countdown = time.time() + 5 
    choices = ['rock', 'paper', 'scissors', 'nothing']
    
    while countdown > time.time(): 
    
        ret, frame = cap.read()
        resized_frame = cv2.resize(frame, (224, 224), interpolation = cv2.INTER_AREA)
        image_np = np.array(resized_frame)
        normalized_image = (image_np.astype(np.float32) / 127.0) - 1 # Normalize the image
        data[0] = normalized_image
        prediction = model.predict(data)
        cv2.imshow('frame', frame)
        # Press q to close the window
        print(prediction)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    
    # After the loop release the cap object
    cap.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
    
    choice_rps = choices[np.argmax(prediction)]
    print(f'you chose {choice_rps}')

get_prediction()
