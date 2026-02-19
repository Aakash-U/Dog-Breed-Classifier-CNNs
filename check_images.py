"""CNN Image Classifier for Pet Breed Identification.

Classifies pet images using pretrained CNN models and evaluates performance
against true labels extracted from image filenames.
"""
from time import time

from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results


def main():
    """
    Execute the CNN image classification pipeline.
    
    Pipeline:
        1. Parse command-line arguments (directory, model architecture, dog file)
        2. Extract pet labels from image filenames
        3. Classify images using pretrained CNN
        4. Validate dog vs non-dog classifications
        5. Calculate and display performance statistics
    """
    start_time = time()

    # Parse command-line arguments
    in_arg = get_input_args()

    # Extract pet labels from image filenames 
    results = get_pet_labels(in_arg.dir)

    # Classify images using pretrained CNN model
    classify_images(in_arg.dir, results, in_arg.arch)

    # Validate dog vs non-dog classifications
    adjust_results4_isadog(results, in_arg.dogfile)

    # Calculate performance statistics
    results_stats = calculates_results_stats(results)

    # Display results
    print_results(results, results_stats, in_arg.arch, False, False)
    
    end_time = time()
    
    # Print total runtime
    tot_time = end_time - start_time
    print("\n** Total Elapsed Runtime:",
          str(int((tot_time/3600)))+":"+str(int((tot_time%3600)/60))+":"
          +str(int((tot_time%3600)%60)) )


if __name__ == "__main__":
    main()