"""Kiểm tra file kịch bản dựng (spec) trước khi quay."""
ACTIONS={"untitle":0,"end":3,"go":1,"load":1,"hl":1,"hlt":1,"off":0,"click":1,"cur":1,"flash":1,"set":2,"sel":2,"js":1,"slide":2}
def validate_spec(s):
    err=[]
    for k in ["name","tag","title","audio","paras"]:
        if k not in s: err.append(f"thiếu trường '{k}'")
    for i,p in enumerate(s.get("paras",[])):
        if not p.get("text"): err.append(f"đoạn {i}: thiếu 'text'")
        for a in p.get("acts",[]):
            if not isinstance(a,list) or len(a)<2: err.append(f"đoạn {i}: hành động sai dạng {a}"); continue
            f,name=a[0],a[1]
            if not isinstance(f,(int,float)) or not 0<=f<=1: err.append(f"đoạn {i}: mốc {f} phải trong 0..1")
            if name not in ACTIONS: err.append(f"đoạn {i}: hành động lạ '{name}'"); continue
            if len(a)-2<ACTIONS[name]: err.append(f"đoạn {i}: '{name}' thiếu tham số")
    return err
