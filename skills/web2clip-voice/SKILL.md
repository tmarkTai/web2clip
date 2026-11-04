---
name: web2clip-voice
description: Use when choosing an AI narrator voice or generating/downloading narration audio for web2clip clips with ElevenLabs — "chọn giọng", "đề xuất giọng đọc", "tạo voice", "giọng bị lỗi", "lấy file giọng về", "/web2clip-voice".
---

# web2clip-voice · Giai đoạn 4–5: giọng đọc

## Đề xuất giọng
1. Liệt kê giọng: lọc `language`, `gender`, `age` (ví dụ `vi`, female, young). Xem `../web2clip/references/chon-giong.md`.
2. Đưa 2–3 giọng kèm lý do (vùng miền khớp người xem, chất kể chuyện, tự nhiên). Mặc định giọng kể chuyện tự nhiên.
3. Dùng **cùng 1 giọng + 1 model cho cả chuỗi** để đồng nhất.

## Viết văn bản cho giọng
- **Số đọc bằng chữ** trong lời ("hai mươi phần trăm", "năm triệu ba trăm mười nghìn"), phụ đề sẽ tự đổi lại thành số (`w2c.captions.capify`).
- Mỗi đoạn thoại cách nhau **1 dòng trống** → giọng ngắt nghỉ rõ, giúp căn hình chính xác.
- Tên miền/số điện thoại viết theo cách đọc ("hệ thống chấm chín biz mentor chấm com").

## Tạo giọng
- Mỗi clip 1 lần tạo, `generations_count=1`. Đặt nhãn: `<Dự án> · Clip N · <Tên phần> · Giọng <vai>`.
- ElevenLabs báo **bận** → nói 1 câu, thử lại lượt sau (không tạo tiếp trong lượt đó).
- Sau khi tạo, **kiểm tra trạng thái** bằng get_generations: `failed` → tạo lại ngay.

## Lấy file về máy dựng
`get_generations` → `full_res_url` (tên miền `elevenlabsusercontent.com`) → `curl -o vN.mp3 "<url>"`. Bị chặn → `/web2clip-setup` mục quyền mạng. Kiểm tra độ dài bằng `ffprobe`.
