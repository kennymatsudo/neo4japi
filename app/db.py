from neo4j import GraphDatabase


class NeoDB:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def get_all(self):
        with self.driver.session() as session:
            results = session.run("MATCH(n) RETURN n")
            return results.data()

    def get_node_info(self, node_id):
        with self.driver.session() as session:
            parent_node = self._get_parent_node(node_id)
            root_node = self._get_root_node()
            node_height = self._get_node_height(node_id)
            results = session.run(
                "MATCH (n:Company {id:$node_id}) "
                "RETURN n", node_id=int(node_id))
            node_data = dict(results.single()[0])
            other_attributes = {"parent": dict(
                parent_node), "root": dict(root_node), "height": node_height}
            node_data.update(other_attributes)
            return node_data

    def get_node_descendants(self, node_id):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (root:Company{id:$node_id})-[:CHILD*]->(descendants:Company) "
                "RETURN descendants", node_id=int(node_id))
            return [record['descendants'] for record in results.data()]

    def remove_pc_relationship(self, node_id):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (curr:Company{id:$node_id})-[pr:PARENT]->(), (curr:Company{id:$node_id})<-[cr:CHILD]->() "
                "DELETE pr,cr", node_id=int(node_id))
            print(results)

    def change_parent_node(self, parent_node, child_node):
        self._delete_current_pc_relation(child_node)
        self._create_pc_relation(parent_node, child_node)

    def _delete_current_pc_relation(self, node_id):
        with self.driver.session() as session:
            session.run(
                "MATCH (curr:Company{id:$node_id})-[pr:PARENT]->(), (curr:Company{id:$node_id})<-[cr:CHILD]-() "
                "DELETE pr,cr", node_id=int(node_id))

    def _create_pc_relation(self, parent_node, child_node):
        with self.driver.session() as session:
            session.run(
                "MATCH(child: Company{id: $child_node}), (parent: Company{id: $parent_node}) "
                "MERGE(child)-[:PARENT] -> (parent) "
                "MERGE (child)<-[:CHILD]-(parent) ", parent_node=int(parent_node), child_node=int(child_node))

    def _get_parent_node(self, node_id):
        with self.driver.session() as session:
            results = session.run(
                "MATCH (node:Company)-[:PARENT]->(parent:Company) "
                "WHERE node.id=$node_id "
                "RETURN parent", node_id=int(node_id))
            return results.single()[0]

    def _get_node_height(self, node_id):
        with self.driver.session() as session:
            results = session.run(
                "MATCH k=(n: Company)-[r:PARENT*0..] -> (c: Company) "
                "WHERE n.id=$node_id "
                "WITH n, collect(length(k)) as height "
                "UNWIND height as e "
                "RETURN max(e) as height", node_id=int(node_id))
            return results.single()[0]

    def _get_root_node(self):
        with self.driver.session() as session:
            results = session.run(
                "MATCH(root: Company)-[:CHILD*0..] -> (child: Company) "
                "WHERE NOT()-[:CHILD] -> (root) "
                "RETURN root")
            return results.single()[0]

    # @staticmethod
    # def _create_and_return_greeting(tx, message):
    #     result = tx.run("CREATE (a:Greeting) "
    #                     "SET a.message = $message "
    #                     "RETURN a.message + ', from node ' + id(a)", message=message)
    #     return result.single()[0]
