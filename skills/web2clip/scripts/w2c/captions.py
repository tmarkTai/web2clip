"""Phụ đề: đổi số đọc bằng chữ sang chữ số và chia câu cho dễ đọc."""
import re
BASE=[
("một trăm tám mươi sáu","186"),("hai trăm năm mươi","250"),("hai trăm bốn mươi","240"),("năm trăm","500"),("sáu trăm","600"),
("bảy mươi hai","72"),("bảy mươi","70"),("một trăm nghìn","100.000"),("một trăm","100"),("ba trăm","300"),
("năm đến mười phần trăm","5–10%"),("hai mươi lăm","25"),("năm mươi phần trăm","50%"),("hai mươi phần trăm","20%"),("mười lăm phần trăm","15%"),("mười phần trăm","10%"),
("sáu mươi","60"),("năm mươi","50"),("bốn mươi","40"),("ba mươi","30"),("hai mươi","20"),("mười sáu","16"),("mười lăm","15"),("mười triệu","10 triệu"),
("một tỷ","1 tỷ"),("hai tỷ","2 tỷ"),("tám triệu","8 triệu"),("sáu triệu","6 triệu")]
def capify(text, extra=None):
    pairs=sorted((extra or [])+BASE, key=lambda p:-len(p[0]))   # cụm dài thay trước
    for a,b in pairs: text=text.replace(a,b)
    return text
def sentences(text, min_len=28, max_len=60):
    parts=[p for p in re.split(r'(?<=[.!?…])\s+', text.strip()) if p]
    out=[]
    for p in parts:
        if out and len(out[-1])<min_len and len(out[-1])+len(p)+1<=max_len: out[-1]+=' '+p
        else: out.append(p)
    return out or [text]
