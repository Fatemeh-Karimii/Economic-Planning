## Economic-Planning

###
An economy consists of three industries: coal, steel and transportation. The production of each product unit of each industry (worth one monetary unit) requires inputs from its own industry as well as other industries.
The required inputs and manpower (in terms of currency) are listed in Table 1. Also, there is a one-year time delay in this economy; That is, to reach the output in period t+1, input must be given to the system in period t.
The output of an industry may be used to create production capacity for itself or other industries in future years. The required inputs for one unit of production capacity increase (1 monetary unit of additional production) are given in Table 2.
The input of an industry in year t leads to a permanent increase in production capacity in year t + 2. Also, goods may be kept in warehouse from year to year. The reserves and production capacities (per year) at present (year 0) are given in Table 3 (in millions). In each year (except year 0), there is an external demand of 60 million units of coal, 60 million units of steel, and 30 million units of freight that must be met.
We want to check how to control the inputs and outputs of each industry in the next 5 years considering each of the following goals.

(1) to maximize total production capacity at the end of five years; While the capacity of human resources is limited and the annual maximum is 470 million monetary units.

(2) Maximizing the total requirement of manpower during the period (ignoring the limitation of manpower employment)

The problem was modeled as linear programming, solved in Python, and the optimal values of the decision variables as well as the value of the objective function were obtained in both cases.
• The optimal solution of the two problems of the first problem was obtained (the capabilities of the MIP library were used)
• It was analyzed if the external demand of each industry has a uniform distribution function and includes values [1.2, 0.8] equal to the average (values raised in the case of the problem).
