{
  "apis": {
    "children": {
      "/patnatpools/{id}/enterprisepermissions": {
        "RESTName": "enterprisepermission", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "enterprisepermissions"
      }, 
      "/patnatpools/{id}/natmapentries": {
        "RESTName": "natmapentry", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "natmapentries"
      }
    }, 
    "parents": {
      "/enterprises/{id}/patnatpools": {
        "RESTName": "enterprise", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "enterprises"
      }, 
      "/gateways/{id}/patnatpools": {
        "RESTName": "gateway", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "PUT"
          }
        ], 
        "resourceName": "gateways"
      }, 
      "/nsgateways/{id}/patnatpools": {
        "RESTName": "nsgateway", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "PUT"
          }
        ], 
        "resourceName": "nsgateways"
      }, 
      "/patnatpools": {
        "RESTName": "patnatpool", 
        "operations": [
          {
            "availability": null, 
            "method": "GET"
          }, 
          {
            "availability": null, 
            "method": "POST"
          }
        ], 
        "resourceName": "patnatpools"
      }
    }, 
    "self": {
      "/patnatpools/{id}": {
        "RESTName": "patnatpool", 
        "operations": [
          {
            "availability": null, 
            "method": "PUT"
          }, 
          {
            "availability": null, 
            "method": "DELETE"
          }, 
          {
            "availability": null, 
            "method": "GET"
          }
        ], 
        "resourceName": "patnatpools"
      }
    }
  }, 
  "model": {
    "RESTName": "patnatpool", 
    "attributes": {
      "addressRange": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Pool of IP Address that is available for use ex : 130.12.0.0/16", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": true, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "associatedGatewayId": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Default PAT IP Address, must belong to the pool above", 
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
      "associatedGatewayType": {
        "allowedChars": null, 
        "allowedChoices": [], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "", 
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
        "type": "enum", 
        "unique": false
      }, 
      "defaultPATIP": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Default PAT IP Address, must belong to the pool above", 
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
      "description": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "A description of the PATNATPool", 
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
      "name": {
        "allowedChars": null, 
        "allowedChoices": null, 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "Name of the PATNATPool", 
        "exposed": true, 
        "filterable": false, 
        "format": null, 
        "maxLength": null, 
        "maxValue": null, 
        "minLength": null, 
        "minValue": null, 
        "orderable": false, 
        "readOnly": false, 
        "required": true, 
        "transient": false, 
        "type": "string", 
        "unique": false
      }, 
      "permittedAction": {
        "allowedChars": null, 
        "allowedChoices": [
          "EXTEND", 
          "INSTANTIATE", 
          "DEPLOY", 
          "USE", 
          "READ", 
          "ALL"
        ], 
        "autogenerated": false, 
        "availability": null, 
        "channel": null, 
        "creationOnly": false, 
        "defaultOrder": false, 
        "defaultValue": null, 
        "description": "The permitted  action to USE/EXTEND  this Gateway Possible values are USE, READ, ALL, INSTANTIATE, EXTEND, DEPLOY, .", 
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
        "type": "enum", 
        "unique": false
      }
    }, 
    "description": "Represents PAT NAT Pool object.", 
    "entityName": "PATNATPool", 
    "package": "/gateway", 
    "resourceName": "patnatpools"
  }
}