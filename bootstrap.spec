{
    "attributes": {
        "installerID": {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "The Installer ID",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": "no"
        },
        "status": {
            "allowed_chars": null,
            "allowed_choices": [
                "ACTIVE",
                "CERTIFICATE_SIGNED",
                "INACTIVE",
                "NOTIFICATION_APP_REQ_ACK",
                "NOTIFICATION_APP_REQ_SENT"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Bootstrap status; can be, for example, Active, Inactive, or Notified. Possible values are INACTIVE, NOTIFICATION_APP_REQ_SENT, NOTIFICATION_APP_REQ_ACK, CERTIFICATE_SIGNED, ACTIVE, .",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": "no"
        }
    },
    "children": {},
    "model": {
        "create": false,
        "delete": false,
        "description": "Gateway bootstrap details.",
        "entity_name": "Bootstrap",
        "extends": [
            "@metadata",
            "@base",
            "@audited"
        ],
        "get": true,
        "package": "gateway",
        "resource_name": "bootstraps",
        "rest_name": "bootstrap",
        "root": false,
        "update": true
    }
}