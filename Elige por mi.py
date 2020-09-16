
import random



Lista_Restaurantes = ["La Birra Bar","Kevin Bacon", "El Club de la Birra","Big Pons", "Mi Barrio", "Wunderbar", "Fat Broders", "Tierra de Nadie"]

random.shuffle(Lista_Restaurantes)

print("Los restaurantes disponibles son: ", Lista_Restaurantes)

print("El restaurante seleccionado es: ", (random.sample(Lista_Restaurantes, 1)))
          
    
