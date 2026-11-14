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
        "update_option('ja26_head_code',$h,false);"
        "$sw=(array)get_option('auhfc_settings_sitewide');"
        "$sw['head']=preg_replace('/ja26\\.css\\?ver=\\d+/','ja26.css?ver='.$v,$sw['head']);"
        "update_option('auhfc_settings_sitewide',$sw);"
        "if(class_exists('WpeCommon')){WpeCommon::purge_varnish_cache();}"
        "return ['bytes'=>$w,'ver'=>$v,'sitewide'=>strpos($sw['head'],'ja26.css?ver='.$v)!==false];"
    )
    print("css:", php(code))


PAGES = {"home": 853, "about": 854, "consulting": 855, "newsletter": 856, "podcast": 857, "contact": 858, "header": 865, "footer": 866, "single": 232, "archive": 393, "blog": 870, "privacy": 867, "terms": 868, "disclosure": 869, "audit": 872, "enterprise": 873, "b2b": 874, "pharma": 875}


THEMER = {
    "fl-post-content": {},
    "fl-author-bio": {"image_size": "88", "bg_color": "", "text_color": ""},
    "fl-post-navigation": {"navigation_link": "both", "prev_text": "&larr; %title", "next_text": "%title &rarr;",
                           "in_same_term": "0", "tax_select": "category", "aria_label": "Posts",
                           "screen_reader_text": "Posts navigation"},
}


def themer_patch(post_id):
    """Swap rich-text placeholders (__THEMER__<slug>) for real Themer modules, which the write ability rejects."""
    code = ("$map=json_decode(base64_decode('" + base64.b64encode(json.dumps(THEMER).encode()).decode() + "'),true);$n=0;$pid=" + str(post_id) + ";"
            "foreach(['_fl_builder_data','_fl_builder_draft'] as $key){ $d=get_post_meta($pid,$key,true); if(!is_array($d)) continue;"
            " foreach($d as $id=>$node){ if($node->type==='module' && ($node->settings->type??'')==='rich-text' && preg_match('/__THEMER__([a-z-]+)/',$node->settings->text??'',$m) && isset($map[$m[1]])){"
            "  $cls=$node->settings->class; $s=new stdClass; foreach(array_merge($map[$m[1]],['type'=>$m[1],'class'=>$cls]) as $k=>$v){ $s->$k=$v; }"
            "  $d[$id]->settings=$s; $n++; } }"
            " update_post_meta($pid,$key,$d); }"
            "if(class_exists('FLBuilderModel')){FLBuilderModel::delete_all_asset_cache($pid);} return $n;")
    print("themer modules:", php(code))


def js():
    src = open(os.path.join(ROOT, "wp-content/themes/bb-theme-child/assets/js/ja26-toc.js"), "rb").read()
    b64 = base64.b64encode(src).decode()
    code = (
        "$f=get_stylesheet_directory().'/assets/js/ja26-toc.js'; wp_mkdir_p(dirname($f));"
        f"$w=file_put_contents($f,base64_decode('{b64}'));clearstatcache();$v=filemtime($f);"
        "$tag='<script src=\"'.get_stylesheet_directory_uri().'/assets/js/ja26-toc.js?ver='.$v.'\" defer></script>';"
        "$sw=(array)get_option('auhfc_settings_sitewide');"
        "$sw['footer']=trim(preg_replace('#<!-- ja26-js -->.*<!-- /ja26-js -->#s','',$sw['footer']??'')).\"\\n<!-- ja26-js -->\".$tag.'<!-- /ja26-js -->';"
        "update_option('auhfc_settings_sitewide',$sw);"
        "if(class_exists('WpeCommon')){WpeCommon::purge_varnish_cache();}"
        "return ['bytes'=>$w,'ver'=>$v];"
    )
    print("js:", php(code))


def page(script):
    name = os.path.splitext(os.path.basename(script))[0]
    env = {**os.environ, "POST_ID": str(PAGES[name])}
    nodes = subprocess.run([sys.executable, os.path.join(ROOT, script)], capture_output=True, text=True, check=True, env=env).stdout
    r = run("novamira/beaver-builder-set-layout", json.loads(nodes))
    d = r.get("data", r)
    print("layout:", d.get("node_counts", d) if isinstance(d, dict) else d)
    if "__THEMER__" in nodes:
        themer_patch(PAGES[name])


if __name__ == "__main__":
    if sys.argv[1] == "css":
        css()
    elif sys.argv[1] == "js":
        js()
    elif sys.argv[1] == "page":
        for script in sys.argv[2:]:
            print(script, end=" ")
            page(script)
