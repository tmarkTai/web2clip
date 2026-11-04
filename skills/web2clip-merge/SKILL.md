---
name: web2clip-merge
description: Use when combining finished web2clip clips into one full-length video, naming and delivering the files, updating the review dashboard or saving to Drive — "ghép clip tổng", "gộp các clip", "lưu clip vào Drive", "/web2clip-merge".
---

# web2clip-merge · Giai đoạn 6–7: clip tổng, giao hàng

## Ghép
```python
from w2c.merge import merge_clips
merge_clips(["Clip1.mp4","Clip2.mp4", ...], "0. <Du-an>_Clip9_TONG-HOP.mp4")
```
Tự chuẩn hóa hình/tiếng trước khi nối. Kiểm tra độ dài = tổng các clip.

## Đặt tên
`<Dự án>_Clip<N>_<TenPhan>.mp4` (không dấu, gạch nối). Clip tổng thêm tiền tố `0. ` để đứng đầu thư mục.

## Giao hàng
1. Gửi file trong chat (present_files), kèm bảng tên + độ dài.
2. Cập nhật bảng duyệt: steps = ok hết, video xem trước có tiếng.
3. Lưu: video lớn → hướng dẫn kéo vào thư mục Drive hoặc lệnh `mv`; kịch bản/hồ sơ chữ → lưu Drive bằng connector.
4. Hỏi người dùng góp ý, sửa đến khi hài lòng 100%.
