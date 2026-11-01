from pathlib import Path
import zipfile,io,json,hashlib
import pandas as pd
import numpy as np
root=Path(__file__).resolve().parent.parent;out=root/'cierre_resultados'
inputs={}
def read(f,n):
 p=root/'upload'/f;inputs[f]=hashlib.sha256(p.read_bytes()).hexdigest()
 with zipfile.ZipFile(p) as z:return pd.read_csv(io.BytesIO(z.read(n)),dtype={'Customer ID':str})
rf=read('Evidencias_RF_validacion_v01.zip','predicciones_RF_seleccionada.csv')
assert set(rf.configuracion)=={'RF09'}
rows=[];details=[]
for mes,n in [('marzo',3338),('junio',2658)]:
 d=read(f'Evidencias_RL_H_{mes}_v01.zip',f'predicciones_{mes}.csv')
 d=d.merge(rf,on=['Customer ID','fecha_corte'],validate='one_to_one',suffixes=('','_rf'))
 assert len(d)==n and np.allclose(d.objetivo_neto_90d,d.objetivo_neto_90d_rf,rtol=0,atol=1e-10)
 total=d.objetivo_neto_90d.sum()
 for pct in [10,20,30]:
  k=n*pct//100
  base=d.sort_values(['referencia_neto_90d','Customer ID'],ascending=[False,True]).head(k).objetivo_neto_90d.sum()
  for name,col in [('H','referencia_neto_90d'),('RL','prediccion_RL'),('RF09','prediccion_RF')]:
   g=d.sort_values([col,'Customer ID'],ascending=[False,True],kind='mergesort').head(k).copy()
   assert len(g)==k and g['Customer ID'].nunique()==k
   s=g.objetivo_neto_90d.sum()
   rows.append(dict(corte=d.fecha_corte.iloc[0],modelo=name,capacidad_pct=pct,n=k,total_cohorte_GBP=total,ventas_grupo_GBP=s,diferencia_H_GBP=s-base,concentracion_pct=100*s/total if total>0 else None))
   g['criterio']=name;g['capacidad_pct']=pct;g['posicion']=range(1,k+1);details.append(g)
r=pd.DataFrame(rows);r.to_csv(out/'priorizacion_validacion.csv',index=False)
pd.concat(details).to_csv(out/'selecciones_validacion.csv',index=False)
(out/'bitacora.json').write_text(json.dumps(dict(entradas_sha256=inputs,alcance='Evaluación comercial descriptiva posterior a prueba final, con predicciones de validación guardadas. No se reentrenó ni se modificó la selección RF09.',reglas='floor(p*n); orden descendente sin redondear; desempate Customer ID textual ascendente',comparaciones=18),indent=2,ensure_ascii=False))
print(r.to_string(index=False))
