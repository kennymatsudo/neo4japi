# Flask + Neo4j

## Dependencies

- Docker

## Deployment

In order to deploy, please run:

```bash
> docker-compose up
```

This will spin up three images, one containing the Python Flask application (exposing port 80) , a Neo4j graph database for data persistence (exposing port 7474), and a test Neo4j graph database to run tests against (exposting port 7475).

![tree](https://raw.githubusercontent.com/kennymatsudo/neo4japi/master/doc/graph.png)

**Note 1** In this iteration, the web application container does not wait for the graph database table to be populated and will therefore show log messages. These can be ignored, and will eventually stop when the script within the database container runs and populates the initial tree.

**Note 2** In order to easily test the API's, an initial script is ran during the building of the Neo4j Docker container that populates the database. The data can be further manipulated by visiting localhost:7687.

## API

### Get descendants of all nodes

GET <http://localhost/nodes/{node_id}/descendants>
Returns a list of all descendants of the specified node.

### Change parent node of a given node

PUT http://localhost/nodes/{parent_node}/parent/{child_node}
Changes the parent of the specified child node to the specified parent node.

### Get Node

GET <http://localhost/nodes/{node_id}>
Returns information about the specified node, including: node id, parent node, root node, and the height of the node.

## Testing

In order to run the tests, please run the following command from the root:

```bash
> pytest
```

This will run tests against the test database spun up in a seperate Docker container.
