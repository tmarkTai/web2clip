"""Kiểm tra môi trường: công cụ dựng + quyền mạng tới các dịch vụ giọng đọc."""
import shutil,subprocess,importlib.util,json,sys
DOMAINS=["elevenlabs.io","api.elevenlabs.io","api.us.elevenlabs.io","elevenlabsusercontent.com","storage.googleapis.com"]
def _reach(d):
    try:
        r=subprocess.run(["curl","-s","-o","/dev/null","-w","%{http_code}","-m","8",f"https://{d}/"],capture_output=True,text=True)
        return r.stdout not in ("","000")
    except Exception: return False
def check_env(domains=None):
    tools={"ffmpeg":bool(shutil.which("ffmpeg")),"ffprobe":bool(shutil.which("ffprobe")),"playwright":importlib.util.find_spec("playwright") is not None}
    net={d:_reach(d) for d in (DOMAINS if domains is None else domains)}
    return {"tools":tools,"network":net,"ok":all(tools.values()) and all(net.values())}
if __name__=="__main__":
    r=check_env(); print(json.dumps(r,indent=2,ensure_ascii=False))
    blocked=[d for d,v in r["network"].items() if not v]
    if blocked: print("\nCần mở quyền mạng cho:", ", ".join(blocked))
    sys.exit(0 if r["ok"] else 1)
