#!/usr/bin/env python3
"""
Deploy helper for the jamilahmed.com redesign, via the Novamira CLI.

  tools/deploy.py css                     upload ja26.css and bump its version on every _ja26 page
  tools/deploy.py page tools/pages/x.py   build a page spec and write its Beaver Builder layout
"""
import base64, json, os, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "jamilahmed.com"
ENV = {**os.environ, "NODE_USE_ENV_PROXY": "1", "NODE_NO_WARNINGS": "1"}


def run(ability, data):
    with tempfile.NamedTemporaryFile("w", suffix=".json", delete=False) as f:
        json.dump(data, f)
    out = subprocess.run(["novamira", "--site", SITE, "run", ability, "--input", "@" + f.name, "--json", "--yes"],
                         capture_output=True, text=True, env=ENV).stdout
    os.unlink(f.name)
    return json.loads(out)


def php(code):
    r = run("novamira/execute-php", {"code": code})
    d = r.get("data", r)
    if isinstance(d, dict) and d.get("errors"):
        print("php errors:", d["errors"][:3])
    return d.get("return_value", d) if isinstance(d, dict) else d


def css():
    src = open(os.path.join(ROOT, "wp-content/themes/bb-theme-child/assets/css/ja26.css"), "rb").read()
    b64 = base64.b64encode(src).decode()
    code = (
        "$f=get_stylesheet_directory().'/assets/css/ja26.css';"
        f"$w=file_put_contents($f,base64_decode('{b64}'));clearstatcache();$v=filemtime($f);"
        "$h=preg_replace('/ja26\\.css\\?ver=\\d+/','ja26.css?ver='.$v,get_option('ja26_head_code'));"
        "update_option('ja26_head_code',$h,false);$n=0;"
        "foreach(get_posts(['post_type'=>'page','post_status'=>'any','numberposts'=>-1,'meta_key'=>'_ja26']) as $p){"
        "$m=get_post_meta($p->ID,'_auhfc',true);if(!is_array($m)){$m=['behavior'=>'append','body'=>'','footer'=>''];}"
        "$m['head']=$h;update_post_meta($p->ID,'_auhfc',wp_slash($m));$n++;}"
        "return ['bytes'=>$w,'ver'=>$v,'pages'=>$n];"
    )
    print("css:", php(code))


PAGES = {"home": 853, "about": 854, "consulting": 855, "newsletter": 856, "podcast": 857, "contact": 858, "header": 865, "footer": 866}


def page(script):
    name = os.path.splitext(os.path.basename(script))[0]
    env = {**os.environ, "POST_ID": str(PAGES[name])}
    nodes = subprocess.run([sys.executable, os.path.join(ROOT, script)], capture_output=True, text=True, check=True, env=env).stdout
    r = run("novamira/beaver-builder-set-layout", json.loads(nodes))
    d = r.get("data", r)
    print("layout:", d.get("node_counts", d) if isinstance(d, dict) else d)


if __name__ == "__main__":
    if sys.argv[1] == "css":
        css()
    elif sys.argv[1] == "page":
        for script in sys.argv[2:]:
            print(script, end=" ")
            page(script)
