# Builds index.html from src.html: injects walking routes and photo credits.
import json, html
src = open("src.html", encoding="utf-8").read()
routes = json.load(open("routes.json"))
slim = {k: {"m": v["m"], "line": v["line"]} for k, v in routes.items()}
cr = json.load(open("img/credits.json"))
names = ["Northeastern", "Newbury St", "Comm Ave Mall", "Washington statue", "Lagoon bridge", "Make Way for Ducklings",
         "Mount Vernon St townhouse", "Charles St", "Acorn St", "Willow St sketch", "Louisburg Square", "Nathaniel Hawthorne",
         "Louisa May Alcott", "State House", "Boston Common", "Granary Burying Ground", "Old State House", "Faneuil Hall",
         "Paul Revere House", "Paul Revere Mall", "Old North Church", "Copp's Hill", "Mike's Pastry", "Haymarket", "Orange Line",
         "Chinatown", "Chinatown Gate"]
lis, cj = [], []
for i, n in enumerate(names):
    c = cr[str(i)]
    lis.append('<li>%s — <a href="%s" target="_blank" rel="noopener">%s</a>, %s</li>' % (
        html.escape(n), html.escape(c["page"]), html.escape(c["artist"] or "Wikimedia Commons"), html.escape(c["license"])))
    cj.append({"artist": c["artist"], "license": c["license"]})
out = (src.replace("__ROUTES__", json.dumps(slim, separators=(",", ":")))
          .replace("__CREDITJSON__", json.dumps(cj, ensure_ascii=False))
          .replace("__CREDITS__", "".join(lis)))
assert "__" + "ROUTES__" not in out and "__CREDIT" not in out
open("index.html", "w", encoding="utf-8").write(out)
print("index.html", len(out), "bytes")
