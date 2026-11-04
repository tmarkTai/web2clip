"""Quay trang web theo kịch bản, đồng bộ với file giọng, xuất MP4 dọc 1080x1920.
Dùng:  python -m w2c.record spec.json [--out final.mp4]
Cơ chế đồng bộ: mỗi đoạn thoại đổi màu ô dấu ẩn ở góc trái; sau khi quay, đọc dấu để biết
thời điểm thật trong video, rồi co giãn từng đoạn cho khớp đúng độ dài đoạn giọng."""
import json,sys,time,os,subprocess,glob,argparse,tempfile
from .align import align
from .captions import capify,sentences
from .detect import detect_markers
from .spec import validate_spec
OV=open(os.path.join(os.path.dirname(__file__),'overlay.js'),encoding='utf-8').read()
MK=['#ff0000','#00ff00','#0000ff']
def record(spec, out=None, w=540, h=960):
    errs=validate_spec(spec)
    if errs: raise ValueError("Kịch bản lỗi: "+"; ".join(errs))
    from playwright.sync_api import sync_playwright
    paras=[p['text'] for p in spec['paras']]; B=align(spec['audio'],paras)
    tmp=tempfile.mkdtemp(prefix="w2c_"); extra=[tuple(x) for x in spec.get('caption_map',[])]
    who=spec.get('host_label',''); contact=spec.get('contact_label','')
    with sync_playwright() as p:
        b=p.chromium.launch()
        ctx=b.new_context(viewport={"width":w,"height":h},record_video_dir=tmp,record_video_size={"width":w,"height":h})
        pg=ctx.new_page(); ev=pg.evaluate; CUR=[0]
        def mark(i): ev("(c=>{let m=document.getElementById('__mk');if(!m){m=document.createElement('div');m.id='__mk';m.style.cssText='position:fixed;left:0;top:0;width:12px;height:12px;z-index:2147483647';document.body.appendChild(m)}m.style.background=c})('"+(MK[i%3] if i>=0 else '#000')+"')")
        def load(url):
            pg.goto(url,wait_until="domcontentloaded")
            try: pg.wait_for_function("[...document.images].every(i=>i.complete)",timeout=3000)
            except Exception: pass
            ev(OV)
        load(spec['start']); mas=spec.get('mascot_selector')
        img=ev(f"(document.querySelector({json.dumps(mas)})||{{}}).src||''") if mas else ''
        ev(f"""__tc(`{'<img src="'+img+'">' if img else ''}{'<span class="who">'+who+'</span>' if who else ''}<small>{spec['tag']}</small><h1>{spec['title']}</h1>`)""")
        mark(-1); pg.wait_for_timeout(600); A0=time.monotonic()
        def at(t):
            d=A0+t-time.monotonic()
            if d>0: time.sleep(d)
        def do(a):
            k=a[0]; q=lambda v: json.dumps(v)
            if k=="untitle": ev("__tc(null)")
            elif k=="end": ev("__hlOff()");ev(f"""__tc(`{'<img src="'+img+'">' if img else ''}<small>{a[1]}</small><h1>{a[2]}</h1><p>{a[3]}</p>{'<span class="who">'+contact+'</span>' if contact else ''}`)""")
            elif k=="go": ev(f"location.hash={q(a[1])}"); pg.wait_for_timeout(350)
            elif k=="load": load(a[1]); mark(CUR[0])
            elif k=="hl": ev(f"__hlOn({q(a[1])},{a[2] if len(a)>2 else 8})")
            elif k=="hlt": ev(f"__hlText({q(a[1])})")
            elif k=="off": ev("__hlOff()")
            elif k=="cur": ev(f"__cur({q(a[1])},false)")
            elif k=="click":
                ev(f"__cur({q(a[1])},true)"); pg.wait_for_timeout(400)
                ev(f"(()=>{{const e=document.querySelector({q(a[1])});if(e){{e.scrollIntoView({{block:'center'}});e.click()}}}})()")
            elif k=="flash": ev(f"__flash({q(a[1])})")
            elif k in ("set","sel"): ev(f"(()=>{{const e=document.querySelector({q(a[1])});if(!e)return;e.value={q(a[2])};e.dispatchEvent(new Event('input',{{bubbles:true}}));e.dispatchEvent(new Event('change',{{bubbles:true}}))}})()")
            elif k=="js": ev(a[1])
            elif k=="slide":
                for v in a[2]:
                    ev(f"(()=>{{const e=document.querySelector({q(a[1])});if(!e)return;e.value={v};e.dispatchEvent(new Event('input',{{bubbles:true}}))}})()"); time.sleep(0.18)
        for i,pa in enumerate(spec['paras']):
            s,e=B[i],B[i+1]; L=e-s; at(s); CUR[0]=i; mark(i)
            sents=sentences(capify(pa.get('cap',pa['text']),extra)); tot=sum(map(len,sents)); acc=0
            evs=[(a[0],0,a[1:]) for a in pa.get('acts',[])]
            for x in sents: evs.append((acc/tot,1,x)); acc+=len(x)
            for f,kind,val in sorted(evs,key=lambda z:(z[0],z[1])):
                at(s+f*L)
                if kind: ev(f"__cap({json.dumps(val)})")
                else: do(val)
        at(B[-1]); mark(len(paras)); time.sleep(0.8); ctx.close(); b.close()
    vid=sorted(glob.glob(os.path.join(tmp,"*.webm")))[-1]
    VT=detect_markers(vid,need=len(paras)+1)
    if len(VT)!=len(paras)+1: raise RuntimeError(f"Chỉ đọc được {len(VT)}/{len(paras)+1} dấu đồng bộ (máy quá tải? chạy ít clip song song hơn)")
    out=out or f"final_{spec['name']}.mp4"; fl=""
    for i in range(len(paras)):
        fct=(B[i+1]-B[i])/(VT[i+1]-VT[i])
        fl+=f"[0:v]trim=start={VT[i]:.3f}:end={VT[i+1]:.3f},setpts=(PTS-STARTPTS)*{fct:.4f},fps=30[s{i}];"
    fl+="".join(f"[s{i}]" for i in range(len(paras)))+f"concat=n={len(paras)}:v=1:a=0,crop={w}:{h-16}:0:16,scale=1080:1920:flags=lanczos[v]"
    subprocess.run(["ffmpeg","-y","-loglevel","error","-i",vid,"-i",spec['audio'],"-filter_complex",fl,"-map","[v]","-map","1:a","-c:v","libx264","-preset","veryfast","-crf","24","-pix_fmt","yuv420p","-c:a","aac","-b:a","160k","-shortest","-movflags","+faststart",out],check=True)
    return out
if __name__=="__main__":
    ap=argparse.ArgumentParser(); ap.add_argument("spec"); ap.add_argument("--out"); a=ap.parse_args()
    print(record(json.load(open(a.spec,encoding='utf-8')),a.out))
