---
name: web2clip-record
description: Use when recording a web page into a narrated clip synced to an audio file — building the spec JSON, running the synced recorder, fixing out-of-sync effects, grey areas, failed clicks or short/corrupt outputs — "quay clip", "hình không khớp giọng", "vùng xám", "/web2clip-record".
---

# web2clip-record · Giai đoạn 4: quay hình đồng bộ giọng

**Đọc trước:** `../web2clip/references/loi-thuong-gap.md`.

## 1. Viết spec cho mỗi clip
Mẫu: `examples/spec_example.json`. Mỗi đoạn trong `paras` = **đúng 1 đoạn thoại của file giọng** (cùng thứ tự, cùng nội dung).
`acts`: `[mốc 0..1 trong đoạn, hành động, tham số...]`. Hành động: `untitle`, `end`(tag,tiêu đề,phụ đề), `go`(#hash), `load`(url), `hl`(selector,pad), `hlt`(chữ), `off`, `cur`, `click`, `flash`, `set`/`sel`(selector,giá trị), `slide`(selector,[giá trị]), `js`.
Tùy chọn: `start`, `mascot_selector`, `host_label`, `contact_label`, `caption_map` [[chữ đọc, chữ hiện]].
Kiểm tra: `python -c "import json;from w2c.spec import validate_spec;print(validate_spec(json.load(open('spec.json'))))"` → phải ra `[]`.

## 2. Quay
```bash
cd <skill web2clip>/scripts && python -m w2c.record /duong/dan/spec.json --out Clip1.mp4
```
- Tối đa **2–3 clip chạy song song** (nhiều hơn máy quá tải, mất khung hình → báo lỗi dấu đồng bộ).
- Lệnh quá 5 phút: chạy nền `nohup ... &` rồi kiểm tra sau.

## 3. Tự soát trước khi gửi
- `ffprobe`: độ dài ≈ file giọng, 1080x1920, có luồng audio.
- Trích 4–6 khung (`ffmpeg -ss T -frames:v 1`) xem phụ đề có khớp đoạn, khung kết hiện đúng lúc.
- Ghi lại `click fail` trong log → sửa selector (tìm bằng Playwright `querySelectorAll`).
