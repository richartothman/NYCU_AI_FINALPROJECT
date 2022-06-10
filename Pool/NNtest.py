from copy import deepcopy
import tensorflow.keras
from itertools import chain
import pygad.kerasga
import numpy
import pygad
import pygame
import Pool
def UseModel(game,Model,full = False):
    
    allballpos = numpy.array([list(chain.from_iterable(game.getAllballPos()))])
    predictions = Model.predict(allballpos)
    game.ForcetoCue(predictions[0][0],predictions[0][1])
    while not game.isStopped():
        display = pygame.display.set_mode((Pool.width,Pool.height))
        if full:
            game.full_update()
        else:
            game.update()
        try:
            game.draw(display)
        except:
            pass
        pygame.display.flip()

def fitness_func(solution, sol_idx):
    global Game, keras_ga, model

    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model,
                                                                 weights_vector=solution)

    model.set_weights(weights=model_weights_matrix)
    test = deepcopy(Game)
    UseModel(test,model,True)
    if test.GameOver:
        solution_fitness = 0.000000000000000000000000001
    else:
        solution_fitness = test.getDistribution()

    return solution_fitness

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

Game = Pool.Game()
# model = tensorflow.keras.Sequential()
# # model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)
# model.add(tensorflow.keras.layers.Dense(16, activation="relu"))
# model.add(tensorflow.keras.layers.Dense(8, activation="relu"))
# model.add(tensorflow.keras.layers.Dense(2, activation="linear"))
# model.build((None,32))
# weights_vector = pygad.kerasga.model_weights_as_vector(model=model)

# keras_ga = pygad.kerasga.KerasGA(model=model,
#                                  num_solutions=20)
# print(keras_ga.population_weights)

# num_generations = 50
# num_parents_mating = 10
# initial_population = keras_ga.population_weights
# mutation_percent = 10
# crossover_type = "two_points"
# mutation_type = "random"
# keep_parents = 2
# ga_instance = pygad.GA( num_generations=num_generations, 
#                         num_parents_mating=num_parents_mating, 
#                         initial_population=initial_population,
#                         fitness_func=fitness_func,
#                         mutation_percent_genes=mutation_percent,
#                         crossover_type=crossover_type,
#                         mutation_type=mutation_type,
#                         # keep_parents=keep_parents,
#                         on_generation=callback_generation
#                       )
# ga_instance.run()

# # After the generations complete, some plots are showed that summarize how the outputs/fitness values evolve over generations.
# ga_instance.plot_result(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)

# # Returning the details of the best solution.
# solution, solution_fitness, solution_idx = ga_instance.best_solution()
# print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
# print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# # Fetch the parameters of the best solution.
# best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model,
#                                                               weights_vector=solution)
# model.set_weights(best_solution_weights)                                                              
# UseModel(Game,model)

# model.save("ALL_model\\test5")

# model = tensorflow.keras.models.load_model(
#     "ALL_model\\test4(best)")

# UseModel(Game,model)

