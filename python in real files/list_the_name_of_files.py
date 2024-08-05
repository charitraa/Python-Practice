import os


def get_image_files(folder_path):
    # Define the valid image file extensions
    valid_extensions = ('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff')

    # Get a list of all files in the specified folder
    all_files = os.listdir(folder_path)

    # Filter the list to include only image files
    image_files = [
        file for file in all_files if file.lower().endswith(valid_extensions)]

    return image_files


# Specify the path to the folder containing the images
folder_path = 'C:\\Programers\\Code\\SAT\\Assets\\image\\images'

# Get the list of image files
image_files = get_image_files(folder_path)

# Print the list of image files
print(image_files)
