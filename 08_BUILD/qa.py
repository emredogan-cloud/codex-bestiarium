import json,re,collections
B=json.load(open('build/book.json',encoding='utf-8'))
S=B['stories']
def txt(s):
    out=[]
    for c in s['content']:
        if isinstance(c,str): out.append(c)
        elif c.get('style')=='quote': out.append(c.get('text',''))
    return '\n'.join(out)
ALL={s['id']:txt(s) for s in S}
FULL='\n'.join(ALL.values())

print("=== 1. VERIFY LOGGED ISSUES ===")
checks=[
 ("Gáe Bolg attributed to Lugaid","cu-chulainn",r"Gáe Bolg"),
 ("'eight times distilled' (sekhmet)","sekhmet",r"eight times distilled"),
 ("'eight times distilled' (susanoo)","susanoo-orochi",r"eight times distilled"),
 ("Bari 'twenty-one years'","princess-bari",r"twenty-one years"),
 ("'the present queen'","bran-blessed",r"present queen"),
 ("'Soften your iron'","prometheus",r"Soften your iron"),
 ("Kalpavriksha missing verb","ocean-of-milk",r"wishing-tree, planted itself"),
 ("Tandava 'on a small drum'","shiva-tandava",r"performs it on a small drum"),
 ("Morrigan 'curse would have healed'","morrigan",r"curse would have healed"),
 ("Simurgh: Sohrab 2nd feather","simurgh",r"matter of Rostam's son Sohrab"),
 ("snake in horse's 'shoe'","jade-emperor",r"shoe of the horse"),
]
for label,sid,pat in checks:
    hit=re.search(pat,ALL.get(sid,''))
    print(f"  [{'CONFIRMED' if hit else 'not found'}] {label}")

print("\n=== 2. Naglfar contradiction ===")
for sid in ('ragnarok','hel'):
    for m in re.finditer(r'[^.]*Naglfar[^.]*\.',ALL[sid]):
        print(f"  [{sid}] {m.group().strip()[:170]}")

print("\n=== 3. Kailasa/Kailash spelling ===")
for sp in ('Kailasa','Kailash'):
    ids=[k for k,v in ALL.items() if sp in v]
    print(f"  {sp}: {ids}")

print("\n=== 4. Cross-story duplicate sentences (>=9 words) ===")
sents=collections.defaultdict(set)
for sid,t in ALL.items():
    for s in re.split(r'(?<=[.!?])\s+',t):
        w=s.strip().lower()
        if len(w.split())>=9: sents[re.sub(r'[^a-z ]','',w)].add(sid)
dupes=[(s,ids) for s,ids in sents.items() if len(ids)>1]
print(f"  exact cross-story duplicate sentences: {len(dupes)}")
for s,ids in dupes[:6]: print(f"    {sorted(ids)}: {s[:110]}")
# near-duplicate phrase
key="monkeys you can still see in the high jungle"
print(f"  '{key}' → {[k for k,v in ALL.items() if key in v]}")

print("\n=== 5. Typography / encoding hygiene ===")
print(f"  straight double-quote \" in prose : {FULL.count(chr(34))}")
print(f"  straight apostrophe ' in prose    : {FULL.count(chr(39))}")
print(f"  curly quotes “ ”                  : {FULL.count(chr(8220))} / {FULL.count(chr(8221))}")
print(f"  em dash —                         : {FULL.count(chr(8212))}")
print(f"  double spaces                     : {len(re.findall(r'  +',FULL))}")
print(f"  space before punctuation          : {len(re.findall(r' [,.;:!?]',FULL))}")
print(f"  non-ASCII chars                   : {len(set(c for c in FULL if ord(c)>127))} distinct")

print("\n=== 6. Structural integrity ===")
bad=[s['id'] for s in S if not s['content'] or not isinstance(s['content'][0],str)]
print(f"  stories not opening with a prose paragraph: {bad or 'none'}")
noq=[s['id'] for s in S if not any(isinstance(c,dict) and c.get('style')=='quote' for c in s['content'])]
print(f"  stories WITHOUT a pull-quote: {noq or 'none'}")
ids=[s['id'] for s in S]; print(f"  duplicate ids: {[k for k,v in collections.Counter(ids).items() if v>1] or 'none'}")
titles=[s['title'] for s in S]; print(f"  duplicate titles: {[k for k,v in collections.Counter(titles).items() if v>1] or 'none'}")
print(f"  stories missing subtitle: {[s['id'] for s in S if not s.get('subtitle')] or 'none'}")
print(f"  stories missing themes:   {[s['id'] for s in S if not s.get('themes')] or 'none'}")
wc=[(s['id'],len(txt(s).split())) for s in S]
wc.sort(key=lambda x:x[1])
print(f"  shortest 3: {wc[:3]}")
print(f"  longest  3: {wc[-3:]}")
