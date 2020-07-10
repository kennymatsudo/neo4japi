"""Module responsible for returning a single node.
"""


def get_node(db, node_id: int):
    current_node = dict(db.get_node_info(node_id).get('n'))
    if current_node:
        parent_node = db.get_parent_node(node_id)
        root_node = db.get_root_node()
        node_height = db.get_node_height(node_id)

        # update current node attributes w/ additional information
        additional_attrs = {
            "parent": dict(parent_node) if parent_node else None,
            "root": dict(root_node) if root_node else None,
            "height": node_height
        }
        current_node.update(additional_attrs)

    return current_node
