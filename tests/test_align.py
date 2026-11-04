import subprocess
from w2c.align import align, silences
def make_audio(path, segs):
    parts=[]
    for t,s in segs:
        parts.append(f"sine=f=440:d={t}")
        if s: parts.append(f"anullsrc=r=44100:cl=mono:d={s}")
    inputs=[]
    for p in parts: inputs += ["-f","lavfi","-i",p]
    n=len(parts)
    fc="".join(f"[{i}:a]aresample=44100,aformat=channel_layouts=mono[a{i}];" for i in range(n))+"".join(f"[a{i}]" for i in range(n))+f"concat=n={n}:v=0:a=1[o]"
    subprocess.run(["ffmpeg","-y","-loglevel","error"]+inputs+["-filter_complex",fc,"-map","[o]",path],check=True)
def test_silences_found(tmp_path):
    p=str(tmp_path/"a.wav"); make_audio(p,[(2,0.8),(3,0)])
    assert any(1.9<s<2.2 and 2.6<e<2.9 for s,e in silences(p))
def test_align_snaps_to_pauses(tmp_path):
    p=str(tmp_path/"a.wav"); make_audio(p,[(2,0.8),(4,0.8),(2,0)])
    B=align(p,["x"*20,"x"*40,"x"*20])
    assert len(B)==4 and B[0]==0.0
    assert abs(B[1]-2.4)<0.35 and abs(B[2]-7.2)<0.35
    assert abs(B[3]-9.6)<0.1
def test_align_monotonic_even_without_pauses(tmp_path):
    p=str(tmp_path/"a.wav"); make_audio(p,[(6,0)])
    B=align(p,["a"*10,"b"*10,"c"*10])
    assert all(B[i]<B[i+1] for i in range(3))
