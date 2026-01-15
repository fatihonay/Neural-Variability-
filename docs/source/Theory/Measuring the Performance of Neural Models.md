# Measuring the Performance of Neural Models

```{attention]
In this section we will review an article titled "Measuring the performance of neural models" by Dr. Oliver Schoppe et al. 
```

Aim of a computational neuroscientist is to create realistic model which describes the neural dynamics in relation to certain tasks or conditions. Reliable performance evaluation of these quantiative models is essemtial to decide whether the model is capable of capturing the underlying dynamics.

The response of neurons to sensory input can vary from trial to trial. This underlying variability could be linked with two main factors;

- Instrinsic neuronal variaiblity which is independent from sensory stimulus
- Variabilty of sensory stimuli across trials


If we want to build a model accurately explaining the complex relationship between response of the neuron and sensory stimulus, we have to keep in mind that variability stemming from both stimulus dependent and independent factors could undermine the model performance. Furthermore, we may also misunderstand the model performance due to the metrics which quantify only the simple correlation between the model’s prediction and the raw neural response. There are two possibilities in evaluating the results in the case of the bad performance, correlation coeﬃcient of 0.5;

 - the noisy dataset with perfect model
 - the poor model with dataset of very low noise

```{note}
The aim is to measure correlation between model-predicted responses ŷ  and actual neuron-recorded responses y. The correlation coefficient measures how well these two match. A value of 1 means perfect prediction, 0 means no relationship.
```

This situation obviously hinders us to interpret what the underlying problem with established model. 





```{index} Algorithms; Normalized Correlation Coefficient
