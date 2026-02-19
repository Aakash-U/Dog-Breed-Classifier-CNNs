"""Extract pet labels from image filenames."""
from os import listdir


def get_pet_labels(images_dir):
    """
    Create dictionary of pet labels from image filenames.
    
    Extracts pet names from filenames by removing numbers and file extensions,
    converting to lowercase. Example: 'Boston_terrier_02259.jpg' -> 'boston terrier'
    
    Args:
        images_dir: Path to folder containing pet images
        
    Returns:
        dict: Mapping of filename to list containing pet label at index 0
              Example: {'Boston_terrier_02259.jpg': ['boston terrier']}
    """
    results = {}
    filename_list = listdir(images_dir)

    for filename in filename_list:
        # Skip hidden files
        if filename[0] != ".":
            # Extract alphabetic words from filename
            pet_name = filename.split(".")[0].lower()
            word_list = pet_name.split("_")
            pet_label = " ".join(word for word in word_list if word.isalpha())

            if filename not in results:
                results[filename] = [pet_label]
            else:
                print(f"** Warning: Duplicate file in directory: {filename}")

    return results
