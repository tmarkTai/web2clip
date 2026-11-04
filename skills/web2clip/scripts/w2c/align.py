"""Căn ranh giới từng đoạn thoại theo khoảng lặng trong file giọng."""
import subprocess,re
def duration(path):
    return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",path],capture_output=True,text=True).stdout)
def silences(path, th=-35, d=0.28):
    err=subprocess.run(["ffmpeg","-hide_banner","-i",path,"-af",f"silencedetect=noise={th}dB:d={d}","-f","null","-"],capture_output=True,text=True).stderr
    st=[float(x) for x in re.findall(r"silence_start: ([0-9.]+)",err)]
    en=[float(x) for x in re.findall(r"silence_end: ([0-9.]+)",err)]
    return list(zip(st,en))
def align(path, paras, window=4.5, min_gap=0.3):
    """Trả về [t0, b1, ..., D]: điểm bắt đầu từng đoạn + độ dài file.
    Ước lượng theo tỉ lệ số chữ rồi bắt dính vào khoảng lặng gần nhất."""
    D=duration(path); S=silences(path); n=sum(len(p) for p in paras) or 1
    t0=S[0][1] if S and S[0][0]<0.05 else 0.0
    t1=S[-1][0] if S and S[-1][1]>D-0.05 else D
    B=[0.0]; acc=0; used=set()
    for p in paras[:-1]:
        acc+=len(p); est=t0+(t1-t0)*acc/n
        c=[(abs((s+e)/2-est),i,(s+e)/2) for i,(s,e) in enumerate(S) if i not in used and e-s>=min_gap and abs((s+e)/2-est)<window]
        if c: best=min(c); used.add(best[1]); B.append(best[2])
        else: B.append(est)
    B.append(D)
    for i in range(1,len(B)):
        if B[i]<=B[i-1]: B[i]=B[i-1]+0.3
    return B
