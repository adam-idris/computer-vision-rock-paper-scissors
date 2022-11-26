import random
import cv2
from keras.models import load_model
import numpy as np

def get_computer_choice():
    return random.choice(["Rock", "Paper", "Scissors"])

def get_prediction():
    model = load_model('keras_model.h5')
    cap = cv2.VideoCapture(0)
    data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
    
    while True: 
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

def get_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It is a tie!")
        
    if (computer_choice == 'Rock' and user_choice == 'Paper') \
    or (computer_choice == 'Paper' and user_choice == 'Scissors'): 
        print("You won!")
        
    if (computer_choice == 'Rock' and user_choice == 'Scissors') \
    or (computer_choice == 'Paper' and user_choice == 'Rock'):
        print("You lost")

def play():
    get_winner(get_computer_choice(), get_user_choice())

play()
