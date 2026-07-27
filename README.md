# civican-schemas

This repository contains central Protobuf schemas and generated source code for the Civican platform.

## Structure

- `src/civican/schemas/proto/`: Protobuf definition files.
- `src/civican/schemas/`: Generated ConnectRPC, Protobuf, and Pydantic Python code.

## Generating schemas

To generate/update the Python client files and Pydantic schemas from the Protobuf definitions, run:

```bash
uv run buf generate src
```

