import cv2, numpy as np, glob, json
out={}
for f in sorted(glob.glob('shots/*.png')):
    im=cv2.imread(f).astype(int)
    isbg=(np.abs(im-51).max(axis=2)<=3)
    border=(np.abs(im-94).max(axis=2)<=3)|(np.abs(im-37).max(axis=2)<=3)
    k=(~border).astype(np.uint8)
    n,l,st,c=cv2.connectedComponentsWithStats(k,connectivity=4)
    tiles=[]
    for i in range(1,n):
        x,y,w,h,a=st[i]
        if w>150 and h>120 and w<300 and h<260: tiles.append((x,y,w,h))
    tiles.sort(key=lambda t:(round(t[1]/40),t[0]))
    res=[]
    for (x,y,w,h) in tiles:
        sub=isbg[y+3:y+h-3, x+6:x+w-6]
        nonbg=(~sub).sum(axis=1)>2
        runs=[];s=None
        for r,v in enumerate(nonbg):
            if v and s is None: s=r
            if (not v) and s is not None: runs.append((s,r));s=None
        if s is not None: runs.append((s,len(nonbg)))
        runs=[r for r in runs if r[1]-r[0]>=6]
        img=None
        if runs and runs[0][1]-runs[0][0]>=50:
            a,b=runs[0]; a+=3; b+=3; cols=(~isbg[y+a:y+b, x+6:x+w-6]).sum(axis=0)>2
            xs=np.nonzero(cols)[0]
            img=[int(x+6+xs[0]),int(y+a),int(xs[-1]-xs[0]+1),int(b-a)]
        res.append(dict(tile=[int(x),int(y),int(w),int(h)],img=img))
    out[f]=res
    vis=cv2.imread(f)
    for k_,t in enumerate(res):
        x,y,w,h=t['tile'];cv2.rectangle(vis,(x,y),(x+w,y+h),(0,255,0),1)
        if t['img']:
            a,b,c_,d=t['img'];cv2.rectangle(vis,(a,b),(a+c_,b+d),(0,0,255),2)
        cv2.putText(vis,str(k_),(x+4,y+20),0,0.7,(0,255,255),2)
    cv2.imwrite(f.replace('shots/','vis_'),vis)
    print(f,len(res),sum(1 for t in res if t['img']))
json.dump(out,open('tiles.json','w'))
