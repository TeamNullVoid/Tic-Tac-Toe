from tensorflow.python.keras.models import load_model
import numpy as np

model = load_model('ai_opponent.h5')

# does not check for win or loose cond.
# Input = 1D array for board, 1 for AIs moves, 0 for BLANK and -1 for human moves
# output = [0,8]
def  predict_move(gameboard):
    print("making prediction : ", np.array(gameboard).reshape(1, 9))
    prediction = model.predict(np.array(gameboard).reshape(1, 9))
    print(prediction)
    n = prediction.argmax()
    while True:
        if gameboard[n] != 0:
            prediction[0][n] = -999
        n = prediction.argmax()
        if gameboard[n] == 0:
            break
    return prediction.argmax()
