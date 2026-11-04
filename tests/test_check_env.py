from w2c.check_env import check_env
def test_check_env_reports_core_tools():
    r=check_env(domains=[])
    for k in ["ffmpeg","ffprobe","playwright"]: assert k in r["tools"]
    assert "ok" in r
