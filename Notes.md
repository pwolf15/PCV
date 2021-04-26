Progress

/ Interactive Animation (p. 19)
/ Principal Component Analysis (p. 27)
* technique for dimensionality reduction
* represent the variability of training data in as few dimensions as possible
* singular value decomposition (SVD) usually used to find principal components

* Pickling: take almost any Python object and convert it to a string representation
* Unpickling: reconstructing Python object from string
* Gaussian blurring, example of image convolution
* Image gradient, image derivatives
* Prewitt filters, sobel filters
* sobel filter used for image derivative; positive => bright, negative derivative => dark
* Gaussian derivative filters: more robust to image noise and derivatives
* morphology: framework and collection of image processing methods for measuring and analyizng basic shapes
* Image de-noising: removing image noise while preserving details and structures
* Rudin-Osher-Fatemi de-noising model (ROF)
* ROF Solver based on Chambolle algorithm
* roll() method: rolls values of array cyclically around an access
* linalg.norm: difference between two arrays
* What is a Gaussian image derivative? Image derivative can be computed using convolutional kernels of size 2 or 3.

Exercise

1. Applying gaussian blur for increasing values of sigma? This increases the amount of blurring due to the size of the convolutional kernel.Gaussian filter acts as low pass filter. High frequency = edges. Sigma controls variation around mean. Larger sigma == more variance. Increase sigma == look at more broad scene.
2. Unsharp masking: blur image and subtracting blurred version from original. End image is sharpened image. My example looks off.