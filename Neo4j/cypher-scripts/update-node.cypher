// Update Node
MATCH (node:Company{id:2}), (child:Company{id:7})
MERGE (node)-[:CHILD]->(child)
MERGE (node)<-[:PARENT]-(child)