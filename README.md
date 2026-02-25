# CNN Dog Breed Classifier

A deep learning image classification system that identifies dog breeds using pretrained Convolutional Neural Networks (CNNs). This project compares three state-of-the-art architectures—ResNet, AlexNet, and VGG—to determine the most effective model for breed classification.

## Project Overview

This classifier addresses the challenge of distinguishing between dog breeds, dogs vs non-dogs, and evaluating model performance across different CNN architectures. By leveraging transfer learning with ImageNet-pretrained models, the system achieves high accuracy without requiring extensive training data or computational resources.

### Key Objectives
- Classify images as dog or non-dog with high precision
- Identify specific dog breeds from 133+ breed categories
- Compare performance across multiple CNN architectures
- Provide actionable insights on model selection for image classification tasks

## Results

Performance comparison across three CNN architectures on 40 test images (30 dogs, 10 non-dogs):

| Model | Dog Detection | Breed Accuracy | Non-Dog Detection | Overall Match | Runtime |
|-------|--------------|----------------|-------------------|---------------|---------|
| **VGG-16** | **100%** | **93.3%** | **100%** | **90.0%** | 2s |
| ResNet-18 | 100% | 90.0% | 100% | 85.0% | <1s |
| AlexNet | 100% | 80.0% | 100% | 77.5% | <1s |

**Winner: VGG-16** achieves the highest breed classification accuracy (93.3%) while maintaining perfect dog/non-dog detection.

### Key Findings
- All models achieved 100% accuracy in distinguishing dogs from non-dogs
- VGG-16 outperformed lighter models in breed-specific classification
- ResNet-18 offers the best speed-accuracy tradeoff
- AlexNet, while fastest, sacrifices breed accuracy

## Features

- **Multi-Architecture Support**: Compare ResNet, AlexNet, and VGG models
- **Transfer Learning**: Leverages ImageNet-pretrained weights
- **Automated Evaluation**: Calculates precision, accuracy, and performance metrics
- **Batch Processing**: Run all models sequentially for comprehensive comparison
- **Flexible Input**: Supports custom image directories and dog breed lists

## Technical Stack

- **Python 3.6+**
- **PyTorch**: Deep learning framework
- **torchvision**: Pretrained CNN models
- **Pillow**: Image processing

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/dog-breed-classifier.git
cd dog-breed-classifier
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

### Quick Start - Single Model
```bash
python check_images.py --dir pet_images --arch vgg --dogfile dognames.txt
```

**Arguments:**
- `--dir`: Path to image directory (default: `pet_images`)
- `--arch`: CNN architecture (`resnet`, `alexnet`, or `vgg`)
- `--dogfile`: Text file with valid dog breed names (default: `dognames.txt`)

### Compare All Models
```bash
./run_models.sh
```
Runs all three architectures and displays comparative results.

### Test Classifier
```bash
python test_classifier.py
```
Quick test with a sample image to verify setup.

## Project Structure

```
├── check_images.py              # Main classification pipeline
├── get_input_args.py            # Command-line argument parser
├── get_pet_labels.py            # Extract labels from filenames
├── classify_images.py           # CNN classification logic
├── adjust_results4_isadog.py    # Dog vs non-dog validation
├── calculates_results_stats.py  # Performance metrics calculation
├── print_results.py             # Results formatting and display
├── classifier.py                # Pretrained CNN model wrapper
├── test_classifier.py           # Standalone test script
├── run_models.sh                # Batch execution script
├── requirements.txt             # Python dependencies
├── dognames.txt                 # Valid dog breed names (133 breeds)
└── pet_images/                  # Sample test images (40 images)
```

## How It Works

### Pipeline Architecture

1. **Input Processing**: Parse command-line arguments and load image directory
2. **Label Extraction**: Extract ground truth labels from image filenames
3. **CNN Classification**: Pass images through pretrained CNN model
4. **Dog Validation**: Verify if predictions correspond to valid dog breeds
5. **Statistics Calculation**: Compute accuracy, precision, and performance metrics
6. **Results Display**: Output formatted results and runtime statistics

### Model Details

- **VGG-16**: 16-layer deep network, excellent feature extraction, higher computational cost
- **ResNet-18**: 18-layer residual network, skip connections prevent vanishing gradients
- **AlexNet**: 8-layer network, pioneering CNN architecture, fastest inference

All models use ImageNet pretrained weights and classify images into 1000 categories, with dog breeds mapped from a curated list of 133 breeds.

## Sample Output

```
*** Results Summary for CNN Model Architecture VGG ***
N Images            :  40
N Dog Images        :  30
N Not-Dog Images    :  10
 
pct_correct_dogs    : 100.0
pct_correct_breed   :  93.3
pct_correct_notdogs : 100.0
pct_match           :  90.0

** Total Elapsed Runtime: 0:0:2
```

## Insights and Learnings

- **Transfer Learning Effectiveness**: Pretrained models significantly reduce training time and data requirements
- **Architecture Tradeoffs**: Deeper networks (VGG) achieve higher accuracy but require more computation
- **Dog Detection vs Breed Classification**: All models excel at binary dog/non-dog classification, but breed-specific accuracy varies significantly
- **Real-World Application**: VGG-16 recommended for production use where accuracy is critical; ResNet-18 for resource-constrained environments

## Future Enhancements

- Add support for custom image uploads via web interface
- Implement fine-tuning on dog-specific datasets (Stanford Dogs, ImageNet Dogs)
- Integrate newer architectures (EfficientNet, Vision Transformers)
- Add confidence scores and top-k predictions
- Deploy as REST API or web application
- Expand to multi-label classification (breed + attributes)

## Author

**Aakash Upadhyay**
- GitHub: [@Aakash-U](https://github.com/Aakash-U)
- LinkedIn: [Aakash Upadhyay](https://www.linkedin.com/in/aakash-upadhyay-524347137/)

## Acknowledgments

This project was completed as part of the **AWS AI Scientist Nanodegree Program** by AWS/Udacity.

---

**Note**: This project demonstrates practical application of transfer learning and CNN architectures for image classification tasks.
