---
name: web2clip
description: Use when the user wants a video/clip (giới thiệu, hướng dẫn, explainer, walkthrough) built from a website or interactive web page, with an AI voice host and on-screen effects synced to the narration — e.g. "làm clip giới thiệu hệ thống", "dựng video từ trang web", "clip có giọng đọc AI", "/web2clip". Also when resuming any phase: setup, kịch bản, giọng đọc, quay hình, ghép clip tổng.
---

# web2clip · Từ trang web thành chuỗi clip có giọng dẫn

Biến một trang web (tốt nhất là trang tương tác) thành **chuỗi clip ngắn theo chương + 1 clip tổng**, dọc 9:16 hoặc ngang 16:9, có **người dẫn AI** (giọng ElevenLabs), **hiệu ứng trên web đi đúng theo lời** (viền sáng, con trỏ bấm, kéo thanh, phụ đề), số liệu đúng 100% vì quay từ trang thật.

## Lệnh con (dùng riêng khi chỉ cần 1 giai đoạn)
| Lệnh | Giai đoạn |
|---|---|
| `/web2clip-setup` | 1–2 · Kiểm tra kết nối, công cụ, quyền mạng, tài khoản |
| `/web2clip-plan` | 3 · Đọc web, đề xuất ý tưởng, kịch bản + bảng duyệt (dashboard) |
| `/web2clip-voice` | 4–5 · Đề xuất giọng, tạo giọng từng clip, lấy file về |
| `/web2clip-record` | 4 · Quay hình đồng bộ giọng, xuất từng clip |
| `/web2clip-merge` | 6 · Ghép clip tổng, đặt tên, giao file, lưu trữ |

Chạy `/web2clip` = đi trọn 7 giai đoạn dưới đây theo thứ tự. **Không bỏ bước duyệt.**

## Luật vàng (đúc kết từ dự án thật)
1. **Duyệt chữ trước, tốn tiền sau:** kịch bản phải được duyệt trước khi tạo giọng (giọng tốn credit).
2. **Làm thử 1 clip trước** (pilot) để người dùng duyệt giọng + kiểu hiệu ứng, rồi mới làm hàng loạt.
3. **Giọng là người dẫn chuyện, không đọc lại chữ trên web.** Có tên vai (ví dụ "Mia, trợ lý của <tên bạn>"), xưng hô thân thiện, mở bằng câu hỏi/tình huống, kết bằng câu dẫn sang phần sau.
4. **Chia chuỗi clip ngắn theo chương (1–2 phút)** rồi mới ghép clip tổng. Không làm 1 clip dài ngay từ đầu.
5. **Hình phải đi theo lời:** câu nhắc tới phần nào thì phần đó sáng lên đúng lúc. Dùng bộ quay đồng bộ có dấu ẩn (`scripts/w2c/record.py`), không ước lượng bằng tay.
6. **Hỏi người dùng tối đa 1–3 câu mỗi lần**, có lựa chọn bấm sẵn. Báo thật khi có giới hạn.

## Quy trình 7 giai đoạn
### 1. Kiểm tra kết nối → xem `/web2clip-setup`
Chạy `python -m w2c.check_env` (trong thư mục `scripts/`). Báo bảng: công cụ nào có, kết nối nào có (ElevenLabs, Drive, Canva, trình duyệt), thiếu gì thì đề xuất cài + hướng dẫn tạo tài khoản.

### 2. Sẵn sàng MCP / API / quyền
Thiếu quyền mạng → hướng dẫn người dùng mở đúng tên miền (danh sách trong setup). Thiếu kết nối ElevenLabs → mời kết nối. Nhắc chọn **"Luôn cho phép"** khi ô xin phép công cụ hiện ra.

### 3. Lên ý tưởng → xem `/web2clip-plan`
Đọc trang web, liệt kê chương/mục, đề xuất: khung hình, độ dài, giọng, người dẫn, chia bao nhiêu clip. Viết kịch bản 2 cột (Lời đọc · Hiệu ứng trên web). Dựng **bảng duyệt** (`w2c.dashboard`) và gửi link để người dùng nắm overview, duyệt từng clip.

### 4. Kịch bản → giọng → quay → ghép từng clip
Giọng: `/web2clip-voice`. Quay: `/web2clip-record`. Cập nhật bảng sau mỗi clip.

### 5. Đề xuất giọng
Lọc giọng theo ngôn ngữ, giới tính, độ tuổi, vùng miền; đưa 2–3 lựa chọn kèm lý do; mặc định chọn giọng tự nhiên, kể chuyện.

### 6. Clip tổng → xem `/web2clip-merge`
Ghép theo thứ tự, đặt tên `<Dự án>_Clip<N>_<TenPhan>.mp4`, clip tổng đặt `0. ..._TONG-HOP` để luôn đứng đầu thư mục.

### 7. Giao hàng tới khi hài lòng 100%
Gửi file + cập nhật bảng, tự soát khung hình trước khi gửi (trích 4–6 khung/clip), liệt kê lỗi tự phát hiện, sửa đến khi người dùng duyệt. Lưu kịch bản, giọng, spec để sửa lại nhanh.

## Tài liệu tham khảo
- `references/loi-thuong-gap.md` — các lỗi đã gặp và cách tránh (BẮT BUỘC đọc trước khi quay).
- `references/viet-kich-ban.md` — cách viết lời dẫn thu hút + mẫu kịch bản.
- `references/chon-giong.md` — cách đề xuất giọng, ước credit, gói ElevenLabs.
- `examples/spec_example.json` (ở gốc repo) — mẫu file kịch bản dựng.
