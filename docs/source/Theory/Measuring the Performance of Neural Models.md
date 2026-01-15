# Measuring the Performance of Neural Models

In this section we will review an article titled "Measuring the performance of neural models" by Dr. Oliver Schoppe et al. 

Aim of a computational neuroscientist is to create realistic model which describes the neural dynamics in relation to certain tasks or conditions. Reliable performance evaluation of these quantiative models is essemtial to decide whether the model is capable of capturing the underlying dynamics.

The response of neurons to sensory input can vary from trial to trial. This underlying variability could be linked with two main factors;

- Instrinsic neuronal variaiblity which is independent from sensory stimulus
- Variabilty of sensory stimuli across trials


If we want to build a model accurately explaining the complex relationship between response of the neuron and sensory stimulus, we have to keep in mind that variability stemming from both stimulus dependent and independent factors could undermine the model performance. Furthermore, we may also misunderstand the model's performance due to the metrics which quantify only the simple correlation between the model’s prediction and the raw neural response.





```{index} Algorithms; Normalized Correlation Coefficient
