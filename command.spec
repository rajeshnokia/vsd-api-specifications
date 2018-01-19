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
            "description": "ID of the object which supplies parameters for this command.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "assocParamID",
            "orderable": false,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Associated Parameter ID"
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
            "description": "Type of the object which supplies parameters for this command.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "assocParamType",
            "orderable": true,
            "read_only": false,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Associated Parameter Type"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "NSG_DOWNLOAD_OS_IMAGE",
                "NSG_UPGRADE_TO_IMAGE",
                "UNKNOWN"
            ],
            "autogenerated": false,
            "channel": null,
            "creation_only": true,
            "default_order": false,
            "default_value": "UNKNOWN",
            "deprecated": false,
            "description": "Specifies the type of command that is stated for execution on the system receiving the operation request.  A request for download, a request for upgrade, a request for revocation, ...",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "command",
            "orderable": true,
            "read_only": false,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Command Requested"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "Informative details on what command is to be executed.  It complements the commandType attribute.  An example of a value could be a URL, a version number, a UUID of another object, ...",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 1023,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "commandInformation",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Command Information"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A string representing the detailed status of the operation that was triggered by the execution of the Command instance.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 0,
            "min_value": null,
            "name": "detailedStatus",
            "orderable": false,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": true,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Detailed Status"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "0",
            "deprecated": false,
            "description": "A numerical code mapping to a list of detailed statuses that can apply to a Command instance.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": 65535,
            "min_length": null,
            "min_value": 0,
            "name": "detailedStatusCode",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "integer",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Detailed Status Code"
        },
        {
            "allowed_chars": null,
            "allowed_choices": [
                "COMPLETE",
                "FAILED",
                "STARTED",
                "UNKNOWN"
            ],
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": "UNKNOWN",
            "deprecated": false,
            "description": "The status of the Command from a VSD perspective.",
            "exposed": true,
            "filterable": true,
            "format": null,
            "max_length": null,
            "max_value": null,
            "min_length": null,
            "min_value": null,
            "name": "status",
            "orderable": true,
            "read_only": true,
            "required": false,
            "subtype": null,
            "transient": false,
            "type": "enum",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Status"
        },
        {
            "allowed_chars": null,
            "allowed_choices": null,
            "autogenerated": true,
            "channel": null,
            "creation_only": false,
            "default_order": false,
            "default_value": null,
            "deprecated": false,
            "description": "A generated summary for the action giving some general context on the command executed.",
            "exposed": true,
            "filterable": false,
            "format": "free",
            "max_length": 255,
            "max_value": null,
            "min_length": 1,
            "min_value": null,
            "name": "summary",
            "orderable": false,
            "read_only": true,
            "required": true,
            "subtype": null,
            "transient": false,
            "type": "string",
            "unique": false,
            "uniqueScope": null,
            "userlabel": "Summary"
        }
    ],
    "children": [],
    "model": {
        "create": null,
        "delete": true,
        "description": "A Command represents an operation that needs to be executed on an entity (NSG, Gateway, ...) which requires little processing by VSD, but may result in a long activity on the external entity.  An example would be to trigger an action on VSD so that a Gateway download a new image.  VSDs handling of the request is limited to generating a message to be sent to the device on which the download process is expected.  The device then acts on the request and proceeds with the download...  That may be a long process.  The commands API is similar to the Jobs API with regards to triggering operations on objects.",
        "entity_name": "Command",
        "extends": [
            "@audited",
            "@base"
        ],
        "get": true,
        "package": "operation",
        "resource_name": "commands",
        "rest_name": "command",
        "root": null,
        "update": true,
        "userlabel": "Command"
    }
}