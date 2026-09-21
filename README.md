# CSPC - Computer Science for Physics and Chemistry
My coursework repository. Each practical is under PW<n>/Lab <X>/.
## Setup
Create the environment for a given lab:
conda env create -f PW<n>/Lab\ <X>/environment.yml
conda activate cspc
---
## PW1 - Lab A: Reproducible Foundations
# CSPC

## PW1
Lab A: Reproducible Foundations

**What I built:**
Set up the conda environment, configured Git, and built pytest unit tests for a radioactive decay simulation.

**Speed comparison (loop vs NumPy):**
- loop: 3.4393 s
- numpy: 0.0003 s
- speed-up: 102308.5x faster

**Tests:** all passing? yes

**Conclusion:**
Vectorizing the simulation with NumPy provided a massive performance boost over standard Python loops by taking advantage of optimized C operations under the hood. Unit testing with pytest made it easy to catch edge cases early and ensured our random decay simulations consistently converged onto the theoretical exponential curve.