import json
from flask import Flask
from db import NeoDB
app = Flask(__name__)

db = NeoDB("bolt://db:7687", "neo4j", "password")


@app.route("/nodes")
def get_all_nodes():
    all_nodes = db.get_all()
    return {
        "data": all_nodes
    }


@app.route("/nodes/<node_id>")
def get_node_height(node_id):
    node_info = db.get_node_info(node_id)
    return {
        "data": node_info
    }


@app.route("/nodes/<node_id>/descendants")
def get_node_descendants(node_id):
    node_descendants = db.get_node_descendants(node_id)
    return {
        "data": {
            "children": node_descendants
        }
    }


@app.route("/nodes/<parent_node>/parent/<child_node>", methods=['POST'])
def change_parent_node(parent_node, child_node):
    db.change_parent_node(parent_node, child_node)
    return {
        "status": "Success"
    }


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
