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
            "description": "Associated Application Group ID",
            "exposed": true,
            "filterable": true,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "associatedApplicationGroupID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null
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
            "description": "Priority of the associated Application Group",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 1000,
            "min_length": null,
            "min_value": 10,
            "name": "priority",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": true,
            "uniqueScope": null
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "Association object for maintaining the priority of AppliationGroup(s) associated to a Domain",
        "entity_name": "ApplicationGroupBinding",
        "extends": [],
        "get": true,
        "package": null,
        "resource_name": "applicationgroupbindings",
        "rest_name": "applicationgroupbinding",
        "root": null,
        "update": true
    }
}