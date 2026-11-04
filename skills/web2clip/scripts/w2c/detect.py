"""Đọc dấu đồng bộ (ô màu 12x12 góc trái trên) trong video quay để biết thời điểm thật mỗi đoạn.
Màu xoay vòng đỏ → xanh lá → xanh dương theo số thứ tự đoạn."""
import subprocess
def detect_markers(video, need, fps=30, box=(2,2,8,8)):
    x,y,w,h=box
    raw=subprocess.run(["ffmpeg","-loglevel","error","-i",video,"-vf",f"crop={w}:{h}:{x}:{y},scale=1:1,fps={fps}","-f","rawvideo","-pix_fmt","rgb24","-"],capture_output=True).stdout
    times=[]; k=0; prev=None
    for j in range(0,len(raw)-2,3):
        r,g,b=raw[j],raw[j+1],raw[j+2]; mx=max(r,g,b)
        c=-1 if mx<120 or (r>200 and g>200 and b>200) else (0 if r==mx else 1 if g==mx else 2)
        if c==k%3 and prev!=c and c>=0:
            times.append(j/3/fps); k+=1
            if k>=need: break
        if c>=0: prev=c
    return times
