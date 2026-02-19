"""Print classification results and statistics."""


def print_results(results, results_stats_dic, model, 
                  print_incorrect_dogs = False, print_incorrect_breed = False):
    """
    Print summary statistics and optionally show misclassifications.
    
    Args:
        results: Dictionary with filename as key and list as value containing:
                 - index 0: pet image label
                 - index 1: classifier label
                 - index 2: match flag (1=match, 0=no match)
                 - index 3: pet is dog flag (1=dog, 0=not dog)
                 - index 4: classifier is dog flag (1=dog, 0=not dog)
        results_stats_dic: Dictionary of statistics (counts and percentages)
        model: CNN model architecture used ('resnet', 'alexnet', or 'vgg')
        print_incorrect_dogs: If True, print incorrectly classified dog/not-dog images
        print_incorrect_breed: If True, print incorrectly classified dog breeds
        
    Returns:
        None: Prints results to console
    """  
    print(f"\n\n*** Results Summary for CNN Model Architecture {model.upper()} ***")
    
    print("{:20}: {:3d}".format('N Images', results_stats_dic['n_images']))
    print("{:20}: {:3d}".format('N Dog Images', results_stats_dic['n_dogs_img']))
    print("{:20}: {:3d}".format('N Not-Dog Images', results_stats_dic['n_notdogs_img']))

    print(" ")
    for key in results_stats_dic:
        if key.startswith('p'):
            print("{:20}: {:5.1f}".format(key, results_stats_dic[key]))

    # Print misclassified dogs if requested
    if (print_incorrect_dogs and
        ((results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'])
         != results_stats_dic['n_images'])):
        print("\nINCORRECT Dog/NOT Dog Assignments:")
        for key in results:
            if ((results[key][3] == 1 and results[key][4] == 0) or
                (results[key][3] == 0 and results[key][4] == 1)):
                print("Real: {:>26}   Classifier: {:>30}".format(results[key][0], results[key][1]))

    # Print misclassified breeds if requested
    if (print_incorrect_breed and
        (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed'])):
        print("\nINCORRECT Dog Breed Assignment:")
        for key in results:
            if (sum(results[key][3:]) == 2 and results[key][2] == 0):
                print("Real: {:>26}   Classifier: {:>30}".format(results[key][0], results[key][1]))
