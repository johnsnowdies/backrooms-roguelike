from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app = Ursina()

# Create the four walls and the floor of the room
Entity(model='cube', color=color.white, scale=(10,0.5,10), position=(0,-0.25,0))  # Floor
Entity(model='cube', color=color.green, scale=(10,0.5,0.5), position=(0,0,5))     # Wall 1
Entity(model='cube', color=color.green, scale=(10,0.5,0.5), position=(0,0,-5))    # Wall 2
Entity(model='cube', color=color.green, scale=(0.5,0.5,10), position=(5,0,0))     # Wall 3
Entity(model='cube', color=color.green, scale=(0.5,0.5,10), position=(-5,0,0))    # Wall 4

# Create a first person controller
player = FirstPersonController()

app.run()
