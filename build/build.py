import json, re, html, os, sys
sys.path.insert(0, os.path.dirname(__file__))
from activities import A
D = os.path.dirname(os.path.abspath(__file__)); OUT = os.path.dirname(D)
BASE = "https://shawnmckenzie11.github.io/VLC-Coding-Math/mth1w-coding/"   # <-- replace with where you host the activity files
T = open(os.path.join(D, "template.html")).read()
LESSONS = {1: "/home/box/agent-data/agents/1adbc78d-3be0-4576-83de-2c5adaa816cf/attachments/5421c369e72f33efec20dad7f56475250900e3f3dc715db9c7ea68290ba39a95.html",
           2: "/home/box/agent-data/agents/1adbc78d-3be0-4576-83de-2c5adaa816cf/attachments/4f87a754be286f0c45f51c74ecb7f8fb21ed5215db2f05d02935497c262a978a.html"}
os.makedirs(os.path.join(OUT, "activities"), exist_ok=True)
pages = {}
for a in A:
    p = (T.replace("__TITLE__", html.escape(a["title"])).replace("__INSTR__", a["instr"]).replace("__ID__", a["id"])
          .replace("__STARTER__", json.dumps(a["starter"]).replace("</", "<\\/")).replace("__CHECK__", a["check"]))
    pages[a["id"]] = p
    open(os.path.join(OUT, "activities", a["id"] + ".html"), "w").write(p)
def lesson(n, mode):
    s = open(LESSONS[n]).read()
    acts = [a for a in A if a["lesson"] == n]; i = iter(acts)
    def rep(m):
        a = next(i); assert m.group(1) in a["trinket"], (m.group(1), a["id"])
        h = 330 if a["id"] != "l2-practice" else 360
        if mode == "canvas":
            return '<iframe title="%s - Python editor" src="%s%s.html" width="100%%" height="%d" loading="lazy" allowfullscreen="allowfullscreen"></iframe>' % (html.escape(a["title"]), BASE, a["id"], h)
        return '<iframe title="%s" srcdoc="%s" width="100%%" height="%d" style="border:1px solid #ccc"></iframe>' % (html.escape(a["title"]), html.escape(pages[a["id"]], quote=True), h)
    s = re.sub(r'<iframe src="https://trinket\.io/embed/python/(\w+)"[^>]*></iframe>', rep, s)
    assert next(i, None) is None and "trinket.io" not in s
    s = s.replace("using a tool called Trinket", "using a built-in Python editor").replace("Use one of the Trinkets above", "Use one of the code editors above")
    return s
names = {1: "lesson-1-introduction-to-python.html", 2: "lesson-2-exploring-relationships.html"}
for n in (1, 2):
    open(os.path.join(OUT, names[n]), "w").write(lesson(n, "canvas"))
pv = '<!DOCTYPE html><html lang="en"><head><meta charset="utf-8"><title>MTH1W coding lessons - preview</title><style>body{font-family:Helvetica,Arial,sans-serif;max-width:1000px;margin:auto;padding:16px}.dp-panel-heading{background:#eef;padding:6px}hr{margin:40px 0}</style></head><body><p style="background:#ffe;padding:8px;border:1px solid #cc9"><b>Preview only.</b> Both lessons with the new Python editors inlined. In Canvas use the lesson-*.html files instead (iframes pointing to hosted activity files).</p>'
pv += lesson(1, "preview") + "<hr>" + lesson(2, "preview") + "</body></html>"
open(os.path.join(OUT, "preview-all.html"), "w").write(pv)
print("ok")
