<div align="center">

# Tabelog MCP Server

Unofficial Tabelog MCP server (experimental): let AI assistants search Japanese restaurants, read reviews and menus through the Tabelog Inbound app API.

[![Python](https://img.shields.io/badge/Python_3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/github/license/horse-3903/tabelog-mcp?style=flat-square)](LICENSE)

</div>

---

## Overview

**tabelog-mcp** is a Model Context Protocol server for Tabelog. It wraps the unofficial Tabelog API documented in [tabelog-api-spec](https://github.com/horse-3903/tabelog-api-spec).

**Status: untested.** The anonymous token request (`secret_token_generate/create`) was answered with HTTP 403 and an HTML page when tried from a normal client, so none of the tools have been verified against the live service. Treat this as a draft.

---

## Features

- **Search** - restaurants by area, genre or coordinates, plus keyword suggestions
- **Detail** - restaurant info, reviews, menus, photos and vacancy
- **Areas** - prefecture, area and station lookups
- **Read-only** - no login, no writes; `tabelog_get` calls any GET endpoint from the spec

---

## Getting Started

```bash
pip install .
tabelog-mcp
```

---

## Disclaimer

Unofficial and not affiliated with Tabelog or Kakaku.com. **Use at your own risk.** Calling the API outside the official app may violate the service's terms and can lead to blocking or a suspended account. The authors accept no responsibility for any consequences.
