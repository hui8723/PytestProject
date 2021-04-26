from jsonschema import validate

def test_schema():
    # data = {"id":520,"name":"hello first blog","price":25.5}
    data = {"id":-1,"name":"hello first blog","price":25.5}
    schema = {"$schema":"http://json-schema.org/draft-04/schema#",
              "title":"BookInfo",
              "description":"some information about book",
              "type":"object",
              "properties": {"id": {"description":"The unique identifier for a book","type":"integer","minimum":1},
                             "name": {"description":"Name of the book","type":"string","maxLength":50,"minLength":1},
                             "price": {"type":"number","minimum":0,"exclusiveMinimum":True}},
              "required": ["id","name","price"]}
    validate(data,schema)