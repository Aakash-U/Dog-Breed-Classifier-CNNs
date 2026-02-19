#!/bin/bash
# Run CNN Image Classifier with all three model architectures

echo "=========================================="
echo "CNN Dog Breed Classifier - Batch Run"
echo "=========================================="
echo ""

# Run with ResNet
echo "Running with ResNet architecture..."
python check_images.py --dir pet_images --arch resnet --dogfile dognames.txt
echo ""
echo "=========================================="
echo ""

# Run with AlexNet
echo "Running with AlexNet architecture..."
python check_images.py --dir pet_images --arch alexnet --dogfile dognames.txt
echo ""
echo "=========================================="
echo ""

# Run with VGG
echo "Running with VGG architecture..."
python check_images.py --dir pet_images --arch vgg --dogfile dognames.txt
echo ""
echo "=========================================="
echo "All models completed!"
