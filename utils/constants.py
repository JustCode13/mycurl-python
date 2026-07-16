import http

HTTP_DEFAULT_PORTS: dict[str, int]
"""Default ports for supported schemes."""

DEFAULT_USER_AGENT: str
"""Default User-Agent header."""

DEFAULT_BUFFER_SIZE: int
"""Default socket receive size."""

SUPPORTED_HTTP_METHODS: frozenset[str]
"""Supported request methods."""

REDIRECT_STATUS_CODES: frozenset[int]
"""HTTP redirect status codes."""

HOP_BY_HOP_HEADERS: frozenset[str]
"""Headers not forwarded across connections."""

DEFAULT_CONNECT_TIMEOUT: float
"""Default TCP connect timeout."""

DEFAULT_READ_TIMEOUT: float
"""Default socket read timeout."""

MAXIMUM_HEADER_SIZE: int
"""Upper bound for accepted response headers."""
