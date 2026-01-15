`{index} Algorithms; FOOOF`

# Fitting Oscillations & One Over F

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


<img width="526" height="390" alt="Methodology" src="https://github.com/user-attachments/assets/1f8874be-0e78-4fca-b573-af175e8ad8d5" />


## The Core Algorithm

The power spectrum is modeled as:

$$
PSD = L + \sum_{n=0}^{N} G_n
$$

where $L$ is the aperiodic component and $G_n$ represents N Gaussian peaks.

Each Gaussian is defined as:

$$
G_n = a \cdot \exp\left(\frac{-(F-c)^2}{2w^2}\right)
$$

where:
- $a$ is the peak power (in log₁₀ units)
- $c$ is the center frequency (Hz)
- $w$ is the standard deviation (Hz)
- $F$ is the frequency vector

The aperiodic component is modeled using a Lorentzian:

$$
L = b - \log(k + F^\chi)
$$

where:
- $b$ is the broadband offset
- $\chi$ is the aperiodic exponent
- $k$ is the knee parameter

  ## Evil in Details
  So far so good? 
  We completed general framework of the method. However, I want you to be careful about the details when performing this methodological approach. Let's talk about these details now.

Step 1:

As you can remember, we should do curve fitting on the original PSD to acquire the aperiodic component at the 1st step. Note that this initial aperiodic component estimation is not the final parameterized model. Fitting at this stage is distorted due to the peaks in PSD and would not be reliable.  Nevertheless, we still need a rough estimation of aperiodic component to proceed. So, what should we do get initial aperiodic componet ?

  - Offset = power at the first frequency point
  - Exponent = slope calculated between first and last frequency points (in log-log space)
  These initial seed values give rough estimation of aperiodic component which is used for subtracting from original to create flattened spectrum.

You may think that everything is okay for the 1st step. I am sorry but no ! We need one further operation to complete 1st step. 

We keep only frequency points below 2.5th percentile threshold to find the lowest-power points in this flattened spectrum.
These low-power points are not part of oscillatory peaks. They represent the true aperiodic component. Then, we  re-fit the aperiodic component using only these selected frequency points from the original PSD. Thus, we obtain a good estimate of the aperiodic component that wasn't biased by the peaks. 

Congratulations !!! Now we can proceed to review detils of the 2nd step.

Step 2:

Firstly, we find the highest peak in the flattened spectrum extract its properties; center frequency (location of the peak), peak power (height of the peak) and the bandwidth (standard deviation). Thus, we can fit a Gaussian with these parameters (center, power, bandwidth) and then subtract this Gaussian from the flattened spectrum
We repeat the same process on the remaining spectrum to find the next highest peak. We terminate this operation when remaining peaks are below the noise threshold (default = 2 standard deviations of the flattened spectrum)


Step 3:

The iterative fitting gave us good initial guesses, but they might not be optimal when considering all peaks together. Actually there are two constrains in the fitting operation of Gaussians;
- Gaussians that heavily overlap (whose means are within 0.75 s.d. of the other),
- and gaussians that are too close to the edge (≤1.0 s.d.) of the spectrum,
are then dropped. The remaining Gaussian parameters are used in optimization (scipy.optimize.curve_fit) to fit all Gaussians simultaneously.
In order to minimize the squared error between the flattened spectrum and all N Gaussians, each Gaussian is constrained to stay within 1.5 s.d. of its initial guess.

Now that we have accurate Gaussian fits for the peaks, we can get an even better estimate of the aperiodic component. Therefore, the optimally fitted Gaussians are subtracted from original PSD. We fit the aperiodic component again on this peak-removed spectrum.

Step 4:

Finaly, we can combine multi-fit Gaussians and aperiodic component together to reach the parameterized PSD generated by the proposed algortihm.

For the further experience related to this method, you can visit this library in Python;

https://pypi.org/project/fooof/

