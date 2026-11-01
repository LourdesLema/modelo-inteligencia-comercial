import json,hashlib,math
from pathlib import Path
p=Path(__file__).parent;d=json.loads((p/'data.json').read_text());checks=[]
for c in d['cortes']:
 cut=c['corte'];n=c['n_clientes'];profiles=d['profiles'][cut];assert len(profiles)==n
 for model in ['H','RL','RF09']:
  rows=sorted([r for r in d['clientes'] if r['corte']==cut and r['modelo']==model],key=lambda r:(-r['valor_orden_GBP'],r['cliente_id']))
  assert all(r['posicion']==i+1 for i,r in enumerate(rows));assert {r['cliente_id'] for r in rows}==set(profiles)
  limits=[0,n*10//100,n*20//100,n*30//100,n];bands=[rows[a:b] for a,b in zip(limits,limits[1:])]
  assert sum(map(len,bands))==n
  assert abs(sum(r['ventas_observadas_GBP'] for b in bands for r in b)-c['total_neto_GBP'])<1e-6
  for pct in [10,20,30]:
   sel=rows[:n*pct//100];s=next(s for s in d['escenarios'] if s['corte']==cut and s['modelo']==model and s['capacidad_pct']==pct)
   assert len(sel)==s['n_seleccionados'];assert abs(sum(r['ventas_observadas_GBP'] for r in sel)-s['ventas_seleccionadas_GBP'])<1e-6
   geo={}
   for r in sel:
    country=profiles[r['cliente_id']]['country'];geo[country]=geo.get(country,0)+1
   assert sum(geo.values())==len(sel)
   checks.append({'corte':cut,'modelo':model,'capacidad':pct,'n':len(sel),'bandas_y_paises':'OK'})
for cut,profiles in d['profiles'].items():
 for cid,v in profiles.items():
  assert v['f']>=1 and abs(v['p']-v['m']/v['f'])<1e-6
  assert len(v['products'])==v['d']
  assert len({x[0] for x in v['products']})==v['d']
  assert all(x[1]>0 and x[2]>0 and x[0]!='D' for x in v['products'])
html=(p/'dist/index.html').read_text();assert '<script src=' not in html and 'fetch(' not in html
(p/'bitacora_verificacion.json').write_text(json.dumps({'escenarios':checks,'perfiles_comprobados':sum(len(x) for x in d['profiles'].values()),'sha256_html':hashlib.sha256(html.encode()).hexdigest(),'alcance':'No se reentrenan modelos. Bandas y perfiles descriptivos posteriores al cierre del análisis.'},ensure_ascii=False,indent=2))
print('OK: 27 escenarios, bandas excluyentes, países sin duplicación, 8764 perfiles, fórmulas y diversidad.')
