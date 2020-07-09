// Get Root Node
MATCH (root:Company)-[:CHILD*0..]->(child:Company)
WHERE NOT ()-[:CHILD]->(root) AND child.id = 3
RETURN root