"""Tạo bảng duyệt kịch bản + xem clip (1 file HTML tự chứa, chạy trên điện thoại)."""
import json,base64,os
TPL=os.path.join(os.path.dirname(__file__),'..','..','templates','dashboard.html')
def build_dashboard(clips, out, title="Bảng dựng clip", subtitle="", videos=None, mascot=None):
    vids={str(k):'data:video/mp4;base64,'+base64.b64encode(open(v,'rb').read()).decode() for k,v in (videos or {}).items()}
    mas=('data:image/png;base64,'+base64.b64encode(open(mascot,'rb').read()).decode()) if mascot else ''
    h=open(TPL,encoding='utf-8').read()
    h=h.replace('__TITLE__',title).replace('__SUB__',subtitle).replace('__MAS__',mas)
    h=h.replace('__DATA__',json.dumps(clips,ensure_ascii=False)).replace('__VIDS__',json.dumps(vids))
    open(out,'w',encoding='utf-8').write(h); return out
