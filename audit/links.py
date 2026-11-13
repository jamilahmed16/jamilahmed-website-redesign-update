import json, sys, urllib.request, concurrent.futures as cf
from urllib.parse import urlparse, urlunparse
sys.path.insert(0,'tools'); import deploy
c=json.load(open('audit/crawl.json'))
linkmap={}; imgmap={}
for page,d in c.items():
    for l in d['links']:
        if l.startswith(('mailto:','tel:','javascript:')): continue
        linkmap.setdefault(l.split('#')[0],set()).add(page)
    for im in d['imgs']:
        if im['src']: imgmap.setdefault(im['src'],set()).add(page)
internal=[u for u in linkmap if urlparse(u).netloc in ('jamilahmed.com','www.jamilahmed.com')]
external=[u for u in linkmap if u not in internal]
print('unique links', len(linkmap), 'internal', len(internal), 'external', len(external), 'images', len(imgmap))
UA={'User-Agent':'Mozilla/5.0 (audit)'}
class NoRedir(urllib.request.HTTPRedirectHandler):
    def redirect_request(self,*a,**k): return None
op=urllib.request.build_opener(NoRedir)
def chk(u):
    try:
        r=op.open(urllib.request.Request(u,headers=UA,method='GET'),timeout=40); return u,r.status,r.headers.get('Content-Length'),r.headers.get('Content-Type'),None
    except urllib.error.HTTPError as e: return u,e.code,None,None,e.headers.get('Location')
    except Exception as e: return u,0,None,None,str(e)[:80]
res={}
with cf.ThreadPoolExecutor(10) as ex:
    for u,s,l,t,loc in ex.map(chk, internal+[i for i in imgmap if urlparse(i).netloc.endswith('jamilahmed.com')]): res[u]={'status':s,'len':l,'type':t,'loc':loc}
# external via server, batches of 25
ext_imgs=[i for i in imgmap if not urlparse(i).netloc.endswith('jamilahmed.com')]
allext=external+ext_imgs
for i in range(0,len(allext),25):
    batch=allext[i:i+25]
    code="$o=[];foreach("+json.dumps(batch).replace('$','\\$')+" as $u){$r=wp_remote_head($u,['timeout'=>15,'redirection'=>5,'user-agent'=>'Mozilla/5.0 (compatible; link-check)']);if(is_wp_error($r)||in_array(wp_remote_retrieve_response_code($r),[403,405,0])){$r=wp_remote_get($u,['timeout'=>15,'redirection'=>5,'limit_response_size'=>2048,'user-agent'=>'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 Chrome/124 Safari/537.36']);}$o[$u]=is_wp_error($r)?'ERR '.$r->get_error_message():wp_remote_retrieve_response_code($r);}return $o;"
    out=deploy.php(code)
    for u,s in (out or {}).items(): res[u]={'status':s}
json.dump({'links':{u:sorted(p) for u,p in linkmap.items()},'imgs':{u:sorted(p) for u,p in imgmap.items()},'res':res},open('audit/linkcheck.json','w'),indent=1)
bad={u:v for u,v in res.items() if not (isinstance(v['status'],int) and 200<=v['status']<300)}
print('problem urls', len(bad))
for u,v in sorted(bad.items()):
    where=linkmap.get(u) or imgmap.get(u) or []
    print(v['status'], v.get('loc') or '', u[:110], '| on', len(where), 'pages')
