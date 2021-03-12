# Python Control Systems Library[](https://python-control.readthedocs.io/en/0.8.4/index.html#python-control-systems-library "Permalink to this headline")

The Python Control Systems Library (python-control) is a Python package that implements basic operations for analysis and design of feedback control systems.

Features
-   Linear input/output systems in state-space and frequency domain
-   Block diagram algebra: serial, parallel, and feedback interconnections
-   Time response: initial, step, impulse
-   Frequency response: Bode and Nyquist plots
-   Control analysis: stability, reachability, observability, stability margins
-   Control design: eigenvalue placement, LQR, H2, Hinf
-   Model reduction: balanced realizations, Hankel singular values
-   Estimator design: linear quadratic estimator (Kalman filter)

--- 

## Installation[](https://python-control.readthedocs.io/en/0.8.4/intro.html#installation "Permalink to this headline")

To install using pip:


```
pip install control
```
For users with the Anaconda distribution of Python, the following commands can be used:

```
conda install numpy scipy matplotlib    # if not yet installed
conda install -c conda-forge control
```

---

## Getting started[](https://python-control.readthedocs.io/en/0.8.4/intro.html#getting-started "Permalink to this headline")

There are two different ways to use the package. For the default interface described in [Function reference](https://python-control.readthedocs.io/en/0.8.4/control.html#function-ref), simply import the control package as follows:

\>>> import control

If you want to have a MATLAB-like environment, use the [MATLAB compatibility module](https://python-control.readthedocs.io/en/0.8.4/matlab.html#matlab-module):

\>>> from control.matlab import \*