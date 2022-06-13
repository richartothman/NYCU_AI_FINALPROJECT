from copy import deepcopy
import tensorflow.keras
from itertools import chain
import pygad.kerasga
import numpy
import pygad
import pygame
import Pool
import time
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

def fitness_func(solution, sol_idx):
    global Game, keras_ga, model, curTime, curIndex , maxfitness, Best

    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model,
                                                                 weights_vector=solution)

    model.set_weights(weights=model_weights_matrix)
    test = deepcopy(Game)
    UseModel(test,model,True)
    if test.GameOver:
        solution_fitness = 0.000000000000000000000000001
    else:
        solution_fitness = test.getDistribution()
    if solution_fitness > maxfitness:
        maxfitness = solution_fitness
        Best = model_weights_matrix
    
    return solution_fitness

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=maxfitness))

    
if __name__ == '__main__':
    curTime = time.time()
    Game = Pool.Game()
    model = tensorflow.keras.Sequential()
    model.add(tensorflow.keras.layers.Dense(16, activation="relu"))
    model.add(tensorflow.keras.layers.Dense(8, activation="relu"))
    model.add(tensorflow.keras.layers.Dense(1, activation=mapping_to_target_range))
    model.build((None,32))

    tensorflow.keras.utils.get_custom_objects().update({'mapping_to_target_range': tensorflow.keras.layers.Activation(mapping_to_target_range)})
    # for i in range(1,14+1):
    #     Testmodel = tensorflow.keras.models.load_model(
    #         "ALL_model\\"+str(int(curTime))+"\\"+str(i)+"\\best")
    #     UseModel(Game,Testmodel)    
    curTime = time.time()
    maxfitness = 0
    curIndex = 1
    solution_fitness = 0

    best_solution_weights = None
    prevbest = 0
    while solution_fitness < 15:
        weights_vector = pygad.kerasga.model_weights_as_vector(model=model)

        keras_ga = pygad.kerasga.KerasGA(model=model,
                                        num_solutions=50)
        Best = best_solution_weights
        num_generations = 5
        num_parents_mating = 24
        initial_population = keras_ga.population_weights
        mutation_percent = 10
        crossover_type = "two_points"
        mutation_type = "random"
        keep_parents = 5
        ga_instance = pygad.GA( num_generations=num_generations, 
                                num_parents_mating=num_parents_mating, 
                                initial_population=initial_population,
                                fitness_func=fitness_func,
                                mutation_percent_genes=mutation_percent,
                                crossover_type=crossover_type,
                                mutation_type=mutation_type,
                                on_generation=callback_generation
                            )
        ga_instance.run()

        # Returning the details of the best solution.

        solution, solution_fitness, solution_idx = ga_instance.best_solution()
        print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
        print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

        # Fetch the parameters of the best solution.
        best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model,
                                                                    weights_vector=solution)
        model.set_weights(best_solution_weights)
        model.save("ALL_model\\"+str(int(curTime))+"\\"+str(curIndex)+"\\best.h5")    
        UseModel(Game,model,True,False)
        NewGame = Pool.Game()         
        for i in range(1,curIndex+1):
            try:
                Testmodel = tensorflow.keras.models.load_model(
                    "ALL_model\\"+str(int(curTime))+"\\"+str(i)+"\\best.h5")
                UseModel(NewGame,Testmodel)            
            except IOError:
                pass   
        curIndex += 1

