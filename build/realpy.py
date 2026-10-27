import json, re, sys, io, contextlib
from activities import A
res = {}
for a in A:
    for kind in ("starter", "solution", "wrong"):
        src = a.get(kind)
        if not src: continue
        py3 = re.sub(r'^(\s*)print (.*)$', r'\1print(\2)', src, flags=re.M)
        g = {}; buf = io.StringIO()
        with contextlib.redirect_stdout(buf): exec(py3, g)
        v = {k: x for k, x in g.items() if not k.startswith("__") and isinstance(x, (int, float, str)) and not isinstance(x, bool)}
        res[a["id"] + "|" + kind] = {"out": buf.getvalue(), "v": v, "code": src}
json.dump(res, open("realpy.json", "w"))
