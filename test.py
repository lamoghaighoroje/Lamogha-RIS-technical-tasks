import unittest
from unittest.mock import patch, MagicMock
import json
import os
import time
from graph import Graph
# from connected_components import app

class ConnectedComponentTestCase(unittest.TestCase):

    def setUP(self):
        self.app = app.test_client()
        self.app.test = True

    def test_numberOfConnectedComponents_non_empty_body(self):
        data = json.loads('{"1":["2","3"],"2":["1","3"],"3":["1","2","4"],"4":["3"],"5":[],"6":["7"],"7":["6"]}')
        graph = Graph(data)
        for key, value in data.items():
            if value != []:
                for item in value:
                    graph.addEdge(int(key),int(item))
        cc = graph.NumberOfconnectedComponents()
        self.assertEqual(cc, 3)
                    
    # def test_connected_components(self):
    #     response = self.app.post('/connected_components', data=json.dumps({"1":[]}), headers={"Content-Type":"application/json"})
    #     self.assertEqual(response.get_data(as_text=True), "")
    #     self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()