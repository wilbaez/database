// Wilfredo Baez
// 
//
db = db.getSiblingDB("BankApp")

// Create and setup Schema Validator for the customer collection
db.createCollection("customers", {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: [ "first_name", "last_name", "address", "social_security", "branch", "phone" ],
      properties: {
        first_name: {
          bsonType: "string",
          description: "All customers must have a First name"
        },
		last_name: {
          bsonType: "string",
          description: "All customers must have a Last name"
        },
		// we make use of MongoDBs ability to store nested objects
        address: {
          bsonType: "object",
          required: [ "street", "city", "state", "zip" ],
          properties: {
            // this is an optional property for extra street information (apartment number, etc)
            street: {
              bsonType: "string",
              description: "All customers must have a Street Address"
            },
			apartment: {
              bsonType: "string",
              description: "Optional when applicable"
            },
            city: {
              bsonType: "string",
              description: "All customers must have a City"
            },
            state: {
               enum: [ "AK", "AL", "AR", "AS", "AZ", "CA", "CO", "CT", "DC", "DE", "FL", "GA", "GU", 
			     "HI", "IA", "ID", "IL", "IN", "KS", "KY", "LA", "MA", "MD", "ME", "MI", "MN", "MO", 
				 "MP", "MS", "MT", "NC", "ND", "NE", "NH", "NJ", "NM", "NV", "NY", "OH", "OK", "OR", 
				 "PA", "PR", "RI", "SC", "SD", "TN", "TX", "UM", "UT", "VA", "VI", "VT", "WA", "WI", 
				 "WV", "WY"],
               description: "All customers must have a State from one of the enum values"
            },
            zip: {
              bsonType: "string",
              description: "All customers must have a Zip Code"
            }
          }
        },
		social_security: {
          bsonType: "string",
          description: "All customers must have a Social Security Number"
        },
		branch: {
          enum: [ "1", "2", "3", "4" ],
          description: "All customers must have a Branch association from one of the enum values"
        },
        phone: {
          bsonType: "string",
          description: "All customers must have a Phone Number"
        }
      }
    }
  }
})

// Create the additional collections accounts and transactions who do not have a validator
db.createCollection("accounts")
db.createCollection("transactions")
])