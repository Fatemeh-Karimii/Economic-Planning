## Economic-Planning

###
An economy consists of three industries: coal, steel, and transportation. The production of each unit (worth one monetary unit) in each industry requires inputs from both its own industry and the others. The required inputs and manpower (in monetary terms) are provided in Table 1.
This economy operates with a one-year time delay: to achieve output in period t+1, inputs must be supplied in period t. The output of an industry can be used to build production capacity for itself or other industries in future years. The required inputs to increase production capacity by one monetary unit are given in Table 2. Inputs provided in year t lead to a permanent increase in production capacity in year t+2. Goods can also be stored in a warehouse from year to year. The current reserves and annual production capacities (in year 0) are listed in Table 3 (in millions). From year 1 onward, the external demand is 60 million units for coal, 60 million for steel, and 30 million for freight per year, and these demands must be met annually.

The objective is to determine how to control the inputs and outputs of each industry over the next five years, under the following goals:

1. Maximize total production capacity at the end of five years, subject to a human resource constraint of 470 million monetary units per year.

2. Maximize total manpower usage over the five-year period (ignoring any employment limitations).

The problem was modeled as a linear programming problem and solved using Python. The optimal values of the decision variables and the objective function were obtained for both cases.
The optimal solutions for both versions of the problem were obtained using the MIP library.
  
A sensitivity analysis was conducted assuming that the external demand for each industry follows a uniform distribution over the interval [0.8, 1.2] times the average demand values provided in the problem.
