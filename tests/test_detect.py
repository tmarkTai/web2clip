import subprocess
from w2c.detect import detect_markers
def make_marker_video(path, colors, seg=1.0):
    inputs=[]; fc=""
    for i,c in enumerate(colors):
        inputs += ["-f","lavfi","-i",f"color=c=white:s=64x64:d={seg}:r=30","-f","lavfi","-i",f"color=c={c}:s=12x12:d={seg}:r=30"]
        fc+=f"[{2*i}:v][{2*i+1}:v]overlay=0:0[v{i}];"
    fc+="".join(f"[v{i}]" for i in range(len(colors)))+f"concat=n={len(colors)}:v=1:a=0[o]"
    subprocess.run(["ffmpeg","-y","-loglevel","error"]+inputs+["-filter_complex",fc,"-map","[o]","-c:v","libx264","-pix_fmt","yuv420p",path],check=True)
def test_detect_sequence(tmp_path):
    p=str(tmp_path/"m.mp4"); make_marker_video(p,["black","red","lime","blue","red"])
    t=detect_markers(p,need=4)
    assert len(t)==4
    assert abs(t[0]-1.0)<0.1 and abs(t[1]-2.0)<0.1 and abs(t[3]-4.0)<0.1
def test_detect_returns_partial_when_missing(tmp_path):
    p=str(tmp_path/"m.mp4"); make_marker_video(p,["black","red"])
    assert len(detect_markers(p,need=3))==1
