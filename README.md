# TASK 1

## PRE-REQUISITES
1. An installation of python is required on your machine. 
2. With python installed, install the required packages in requirements file using:
    pip3 install -r requirements.txt 

## RUN SERVICE LOCALLY 
Start the service by running in a terminal:
    python3 connected_components.py 

## TEST
Once the service has started, test a POST request. An example request is:
```
    curl -i -H "Content-Type: application/json" -X POST -d '{"1":["2","3"],"2":["1","3"],"3":["1","2","4"],"4":["3"],"5":[],"6":["7"],"7":["6"]}' http://localhost:5000/connected_components
```

# TASK 2
