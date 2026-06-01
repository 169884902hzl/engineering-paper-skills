#!/usr/bin/env python3
"""Validate venue profile JSON files and optionally refresh official URLs."""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

ROOT = Path(__file__).resolve().parents[1]
VENUE_PROFILE_DIR = ROOT / "skills/engineering-validation/venue_profiles"
MAX_SOURCE_AGE_DAYS = 370


def load_json(path: Path) -> dict:
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise ValueError(f"{path.relative_to(ROOT)} invalid JSON: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError(f"{path.relative_to(ROOT)} must contain a JSON object")
    return data


def parse_source_date(path: Path, profile_name: str, value: object) -> date:
    if not isinstance(value, str) or not value:
        raise ValueError(f"{path.relative_to(ROOT)}:{profile_name} missing source_date")
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"{path.relative_to(ROOT)}:{profile_name} invalid source_date: {value}") from exc


def check_url(url: str, timeout: float) -> str | None:
    request = Request(url, headers={"User-Agent": "engineering-paper-skills-venue-check/1.0"})
    try:
        with urlopen(request, timeout=timeout) as response:
            status = getattr(response, "status", 200)
            if status >= 400:
                return f"HTTP {status}"
    except HTTPError as exc:
        return f"HTTP {exc.code}"
    except URLError as exc:
        return str(exc.reason)
    except TimeoutError:
        return "timeout"
    return None


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--profile-dir", default=VENUE_PROFILE_DIR, type=Path)
    parser.add_argument("--refresh", action="store_true", help="Fetch official source URLs")
    parser.add_argument("--timeout", type=float, default=12.0)
    args = parser.parse_args()

    errors: list[str] = []
    if not args.profile_dir.exists():
        print(f"Venue profile directory missing: {args.profile_dir}")
        return 1

    for path in sorted(args.profile_dir.glob("*.json")):
        try:
            data = load_json(path)
        except ValueError as exc:
            errors.append(str(exc))
            continue

        profiles = data.get("profiles")
        if not isinstance(profiles, dict) or not profiles:
            errors.append(f"{path.relative_to(ROOT)} missing profiles object")
            continue

        for name, profile in profiles.items():
            if not isinstance(profile, dict):
                errors.append(f"{path.relative_to(ROOT)}:{name} must be an object")
                continue
            if profile.get("official_policy_checked_required") is not True:
                errors.append(f"{path.relative_to(ROOT)}:{name} must require official policy checks")
            if profile.get("profile_status") != "STATIC_SUMMARY_NOT_LIVE_CHECK":
                errors.append(
                    f"{path.relative_to(ROOT)}:{name} must mark profile_status=STATIC_SUMMARY_NOT_LIVE_CHECK"
                )
            url = profile.get("source_url")
            if not isinstance(url, str) or not url.startswith("https://"):
                errors.append(f"{path.relative_to(ROOT)}:{name} must include https source_url")
                continue
            try:
                source_date = parse_source_date(path, name, profile.get("source_date"))
            except ValueError as exc:
                errors.append(str(exc))
                continue
            age = (date.today() - source_date).days
            if age > MAX_SOURCE_AGE_DAYS:
                errors.append(
                    f"{path.relative_to(ROOT)}:{name} source_date is stale by {age} days; refresh profile"
                )
            fields = profile.get("required_fields")
            if not isinstance(fields, list) or "source_url" not in fields or "source_date" not in fields:
                errors.append(f"{path.relative_to(ROOT)}:{name} must require source_url and source_date fields")
            policy_checks = profile.get("policy_checks")
            if not isinstance(policy_checks, list) or len(policy_checks) < 3:
                errors.append(f"{path.relative_to(ROOT)}:{name} must include at least three policy_checks")
            if args.refresh:
                problem = check_url(url, args.timeout)
                if problem is not None:
                    errors.append(f"{path.relative_to(ROOT)}:{name} source_url unreachable: {problem}")
                formatting_url = profile.get("formatting_source_url")
                if isinstance(formatting_url, str) and formatting_url:
                    problem = check_url(formatting_url, args.timeout)
                    if problem is not None:
                        errors.append(
                            f"{path.relative_to(ROOT)}:{name} formatting_source_url unreachable: {problem}"
                        )
            snapshot = profile.get("policy_snapshot")
            if not isinstance(snapshot, dict):
                errors.append(f"{path.relative_to(ROOT)}:{name} missing policy_snapshot")
                continue
            last_checked = snapshot.get("last_checked")
            try:
                parse_source_date(path, f"{name}.policy_snapshot", last_checked)
            except ValueError as exc:
                errors.append(str(exc))
            verification_method = snapshot.get("verification_method")
            if not isinstance(verification_method, str) or "not live policy extraction" not in verification_method:
                errors.append(
                    f"{path.relative_to(ROOT)}:{name} policy_snapshot must state whether it is live extraction"
                )
            excerpt_hash = snapshot.get("policy_excerpt_hash")
            if not isinstance(excerpt_hash, str) or len(excerpt_hash) < 12:
                errors.append(f"{path.relative_to(ROOT)}:{name} policy_snapshot missing policy_excerpt_hash")
            hash_basis = snapshot.get("hash_basis")
            if not isinstance(hash_basis, str) or "policy_checks" not in hash_basis:
                errors.append(f"{path.relative_to(ROOT)}:{name} policy_snapshot missing hash_basis")

    if errors:
        print("Venue profile check failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    mode = "with URL refresh" if args.refresh else "without URL refresh"
    print(f"Venue profile check passed ({mode}).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
