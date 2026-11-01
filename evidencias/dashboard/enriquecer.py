from pathlib import Path
import pandas as pd, json, zipfile, hashlib
p=Path(__file__).parent; root=p.parent
b=pd.read_csv(root/'upload/base_preprocesada_v04.csv.gz',dtype={'Customer ID':str,'Invoice':str,'StockCode':str},parse_dates=['InvoiceDate'])
z=zipfile.ZipFile(root/'upload/Evidencias_cortes_v06(1).zip')
m=pd.concat([pd.read_csv(z.open(n),dtype={'Customer ID':str}) for n in ['validacion_v06.csv','prueba_reservada_v06.csv']])
D={n:pd.read_csv(root/'base_dashboard'/f'{n}.csv',dtype={'cliente_id':str}).to_dict('records') for n in ['cortes','modelos','metricas','escenarios','clientes']}
D['profiles']={};D['catalog']={};audit=[]
for c in D['cortes']:
 cut=c['corte'];t=pd.Timestamp(cut);h=b[(b.InvoiceDate>=t-pd.Timedelta(days=180))&(b.InvoiceDate<t)].copy();mc=m[m.fecha_corte==cut];ids=set(mc['Customer ID']);h=h[h['Customer ID'].isin(ids)]
 good=(h.concepto_limpieza=='Mercancía (definición operativa)')&(~h.Invoice.str.upper().str.startswith('C'))&(h.Quantity>0)&(h.Price>0)
 purchases=h[good]; hist=h.groupby('Customer ID').Importe_linea.sum(); assert all(abs(hist[r['Customer ID']]-r['importe_neto_180d'])<1e-6 for _,r in mc.iterrows())
 countries=h.groupby('Customer ID').Country.agg(lambda x:sorted(set(x.dropna())))
 merch=h[h.concepto_limpieza=='Mercancía (definición operativa)']; net=merch.groupby(['Customer ID','StockCode']).Importe_linea.sum()
 prod=purchases.groupby(['Customer ID','StockCode']).agg(q=('Quantity','sum'),v=('Importe_linea','sum')).reset_index()
 per={}
 for r in prod.itertuples(index=False,name=None):
  cid,code,q,v=r;per.setdefault(cid,[]).append([code,int(q),float(v),float(net.get((cid,code),0))])
 catalog=merch.sort_values('InvoiceDate',kind='stable').drop_duplicates('StockCode',keep='last').set_index('StockCode').Description.fillna('').to_dict();D['catalog'][cut]=catalog
 profiles={}
 for _,r in mc.iterrows():
  cid=r['Customer ID'];cs=countries[cid];country=cs[0] if len(cs)==1 else ('Múltiples países' if cs else 'Sin país')
  profiles[cid]={'country':country,'countries':cs,'r':r.recencia_dias,'f':int(r.frecuencia_180d),'d':int(r.diversidad_180d),'m':r.importe_neto_180d,'p':r.importe_neto_por_compra_180d,'products':per.get(cid,[])}
  assert len(profiles[cid]['products'])==int(r.diversidad_180d)
 D['profiles'][cut]=profiles;audit.append({'corte':cut,'perfiles':len(profiles),'multipais':sum(len(countries[i])>1 for i in ids),'pares_cliente_producto':len(prod),'importe_historico_cotejado':True,'diversidad_cotejada':True})
world=json.loads((p/'world.geojson').read_text());D['world']=[]
for f in world['features']:
 props=f['properties'];geo=f['geometry'];polys=geo['coordinates'] if geo['type']=='MultiPolygon' else [geo['coordinates']]
 paths=[]
 for poly in polys:
  for ring in poly:
   paths.append('M'+'L'.join(f'{(x+180)*2.5:.1f},{(90-y)*2.5:.1f}' for x,y in ring)+'Z')
 D['world'].append({'name':props.get('ADMIN'), 'path':''.join(paths)})
(p/'data.json').write_text(json.dumps(D,ensure_ascii=False,separators=(',',':')))
(p/'auditoria_enriquecimiento.json').write_text(json.dumps({'cortes':audit,'base_sha256':hashlib.sha256((root/'upload/base_preprocesada_v04.csv.gz').read_bytes()).hexdigest(),'pais':'País único en historia; múltiples países se muestran aparte. No se utiliza futuro.','productos':'Compras válidas de mercancía, cantidades e importe positivos; neto por producto separado, sin atribuir descuentos D.','mapa':'Natural Earth 1:110m, dominio público; límites generalizados, no direcciones de clientes. https://github.com/nvkelso/natural-earth-vector/blob/master/geojson/ne_110m_admin_0_countries.geojson'},ensure_ascii=False,indent=2))
print(audit)
