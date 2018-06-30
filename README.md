# citrine_point_sampler

This library is meant as a submission to the Citrine Informatics technical challenge for scientific software engineers.

## Modules
The library is organized into the following modules:  
> console - parsing and validating CLI inputs.  
  constraint_parser - parsing and validating constraint input files.  
  generator - functions for generating n-dimensional points on a hypercube.  
  tests - unit tests for validating code base.

## Usage
The final component is the "API" of the library, a script that can be run as:
```bash
$ python ./sampler.py <input_file> <output_file> <n_results>
```
A help menu is accessible with the following flag:
```bash
$ python ./sampler.py --help
```

## Input Configuration
Input files are expected to have the following structure:  
> Line 1: Integer defining dimensionality of vectors that will be produced.  
  Line 2: Example vector of feasible point that satisfies constraints in this file.  
  Remaining Lines: List of constraints as python expressions containing +, -, *,
  /, and ** operators.

## Output Configuration
Output files will contain a list of generated vectors. Vector values are delimited with spaces, vectors are delimited by newlines.

## Setup
This library is installed by invoking the following:
```bash
$ python -m pip install .
```
All dependencies should be automatically retrieved and installed via pip.

## Tests
Unit tests may be run with the following:
```bash
$ python setup.py test
```

## Point Generation Algorithms
The following algorithms are used to generate points:  
#### 1. Rejection Sampling  
This algorithm continuously generates points in an N-dimensional hypercube until one which satisfies a set of constraints is found. This process is repeated until the desired number of points is found. A uniform distribution is used to avoid biasing any one region within the hypercube. This method's efficiency is directly proportional to the fraction of volume occupied by the constrained region relative to the total volume of the hypercube. This behavior makes this method unsuitable for problems where an extremely small volume within the hypercube is considered valid points.
#### 2. Markov Chain Monte Carlo (MCMC) Sampling  
This algorithm generates points by modifying known examples. Unlike rejection sampling, this method converges toward a uniform sample from the space within the given constraints. This is done in 2 stages:  
##### Stage 1: Population of Results List.  
The example point provided in the constraint input file is used as the first entry in the results. Points are proposed by applying a random offset to a random dimension of a randomly selected point from the results list until one which satisfies the constraints is selected. Redrawing from the list of results upon failure should promote exploration of the constrained space (points near the constraints will have modifications rejected more often than those further away). The magnitude of the proposed offset is reduced each time a proposed point is rejected to improve the rejection rate (this scheme allows for large offsets to be proposed initially while still avoiding the inefficiencies associated with large rejection rates).  
##### Stage 2: Result Random Walk.  
Once the specified  number of points are generated, points are randomly chosen from the results list to be modified in place. This can be interpreted as an ensemble of random walkers in the constrained space. Longer runtimes give the points more time to diffuse into the available space, which improves the uniformity of the resulting sample.

## License
MIT