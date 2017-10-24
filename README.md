# TBM_Shield-Flow

To run the 1D_Shield-Flow.py online - click here: https://repl.it/NHpG/3

The objective here is to model the flow of excavation fluids around the shield of a tunnel boring machines (TBMs) in soft ground. The model follows these assumptions:
1. The convergence/expansion of the tunnel cavity can be calculated with dR=2.R.dP/G. This is valid for a linear elastic domain under isotropic stress.
1. This isotropy turns the cross-sectional plane to a single point with constant values (Initial Radius - R, Shear Modulus -G) and variables (Pressure, Deformation).
1. The excavation fluids follow the Bingham-Plastic model at zero shear rate (Shear=Yield Stress).
1. The flow in the GAP between the shield and the soil cavity causes a pressure drop in the fluid, which can be computed through the equilibrium of forces in a rectangular section (dl x GAP) where the pressure difference (dP.gap) is equal to the shear force (T.dl), so that dP=T.dl/gap


![Increment of Water Pressure](/images/tbm_flow.png)


**Published References:**

1. Dias, T. G. S., & Bezuijen, A. (2015). TBM Pressure Models - Observations, Theory and Practice. 15th Pan-American Conference on Soil Mechanics and Geotechnical Engineering - Geotechnical Synergy in Buenos Aires 2015 - Invited Lectures [(Download)](https://www.researchgate.net/publication/283855639_TBM_Pressure_Models__Observations_Theory_and_Practice)
1. Bezuijen, A., & Talmon, A. M. (2008). Processes around a TBM. Geotechnical Aspects of Underground Construction in Soft Ground - 6th International Symposium (IS-Shanghai).
