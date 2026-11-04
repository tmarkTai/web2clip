# web2clip 🎬 · Từ trang web thành chuỗi clip có giọng dẫn AI

Skill cho Claude: biến một trang web (nhất là trang tương tác) thành **chuỗi clip ngắn theo chương + clip tổng**, có **người dẫn AI** (ElevenLabs), **hiệu ứng trên web đi đúng theo lời** (viền sáng, con trỏ bấm, kéo thanh, phụ đề), số liệu đúng 100% vì quay từ trang thật. Kèm **bảng duyệt kịch bản** trên điện thoại.

Đúc kết từ dự án thật: chuỗi 8 clip giới thiệu hệ thống Team Sale MODORO (dọc 9:16, ~9 phút).

## Lệnh
| Lệnh | Làm gì |
|---|---|
| `/web2clip` | Trọn quy trình 7 giai đoạn |
| `/web2clip-setup` | Kiểm tra công cụ, kết nối, quyền mạng, tài khoản ElevenLabs |
| `/web2clip-plan` | Đọc web, ý tưởng, kịch bản 2 cột, bảng duyệt |
| `/web2clip-voice` | Đề xuất giọng, tạo giọng, lấy file về |
| `/web2clip-record` | Quay hình đồng bộ giọng, xuất clip |
| `/web2clip-merge` | Ghép clip tổng, đặt tên, giao file |

Hoặc nói tự nhiên: *"làm clip giới thiệu từ trang web này"*, *"dựng video có giọng đọc AI cho hệ thống của mình"*.

## Cài đặt
**Claude Code (plugin):**
```bash
/plugin marketplace add tmarkTai/web2clip
/plugin install web2clip
```
**Claude Code (thủ công):** `git clone https://github.com/tmarkTai/web2clip` rồi chép các thư mục trong `skills/` vào `~/.claude/skills/`.
**Claude.ai / app:** Cài đặt → Khả năng → Skills → tải lên từng thư mục trong `skills/` (nén zip). Bật **Chạy code và tạo file**.

## Cần chuẩn bị
- Kết nối **ElevenLabs** (giọng đọc). Clip dùng cho kinh doanh nên dùng gói **Starter** trở lên.
- Quyền mạng cho máy dựng: `elevenlabs.io`, `api.elevenlabs.io`, `api.us.elevenlabs.io`, `elevenlabsusercontent.com`, `storage.googleapis.com`.
- Máy dựng có `ffmpeg`, `playwright` (Chromium) — kiểm tra: `python -m w2c.check_env` trong `skills/web2clip/scripts`.

## Quy trình
1. Kiểm tra kết nối → 2. Sẵn sàng quyền → 3. Ý tưởng + bảng duyệt → 4. Kịch bản, giọng, quay, ghép từng clip → 5. Đề xuất giọng → 6. Clip tổng → 7. Sửa đến khi hài lòng.

## Kiểm thử
```bash
pip install pytest playwright && playwright install chromium
python -m pytest -q tests
```
20 bài kiểm thử: phụ đề, căn thời gian theo khoảng lặng, dấu đồng bộ, kiểm tra kịch bản, bảng duyệt, ghép clip, kiểm tra môi trường và **1 bài quay thử toàn trình** (trang mẫu + giọng giả lập → MP4 1080x1920 có tiếng).

## Giấy phép
MIT. Tác giả: Tmark Tài · MODORO.
