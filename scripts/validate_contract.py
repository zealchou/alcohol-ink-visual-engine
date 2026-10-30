import json, sys
STYLES={'silk-mist','mineral-vein','organic-bloom','coastal-flow','mountain-haze','vivid-current','quiet-space','nocturne-metal'}
def validate(d):
    errors=[]
    for k in ('version','task_id','mode','goal','audience','canvas','brand','style','visual_lock','regions','preserve','skills','pages','output','authorization','qa'):
        if k not in d: errors.append('missing '+k)
    c=d.get('canvas',{}); s=d.get('style',{})
    for k in ('width','height','pages'):
        if type(c.get(k)) is not int or c[k]<=0: errors.append('invalid canvas.'+k)
    if d.get('mode') not in ('design-only','generate','edit','batch','adapt'): errors.append('invalid mode')
    if s.get('primary') not in STYLES: errors.append('invalid primary')
    if s.get('secondary') is not None and s['secondary'] not in STYLES: errors.append('invalid secondary')
    if s.get('role') not in ('background','accent','subject','none'): errors.append('invalid role')
    for k in ('ink_strength','texture_density','metallic_ratio','negative_space'):
        v=s.get(k)
        if type(v) not in (int,float) or not 0<=v<=1: errors.append('invalid style.'+k)
    for k,b in d.get('regions',{}).items():
        if not isinstance(b,list) or len(b)!=4 or any(type(v) not in (int,float) or not 0<=v<=1 for v in b): errors.append('invalid region '+k)
        elif b[2]<=0 or b[3]<=0 or b[0]+b[2]>1.000001 or b[1]+b[3]>1.000001: errors.append('out of bounds '+k)
    pages=d.get('pages',[])
    if not isinstance(pages,list): errors.append('pages must be list')
    elif type(c.get('pages')) is int and [p.get('index') for p in pages if isinstance(p,dict)]!=list(range(1,c['pages']+1)): errors.append('page count/order mismatch')
    a=d.get('authorization',{})
    if any(type(a.get(k)) is not bool for k in ('publish','schedule')): errors.append('authorization must be explicit booleans')
    return errors
if __name__=='__main__':
    try:
        d=json.load(open(sys.argv[1],encoding='utf-8'))
        if not isinstance(d,dict): raise ValueError('root must be object')
        e=validate(d)
        print(json.dumps({'valid':not e,'errors':e},ensure_ascii=False)); sys.exit(bool(e))
    except (OSError,ValueError,IndexError,TypeError) as e:
        print(json.dumps({'valid':False,'errors':[str(e)]}));sys.exit(1)
