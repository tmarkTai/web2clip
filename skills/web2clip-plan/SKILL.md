---
name: web2clip-plan
description: Use when planning a clip series from a website — reading the site, proposing format/length/voice/host persona, writing the 2-column script (lời đọc · hiệu ứng trên web) and building the review dashboard — "lên ý tưởng clip", "viết kịch bản clip", "làm dashboard duyệt kịch bản", "/web2clip-plan".
---

# web2clip-plan · Giai đoạn 3: ý tưởng, kịch bản, bảng duyệt

## Bước 1 · Hiểu trang web
Mở trang (Playwright), liệt kê chương/mục, các công cụ tương tác (thanh kéo, nút, biểu đồ), các con số quan trọng. Ghi selector (id/class) của từng phần sẽ quay.

## Bước 2 · Hỏi 3 điểm (dùng câu hỏi có nút bấm)
1. Khung hình: dọc 9:16 (Zalo/TikTok/Reels) · ngang 16:9 · cả hai.
2. Mục đích: **thu hút người mới** (ngắn, cảm xúc) hay **hướng dẫn chi tiết 100%** (đủ ý từng chương). Nếu chi tiết → **chuỗi clip ngắn theo chương** + gộp clip tổng sau.
3. Giọng: nữ trẻ · nam chắc chắn · người dùng tự thu · không lời.

## Bước 3 · Người dẫn và giọng văn
Đặt tên vai (ví dụ "Mia, trợ lý của <tên bạn>"). Lời đọc theo `../web2clip/references/viet-kich-ban.md`: nói chuyện trực tiếp, câu hỏi, ví dụ con số, không đọc lại chữ trên web.

## Bước 4 · Kịch bản 2 cột
Mỗi clip: bảng `Lời đọc | Hiệu ứng trên web`, mỗi hàng 1 đoạn thoại (1–3 câu). Mở: chào + câu hỏi. Kết: câu dẫn sang phần sau + liên hệ (clip cuối).

## Bước 5 · Bảng duyệt (dashboard)
```python
from w2c.dashboard import build_dashboard
build_dashboard(clips, "bang-dung-clip.html", title="Bảng dựng clip <Dự án>", subtitle="<người dẫn> · <số clip> clip", videos={1:"pv_1.mp4"}, mascot="logo.png")
```
`clips=[{"n":1,"t":"Tổng quan","len":"~1:30","rows":[[lời, hiệu ứng],...],"steps":["ok","todo","todo","todo"]}]` (steps = Kịch bản · Giọng · Quay · Ghép; giá trị ok/wait/todo). Đăng thành artifact, gửi link. Video xem trước nén `432x768 crf 31` để bảng nhẹ (giới hạn 16MB).

## Bước 6 · Duyệt
Duyệt clip 1 trước (pilot). Người dùng duyệt hết → sang `/web2clip-voice`.
