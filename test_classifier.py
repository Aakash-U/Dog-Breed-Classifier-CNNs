"""Test script to demonstrate classifier function usage.

Tests the pretrained CNN classifier with a sample image.
Supports model architectures: resnet, alexnet, vgg

Usage:
    python test_classifier.py
"""
from classifier import classifier


def main():
    """Test classifier with a sample dog image."""
    test_image = "pet_images/Collie_03797.jpg"
    model = "vgg"
    
    image_classification = classifier(test_image, model)
    
    print(f"\nClassifier Test Results:")
    print(f"Image: {test_image}")
    print(f"Model: {model}")
    print(f"Classification: {image_classification}")


if __name__ == "__main__":
    main()
