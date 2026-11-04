import subprocess
from w2c.merge import merge_clips
def mk(p,d,f):
    subprocess.run(["ffmpeg","-y","-loglevel","error","-f","lavfi","-i",f"color=c=blue:s=108x192:d={d}:r=30","-f","lavfi","-i",f"sine=f={f}:d={d}","-c:v","libx264","-pix_fmt","yuv420p","-c:a","aac","-shortest",p],check=True)
def dur(p): return float(subprocess.run(["ffprobe","-v","error","-show_entries","format=duration","-of","csv=p=0",p],capture_output=True,text=True).stdout)
def test_merge_duration_is_sum(tmp_path):
    a,b=str(tmp_path/"a.mp4"),str(tmp_path/"b.mp4"); mk(a,1.5,440); mk(b,2.0,660)
    out=str(tmp_path/"o.mp4"); merge_clips([a,b],out)
    assert abs(dur(out)-3.5)<0.2
