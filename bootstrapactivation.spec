{
  "apis": {
    "children": {}, 
    "parents": {
      "/nsgateways/{id}/bootstrapactivations": {
        "RESTName": "nsgateway", 
        "operations": [
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "nsgateways"
      }
    }, 
    "self": {
      "/bootstrapactivations/{id}": {
        "RESTName": "bootstrapactivation", 
        "operations": [
          {
            "availability": null, 
            "method": "PUT"
          }
        ], 
        "resourceName": "bootstrapactivations"
      }
    }
  }, 
  "model": {
    "RESTName": "bootstrapactivation", 
    "attributes": {
      "action": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The bootstrap action to perform", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "Action", 
        "unique": false
      }, 
      "cacert": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The CA Certificate Chain", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "cert": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The signed Certificate", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "configURL": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The configuration URL", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "csr": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The CSR of the request", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "entityScope": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Specify if scope of entity is Data center or Enterprise level", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "EntityScope", 
        "unique": false
      }, 
      "hash": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The authentication hash of this request", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "seed": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The random seed for this request", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "status": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The agent status for the request", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": false, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }
    }, 
    "description": "NSG Gateway initiated Bootstrap Activation", 
    "entityName": "BootstrapActivation", 
    "package": "/gateway", 
    "resourceName": "bootstrapactivations"
  }
}