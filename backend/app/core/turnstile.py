import json
from typing import Optional, Tuple
from urllib.error import URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen

from . import config

SITEVERIFY_URL = "https://challenges.cloudflare.com/turnstile/v0/siteverify"


def validate_turnstile_token(
    token: str, remote_ip: Optional[str] = None
) -> Tuple[bool, list[str]]:
    if not token:
        return False, ["missing-input-response"]
    if not config.TURNSTILE_SECRET_KEY:
        return False, ["missing-input-secret"]

    payload = {
        "secret": config.TURNSTILE_SECRET_KEY,
        "response": token,
    }
    if remote_ip:
        payload["remoteip"] = remote_ip

    request = Request(
        SITEVERIFY_URL,
        data=urlencode(payload).encode("utf-8"),
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )

    try:
        with urlopen(request, timeout=5) as response:
            result = json.loads(response.read().decode("utf-8"))
    except (TimeoutError, URLError, ValueError):
        return False, ["internal-error"]

    return bool(result.get("success")), list(result.get("error-codes", []))
