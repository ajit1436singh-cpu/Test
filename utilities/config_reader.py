from __future__ import annotations

import configparser
import os
from pathlib import Path


ROOT_DIR = Path(__file__).resolve().parents[1]
CONFIG_FILE = ROOT_DIR / "config" / "config.ini"


def _as_bool(value: str) -> bool:
    return value.strip().lower() in {"1", "true", "yes", "on"}


def load_settings() -> dict[str, object]:
    parser = configparser.ConfigParser()
    parser.read(CONFIG_FILE, encoding="utf-8")

    return {
        "base_url": os.getenv("BASE_URL", parser["application"]["base_url"]).rstrip("/"),
        "username": os.getenv("SAUCE_USERNAME", parser["credentials"]["username"]),
        "password": os.getenv("SAUCE_PASSWORD", parser["credentials"]["password"]),
        "headless": _as_bool(os.getenv("HEADLESS", parser["browser"]["headless"])),
        "ignore_https_errors": _as_bool(os.getenv("IGNORE_HTTPS_ERRORS", parser["browser"]["ignore_https_errors"])),
        "viewport_width": int(os.getenv("VIEWPORT_WIDTH", parser["browser"]["viewport_width"])),
        "viewport_height": int(os.getenv("VIEWPORT_HEIGHT", parser["browser"]["viewport_height"])),
        "timeout_ms": int(os.getenv("PLAYWRIGHT_TIMEOUT_MS", parser["browser"]["timeout_ms"])),
        "artifacts_dir": ROOT_DIR / os.getenv("ARTIFACTS_DIR", parser["artifacts"]["directory"]),
        "log_level": os.getenv("LOG_LEVEL", parser["logging"]["level"]),
    }
