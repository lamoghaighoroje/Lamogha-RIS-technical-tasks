from flask import Flask
from flask import request as f_request
import json
from datetime import datetime
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
            # create instance of our graph class and send the graph data
            graph = Graph(body)   
            # get the number of connected components from the graph
            response = str(graph.NumberOfconnectedComponents())
        else:
            response = "Your input is empty."
    return response

if __name__ == '__main__':
    print('\n\nFinding connected components program')
    print(f'Started at: {datetime.now().strftime("%d/%m/%Y %H:%M:%S")}\n\n')
    print('ENDPOINTS:')
    print(app.url_map)
    app.run(debug=True, port=5000, host='localhost')