# AGENTS.md: tabelog-mcp

MCP server for the Tabelog Inbound app API documented in `tabelog-api-spec`.

## Layout

- `tabelog_mcp/server.py`: all tools and the HTTP client (anonymous secret token, GET helper).

## Run and test

```bash
pip install -e .
tabelog-mcp
```

## Conventions

- Pin `mcp<2`: the code uses `mcp.server.fastmcp.FastMCP`, which v2 renamed.
- Use `requests`, not `httpx`: Tabelog's Cloudflare answered the token request from `httpx` with HTTP 403 while `requests` succeeded. Do not add header or fingerprint tricks to get around blocks.
- `search_restaurants` needs `page` and `search_type` (normal, current or map), otherwise Tabelog returns HTTP 400.
- Keep the server read-only. Write endpoints need a logged-in account and are not covered.

## Rules

- Never commit credentials, tokens or `.env` files.
- Do not use em dashes in any text. Keep commit messages to one short line, with no Co-Authored-By trailers. Only commit when asked.
