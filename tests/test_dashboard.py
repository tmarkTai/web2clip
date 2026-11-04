from w2c.dashboard import build_dashboard
def test_dashboard_contains_all_clips(tmp_path):
    clips=[{"n":i,"t":f"Clip {i}","len":"~1:00","rows":[["Lời","Hiệu ứng"]],"steps":["ok","todo","todo","todo"]} for i in range(1,4)]
    out=tmp_path/"d.html"; build_dashboard(clips,str(out),title="Test",videos={})
    h=out.read_text()
    assert h.count('"n":')>=3 and "Test" in h and 'name="viewport"' in h
def test_dashboard_embeds_video(tmp_path):
    v=tmp_path/"v.mp4"; v.write_bytes(b"0000ftypmp42")
    clips=[{"n":1,"t":"A","len":"1","rows":[],"steps":["ok","ok","ok","ok"]}]
    out=tmp_path/"d.html"; build_dashboard(clips,str(out),title="T",videos={1:str(v)})
    assert "data:video/mp4;base64," in out.read_text()
