
def get_node(db, node_id):
    all_nodes = db.get_node_info(node_id)
    return {
        "data": all_nodes
    }
