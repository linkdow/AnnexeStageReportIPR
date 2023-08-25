import pygame
import sys
import os
import pandas as pd
from PIL import Image
import numpy as np

pygame.init()

pygame.display.set_caption("Image Sorting Game")

SCREEN_UPDATE = pygame.USEREVENT
WHITE = (255, 255, 255)

# Define a font and font size
font = pygame.font.Font(None, 36)  # You can choose the font and size you prefer


# Screen
SCREEN_WIDTH, SCREEN_HEIGHT = 1280, 720
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

def load_image(folder_path):
    image = Image.open(folder_path)
    image = image.resize((420,420))
    image = np.array(image)
    surface = pygame.surfarray.make_surface(image)
    return surface

def load_mask(folder_path):
    image = Image.open(folder_path)
    image = image.resize((420,420))
    image = np.array(image) * 255
    surface = pygame.surfarray.make_surface(image)
    return surface

def display_text(message,coordinates=(0,0),color=(0,0,0)):
    # Display the message on the screen
    text_surface = font.render(message, True, color) 
    screen.blit(text_surface, coordinates)

def list_images_in_folder(folder_path):
    return [os.path.join(folder_path,f) for f in os.listdir(folder_path) if f.endswith('.jpg') or f.endswith('.png')]

def save_to_csv(list_decisions,left_list,right_list,index):
    df = pd.DataFrame()
    df["left_paths"] = left_list[:index]
    df["right_paths"] = right_list[:index]
    df["decisions"] = list_decisions
    
    df.to_csv(os.path.join("H:/Python/sortgame","decisions.csv"),sep=";")

def main():
    left_path = r"H:\Datasets\Siamois_62_5\images\2017"
    right_path = r"H:\Datasets\Siamois_62_5\images\2021"

    left_list = list_images_in_folder(left_path)
    right_list = list_images_in_folder(right_path)

    # Assuming both folders have the same number of images
    num_images = min(len(left_list), len(right_list))
    index = 0
    running = True
    sorting_decisions = []  # A list to store the sorting decisions
    Undo_first_image = False
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_to_csv(sorting_decisions,left_list,right_list,index)
                running = False
            elif event.type == pygame.KEYDOWN:
                Undo_first_image = False
                if event.key == pygame.K_LEFT:
                    print("Sorted left")
                    sorting_decisions.append((index, 'left'))  # Store the sorting decision
                    index += 1
                elif event.key == pygame.K_RIGHT:
                    print("Sorted right")
                    sorting_decisions.append((index, 'right'))  # Store the sorting decision
                    index += 1
                elif event.key == pygame.K_r:
                    if index == 0:
                        print("Can't undo for first image")
                        Undo_first_image = True
                    else:
                        index -= 1
                        sorting_decisions.pop()
                elif event.key == pygame.K_s:
                    print("Saving results")
                    save_to_csv(sorting_decisions,left_list,right_list,index)
                if index >= num_images:
                    save_to_csv(sorting_decisions,left_list,right_list,index)
                    # running = False

        # Clear the screen
        screen.fill(WHITE)

        if Undo_first_image:
            display_text("Can't undo for first image")

        # Display the current image pair
        image1 = load_image(left_list[index])
        image2 = load_image(right_list[index]) # * 255 uncomment if mask
        screen.blit(image1, (100, 100))
        screen.blit(image2, (600, 100))


        
        # Display the message on the screen
        message = "Press LEFT or RIGHT to sort, R to undo, S to save results"
        text_surface = font.render(message, True, (0, 0, 0))  # (0, 0, 0) represents black color
        screen.blit(text_surface, (100, 600))  # You can adjust the position of the message

        # Display the message on the screen
        message = "Something changed ? LEFT for NO, RIGHT for YES"
        text_surface = font.render(message, True, (0, 0, 0))  # (0, 0, 0) represents black color
        screen.blit(text_surface, (160, 50))  # You can adjust the position of the message

        # Display the remaining images count on the screen
        remaining_images = num_images - index
        remaining_message = f"Images left to sort: {remaining_images}"
        remaining_surface = font.render(remaining_message, True, (0, 0, 0))  # (0, 0, 0) represents black color
        screen.blit(remaining_surface, (50, 550))  # You can adjust the position of the message

        pygame.display.flip()

    pygame.quit()

if __name__ == "__main__":
    main()