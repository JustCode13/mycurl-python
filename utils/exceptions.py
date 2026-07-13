import typing

class CurlError(Exception):
    def __init__(self, message: str) -> None:
        if not isinstance(message, str):
            raise TypeError("message must be a string")
        
        if not message.strip():
            raise ValueError("message cannot be empty")
        
        self.message = message
        super().__init__(message)

    def __str__(self):
        return self.message;



class ConfigurationError(CurlError):
    """Invalid runtime configuration."""


class InvalidURLException(CurlError):
    """Malformed URL supplied by user."""


class UnsupportedSchemeError(CurlError):
    """Unsupported URL scheme encountered."""


class InvalidMethodError(CurlError):
    """Unsupported HTTP method."""


class InvalidHeaderError(CurlError):
    """Malformed HTTP header."""


class InvalidHostError(CurlError):
    """Hostname validation failed."""


class DNSResolutionError(CurlError):
    """DNS lookup failed."""


class NetworkConnectionError(CurlError):
    """TCP connection could not be established."""


class SocketReadError(CurlError):
    """Socket receive operation failed."""


class SocketWriteError(CurlError):
    """Socket send operation failed."""


class ConnectionClosedError(CurlError):
    """Peer closed connection unexpectedly."""


class ConnectionPoolError(CurlError):
    """Connection pool operation failed."""


class TLSHandshakeError(CurlError):
    """TLS handshake failed."""


class CertificateVerificationError(CurlError):
    """Server certificate verification failed."""


class HttpProtocolError(CurlError):
    """HTTP protocol violation detected."""


class InvalidChunkEncodingError(CurlError):
    """Malformed chunked transfer encoding."""


class RedirectLoopError(CurlError):
    """Redirect cycle detected."""


class RedirectLimitExceededError(CurlError):
    """Maximum redirect depth exceeded."""


class RetryLimitExceededError(CurlError):
    """Retry policy exhausted."""