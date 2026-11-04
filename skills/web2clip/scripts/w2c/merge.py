"""Ghép nhiều clip thành clip tổng (chuẩn hóa hình + tiếng trước khi nối)."""
import subprocess
def merge_clips(paths, out, crf=25):
    args=[]; fc=""
    for i,p in enumerate(paths):
        args+=["-i",p]; fc+=f"[{i}:v]fps=30,format=yuv420p,setsar=1[v{i}];[{i}:a]aresample=44100,aformat=channel_layouts=stereo[a{i}];"
    fc+="".join(f"[v{i}][a{i}]" for i in range(len(paths)))+f"concat=n={len(paths)}:v=1:a=1[v][a]"
    subprocess.run(["ffmpeg","-y","-loglevel","error"]+args+["-filter_complex",fc,"-map","[v]","-map","[a]","-c:v","libx264","-preset","veryfast","-crf",str(crf),"-c:a","aac","-b:a","160k","-movflags","+faststart",out],check=True)
    return out
