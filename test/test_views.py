from app.routes.get_all_nodes import get_all_nodes
from app.routes.get_node import get_node
from app.routes.get_node_descendants import get_node_descendants
from app.routes.put_parent_node import put_parent_node
from app.util.db import NeoDB

db = NeoDB("bolt://localhost:7688", "neo4j", "password")


def test_get_all_nodes():
    expected = {
        'data': [
            {
                'name': 'Walt Disney', 'id': 1}, {
                'name': 'ABC', 'id': 2}, {
                'name': 'Touchstone Pictures', 'id': 3}, {
                'name': 'Marvel', 'id': 4}, {
                'name': 'Lucas Films', 'id': 5}, {
                'name': 'AE', 'id': 6}, {
                'name': 'Historical Channell', 'id': 7}, {
                'name': 'Pixar', 'id': 8}, {
                'name': 'Holywood Records', 'id': 9}, {
                'name': 'Core Publishing', 'id': 10}]}
    all_nodes = get_all_nodes(db)
    assert all_nodes == expected


def test_get_node():
    expected = {'name': 'Walt Disney', 'id': 1, 'parent': None,
                'root': {'name': 'Walt Disney', 'id': 1}, 'height': 0}
    node = get_node(db, 1)
    print(node)
    assert node == expected


def test_get_node_descendants():
    expected = {
        'data': {
            'children': [
                {
                    'name': 'Holywood Records', 'id': 9}, {
                    'name': 'Core Publishing', 'id': 10}, {
                        'name': 'Marvel', 'id': 4}, {
                            'name': 'Lucas Films', 'id': 5}, {
                                'name': 'AE', 'id': 6}]}}
    node_descendants = get_node_descendants(db, 8)
    assert node_descendants == expected


def test_put_parent_node():
    put_parent_node(db, 4, 6)
    node = get_node(db, 6)
    assert node['parent']['id'] == 4
    put_parent_node(db, 5, 6)
    node = get_node(db, 6)
    assert node['parent']['id'] == 5
