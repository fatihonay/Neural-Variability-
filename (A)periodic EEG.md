Neural activity mainly consists of two major components;
 - Peridodic oscillatory activity 
 - Aperiodic non-oscillatory activity 

This separation is important because it provides us to reveal systematic changes in brain function within different conditions. In this 
session, I will review an article titled "Parameterizing neural power spectra into periodic and aperiodic components" which is published
in Nature Neuroscience. 

The power spectrum of neurophysilogical signals is informative about which oscillatory components contribute to neural activity. However,  estimation of power spectrum could be conflated by aperiodic non-oscillatory neural activity. In order to deal with this problem, the  authors developed an algorithm to systematically separate periodic and aperiodic component related power spectrum. 

At this point, I want to ask a question for you to think.
- What functional roles do oscillations play in brain and why do detection of these oscillations important for us ?

I will return back to this question in the end of this session. However, keep in mind what we deal with is a valuable problem. Now observe the figure below and try to see what happens.

<img width="935" height="278" alt="Aperiodic" src="https://github.com/user-attachments/assets/da0d749c-e497-41ac-b15d-5892abc515f4" />

As you can see, there are a few terms describing the properties of the PSD associated with neural activity. Let's clearly define key terms that will enhance our insight. 
- Aperiodic Exponent: Shows the how steep background neural activity is. The level of steepnes or flatness can indicate different physiological states, such as the balance between excitation and inhibition.
- Center Frequency: The specific narrow-band oscillatory component with a peak at center frequency.

Now, let's emphasize how chages in oscillatory power could be associated with different mechanisms rather than simple power change of neural oscillations. The broadband shift and exponent change of aperiodic component results in altered oscillattory peak. However, this is misleading ant not reflect reality. This simple illustrative example simply explaing why we need to model the estmation of both components separately. 

<img width="1170" height="341" alt="Screenshot 2026-01-13 at 14 28 48" src="https://github.com/user-attachments/assets/75d9e8b3-d252-4737-bbaf-2ff161edd1b3" />



The effective way of getting information from both periodic and aperiodic PDS compoents is to parameterize them. Thus, we can easily describe changes of PSD using a few parameters. This will enables us to compare different conditions, cohorts, poopulations, subjects and so on. For this purpose, we can use the followin parameters;

- Periodic Componenet Parameters: Center frequency, bandwidth, power
- Aperiodic Component Parameters: Aperiodic exponent and aperiodic offset

## The Proposed Method

- 1st Step: Perform curve fitting on estimated PSD to characterize aperiodic component. Then, subtract fitted curve from original PSD (a and b in the figure below)
- 2nd Step: Fit Gaussian around the peak of the remaining spectrum and subtract the Gaussian fit. If there are another peaks, continue to subtract them until no peaks remain.
- 3th Step: Gaussians are removed from original PSD to reveal aperiodic component alone and curve fitting is peformed on the aperiodic component.
- 4th Step: This re-fit aperiodic component is combined with the multi-Gaussian model to give the final fit.


<img width="854" height="573" alt="Method" src="https://github.com/user-attachments/assets/80e60c35-04d8-4814-9a87-fcb7927e2316" />









