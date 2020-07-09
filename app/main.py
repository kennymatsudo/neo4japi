import json

from flask import Flask
from routes.get_all_nodes import get_all_nodes
from routes.get_node import get_node
from routes.get_node_descendants import get_node_descendants
from routes.put_parent_node import put_parent_node
from util.db import NeoDB

app = Flask(__name__)

db = NeoDB("bolt://db:7687", "neo4j", "password")


@app.route("/nodes")
def route_get_all_nodes():
    response = get_all_nodes(db)
    return response


@app.route("/nodes/<node_id>")
def route_get_node(node_id):
    response = get_node(db, node_id)
    return response


@app.route("/nodes/<node_id>/descendants")
def route_get_node_descendants(node_id):
    response = get_node_descendants(db, node_id)
    return response


@app.route("/nodes/<parent_node>/parent/<child_node>", methods=['PUT'])
def change_parent_node(parent_node, child_node):
    response = put_parent_node(db, parent_node, child_node)
    return response


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
