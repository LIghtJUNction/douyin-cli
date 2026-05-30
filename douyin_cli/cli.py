"""Command line entry point for douyin-cli."""

from __future__ import annotations

import sys


def _prefer_utf8_stdio() -> None:
    for stream in (sys.stdout, sys.stderr):
        reconfigure = getattr(stream, "reconfigure", None)
        if reconfigure is None:
            continue
        try:
            reconfigure(encoding="utf-8")
        except (OSError, ValueError):
            continue


_prefer_utf8_stdio()

from douyin_cli.commands.root import main  # noqa: E402

__all__ = ["main"]


if __name__ == "__main__":
    main()
