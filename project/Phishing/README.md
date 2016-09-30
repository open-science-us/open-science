## Phishing Email Detection

### Data Set

(1) Phishing Email Dataset: J. Nazario, “Phishingcorpus homepage,” 2006, http://monkey.org/%7Ejose/wiki/doku.php?id=PhishingCorpus
~~~
// download mbox files to /work/phishing/jose from http://monkey.org/%7Ejose/wiki/doku.php?id=PhishingCorpus

// download mb2md-3.20.pl to /work/phishing from http://batleth.sapienti-sat.org/projects/mb2md/

cd /work/phishing

chmod +x mb2md-3.20.pl

./mb2md-3.20.pl -s /work/phishing/jose/phishing0.mbox -d /work/phishing/jose/phishing0

~~~
(2) Good or Ham Email Dataset: Apache SpamAssassin, https://spamassassin.apache.org/publiccorpus/(3) TREC 2005 Email Dataset: http://plg.uwaterloo.ca/cgi-bin/cgiwrap/gvcormac/foo

### Reference

