# Internship and Thesis Project

This repository contains the project related to my internship and thesis. The project includes written documentation (the thesis itself), images used in the documentation, and Python source code.

## Description

The project aims to reconstruct, based on an electrocardiogram (ECG), the signal that would ideally precede and follow it over time. This necessitated preliminary analysis of the ECGs under examination to subsequently define and train a convolutional neural network (CNN) using deep learning, enabling prediction of the ECG's evolution.\
Given that clinics still extensively use 10-second paper ECGs, where the first five seconds display the initial 6 leads of the ECG and the remaining five seconds show the remaining 6 leads, the goal was to reconstruct the leads not initially observed. Specifically, this involved reconstructing the first 6 leads in the latter five seconds and the second 6 leads in the initial five seconds, starting from the initial information available.\
The entire process was conducted using the Python programming language..

## Contents

- `thesis/`: Directory containing the main thesis document, images, and related files.
- `code/`: Directory with Python source code used in the project.
- `README.md`: This file, providing an overview of the project.
- `LICENSE`: The license file specifying the terms of use for the code and documentation.

## Installation

To run the code in this repository, it is recommended to follow this step:

- Clone the repository to your computer:

   ```bash
   git clone https://github.com/lucaarmetta/UseOfDeepLearningTechniquesForTheReconstructionOfElectrocardiographicSignals
   cd UseOfDeepLearningTechniquesForTheReconstructionOfElectrocardiographicSignals
