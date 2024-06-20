# Use of deep learning techniques for the reconstruction of electrocardiographic signals

## Abstract

### ECG

Electrocardiography (ECG) is a common, non-invasive diagnostic procedure that records the heart's electrical activity via electrodes, with algorithmic support enhancing interpretation. Advances in automated ECG analysis have been hindered by inadequate training datasets and evaluation procedures for algorithm consistency. Standard ECGs use 12 leads from electrodes placed on the limbs and thorax, capturing the heart's electrical potentials through depolarization (heart cells changing from negative to positive) and repolarization (returning to negative). Accurate ECG interpretation requires high-quality 12-lead recordings and a systematic approach. ECGs can detect various heart conditions, such as arrhythmias, myocardial infarctions, and coronary heart disease, and can continuously monitor patients over a day to assess heart rhythm changes and detect events like tachycardia or bradycardia.

### Vectorcardiographic Lead Systems

Frank’s signals represent an electrocardiographic method providing detailed spatial information on the heart’s electrical activity. This non-invasive procedure uses electrodes placed on the chest to cover different heart regions, offering a more comprehensive map of cardiac activity compared to standard 12-lead ECGs. This method enhances the assessment of electrical impulse morphology and detects abnormalities and disorders. Frank’s signals correlate significantly with three-dimensional X, Y, and Z leads, providing a spatial representation of the heart’s electrical activity. By using a linear transformation and the Dower inverse matrix, a 12-lead ECG can estimate ECG readings with Frank’s derivations, thereby obtaining detailed weighted signals through matrix multiplication.

### Artificial Intelligence and Deep Learning

The field of ECG analysis has been significantly transformed by deep learning techniques, particularly convolutional and recurrent neural networks, which have improved the accuracy and efficiency of diagnosing heart conditions. Convolutional neural networks (CNNs) are effective in classifying cardiac arrhythmias by learning relevant features from data, while recurrent neural networks (RNNs) model temporal dependencies in ECGs for detecting abnormalities and predicting cardiac events.\
A crucial element for deep learning in ECG analysis is the availability of large, high-quality training datasets with expert-annotated ECG records, enabling neural networks to learn from past cases. However, collecting and annotating these datasets is challenging, requiring significant human effort and collaboration.\
The application of deep learning in ECG analysis presents opportunities and challenges, such as network robustness to signal changes, explicability of decisions, and customization for different clinical contexts. The scarcity of labeled data, due to the need for expert annotation and the variability in ECGs among patients, complicates the training of neural networks to generalize effectively.\
Proper ECG pre-processing is essential to improve signal quality by eliminating noise and preparing data for analysis. This involves filtering techniques to remove unwanted noise from electrical interference or muscle movements, resulting in a cleaner signal that aids in identifying significant patterns and anomalies.\
Despite these challenges, the combination of medical expertise and deep learning is yielding promising results, enabling more accurate, timely, and personalized diagnoses for heart disease patients. The integration of deep learning into clinical practice requires careful consideration of risks, safety, and ethics, but ongoing research and collaboration between doctors and researchers are paving the way for significant advancements in ECG analysis and cardiology.

### Research Goal

The research aimed to reconstruct the ECG signal before and after the recorded time, utilizing deep learning techniques. The process involved a preliminary analysis of the ECGs to define and train a convolutional neural network (CNN) capable of predicting the ECG's evolution. Clinics often use ten-second paper ECGs, with the first five seconds displaying the first six leads and the remaining five seconds showing the last six leads. The goal was to reconstruct the unobserved leads: predicting the first six leads for the second five seconds and the last six leads for the first five seconds, based on the available initial information.

## Methods and Materials Used

### Dataset

The dataset used for the research is the PTB-XL, an extensive ECG dataset developed in Germany, featuring high-resolution signal recordings from patients with various heart conditions. Created for research purposes, it includes a wide range of signals, including 12-lead and 15-lead data, from both healthy patients and those with heart abnormalities. This makes it a valuable resource for deep learning and AI experts in cardiology, providing ample data for training and evaluating neural networks for diagnosing and classifying heart disease.\
PTB-XL contains 21,799 12-lead ECGs from 18,869 patients, each with a duration of 10 seconds. The raw waveform data is annotated by cardiologists with multiple ECG statements per record, adhering to the SCP-ECG standard. These statements include diagnostic, form, and rhythm information. Additionally, the dataset includes detailed metadata on demographics, heart attack features, diagnostic statement probabilities, and reported properties. Data collection spanned from October 1989 to June 1996, with an optimized version published in 2019 for better usability and accessibility for the deep learning community. The waveforms and metadata were converted into formats compatible with standard software.\
The dataset offers two versions for each ECG, one with a sampling frequency of 100 Hz and another with 500 Hz. For this research, the ECGs with a 100 Hz sampling rate were selected.

### Signal Selection and Filtering

To ensure the dataset used for analysis included only ECGs from healthy patients, several filtering steps were implemented. Initially, minimum and maximum frequencies of 0.5 Hz and 15 Hz were set to determine low and high cut frequencies for filtering. These parameters were applied in a Butterworth filter to maintain a flat frequency response within the desired bandwidth. Following this initial filtering, Gustafson filtering was then applied to each ECG. This technique aimed to further enhance signal quality by reducing noise and unwanted interference, particularly at the signal edges.\
The filtering process utilized "filtfilt" or zero-phase filtering, which processes the signal to attenuate unwanted components while preserving the time delay between different signal frequencies. Zero-phase filtering effectively removes the delay in the filtered signal, ensuring a more accurate representation of the original signal. This capability is crucial in contexts where maintaining the temporal relationships between signal frequencies is essential for detailed analysis, as in this research.

### Inverse Dower Transformation

Inverse Dower transformation is a process used in ECG analysis to convert a spatial representation of heart signals back into the original temporal and amplitude domain. Initially, Dower's transformation projects ECG signals onto orthogonal axes known as Frank’s leads, which represent the directions of electrical flow through the heart. The reverse transformation allows the recovery of the original signals from their spatial representation according to Frank’s leads. This process enables the visualization of ECG signals as temporal paths of voltage variations over time, providing a standard view of the heart's electrical activity.

### Entropy

Matrix entropy quantifies the complexity or uncertainty within a distribution. A uniform distribution exhibits maximum entropy, while a constant distribution has zero entropy. Higher entropy indicates greater diversity in the data.\
The objective was to reconstruct six signals from the frontal plane using the six signals from the horizontal plane, implying an inability to directly determine each frontal signal from its corresponding horizontal counterpart. However, Frank's X, Y, and Z derivations could be projected onto a two-dimensional plane to construct histograms. These histograms serve as probability density estimates, facilitating entropy calculation to assess predictability.\
Subsequently, two-dimensional distributions were computed from each histogram relative to every ECG. These distributions provided a comprehensive view over time, with breakdowns across the X, Y, and Z axes to identify distribution cells crucial for entropy calculation.\
Entropy was computed using various formulas, including a generalized version of Shannon's formula adapted for probability matrices. Additionally, a specific formula yielded a predictability index ranging from 0 to 1. A predictability index of 0 signifies a perfectly unpredictable uniform distribution, whereas an index of 1 indicates a completely predictable constant distribution. This index provided a numeric measure of how predictable the distributions were within the dataset.
