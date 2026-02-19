"""Image classification using pretrained CNN models."""
from classifier import classifier 


def classify_images(images_dir, results, model):
    """
    Classify images using CNN and compare with pet labels.
    
    Adds classifier predictions to results dictionary and compares them with
    pet labels extracted from filenames.
    
    Args:
        images_dir: Path to folder containing images
        results: Dictionary with filename as key and list as value.
                 Function extends each list with:
                 - index 1: classifier label (lowercase, stripped)
                 - index 2: match flag (1 if pet label in classifier label, 0 otherwise)
        model: CNN architecture to use ('resnet', 'alexnet', or 'vgg')
        
    Returns:
        None: Modifies results dictionary in-place
    """
    for filename in results:
        image_path = images_dir + "/" + filename
        classifier_label = classifier(image_path, model).lower().strip()
        pet_label = results[filename][0]
        
        # Check if pet label matches classifier prediction
        match = 1 if pet_label in classifier_label else 0
        results[filename].extend([classifier_label, match])
