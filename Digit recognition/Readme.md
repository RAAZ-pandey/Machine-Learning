# Handwritten Digit Recognition

This project implements a Handwritten Digit Recognition system using machine learning techniques. It is designed to classify digits from 0 to 9 based on image input from the popular MNIST dataset.

## Table of Contents

- [Overview](#overview)
- [Dataset](#dataset)
- [Model](#model)
- [Requirements](#requirements)
- [Installation](#installation)
- [How to Run](#how-to-run)
- [Results](#results)
- [Acknowledgements](#acknowledgements)

## Overview

This project builds and trains a model that can recognize handwritten digits using a neural network. The project goes through:
- Loading and visualizing the dataset
- Preprocessing the data
- Building and training the model
- Evaluating performance
- Making predictions

## Dataset

The project uses the **MNIST** dataset, which consists of:
- 60,000 training images
- 10,000 testing images
- Each image is a 28x28 grayscale image of a single digit (0-9)

## Model

The model is a simple feedforward neural network created using TensorFlow and Keras:
- Input layer: 784 neurons (flattened 28x28 image)
- Hidden layers: Dense layers with ReLU activation
- Output layer: 10 neurons with Softmax activation (for 10 classes)

Optimizer: `Adam`  
Loss function: `sparse_categorical_crossentropy`  
Metrics: `accuracy`



You can install the dependencies via:

```bash
pip install tensorflow numpy matplotlib jupyter
```

## Installation

1. Clone this repository:

   ```bash
   git clone https://github.com/your-username/handwritten-digit-recognition.git
   ```

2. Navigate into the project directory:

   ```bash
   cd handwritten-digit-recognition
   ```

3. Launch the Jupyter Notebook:

   ```bash
   jupyter notebook
   ```

## How to Run

- Open the `Handwritten_Digit_Recognition.ipynb` notebook.
- Run the cells sequentially to:
  - Load and visualize the data
  - Preprocess the images
  - Build and train the model
  - Evaluate the model
  - Predict new digits

## Results

The model achieves a high accuracy (around 98%) on the MNIST test set. Sample predictions and corresponding ground truths are displayed at the end of the notebook.

## Acknowledgements

- [MNIST Dataset](http://yann.lecun.com/exdb/mnist/)
- [TensorFlow Documentation](https://www.tensorflow.org/)
