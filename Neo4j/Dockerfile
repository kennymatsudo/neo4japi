FROM neo4j:latest
ENV NEO4J_AUTH=neo4j/password

COPY ./cypher-scripts/create-tree.cypher /var/lib/neo4j/import/
COPY ./create-tree.sh /var/lib/neo4j/create-tree.sh
COPY ./wrapper.sh /var/lib/neo4j/wrapper.sh

ENTRYPOINT ["./wrapper.sh"]