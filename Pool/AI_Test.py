import tensorflow.keras
from itertools import chain
import numpy
import pygame
import Pool
import os
from math import pi

from keras import backend as BK
def mapping_to_target_range( x, target_min=0, target_max=(2*pi) ) :
    return  x/1000

def UseModel(game,Model,full = False,draw = True):
    
    allballpos = numpy.array([list(chain.from_iterable(game.getAllballPos()))])
    predictions = Model.predict(allballpos)
    game.ForcetoCue(predictions[0][0],2)
    while not game.isStopped():

        if full:
            game.full_update()
        else:
            game.update()
        if draw:
            display = pygame.display.set_mode((Pool.width,Pool.height))
            try:
                game.draw(display)
            except:
                pass
            pygame.display.flip()

if __name__ == '__main__':
    ModelID = 1655022538
    model = tensorflow.keras.Sequential()
    model.add(tensorflow.keras.layers.Dense(16, activation="relu"))
    model.add(tensorflow.keras.layers.Dense(8, activation="relu"))
    model.add(tensorflow.keras.layers.Dense(1, activation=mapping_to_target_range))
    model.build((None,32))

    MoveNum = len(os.listdir(".\\ALL_model\\"+str(ModelID)))

    NewGame = Pool.Game()

    for i in range(1,MoveNum+1):
        tensorflow.keras.utils.get_custom_objects().update({'mapping_to_target_range': tensorflow.keras.layers.Activation(mapping_to_target_range)})
        Testmodel = tensorflow.keras.models.load_model(
            "ALL_model\\"+str(int(ModelID))+"test\\"+str(i)+"\\best.h5")                                          
        UseModel(NewGame,Testmodel)
        # Testmodel.save("ALL_model\\"+str(int(ModelID))+"test\\"+str(i)+"\\best.h5")

