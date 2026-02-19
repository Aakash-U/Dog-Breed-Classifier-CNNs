"""Validate dog vs non-dog classifications."""

def adjust_results4_isadog(results, dogfile):
    """
    Determine if images are correctly classified as dog or not dog.
    
    Adds flags to results dictionary indicating whether the pet label and
    classifier label correspond to dog breeds.
    
    Args:
        results: Dictionary with filename as key and list as value.
                 Function extends each list with:
                 - index 3: pet is dog flag (1 if pet label is a dog breed, 0 otherwise)
                 - index 4: classifier is dog flag (1 if classifier label contains a dog breed, 0 otherwise)
        dogfile: Path to text file containing valid dog breed names (one per line, lowercase)
        
    Returns:
        None: Modifies results dictionary in-place
    """   
    dognames_dic = dict()

    # Load dog breed names from file
    with open (dogfile, 'r') as infile:
      for line in infile:
        line =line.rstrip()
        if line in dognames_dic:
          print("** Warning: Duplicate dog name", line)
        else:
          dognames_dic[line] = 1

    for filename in results:
        pet_label = results[filename][0]
        classifier_label = results[filename][1]
        
        # Check if pet label is a dog breed
        pet_is_dog = 1 if pet_label in dognames_dic else 0
        
        # Check if classifier label contains any dog breed
        classifier_is_dog = 0
        for dog_name in dognames_dic:
            if dog_name in classifier_label:
                classifier_is_dog = 1
                break
        
        results[filename].extend([pet_is_dog, classifier_is_dog])
