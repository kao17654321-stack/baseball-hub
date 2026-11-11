"""從 JSON 產生供雙擊 index.html 預覽的離線資料快取。"""
from pathlib import Path
import json
ROOT = Path(__file__).resolve().parents[1]
FILES = {"teams":"teams", "players":"players", "batting":"batting", "pitching":"pitching", "highlights":"team-highlights", "glossary":"glossary", "awards":"awards", "postseason":"postseason", "freeAgents":"free-agents"}
records = {k: json.loads((ROOT / "data" / (v + ".json")).read_text(encoding="utf-8")) for k, v in FILES.items()}
(ROOT / "js" / "data-bundle.js").write_text("// Generated from data/*.json. Do not edit by hand.\nwindow.BASEBALL_DATA = " + json.dumps(records, ensure_ascii=False, separators=(",", ":")) + ";\n", encoding="utf-8")
print("js/data-bundle.js 已更新")
