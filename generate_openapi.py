#!/usr/bin/env python3
"""
OpenAPI仕様を生成してJSONファイルとして保存するスクリプト
"""

import json
import sys
from pathlib import Path

try:
    sys.path.append("src")
    from src.api.api import app
except ImportError as e:
    print(f"❌ FastAPIアプリのインポートに失敗しました: {e}")
    print("src/api/api.py に FastAPI アプリ (app) があることを確認してください")
    sys.exit(1)


def generate_openapi_spec() -> bool:
    docs_dir = Path("docs")
    docs_dir.mkdir(parents=True, exist_ok=True)
    
    try:
        openapi_spec = app.openapi()

        openapi_spec["info"]["title"] = "daily-wisdom-API"
        openapi_spec["info"]["description"] = "哲学者の名言を提供するAPI"
        openapi_spec["info"]["version"] = "1.0.0"

        output_file = docs_dir / "openapi.json"
        output_file.write_text(
            json.dumps(openapi_spec, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

        print(f"✅ OpenAPI仕様を生成しました: {output_file.resolve()}")
        return True

    except Exception as e:
        print(f"❌ OpenAPI仕様の生成に失敗しました: {e}")
        return False


if __name__ == "__main__":
    success = generate_openapi_spec()
    sys.exit(0 if success else 1)