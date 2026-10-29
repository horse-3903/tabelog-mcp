<div align="center">

# Tabelog MCP Server

Unofficial Tabelog MCP server: let AI assistants search Japanese restaurants, read reviews and menus through the Tabelog Inbound app API.

[![Python](https://img.shields.io/badge/Python_3.10-3776AB?style=flat-square&logo=python&logoColor=white)](https://www.python.org/)
[![MCP](https://img.shields.io/badge/MCP-000000?style=flat-square&logo=anthropic&logoColor=white)](https://modelcontextprotocol.io/)
[![License](https://img.shields.io/github/license/horse-3903/tabelog-mcp?style=flat-square)](LICENSE)

</div>

---

## Overview

**tabelog-mcp** is a Model Context Protocol server for Tabelog. It wraps the unofficial Tabelog API documented in [tabelog-api-spec](https://github.com/horse-3903/tabelog-api-spec).

**Status:** the anonymous token request, area lookup, keyword suggestions, restaurant search, detail, reviews, menu, photos and nearby popular items were checked live and return data. Other tools and the `tabelog_get` escape hatch are untested. The server uses `requests`, because the same token request from `httpx` was answered with HTTP 403 by Tabelog's Cloudflare.

---

## Features

- **Search** - restaurants by area, genre or coordinates, plus keyword suggestions
- **Detail** - restaurant info, reviews, menus, photos and vacancy
- **Areas** - prefecture, area and station lookups
- **Read-only** - no login and no writes; `tabelog_get` calls any GET endpoint from the spec

---

## Tech Stack

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![MCP](https://img.shields.io/badge/MCP-000000?style=for-the-badge&logo=anthropic&logoColor=white)

---

## Getting Started

### Prerequisites

- Python 3.10+

### Installation

```bash
git clone https://github.com/horse-3903/tabelog-mcp
cd tabelog-mcp
pip install .
```

### Run locally

```bash
tabelog-mcp
```

### Add to Claude Desktop or Claude Code

```json
{
  "mcpServers": {
    "tabelog": { "command": "tabelog-mcp" }
  }
}
```

---

## FAQ

**Is there an official Tabelog MCP server?** No. This one is unofficial and uses the reverse engineered Tabelog Inbound app API from [tabelog-api-spec](https://github.com/horse-3903/tabelog-api-spec).

**Does it need a Tabelog account?** No. It requests an anonymous device token on first use.

---

## Disclaimer

Unofficial and not affiliated with Tabelog or Kakaku.com. **Use at your own risk.** Calling the API outside the official app may violate the service's terms and can lead to blocking or a suspended account. The authors accept no responsibility for any consequences.
