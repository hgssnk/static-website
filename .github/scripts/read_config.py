#!/usr/bin/env python3
"""services/<service>/deploy.yml を読み込み、GitHub Actionsのoutputとして書き出す。
'key: value' の単純な形式のみを想定した最小パーサー(PyYAML不要)。

使い方: read_config.py <service>
"""
import os
import sys


def main() -> None:
    if len(sys.argv) != 2:
        print("使い方: read_config.py <service>", file=sys.stderr)
        sys.exit(1)

    service = sys.argv[1]
    config_path = f"services/{service}/deploy.yml"

    if not os.path.isfile(config_path):
        print(f"設定ファイルが見つかりません: {config_path}", file=sys.stderr)
        sys.exit(1)

    github_output = os.environ["GITHUB_OUTPUT"]
    with open(config_path, encoding="utf-8") as f, open(github_output, "a", encoding="utf-8") as out:
        for line in f:
            line = line.strip()
            if not line or line.startswith("#") or ":" not in line:
                continue
            key, value = line.split(":", 1)
            out.write(f"{key.strip()}={value.strip()}\n")


if __name__ == "__main__":
    main()
