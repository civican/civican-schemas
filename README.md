# civican-schemas

This repository contains central Protobuf schemas and generated source code for the Civican platform.

## Structure

- `src/civican_schemas/proto/`: Protobuf definition files.
- `src/civican_schemas/`: Generated ConnectRPC/Protobuf Python code.

## Generating schemas

To generate/update the Python client files from the Protobuf definitions, run:

```bash
buf generate src
```
