## Data Preparation using Spark

~~~
bin/spark-shell --master spark://localhost:7077 \
--conf spark.serializer=org.apache.spark.serializer.KryoSerializer \
--executor-cores=2 --num-executors=2


import org.apache.log4j.Logger
import org.apache.log4j.Level
Logger.getLogger("org.apache.spark").setLevel(Level.WARN)

import org.apache.spark.rdd.RDD
import org.apache.spark.storage.StorageLevel


val alexRDD =  sc.textFile("/work/dga/top-1m.csv", 4)

alexRDD.cache()

alexRDD.take(10).foreach(println)

1,google.com
2,youtube.com
3,facebook.com
4,baidu.com
5,yahoo.com
6,amazon.com
7,wikipedia.org
8,qq.com
9,google.co.in
10,twitter.com

alexRDD.count

res3: Long = 1000000                                                            


val alexTupleRDD = alexRDD.map{ line => 
  val host = line.split(",")(1)

  val i = host.indexOf(".")
  // val j = host.indexOf(".", i+1)
  
  val domain = host.substring(0, i)
  
  (host, domain, host.substring(i+1), domain.length)
}

alexTupleRDD.coalesce(1).map{t => (t._1 + "," + t._2 + "," + t._3 + "," + t._4)}.saveAsTextFile("/work/dga/top-1m_legit.csv")


val tlds = alexRDD.map{ line => 
  val host = line.split(",")(1)

  val i = host.indexOf(".")
  
  host.substring(i+1)
}.distinct().collect()

tlds.size

res22: Int = 2048

tlds.foreach(println)

alexRDD.map{ line => 
  val host = line.split(",")(1)

  val i = host.indexOf(".")
  
  (host.substring(i+1), 1)
}.reduceByKey(_ + _).map(item => item.swap).sortByKey(false).map(item => item.swap).take(300).foreach(println)

(com,483529)                                                                    
(net,51004)
(ru,50711)
(org,44637)
(de,22956)
(jp,13794)
(co.uk,13398)
(com.br,12087)
(ir,11573)
(it,11432)
(in,11377)
(info,10033)
(fr,9842)
(pl,9552)
(co.jp,7497)
(nl,7115)
(cn,6613)
(es,6373)
(com.au,6227)
(gr,5504)
(cz,4544)
(co,4368)
(eu,4174)
(ca,3999)
(tv,3802)
(tmall.com,3705)
(com.cn,3526)
(me,3519)
(ro,3484)
(blogspot.com,3419)
(edu,3351)
(biz,3345)
(se,3045)
(hu,3005)
(com.tw,3003)
(com.tr,2922)
(co.za,2891)
(co.kr,2704)
(tumblr.com,2670)
(com.ua,2668)
(xyz,2551)
(ch,2422)
(wordpress.com,2241)
(be,2236)
(dk,2115)
(vn,2080)
(at,2036)
(us,2016)
(io,1975)
(co.in,1952)
(sk,1948)
(no,1823)
(cc,1774)
(com.mx,1749)
(com.ar,1746)
(fi,1710)
(by,1594)
(gov.cn,1469)
(kz,1413)
(blogspot.co.id,1391)
(blogspot.in,1351)
(ua,1344)
(co.il,1249)
(cl,1245)
(pt,1214)
(livejournal.com,1189)
(org.uk,1173)
(gov,1138)
(co.id,1114)
(ie,1109)
(lt,1105)
(or.jp,1104)
(su,1072)
(bg,1061)
(xn--p1ai,987)
(club,957)
(mx,919)
(gov.in,885)
(az,810)
(co.nz,807)
(tw,803)
(com.my,787)
(pk,719)
(com.hk,711)
(edu.cn,711)
(lv,709)
(hr,683)
(ae,664)
(ne.jp,661)
(top,652)
(com.sg,637)
(pro,632)
(asia,628)
(com.pl,622)
(com.vn,615)
(rs,615)
(mobi,604)
(nic.in,602)
(tk,601)
(ac.in,599)
(myshopify.com,599)
(kr,588)
(org.br,582)
(pw,566)
(ac.jp,559)
(ws,554)
(si,554)
(com.co,519)
(ee,516)
(blogspot.com.br,513)
(ac.uk,508)
(to,484)
(gov.uk,478)
(sharepoint.com,475)
(hk,466)
(blogspot.gr,441)
(lk,431)
(co.th,410)
(com.ng,409)
(sg,403)
(com.pk,401)
(online,398)
(ma,397)
(org.cn,397)
(xxx,391)
(fm,390)
(am,383)
(blogfa.com,381)
(ge,372)
(gob.mx,367)
(uz,363)
(edu.vn,355)
(my,350)
(blogspot.com.eg,340)
(cat,337)
(id,337)
(ac.ir,333)
(pe,332)
(is,330)
(com.pe,324)
(org.au,323)
(or.kr,320)
(tech,310)
(br,300)
(com.ve,299)
(lg.jp,299)
(gov.tr,290)
(org.tw,290)
(ac.id,284)
(nu,282)
(blogspot.ru,274)
(com.ph,273)
(in.ua,273)
(rozblog.com,270)
(go.id,269)
(link,265)
(org.tr,259)
(appspot.com,257)
(web.id,257)
(website,257)
(edu.br,255)
(name,255)
(ph,254)
(go.kr,251)
(uol.com.br,249)
(altervista.org,249)
(org.ua,248)
(blog.ir,248)
(mn,246)
(gov.br,241)
(net.cn,240)
(kiev.ua,238)
(gov.tw,234)
(gen.tr,230)
(ng,230)
(space,228)
(blogspot.com.es,226)
(pics,223)
(site,223)
(ml,222)
(dev,219)
(edu.in,218)
(org.in,218)
(edu.au,216)
(lu,214)
(wix.com,213)
(com.sa,213)
(gov.au,210)
(edu.mx,210)
(co.ke,209)
(blogspot.com.tr,207)
(ba,207)
(weebly.com,207)
(bz,205)
(go.jp,203)
(la,203)
(edu.tw,203)
(free.fr,201)
(travel,199)
(gov.co,196)
(edu.co,196)
(in.th,196)
(spb.ru,193)
(mk,192)
(gov.my,186)
(im,183)
(md,182)
(net.au,181)
(edu.tr,180)
(16mb.com,178)
(mihanblog.com,175)
(blogspot.it,175)
(ga,171)
(news,171)
(gr.jp,167)
(jimdo.com,165)
(blogspot.mx,165)
(ac.th,164)
(tn,164)
(qc.ca,163)
(uk,160)
(com.do,157)
(cf,155)
(edu.pk,155)
(gov.ar,153)
(dz,152)
(today,151)
(com.bd,149)
(edu.pl,143)
(com.uy,140)
(gov.it,140)
(bel.tr,138)
(ly,136)
(go.th,135)
(al,134)
(narod.ru,133)
(gob.pe,133)
(gov.vn,131)
(ed.jp,129)
(click,127)
(net.br,126)
(herokuapp.com,125)
(gov.pl,125)
(gov.sa,124)
(edu.ar,123)
(kg,122)
(gc.ca,122)
(tokyo,122)
(org.za,122)
(gouv.fr,122)
(edu.my,120)
(edu.pe,120)
(jobs,119)
(gov.hk,119)
(or.id,118)
(coop,118)
(ucoz.ru,117)
(org.ar,117)
(gov.bd,116)
(com.eg,114)
(nhs.uk,113)
(org.mx,112)
(guru,112)
(li,111)
(work,110)
(org.pl,109)
(persianblog.ir,109)
(typepad.com,108)
(org.il,108)
(net.ua,108)
(ning.com,108)
(net.in,106)
(com.cy,106)
(com.ru,105)
(gov.sg,105)
(ac.kr,105)
(azurewebsites.net,103)
(jus.br,103)
(com.es,103)
(gov.pk,103)
(on.ca,101)
(aero,100)
(ac.cn,100)
(squarespace.com,99)
(com.py,99)
(org.hk,99)
(com.ec,99)
(gov.ua,98)
(net.pl,98)
(blogsky.com,96)
(edu.hk,95)
(gob.ve,94)
(blog.br,92)
(blog.163.com,92)
(cm,90)
(st,89)
(sa,88)
(gob.ar,88)
(so,86)
(gov.ph,85)

# removing xn--p1ai, jus.br
~~~

~~~
more tld.txt

com
net
ru
org
de
jp
co.uk
com.br
ir
it
in
info
fr
pl
co.jp
nl
cn
es
com.au
gr
cz
co
eu
ca
tv
com.cn
me
ro
edu
biz
se
hu
com.tw
com.tr
co.za
co.kr
com.ua
xyz
ch
be
dk
vn
at
us
io
co.in
sk
no
cc
com.mx
com.ar
fi
by
gov.cn
kz
ua
co.il
cl
pt
org.uk
gov
co.id
ie
lt
or.jp
su
bg
club
mx
gov.in
az
co.nz
tw
com.my
pk
com.hk
edu.cn
lv
hr
ae
ne.jp
top
com.sg
pro
asia
com.pl
com.vn
rs
mobi
nic.in
tk
ac.in
kr
org.br
pw
ac.jp
ws
si
com.co
ee
ac.uk
to
gov.uk
hk
lk
co.th
com.ng
sg
com.pk
online
ma
org.cn
xxx
fm
am
ge
gob.mx
uz
edu.vn
my
cat
id
ac.ir
pe
is
com.pe
org.au
or.kr
tech
br
com.ve
lg.jp
gov.tr
org.tw
ac.id
nu
com.ph
in.ua
go.id
link
org.tr
web.id
website
edu.br
name
ph
go.kr
org.ua
mn
gov.br
net.cn
gov.tw
ng
space
pics
site
ml
dev
edu.in
org.in
edu.au
lu
com.sa
gov.au
edu.mx
co.ke
ba
bz
go.jp
la
edu.tw
free.fr
travel
gov.co
edu.co
in.th
spb.ru
mk
gov.my
im
md
net.au
edu.tr
ga
news
gr.jp
ac.th
tn
qc.ca
uk
com.do
cf
edu.pk
gov.ar
dz
today
com.bd
edu.pl
com.uy
gov.it
bel.tr
ly
go.th
al
narod.ru
gob.pe
gov.vn
ed.jp
click
net.br
gov.pl
gov.sa
edu.ar
kg
gc.ca
tokyo
org.za
gouv.fr
edu.my
edu.pe
jobs
gov.uk
or.id
coop
ucoz.ru
org.ar
gov.bd
com.eg
nhs.uk
org.mx
guru
li
work
org.pl
org.il
net.ua
net.in
com.cy
com.ru
gov.sg
ac.kr
com.es
gov.pk
on.ca
aero
ac.cn
com.py
org.hk
com.ec
gov.ua
net.pl
edu.hk
gob.ve
cm
st
sa
gob.ar
so
gov.ph
~~~

~~~
more url_domain.txt

tmall.com
blogspot.com
tumblr.com
wordpress.com
blogspot.co.id
blogspot.in
livejournal.com
myshopify.com
blogspot.com.br
sharepoint.com
blogspot.gr
blogfa.com
blogspot.com.eg
blogspot.ru
rozblog.com
appspot.com
uol.com.br
altervista.org
blog.ir
kiev.ua
gen.tr
blogspot.com.es
wix.com
blogspot.com.tr
weebly.com
16mb.com
mihanblog.com
blogspot.it
jimdo.com
blogspot.mx
herokuapp.com
persianblog.ir
typepad.com
ning.com
azurewebsites.net
squarespace.com
blogsky.com
blog.br
blog.163.com
~~~


~~~
val tldRDD =  sc.textFile("/work/dga/tld.txt")

val tlds = tldRDD.collect()

val bcTLD = sc.broadcast(tlds)

alexTupleRDD.filter{t => bcTLD.value.contains(t._3)}.count

res35: Long = 956934

~~~
