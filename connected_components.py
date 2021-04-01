from flask import Flask, jsonify, render_template
from flask import request as f_request
import json
import subprocess
import time
from graph import Graph

app = Flask(__name__)

# endpoint for getting a count of connected components
@app.route('/connected_components', methods = ['POST'])
def connected_components():
    try:
        body = f_request.get_json()
    except Exception:
        return "Error: Content-Type must be set to application/json", 400
    # check if the body of the request is empty
    if body == None:
        return "Error: Input body to the request must be a valid JSON", 400
    else:
        # check if the request data is an empty json
        empty_body = not body
        if empty_body != True:
            # create instance of our graph class using the request data
            graph = Graph(body)
            # get every key and value pair in the request data. Keys represent the nodes
            for key, value in body.items():
                # if the value is not an empty list, the values represent adjacent nodes of a given node
                if value != []:
                    for item in value:
                        # add an edge from a node to its adjacent node
                        graph.addEdge(int(key),int(item))             
            # get the number of connected components from the graph
            response = str(graph.NumberOfconnectedComponents())
        else:
            response = "Your input is an empty json"
    return response

if __name__ == '__main__':
    print('\n\nFinding connected components program')
    print('Started at: {}\n\n'.format(time.time()))
    print('ENDPOINTS:')
    print(app.url_map)
    app.run(debug=True, port=5000, host='localhost')