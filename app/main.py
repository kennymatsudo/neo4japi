import json

from flask import Flask, request
from routes.get_all_nodes import get_all_nodes
from routes.get_node import get_node
from routes.get_node_descendants import get_node_descendants
from routes.put_parent_node import put_parent_node
from util import validation_schema as vs
from util.db import NeoDB

app = Flask(__name__)

db = NeoDB("bolt://db:7687", "neo4j", "password")


@app.route("/nodes")
def route_get_all_nodes():
    """ Returns all the nodes within the graph. """
    try:
        response = get_all_nodes(db)
        return response
    except Exception as err:
        response = app.response_class(
            response=json.dumps(str(err)),
            status=404
        )
        return response


@app.route("/nodes/<node_id>")
def route_get_node(node_id):
    """ Returns information about the specified node. """
    try:
        path_params = vs.SingleNodeSchema().load(request.view_args)
        response = get_node(db, path_params['node_id'])
        return response
    except Exception as err:
        response = app.response_class(
            response=json.dumps(str(err)),
            status=404
        )
        return response


@app.route("/nodes/<node_id>/descendants")
def route_get_node_descendants(node_id):
    """ Returns all the descendants of the specified node. """
    try:
        path_params = vs.SingleNodeSchema().load(request.view_args)
        response = get_node_descendants(db, path_params['node_id'])
        return response
    except Exception as err:
        response = app.response_class(
            response=json.dumps(str(err)),
            status=404
        )
        return response


@app.route("/nodes/<parent_node>/parent/<child_node>", methods=['PUT'])
def change_parent_node(parent_node, child_node):
    """ Changes the parent of the specified node. """
    try:
        path_params = vs.ParentChildSchema().load(request.view_args)
        response = put_parent_node(
            db, path_params['parent_node'], path_params['child_node'])
        return response
    except Exception as err:
        response = app.response_class(
            response=json.dumps(str(err)),
            status=404
        )
        return response


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=80)
