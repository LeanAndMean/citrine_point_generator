citrine_point_sampler
---------------------

This library is meant as a submission to the Citrine Informatics technical
challenge for scientific software engineers.

## Modules
The library is organized into the following modules:
  console - parsing and validating CLI inputs.
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

### Input Configuration
Input files are expected to have the following structure:
Line 1: Integer defining dimensionality of vectors that will be produced.
Line 2: Example vector of feasible point that satisfies constraints in this file.
Remaining Lines: List of constraints as python expressions containing +, -, *,
/, and ** operators.

### Output Configuration
Output files will contain a list of generated vectors. Vector values are
delimited with spaces, vectors are delimited by newlines.

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

### NOTE:
At the time of submission, 1 of the unit tests is expected to fail. This test
is for the validation of the python class (provided by Citrine in the prompt)
responsible for parsing input files containing point generation constraints.
2 of the 4 examples provided in the prompt contain invalid examples of points
which do not satisfy the constraints in their respective files.
The failing test has been left in to indicate this discrepency and to aid in
the process of remedying the example files.
The constraint class provided by Citrine has been modified to raise an IOError
in the event that an input file contains inappropriate values (E.g., the
dimensionality of the problem (line 1) does not match the dimensionality of the
example point (line 2)).

## Point Generation Algorithms
The following algorithms are used to generate points:
1. Rejection Sampling
This algorithm continuously generates points in an N-dimensional hypercube until
one which satisfies a set of constraints is found. This process is repeated
until the desired number of points is found. A uniform distribution is used to
avoid biasing any one region within the hypercube. This method's efficiency is
directly proportional to the fraction of volume occupied by the constrained
region relative to the total volume of the hypercube. This behavior makes this
method unsuitable for problems where an extremely small volume within the
hypercube is considered valid points.
The 2 input examples that were parseable did not prove to be a problem; 10,000
points can be generated in < 0.5 seconds.

## License
MIT