{
    "attributes": [
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The name of the custom attribute (key) used to enrich the object the customProperty instance is attached to.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "attributeName",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Attribute Name"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The value assigned to the custom attribute (key) of that customProperty instance.",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": 4091,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "attributeValue",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Attribute Value"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "Developed in the context of the Uplink Connection on the NSG, this API could be used for other types of objects. It is used as a collection of name-value (or key-value) pairs for custom attributes that could be used to enrich existing class instances.",
        "entity_name": "CustomProperty",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "customproperties",
        "rest_name": "customproperty",
        "root": null,
        "update": true,
        "userlabel": "Custom Property"
    }
}