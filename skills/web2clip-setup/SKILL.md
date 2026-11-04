---
name: web2clip-setup
description: Use when starting a web-to-video (web2clip) project or when a clip step fails because of missing tools, connectors, network domains, accounts or credits — "kiểm tra máy", "cần cài gì để làm clip", "không tải được giọng", "/web2clip-setup".
---

# web2clip-setup · Giai đoạn 1–2: kiểm tra và chuẩn bị

## 1. Kiểm tra công cụ trong máy dựng
```bash
cd <skill web2clip>/scripts && python -m w2c.check_env
```
Cần: `ffmpeg`, `ffprobe`, `playwright` (Chromium). Thiếu thì: `pip install playwright && playwright install chromium`.

## 2. Kiểm tra kết nối (connector / MCP)
| Kết nối | Dùng để | Bắt buộc |
|---|---|---|
| **ElevenLabs** | Giọng đọc AI tiếng Việt | Có |
| Google Drive | Lưu tài liệu chữ (kịch bản, hồ sơ) | Nên có |
| Canva | Ảnh bìa (thumbnail) | Tùy chọn |
| Netlify / hosting | Đưa trang web lên link thật để quay | Khi web chưa có link |
Thiếu ElevenLabs → mời người dùng kết nối (tìm trong danh mục connector). Không tự chọn thay đối tác khác.

## 3. Quyền mạng của máy dựng (hay bị vướng nhất)
Nếu `check_env` báo chặn, hướng dẫn người dùng: **Cài đặt → Khả năng (Capabilities) → Chạy code và tạo file → Danh sách tên miền**, thêm đủ 5 tên miền:
`elevenlabs.io`, `api.elevenlabs.io`, `api.us.elevenlabs.io`, `elevenlabsusercontent.com`, `storage.googleapis.com`
(file giọng nằm ở `elevenlabsusercontent.com` — hay bị quên).

## 4. Tài khoản và credit
- ElevenLabs tính **credit theo số ký tự** (gộp 1 file dài không tiết kiệm). Ước: ~1 credit/ký tự với model v4; clip 1–2 phút ≈ 600–1.500 credit.
- Gói Free (~10.000 credit/tháng) **không có quyền thương mại**. Clip cho kinh doanh → khuyên **Starter** (thường có ưu đãi tháng đầu).
- **Không** khuyên lập nhiều tài khoản free (vi phạm điều khoản, dễ bị khóa).
- Thanh toán: người dùng tự làm, không nhập thẻ thay. Gửi link `https://elevenlabs.io/app/subscription`.

## 5. Ô xin phép công cụ
Mỗi lệnh ElevenLabs / đăng bảng có thể hiện ô xin phép. Nhắc người dùng chọn **"Luôn cho phép"**; nếu lệnh báo "No approval received" thì nói rõ và gửi lại sau.

## 6. Lưu file lớn
Connector Drive không mang được video lớn. Giao file trong chat + hướng dẫn kéo vào thư mục, hoặc lệnh `mv ~/Downloads/<tiền tố>*.mp4 "<đường dẫn thư mục Drive trên máy>"`. Muốn lưu thẳng → dùng Claude Cowork trên máy tính.
