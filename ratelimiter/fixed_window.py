"""Fixed window rate limiter.

Stage 1: Brandon writes this one by hand.
"""


class FixedWindowLimiter:
    """Allow at most `limit` requests per user in each `window_seconds` window."""

    def __init__(self, limit: int, window_seconds: int) -> None:
        # TODO(Stage 1): store the config and set up your counter dict.
        raise NotImplementedError

    def allow(self, user_id: str) -> bool:
        """Return True if this request is allowed, False if the user is over the limit."""
        # TODO(Stage 1): figure out the current window, check the count, update it.
        raise NotImplementedError
