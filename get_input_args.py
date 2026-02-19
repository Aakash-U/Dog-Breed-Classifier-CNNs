"""Command-line argument parser for CNN image classifier."""
import argparse


def get_input_args():
    """
    Parse command-line arguments for the image classifier.
    
    Returns:
        argparse.Namespace: Parsed arguments containing:
            - dir: Path to image directory (default: 'pet_images')
            - arch: CNN architecture to use (default: 'resnet')
            - dogfile: Path to dog names file (default: 'dognames.txt')
    """
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir', type=str, default='pet_images', help = 'path to the folder of pet images')
    parser.add_argument('--arch', default='resnet', help='CNN model architecture')
    parser.add_argument('--dogfile', default='dognames.txt', help='text file with dog names')
    return parser.parse_args()