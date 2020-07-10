"""Schemas for various request/response objects.
"""

from marshmallow import Schema, fields


class EmptyString(fields.String):
    """ Custom field that returns None when string is blank."""

    def _deserialize(self, value, attr, obj, **kwargs):
        if value == '':
            return None
        return super()._deserialize(value, attr, obj, **kwargs)


class SingleNodeSchema(Schema):
    ''' Schema representing query parameters passed to routes requesting a single node as the starting point.
    Example:
        {
            'node_id': int
        }
    '''
    node_id = fields.Int(required=True)


class ParentChildSchema(Schema):
    ''' Schema representing query parameters passed to routes requesting a parent and child node as the starting point.
    Example:
        {
            'parent_node': int,
            'child_node': int
        }
    '''
    parent_node = fields.Int(required=True)
    child_node = fields.Int(required=True)
