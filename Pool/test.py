import tensorflow.keras
import pygad.kerasga
import numpy
import pygad

def fitness_func(solution, sol_idx):
    global data_inputs, data_outputs, keras_ga, model

    model_weights_matrix = pygad.kerasga.model_weights_as_matrix(model=model,
                                                                 weights_vector=solution)

    model.set_weights(weights=model_weights_matrix)

    predictions = model.predict(data_inputs)

    mae = tensorflow.keras.losses.MeanAbsoluteError()
    abs_error = mae(data_outputs, predictions).numpy() + 0.00000001 #change this into fitness for distance of every ball
    solution_fitness = 1.0 / abs_error

    return solution_fitness

def callback_generation(ga_instance):
    print("Generation = {generation}".format(generation=ga_instance.generations_completed))
    print("Fitness    = {fitness}".format(fitness=ga_instance.best_solution()[1]))

# input_layer  = tensorflow.keras.layers.Input(3)
# dense_layer1 = tensorflow.keras.layers.Dense(5, activation="relu")(input_layer)
# dense_layer2 = tensorflow.keras.layers.Dense(4, activation="relu")(dense_layer1)
# output_layer = tensorflow.keras.layers.Dense(2, activation="linear")(dense_layer2)
model = tensorflow.keras.Sequential()
# model = tensorflow.keras.Model(inputs=input_layer, outputs=output_layer)
model.add(tensorflow.keras.layers.Dense(6, activation="relu"))
model.add(tensorflow.keras.layers.Dense(3, activation="relu"))
model.add(tensorflow.keras.layers.Dense(2, activation="linear"))
model.build((None, 3))
weights_vector = pygad.kerasga.model_weights_as_vector(model=model)

keras_ga = pygad.kerasga.KerasGA(model=model,
                                 num_solutions=100)

# Data inputs
data_inputs = numpy.array([[0.02, 0.1, 0.15],
                           [0.7, 0.6, 0.8],
                           [1.5, 1.2, 1.7],
                           [3.2, 2.9, 3.1]])

# Data outputs
data_outputs = numpy.array([[0.1,0.13],
                            [0.6,0.5],
                            [1.3,1.9],
                            [2.5,3.0]])

num_generations = 100
num_parents_mating = 10
initial_population = keras_ga.population_weights
mutation_percent = 10
crossover_type = "two_points"
mutation_type = "random"
keep_parents = 10
ga_instance = pygad.GA( num_generations=num_generations, 
                        num_parents_mating=num_parents_mating, 
                        initial_population=initial_population,
                        fitness_func=fitness_func,
                        mutation_percent_genes=mutation_percent,
                        crossover_type=crossover_type,
                        mutation_type=mutation_type,
                        # keep_parents=keep_parents,
                    #   on_generation=callback_generation
                      )
ga_instance.run()

# After the generations complete, some plots are showed that summarize how the outputs/fitness values evolve over generations.
ga_instance.plot_result(title="PyGAD & Keras - Iteration vs. Fitness", linewidth=4)

# Returning the details of the best solution.
solution, solution_fitness, solution_idx = ga_instance.best_solution()
print("Fitness value of the best solution = {solution_fitness}".format(solution_fitness=solution_fitness))
print("Index of the best solution : {solution_idx}".format(solution_idx=solution_idx))

# Fetch the parameters of the best solution.
best_solution_weights = pygad.kerasga.model_weights_as_matrix(model=model,
                                                              weights_vector=solution)
model.set_weights(best_solution_weights)
predictions = model.predict(data_inputs)
print("Predictions : \n", predictions)

mae = tensorflow.keras.losses.MeanAbsoluteError()
abs_error = mae(data_outputs, predictions).numpy()
print("Absolute Error : ", abs_error)