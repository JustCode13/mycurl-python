import http

# Default ports for supported URL schemes.
HTTP_DEFAULT_PORTS: dict[str, int] = {
    "http": 80,
    "https": 443,
}

# Default User-Agent sent with every request.
DEFAULT_USER_AGENT: str = "mycurl/1.0"

# Default number of bytes to read from a socket at a time.
DEFAULT_BUFFER_SIZE: int = 4096

# HTTP methods supported by the client.
SUPPORTED_HTTP_METHODS: frozenset[str] = frozenset({
    "GET",
    "POST",
    "PUT",
    "PATCH",
    "DELETE",
    "HEAD",
    "OPTIONS",
})

# HTTP status codes that indicate a redirect.
REDIRECT_STATUS_CODES: frozenset[int] = frozenset({
    http.HTTPStatus.MOVED_PERMANENTLY,   # 301
    http.HTTPStatus.FOUND,               # 302
    http.HTTPStatus.SEE_OTHER,           # 303
    http.HTTPStatus.TEMPORARY_REDIRECT,  # 307
    http.HTTPStatus.PERMANENT_REDIRECT,  # 308
})

# Headers that apply only to a single transport connection.
HOP_BY_HOP_HEADERS: frozenset[str] = frozenset({
    "connection",
    "keep-alive",
    "proxy-authenticate",
    "proxy-authorization",
    "te",
    "trailer",
    "transfer-encoding",
    "upgrade",
})

# Default timeout (seconds) for establishing a TCP connection.
DEFAULT_CONNECT_TIMEOUT: float = 10.0

# Default timeout (seconds) for receiving data from the socket.
DEFAULT_READ_TIMEOUT: float = 30.0

# Maximum allowed size (bytes) of all response headers combined.
MAXIMUM_HEADER_SIZE: int = 65_536