CREATE (c1:Company {id:1,name:"Walt Disney"}),
    (c2:Company {id:2,name:"ABC"}),
    (c3:Company {id:3,name:"Touchstone Pictures"}),
    (c4:Company {id:4,name:"Marvel"}),
    (c5:Company {id:5,name:"Lucas Films"}),
    (c6:Company {id:6,name:"AE"}),
    (c7:Company {id:7,name:"Historical Channell"}),
    (c8:Company {id:8,name:"Pixar"}),
    (c9:Company {id:9,name:"Holywood Records"}),
    (c10:Company {id:10,name:"Core Publishing"}),

    (c1)-[:CHILD]->(c2)-[:CHILD]->(c3),
    (c1)<-[:PARENT]-(c2)<-[:PARENT]-(c3),
    (c7)-[:CHILD]->(c8)-[:CHILD]->(c9),
    (c7)<-[:PARENT]-(c8)<-[:PARENT]-(c9),
    (c8)-[:CHILD]->(c10)-[:CHILD]->(c4)-[:CHILD]->(c5)-[:CHILD]->(c6),
    (c8)<-[:PARENT]-(c10)<-[:PARENT]-(c4)<-[:PARENT]-(c5)<-[:PARENT]-(c6);


MATCH (node:Company{id:2}), (child:Company{id:7})
MERGE (node)-[:CHILD]->(child)
MERGE (node)<-[:PARENT]-(child);