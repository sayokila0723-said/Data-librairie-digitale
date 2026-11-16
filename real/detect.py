import cv2, numpy as np, glob, json, sys
out={}
for f in sorted(glob.glob('shots/*.png')):
    im=cv2.imread(f); g=im.astype(int)
    bg=np.array([45,45,45])
    d=np.abs(g-g[...,:1].mean()*0).max(axis=2)
    lum=im.max(axis=2)
    m=(lum>100).astype(np.uint8)
    m=cv2.morphologyEx(m,cv2.MORPH_OPEN,np.ones((3,3),np.uint8))
    m=cv2.morphologyEx(m,cv2.MORPH_CLOSE,np.ones((9,9),np.uint8))
    n,l,st,c=cv2.connectedComponentsWithStats(m)
    boxes=[]
    for i in range(1,n):
        x,y,w,h,a=st[i]
        if h>=55 and w>=30 and a>1500 and h<200 and w<260:
            boxes.append([int(x),int(y),int(w),int(h)])
    # order: rows by y (tolerance), then x
    boxes.sort(key=lambda b:(round((b[1])/60),b[0]))
    out[f]=boxes
    vis=im.copy()
    for k,(x,y,w,h) in enumerate(boxes):
        cv2.rectangle(vis,(x,y),(x+w,y+h),(0,0,255),2); cv2.putText(vis,str(k),(x+2,y+18),0,0.7,(0,255,255),2)
    cv2.imwrite(f.replace('shots/','vis_'),vis)
    print(f,len(boxes))
json.dump(out,open('boxes.json','w'))
