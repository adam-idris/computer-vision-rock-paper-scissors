import random
import cv2
from keras.models import load_model
import numpy as np
import time

class RockPaperScissors:
    
    def __init__(self):
        self.user_wins = 0
        self.computer_wins = 0
    
    def get_computer_choice(self):
        self.computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        return self.computer_choice

    def get_prediction(self):
        model = load_model('keras_model.h5')
        cap = cv2.VideoCapture(0)
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        countdown = time.time() + 5 
        choices = ['Rock', 'Paper', 'Scissors', 'Nothing']
        
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
        
        self.user_choice = choices[np.argmax(prediction)]
        print(f'you chose {self.user_choice}')
        return self.user_choice

    def get_winner(self, computer_choice, user_choice):
        
        self.computer_choice = computer_choice
        self.user_choice = user_choice
            
        if [self.computer_choice, self.user_choice] in [['Rock', 'Paper'], ['Paper', 'Scissors'], ['Scissors', 'Rock']]:
            self.user_wins += 1
            self.outcome = 'win'
            
        elif [self.computer_choice, self.user_choice] in [['Paper', 'Rock'], ['Rock', 'Scissors'], ['Scissors', 'Paper']]:
            self.user_wins += 1
            self.outcome = 'lose'
            
        elif self.computer_choice == self.user_choice:
            self.outcome = 'tie'
            
        elif self.user_choice == 'Nothing':
            self.outcome = 'nothing'

def play():
    
    game = RockPaperScissors()
    while True:

        computer_choice = game.get_computer_choice()
        user_choice = game.get_prediction()
        game.get_winner(computer_choice, user_choice)
        print(f"You chose {game.user_choice}. " + f"The computer chose {game.computer_choice} " f"You {game.outcome}!")
        print(f"The score is {game.user_wins} - {game.computer_wins}")
        
        
        if game.user_wins == 3:
            print("You won the game!")
            break
        
        elif game.computer_wins == 3:
            print(f'The score is {game.user_wins} - {game.computer_wins}')
            print("You lost the game!")
            break
        
        elif game.outcome == 'tie':
            print("It's a tie")
            
        elif game.outcome == 'nothing':
            print("I didn't recognise your guess. Try again!")
            print(f"The score is {game.user_wins} - {game.computer_wins}")
        
            
play()