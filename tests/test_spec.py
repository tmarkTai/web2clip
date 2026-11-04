import json, os
from w2c.spec import validate_spec
def good():
    return {"name":"c1","tag":"PHẦN 1","title":"Tổng quan","audio":"v1.mp3","paras":[{"text":"Xin chào","acts":[[0,"hl","#a"],[0.5,"untitle"]]}]}
def test_valid_spec_passes(): assert validate_spec(good())==[]
def test_unknown_action_reported():
    s=good(); s["paras"][0]["acts"].append([0.2,"fly","#x"])
    assert any("fly" in e for e in validate_spec(s))
def test_fraction_out_of_range():
    s=good(); s["paras"][0]["acts"][0][0]=1.5
    assert any("0..1" in e for e in validate_spec(s))
def test_missing_fields(): assert validate_spec({"name":"x"})
def test_example_spec_valid():
    p=os.path.join(os.path.dirname(__file__),'..','examples','spec_example.json')
    assert validate_spec(json.load(open(p)))==[]
