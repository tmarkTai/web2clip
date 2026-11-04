# Lỗi thường gặp và cách tránh (đúc kết từ dự án thật)

| Triệu chứng | Nguyên nhân | Cách đúng |
|---|---|---|
| Video có **vùng xám**, trang chỉ ở góc | `record_video_size` lớn hơn viewport | Quay đúng bằng viewport (540x960), phóng lên 1080x1920 bằng ffmpeg |
| **Hình trễ dần** so với giọng về cuối | Video Playwright chạy chậm hơn đồng hồ thật ~15% | Dùng dấu ẩn đổi màu mỗi đoạn + `detect_markers` + co giãn từng đoạn (đã có trong `record.py`) |
| Clip ra **ngắn bất thường** / mất đoạn | Chạy 4+ clip song song, mất khung hình | Tối đa 2–3 clip song song |
| File MP4 **hỏng** (moov atom not found) | Lệnh bị ngắt do quá 5 phút | Chạy nền `nohup`, kiểm tra bằng ffprobe |
| Con trỏ **không bấm được** | Lớp phụ đề chặn cú bấm | Phụ đề `pointer-events:none`; bấm bằng JS `el.click()` |
| Khung tiêu đề che trang lúc chuyển | Tắt khung trước khi đổi trang | `go` trước, rồi mới `untitle` |
| Không tải được giọng | Thiếu tên miền `elevenlabsusercontent.com` | Mở đủ 5 tên miền (xem setup) |
| "No approval received" | Người dùng chưa bấm ô xin phép | Nhắc chọn "Luôn cho phép", gửi lại |
| Giọng `failed` | ElevenLabs lỗi | Kiểm tra trạng thái sau khi tạo, tạo lại |
| Lời đọc như **đọc chữ trên web** | Viết văn bản theo nội dung trang | Viết như người dẫn: câu hỏi, ví dụ, xưng hô, vai |
| Trang quay ra **sai bố cục điện thoại** | Viewport rộng | Dùng 540x960 để ra bố cục di động |
