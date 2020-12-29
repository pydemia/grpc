# Protobuf

## Types

## Json Mapping

| proto3                 | JSON          | JSON example                              | Notes                                                                                                                                                                                                                                                           |
|------------------------|---------------|-------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| enum                   | string        | `"FOO_BAR"`                               | The name of the enum value as specified in proto is used. Parsers accept both enum names and integer values.                                                                                                                                                    |
| map<K,V>               | object        | `{"k": v, …}`                             | All keys are converted to strings.                                                                                                                                                                                                                              |
| repeated V             | array         | `[v, …]`                                  | null is accepted as the empty list [].                                                                                                                                                                                                                          |
| bool                   | true, false   | `true, false `                            | -                                                                                                                                                                                                                                                               |
| string                 | string        | `"Hello World!" `                         | -                                                                                                                                                                                                                                                               |
| bytes                  | base64 string | `"YWJjMTIzIT8kKiYoKSctPUB+" `             | JSON value will be the data encoded as a string using standard base64 encoding with paddings. Either standard or URL-safe base64 encoding with/without paddings are accepted.                                                                                   |
| int32, fixed32, uint32 | number        | `1, -10, 0 `                              | JSON value will be a decimal number. Either numbers or strings are accepted.                                                                                                                                                                                    |
| int64, fixed64, uint64 | string        | `"1", "-10"`                              | JSON value will be a decimal string. Either numbers or strings are accepted.                                                                                                                                                                                    |
| float, double          | number        | `1.1, -10.0, 0, "NaN", "Infinity"`        | JSON value will be a number or one of the special string values "NaN", "Infinity", and "-Infinity". Either numbers or strings are accepted. Exponent notation is also accepted. -0 is considered equivalent to 0.                                               |
| Any                    | object        | `{"@type": "url", "f": v, … } `           | If the Any contains a value that has a special JSON mapping, it will be converted as follows: {"@type": xxx, "value": yyy}. Otherwise, the value will be converted into a JSON object, and the "@type" field will be inserted to indicate the actual data type. |
| Timestamp              | string        | `"1972-01-01T10:00:20.021Z"`              | Uses RFC 3339, where generated output will always be Z-normalized and uses 0, 3, 6 or 9 fractional digits. Offsets other than "Z" are also accepted.                                                                                                            |
| Duration               | string        | `"1.000340012s", "1s"`                    | Generated output always contains 0, 3, 6, or 9 fractional digits, depending on required precision, followed by the suffix "s". Accepted are any fractional digits (also none) as long as they fit into nano-seconds precision and the suffix "s" is required.   |
| Struct                 | object        | `{ … } `                                  | Any JSON object. See struct.proto.                                                                                                                                                                                                                              |
| Wrapper types          | various types | `2, "2", "foo", true, "true", null, 0, … `| Wrappers use the same representation in JSON as the wrapped primitive type, except that null is allowed and preserved during data conversion and transfer.                                                                                                      |
| FieldMask              | string        | `"f.fooBar,h"`                            | See field_mask.proto.                                                                                                                                                                                                                                           |
| ListValue              | array         | `[foo, bar, …]`                           | -                                                                                                                                                                                                                                                               |
| Value                  | value         | `some_value`                              | Any JSON value. Check google.protobuf.Value for details.                                                                                                                                                                                                        |
| NullValue              | null          | ` `                                       | JSON null                                                                                                                                                                                                                                                       |
| Empty                  | object        | `{} `                                     | An empty JSON object                                                                                                                                                                                                                                            |

### Json Options

* **Emit fields with default values**:
  Fields with default values are omitted by default in proto3 JSON output. An implementation may provide an option to override this behavior and output fields with their default values.
* **Ignore unknown fields**: 
  Proto3 JSON parser should reject unknown fields by default but may provide an option to ignore unknown fields in parsing.
* **Use proto field name instead of lowerCamelCase name**:
  By default proto3 JSON printer should convert the field name to lowerCamelCase and use that as the JSON name. An implementation may provide an option to use proto field name as the JSON name instead. Proto3 JSON parsers are required to accept both the converted lowerCamelCase name and the proto field name.
* **Emit enum values as integers instead of strings**:
  The name of an enum value is used by default in JSON output. An option may be provided to use the numeric value of the enum value instead.


## Generate classes

```bash
protoc path/to/file.proto \
  --proto_path=IMPORT_PATH \
  --cpp_out=DST_DIR \
  --java_out=DST_DIR \
  --python_out=DST_DIR \
  --go_out=DST_DIR \
  --ruby_out=DST_DIR \
  --objc_out=DST_DIR \
  --csharp_out=DST_DIR
```

* You must provide one or more `.proto` files as input.
  Multiple `.proto` files can be specified at once. Although the files are named relative to the current directory, each file must reside in one of the `IMPORT_PATHs` so that the compiler can determine its canonical name.