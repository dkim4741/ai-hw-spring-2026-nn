# ai-hw-spring-2026-nn

# MNIST Recognition by Neural Network

## Objective

Build a simple neural network to recognize handwritten digits using the MNIST dataset.

## Dataset Summary

The MNIST dataset consists of 70,000 28x28 black-and-white images of handwritten digits extracted from two NIST databases. There are 60,000 images in the training dataset and 10,000 images in the test dataset. The dataset contains ten classes representing the digits 0 through 9.

## Dataset

- MNIST Handwritten Digits Dataset
- Training Set: 60,000 images
- Test Set: 10,000 images
- Image Size: 28 × 28 pixels
- Number of Classes: 10

## Data Preprocessing

Before training, all images were converted into PyTorch tensors using the `ToTensor()` transform. Pixel values were normalized to the range [0,1], making the data suitable for neural network training.

## Model

A shallow Multi-Layer Perceptron (MLP) was used for digit classification.

## Architecture

```text
Input Image (28x28)
        ↓
Flatten (784)
        ↓
Linear Layer (784 → 128)
        ↓
ReLU Activation
        ↓
Linear Layer (128 → 10)
        ↓
Digit Prediction (0-9)
```

## Layer Description

- Flatten: Converts the 28×28 image into a 784-element vector.
- Linear Layer (784→128): Extracts useful features from the input.
- ReLU Activation: Introduces non-linearity into the network.
- Linear Layer (128→10): Produces output scores for each digit class.

## Training

The model was trained using the MNIST training dataset.

### Hyperparameters

- Epochs: 5
- Batch Size: 64
- Optimizer: Adam
- Loss Function: CrossEntropyLoss
- Learning Rate: 0.001

### Training Process

During each epoch, the model performs a forward pass, computes the loss, and updates its weights using the Adam optimizer through backpropagation.

## Evaluation

After training, the model was evaluated on the MNIST test dataset, which was not used during training.

The classification accuracy was calculated as:

```text
Accuracy = Correct Predictions / Total Predictions
```

## Results

- Test Accuracy: 97.22%

The model achieved over 97% accuracy on unseen test data, demonstrating that even a simple MLP can effectively classify handwritten digits in the MNIST dataset.

## Repository Structure

```text
model.py   - Defines the MLP architecture
train.py   - Trains the model using the MNIST training set
test.py    - Evaluates the model using the MNIST test set
```

## Conclusion

This project successfully implemented a simple neural network for handwritten digit recognition. The trained MLP achieved high classification accuracy and demonstrated the effectiveness of neural networks for image classification tasks.
