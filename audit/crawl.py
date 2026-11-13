import re, json, urllib.request, concurrent.futures as cf, html
from urllib.parse import urljoin, urlparse
UA={'User-Agent':'Mozilla/5.0 (audit; jamilahmed.com)'}
def get(u, method='GET'):
    req=urllib.request.Request(u, headers=UA, method=method)
    try:
        with urllib.request.urlopen(req, timeout=40) as r:
            body=r.read() if method=='GET' else b''
            return r.status, r.geturl(), body, dict(r.headers)
    except urllib.error.HTTPError as e:
        return e.code, u, e.read() if method=='GET' else b'', dict(e.headers or {})
    except Exception as e:
        return 0, u, b'', {'err':str(e)[:120]}
# sitemaps
idx=get('https://jamilahmed.com/sitemap_index.xml')[2].decode()
maps=re.findall(r'<loc>([^<]+)</loc>', idx)
urls=[]
for m in maps:
    urls+=re.findall(r'<loc>([^<]+)</loc>', get(m)[2].decode())
urls=sorted(set(u for u in urls if not re.search(r'\.(jpe?g|png|webp|gif|svg)$',u)))
print('sitemaps',maps); print('urls',len(urls))
extra=['https://jamilahmed.com/','https://jamilahmed.com/blog/','https://jamilahmed.com/author/jamilahmed/','https://jamilahmed.com/robots.txt','https://jamilahmed.com/llms.txt']
pages={}
def fetch(u):
    s,final,b,h=get(u); t=b.decode('utf-8','ignore')
    return u,{'status':s,'final':final,'bytes':len(b),'html':t,'headers':{k.lower():v for k,v in h.items()}}
with cf.ThreadPoolExecutor(8) as ex:
    for u,d in ex.map(fetch, sorted(set(urls+extra))): pages[u]=d
out={}
for u,d in pages.items():
    t=d['html']
    links=set(urljoin(u,html.unescape(x)) for x in re.findall(r'<a\s[^>]*href=["\']([^"\'#][^"\']*)',t,re.I))
    imgs=re.findall(r'<img\s[^>]*>',t,re.I)
    imgd=[]
    for tag in imgs:
        src=re.search(r'\ssrc=["\']([^"\']+)',tag); alt=re.search(r'\salt=["\']([^"\']*)',tag)
        imgd.append({'src':urljoin(u,html.unescape(src.group(1))) if src else None,'alt':alt.group(1) if alt else None,'dims':bool(re.search(r'\swidth=',tag)),'lazy':'loading="lazy"' in tag})
    out[u]={'status':d['status'],'final':d['final'],'bytes':d['bytes'],
      'title':(re.search(r'<title>([^<]*)',t) or [None,None])[1],
      'desc':(re.search(r'<meta name="description" content="([^"]*)',t) or [None,None])[1],
      'canonical':(re.search(r'<link rel="canonical" href="([^"]+)',t) or [None,None])[1],
      'robots':(re.search(r'<meta name=.robots. content="([^"]+)',t) or [None,None])[1],
      'h1':[re.sub('<[^>]+>','',x).strip() for x in re.findall(r'<h1[^>]*>(.*?)</h1>',t,re.S|re.I)],
      'h2n':len(re.findall(r'<h2',t,re.I)),
      'schema_types':re.findall(r'"@type":\s*"([A-Za-z]+)"',t),
      'jsonld':len(re.findall(r'application/ld\+json',t)),
      'scripts':len(re.findall(r'<script[^>]+src=',t,re.I)),'styles':len(re.findall(r'<link[^>]+stylesheet',t,re.I)),
      'inline_style_kb':round(sum(len(x) for x in re.findall(r'<style[^>]*>(.*?)</style>',t,re.S))/1024,1),
      'script_srcs':re.findall(r'<script[^>]+src=["\']([^"\']+)',t,re.I),
      'style_hrefs':re.findall(r'<link[^>]+stylesheet[^>]+href=["\']([^"\']+)',t,re.I)+re.findall(r'<link[^>]+href=["\']([^"\']+)[^>]+stylesheet',t,re.I),
      'links':sorted(links),'imgs':imgd,'text':t if u.endswith(('robots.txt','llms.txt')) else None,
      'cache':d['headers'].get('x-cache') or d['headers'].get('x-cacheable'),'server':d['headers'].get('server'),
      'words':len(re.sub(r'<[^>]+>',' ',re.sub(r'<(script|style)[^>]*>.*?</\1>','',t,flags=re.S)).split())}
json.dump(out,open('audit/crawl.json','w'),indent=1)
print('crawled',len(out), 'non-200:',[(u,v['status']) for u,v in out.items() if v['status']!=200])
