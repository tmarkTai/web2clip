import json, os, subprocess
from w2c.record import record
from test_align import make_audio
HERE=os.path.dirname(os.path.abspath(__file__))
def probe(p,k):
    return subprocess.run(["ffprobe","-v","error","-select_streams",k,"-show_entries","stream=width,height,codec_type","-show_entries","format=duration","-of","json",p],capture_output=True,text=True).stdout
def test_record_end_to_end(tmp_path):
    wav=str(tmp_path/"demo.wav"); make_audio(wav,[(2.5,0.7),(2.5,0.7),(3,0)])
    spec=json.load(open(os.path.join(HERE,'..','examples','spec_example.json')))
    spec["audio"]=wav; spec["start"]="file://"+os.path.join(HERE,'fixtures','demo.html')
    out=record(spec,str(tmp_path/"out.mp4"))
    v=json.loads(probe(out,"v")); a=json.loads(probe(out,"a"))
    assert v["streams"][0]["width"]==1080 and v["streams"][0]["height"]==1920
    assert a["streams"] and a["streams"][0]["codec_type"]=="audio"
    from w2c.align import duration
    assert abs(float(v["format"]["duration"])-duration(wav))<0.3
