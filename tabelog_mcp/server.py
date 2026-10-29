import uuid

import requests
from mcp.server.fastmcp import FastMCP

BASE = "https://api.tabelog.com/tabelog_inbound_appli"
VERSION = "TabelogInbound Android/ver2.24.1"

mcp = FastMCP("tabelog")
_http = requests.Session()
_http.headers.update({"User-Agent": VERSION, "X-Tabelog-Appli-Version": VERSION})
_state = {"secret": ""}


def _secret():
    if not _state["secret"]:
        r = _http.post(f"{BASE}/secret_token_generate/create", data={"lang": "en", "code": str(uuid.uuid4())}, timeout=30)
        r.raise_for_status()
        _state["secret"] = r.json()["secret_token"]
    return _state["secret"]


def _get(endpoint, params):
    params = {k: v for k, v in params.items() if v is not None}
    params.setdefault("lang", "en")
    r = _http.get(f"{BASE}/{endpoint}", params=params, headers={"X-Tabelog-Secret-Token": _secret()}, timeout=30)
    if r.status_code >= 400:
        raise RuntimeError(f"Tabelog returned HTTP {r.status_code}: {r.text[:200]}")
    return r.json()


@mcp.tool()
def suggest_search(keyword: str, current_latitude: float | None = None, current_longitude: float | None = None) -> dict:
    """Autocomplete restaurants, areas and genres for a keyword."""
    return _get("suggest_search/index", {"keyword": keyword, "current_latitude": current_latitude, "current_longitude": current_longitude})


@mcp.tool()
def search_restaurants(page: int = 1, search_type: str = "normal", latitude: float | None = None, longitude: float | None = None, range: float | None = None,
                       area_datatype: str | None = None, area_datatype_id: int | None = None,
                       genre_datatype: str | None = None, genre_datatype_id: int | None = None, sort_mode: str | None = None) -> dict:
    """Search Japanese restaurants. search_type is normal, current or map; area_datatype is area1, area2, majorCity, municipal, prefecture or station; genre_datatype is genre0 to genre3; sort_mode is totalRanking, distance, accessRanking, reservationRanking or domesticMostReserved. Get ids from the area tools and suggest_search."""
    return _get("restaurant_search/index", {"page": page, "search_type": search_type, "latitude": latitude, "longitude": longitude, "range": range,
                                            "area_datatype": area_datatype, "area_datatype_id": area_datatype_id,
                                            "genre_datatype": genre_datatype, "genre_datatype_id": genre_datatype_id, "sort_mode": sort_mode})


@mcp.tool()
def restaurant_detail(restaurant_id: int) -> dict:
    """Get details for one restaurant."""
    return _get("restaurant_detail/show", {"restaurant_id": restaurant_id})


@mcp.tool()
def restaurant_reviews(restaurant_id: int, page: int = 1) -> dict:
    """Get reviews for a restaurant."""
    return _get("restaurant_detail_review_list/index", {"restaurant_id": restaurant_id, "page": page})


@mcp.tool()
def restaurant_menu(restaurant_id: int) -> dict:
    """Get a restaurant's menu list."""
    return _get("restaurant_detail_menu_list/index", {"restaurant_id": restaurant_id})


@mcp.tool()
def restaurant_photos(restaurant_id: int, page: int = 1) -> dict:
    """Get a restaurant's photos."""
    return _get("restaurant_detail_photo_list/index", {"restaurant_id": restaurant_id, "page": page})


@mcp.tool()
def restaurant_vacancy(restaurant_id: int) -> dict:
    """Get vacancy status for a restaurant over the next few days."""
    return _get("restaurant_detail_vacancy_status_on_latest_days/index", {"restaurant_id": restaurant_id})


@mcp.tool()
def popular_nearby(latitude: float, longitude: float) -> dict:
    """Get popular items near a coordinate."""
    return _get("popular_item_nearby/index", {"latitude": latitude, "longitude": longitude})


@mcp.tool()
def area_level1(prefecture_id: int) -> dict:
    """List first level areas for a prefecture."""
    return _get("area_area1/index", {"prefecture_id": prefecture_id})


@mcp.tool()
def area_level2(area1_id: int) -> dict:
    """List second level areas inside a first level area."""
    return _get("area_area2/index", {"area1_id": area1_id})


@mcp.tool()
def stations(area2_id: int) -> dict:
    """List stations in a second level area."""
    return _get("area_station/index", {"area2_id": area2_id})


@mcp.tool()
def tabelog_get(endpoint: str, params: dict | None = None) -> dict:
    """Read-only escape hatch: GET any endpoint name under /tabelog_inbound_appli/ from the Tabelog spec (see tabelog-api-spec)."""
    if ".." in endpoint or endpoint.startswith("/"):
        raise ValueError("endpoint must be relative, such as restaurant_detail/show")
    return _get(endpoint, params or {})


def main():
    mcp.run()


if __name__ == "__main__":
    main()
