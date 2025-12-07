import time
import json
import random
from faker import Faker
import os

# Load scenes from JSON file
def load_scenes(filepath):
    base_path = os.path.dirname(__file__)  
    full_path = os.path.join(base_path, filepath)  
    with open(full_path, 'r') as f:
        return json.load(f)

# Display current scene text and choices
def display_scene(scene_data, game_state):
    text = scene_data['text']
    # Dynamic replacement for battery
    if '[BATTERY]' in text:
        text = text.replace('[BATTERY]', str(game_state['battery']))
    print("\n" + text)
    if 'choices' in scene_data:
        for idx, choice in enumerate(scene_data['choices'], start=1):
            print(f"{idx}. {choice['text']}")

# Get player's choice
def get_player_choice(scene_data):
    if 'choices' not in scene_data:
        input("(Press Enter to continue...)\n")
        return scene_data.get('next_scene', None)
    while True:
        try:
            print("\nYour choice:")
            choice = int(input("> ")) 
            if 1 <= choice <= len(scene_data['choices']):
                return scene_data['choices'][choice - 1]['next_scene']
            else:
                print("Invalid choice. Try again.")
        except ValueError:
            print("Invalid input. Enter a number.")

# Handle events and update game state
def handle_events(scene_data, game_state):
    if 'event' in scene_data:
        event = scene_data['event']
        print(f"\n-- Event Triggered: {event} --")
        if event == 'network_lost':
            game_state['network'] = 0
            print("Network signal lost!")
        elif event == 'insects_begin':
            game_state['insects'] += 1
            print("Insects start crawling on you...")
        elif event == 'insects_aggravated':
            game_state['insects'] += 2
            print("More insects are crawling aggressively!")
        elif event == 'breath_rapid':
            game_state['breath'] = max(0, game_state['breath'] - 5)
            print("Your breathing becomes rapid.")
        elif event == 'breath_critical':
            game_state['breath'] = max(0, game_state['breath'] - 10)
            print("You struggle to breathe!")
    if 'event_chance' in scene_data and random.random() < scene_data['event_chance']:
        print("A random bad event occurs...")
        game_state['insects'] += 1
        game_state['breath'] = max(0, game_state['breath'] - 2)

    if 'battery_drain' in scene_data:
        game_state['battery'] = max(0, game_state['battery'] - scene_data['battery_drain'])
        print(f"Battery now: {game_state['battery']}%")
        if game_state['battery'] == 0:
            print("Your phone has died.")
            game_state['alive'] = False
    if 'breath_drain' in scene_data:
        game_state['breath'] = max(0, game_state['breath'] - scene_data['breath_drain'])
        print(f"Breath remaining: {game_state['breath']}%")
        if game_state['breath'] == 0:
            print("You can no longer breathe.")
            game_state['alive'] = False

# Main game loop
def main():
    print("===================================")
    print("     WELCOME TO BURIED")
    print("        Try to survive...")
    print("===================================")
    time.sleep(2)  # Petite pause de 2 secondes pour le suspense
    print("Loading scenes...")
    scenes = load_scenes('scenes_buried.json')
    current_scene_id = 'start'
    game_state = {
        'battery': 12,
        'network': 1,
        'breath': 100,
        'insects': 0,
        'alive': True
    }
    fake = Faker()
    interlocutor_name = fake.name()

    while current_scene_id and game_state['alive']:
        scene = scenes[current_scene_id]
        # Handle dynamic names if needed
        if 'interlocutor' in scene and scene['interlocutor'] == 'random_name':
            scene['text'] = scene['text'].replace('Hello?', f"Hello, this is {interlocutor_name}.")
        display_scene(scene, game_state)
        handle_events(scene, game_state)
        if not game_state['alive']:
            break
        if 'end' in scene:
            print("\n--- The End ---")
            break
        current_scene_id = get_player_choice(scene)

    if not game_state['alive']:
        print("\n--- You have died... ---")

if __name__ == "__main__":
    main()
