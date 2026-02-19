"""Calculate performance statistics for image classification results."""


def calculates_results_stats(results):
    """
    Calculate statistics from classification results.
    
    Computes counts and percentages for correct classifications of dogs,
    non-dogs, and breed matches.
    
    Args:
        results: Dictionary with filename as key and list as value containing:
                 - index 0: pet image label
                 - index 1: classifier label
                 - index 2: match flag (1=match, 0=no match)
                 - index 3: pet is dog flag (1=dog, 0=not dog)
                 - index 4: classifier is dog flag (1=dog, 0=not dog)
    
    Returns:
        dict: Statistics dictionary with counts (n_*) and percentages (pct_*):
              - n_images: Total number of images
              - n_dogs_img: Number of dog images
              - n_notdogs_img: Number of non-dog images
              - n_correct_dogs: Correctly classified as dog
              - n_correct_notdogs: Correctly classified as not dog
              - n_correct_breed: Correctly classified breed
              - n_match: Total label matches
              - pct_correct_dogs: Percentage of correct dog classifications
              - pct_correct_notdogs: Percentage of correct non-dog classifications
              - pct_correct_breed: Percentage of correct breed classifications
              - pct_match: Percentage of label matches
    """
    # Initialize counters
    results_stats_dic = {}
    n_images = 0
    n_dogs_img = 0
    n_correct_dogs = 0
    n_correct_notdogs = 0
    n_correct_breed = 0
    n_match = 0

    # Count statistics from results
    for filename in results:
        n_images += 1
        if results[filename][2] == 1:
            n_match += 1
        if results[filename][3] == 1:
            n_dogs_img += 1
            if results[filename][2] == 1:
                n_correct_breed += 1
        if results[filename][3] == 1 and results[filename][4] == 1:
            n_correct_dogs += 1
        if results[filename][3] == 0 and results[filename][4] == 0:
            n_correct_notdogs += 1

    n_notdogs_img = n_images - n_dogs_img

    # Store counts
    results_stats_dic['n_images'] = n_images
    results_stats_dic['n_dogs_img'] = n_dogs_img
    results_stats_dic['n_notdogs_img'] = n_notdogs_img
    results_stats_dic['n_correct_dogs'] = n_correct_dogs
    results_stats_dic['n_correct_notdogs'] = n_correct_notdogs
    results_stats_dic['n_correct_breed'] = n_correct_breed
    results_stats_dic['n_match'] = n_match

    # Calculate percentages
    if n_dogs_img > 0:
        results_stats_dic['pct_correct_dogs'] = (n_correct_dogs / n_dogs_img) * 100.0
        results_stats_dic['pct_correct_breed'] = (n_correct_breed / n_dogs_img) * 100.0
    else:
        results_stats_dic['pct_correct_dogs'] = 0.0
        results_stats_dic['pct_correct_breed'] = 0.0

    if n_notdogs_img > 0:
        results_stats_dic['pct_correct_notdogs'] = (n_correct_notdogs / n_notdogs_img) * 100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
    results_stats_dic['pct_match'] = (n_match / n_images) * 100.0
    
    return results_stats_dic
