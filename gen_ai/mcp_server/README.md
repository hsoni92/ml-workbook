# MCP Server (FastMCP)

A minimal [FastMCP](https://gofastmcp.com) MCP server using Python, [uv](https://docs.astral.sh/uv/), and `.env` for configuration.

## Setup

1. **Copy env template and edit (optional):**
   ```bash
   cp .env.example .env
   ```

2. **Install and run with uv:**
   ```bash
   uv sync
   uv run python server.py
   ```

   Or use the FastMCP CLI (auto-finds the server in `server.py`):
   ```bash
   uv run fastmcp run server.py
   ```

## Configuration (.env)

| Variable        | Default     | Description                                      |
|----------------|-------------|--------------------------------------------------|
| `MCP_NAME`     | My MCP Server | Server display name                             |
| `MCP_TRANSPORT`| stdio       | `stdio` (for Claude/Cursor) or `http`            |
| `MCP_HOST`     | 127.0.0.1   | Bind address when using HTTP transport          |
| `MCP_PORT`     | 8000        | Port when using HTTP transport                  |

- **stdio**: Default; use for Cursor, Claude Desktop, etc. (client spawns the server).
- **http**: Run as a web server; endpoint is `http://<MCP_HOST>:<MCP_PORT>/mcp`.

## Run over HTTP

In `.env` set:
```env
MCP_TRANSPORT=http
MCP_PORT=8000
```

Then:
```bash
uv run python server.py
```

Or with the CLI:
```bash
uv run fastmcp run server.py --transport http --port 8000
```

## Verify

```bash
uv run fastmcp version
uv run fastmcp list server.py
```

## Basic testing (client)

A minimal client runs the server over stdio, lists tools, and calls `greet`:

```bash
uv run python client.py
# Hello, World!

uv run python client.py --name "Alice"
# Hello, Alice!
```

Options:

- `--server PATH` – path to `server.py` (default: `server.py` in current directory)
- `--name NAME` – argument for the `greet` tool (default: `World`)
