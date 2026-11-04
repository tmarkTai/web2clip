import os,re,json
ROOT=os.path.join(os.path.dirname(__file__),'..')
SK=["web2clip","web2clip-setup","web2clip-plan","web2clip-voice","web2clip-record","web2clip-merge"]
def fm(p):
    t=open(p,encoding='utf-8').read(); m=re.match(r'^---\nname: (.+)\ndescription: (.+)\n---\n',t); return m,t
def test_every_skill_has_valid_frontmatter():
    for s in SK:
        m,t=fm(os.path.join(ROOT,'skills',s,'SKILL.md'))
        assert m, s
        assert m.group(1)==s
        assert m.group(2).startswith("Use when"), s
        assert len(m.group(2))<=1024
def test_master_lists_all_subcommands():
    _,t=fm(os.path.join(ROOT,'skills','web2clip','SKILL.md'))
    for s in SK[1:]: assert "/"+s in t
def test_referenced_files_exist():
    for r in ["loi-thuong-gap.md","viet-kich-ban.md","chon-giong.md"]:
        assert os.path.exists(os.path.join(ROOT,'skills','web2clip','references',r))
def test_plugin_json_points_to_skills():
    pj=json.load(open(os.path.join(ROOT,'.claude-plugin','plugin.json')))
    for p in pj["skills"]: assert os.path.exists(os.path.join(ROOT,p,'SKILL.md'))
def test_no_private_contact_in_skill_files():
    for s in SK:
        t=open(os.path.join(ROOT,'skills',s,'SKILL.md'),encoding='utf-8').read()
        assert "0948" not in t

def test_no_private_phone_anywhere_in_code():
    import glob
    for f in glob.glob(os.path.join(ROOT,'skills','**','*.*'),recursive=True):
        if f.endswith(('.py','.md','.js','.html','.json')):
            assert "0948" not in open(f,encoding='utf-8',errors='ignore').read(), f
