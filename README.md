# Daily Wisdom API

A simple **FastAPI + SQLite** project that provides random quotes (wisdom sayings) via API.  
This project is designed as an **open-source tool** that anyone can clone, run, and extend.

## 技術スタック
- スクレイピング関連
    - requests : HTML データ取得
    - BeautifulSoup4 : HTML パース
- データベース関連
    - SQLite3
- API
    - FastAPI

## API設計

### ランダム取得
- GET /quotes/random
- レスポンス例
```json
{
    "philosopher": "Socrates", 
    "quote": "The unexamined life is not worth living."
}
```
- クエリパラメータ不要（特定の哲学者から取得したい場合は ?philosopher=... を利用）

### 名言の追加
- POST /quotes
- リクエストボディ(JSON):
```json
{
    "philosopher": "Plato",
    "quote": "Wise men speak because they have something to say."
}
```

### 名言の削除
- DELETE /quotes
- クエリパラメータ:
```json
{
    "philosopher": "Plato",
    "quote": "Wise men speak because they have something to say." 
}
```