
# PRE-REQUISITES
1. An installation of python is required on your machine. 
2. With python installed, install the required packages in requirements file using:
```
    pip3 install -r requirements.txt 
```
## TASK 1
### RUN SERVICE LOCALLY 
Start the service by running in a terminal:
```
    python3 connected_components.py 
```
### TEST
Once the service has started, run a POST request in the terminal or using an API test tool like Postman. An example request is:
```
    curl -i -H "Content-Type: application/json" -X POST -d '{"1":["2","3"],"2":["1","3"],"3":["1","2","4"],"4":["3"],"5":[],"6":["7"],"7":["6"]}' http://localhost:5000/connected_components
```

## TASK 2
The script for the second solution is `estimate_run_stats.py`, which expects to a csv file for the data for be passed in at run time:
```
    python3 estimate_run_stats.py running_observations.csv
```
A scatter plot (similar to the diagram below) showing the cluster points of the 3 routes is expected.
![Example of expected plot](3cluster_n_init-10.png) Figure 1: Example of expected plots. It shows how the points in the running observation fit into the 3 potential routes known.

**Question 1**: Based on this data, can you work out the lengths (in meters) of each of the 3 routes, and how long it takes me on average (in minutes) to run each one?

**Answer 1**: 
The average time per route is: [48.24516129032258, 55.64, 40.941538461538464] minutes

The Average distance per route is: [7340.0, 7006.833333333333, 6428.205128205128] meters

**Question 2**: Do I tend to run on each route about as often, or do I have a favorite route?

**Answer 2**: The number of times each route is ran is about: `30`,`31`, and `39`. 
This means that you run two routes about as often, but one route a little bit more (about 0.09% more).