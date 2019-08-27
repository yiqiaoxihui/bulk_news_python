  155  ls
  156  python usnews_national_news.py 1 10
  157  mkdir download
  158  python usnews_national_news.py 1 10
  159  python usnews_national_news.py ew 10
  160  python usnews_national_news.py 1 10
  161  cd ..
  162  ls
  163  ls bulk_news/download/
  164  python usnews_national_news.py 1 10
  165  python bulk_news_python/usnews_national_news.py 1 10
  166  python bulk_news_python/usnews_national_news.py 0 10
  167  screen -r  django 
  168  cd /home/ly/
  169  cd bulk_news_django/
  170  cd ..
  171  cd bulk_news_python/
  172  ls
  173  rm download/*
  174  python wsj_opinion.py 1 1|tee 1
  175  vim download/wsj_opinion_commentary-u-s_page_1_to_1_1555668499.txt 
  176  mv download/wsj_opinion_commentary-u-s_page_1_to_1_1555668499.txt 1
  177  ls
  178  python wsj_opinion.py 1 1
  179  python wsj_opinion.py 1 1|tee 1.r
  180  rm download/*
  181  python wsj_opinion.py 1 1|tee 1.r
  182  vim 1
  183  python wsj_opinion.py 1 1|tee 1.r
  184  vim 1
  185  python wsj_opinion.py 1 1|tee 1.r
  186  rz
  187  ls
  188  python wsj_opinion.py 1 1|tee 1.r
  189  vim 1.r 
  190  python wsj_opinion.py 1 1|tee 1.r
  191  vim 1.r 
  192  python wsj_opinion.py 1 1|tee 1.r
  193  vim 1.r 
  194  python wsj_opinion.py 1 1|tee 1.r
  195  vim riyu
  196  python wsj_opinion.py 1 1|tee 1.r
  197  python3 wsj_opinion.py 1 1|tee 1.r
  198  apt install pip3
  199  python3 install bs4
  200  ll bs4
  201  python3: can't open file 'install': [Errno 2] No such file or
  202  ll bs4
  203  python3: can't open file 'install': [Errno 2] No such file or
  204  python3 -m pip install --upgrade pip
  205  ls -l which python
  206  ls -l 'which python'
  207  ls -l 'which python3'
  208  which python
  209  which python3
  210  pip show pop
  211  pip show pip
  212  pip3
  213  python wsj_opinion.py 1 1|tee 1.r
  214  python3 -v
  215  python3 -V
  216  python wsj_opinion.py 1 1
  217  python wsj_opinion.py 1 20
  218  python
  219  python wsj_opinion.py 1 20
  220  python wsj_opinion.py 1 1
  221  python
  222  python wsj_opinion.py 1 1
  223  ls
  224  rm q*
  225  rm 1
  226  rm 1.html 
  227  rm 1.r 
  228  ls
  229  rm term.html\?isAdvanced\=true\&articleType\=Review%20%26%20Outlook%20U.S.\&daysback\=4y\&min-date\=2015%2F04%2F19\&max-date\=2019%2F04%2F19\&source\=wsjarticle\,wsjblogs\,wsjvideo\,sitesearch\&page\=3 
  230  ls
  231  git status 
  232  git add usnews_national_news.py 
  233  git add wsj_opinion.py 
  234  git push origin master 
  235  git commmit -m "compelete wsj use lxml or htmllib"
  236  git commit -m "compelete wsj use lxml or htmllib"
  237  git push origin master 
  238  python
  239  vim 1
  240  cd /home/ly/bulk_news_python/
  241  ls
  242  screen -r django 
  243  cd ../bulk_news
  244  vim visit.log 
  245  date
  246  python
  247  python wsj_opinion.py 1 1
  248  python wsj_opinion.py 1ds d
  249  cp usnews_national_news.py washingtonpost_opinion.py
  250  chmod washingtonpost_opinion.py a+w
  251  chmod a+w  washingtonpost_opinion.py
  252  wget https://www.washingtonpost.com/pb/api/v2/render/feature?id=fRRAZV1tyeKUar&contentConfig=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D&uri=/pb/opinions/the-posts-view/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService
  253  ls
  254  vim feature\?id\=fRRAZV1tyeKUar 
  255  rm feature\?id\=fRRAZV1tyeKUar 
  256  wget 'https://www.washingtonpost.com/pb/api/v2/render/feature?id=fRRAZV1tyeKUar&contentConfig=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D&uri=/pb/opinions/the-posts-view/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
  257  vim feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer 
  258  ls
  259  mv feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer  1
  260  vim 1
  261  ls
  262  wget 'https://www.washingtonpost.com/pb/api/v2/render/feature?id=fRRAZV1tyeKUar&contentConfig=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D&uri=/pb/opinions/the-posts-view/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
  263  vim feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer 
  264  mv feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer 2
  265  sz 2
  266  ls
  267  wget -c 'https://www.washingtonpost.com/pb/api/v2/render/feature?id=fRRAZV1tyeKUar&contentConfig=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D&uri=/pb/opinions/the-posts-view/&service=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterService'
  268  ls
  269  vim feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer 
  270  ls
  271  python washingtonpost_opinion.py 1 1
  272  ls
  273  python washingtonpost_opinion.py 1 1
  274  python washingtonpost_opinion.py 1 10
  275  python washingtonpost_opinion.py 1 4
  276  python washingtonpost_opinion.py 1 1
  277  cd ..
  278  cd bulk_news
  279  git add .
  280  git commit -m "wash"
  281  ls
  282  cd ..
  283  cp bulk_news/bulk_news/ bulk_news_django/
  284  cp bulk_news/bulk_news/* bulk_news_django/bulk_news/
  285  cd bulk_news_django/
  286  ls
  287  ls  bulk_news/
  288  git status
  289  git add .
  290  git commit -m "wash"
  291  git add .
  292  git status
  293  ls
  294  cd ..
  295  cd bulk_news
  296  ls
  297  git status
  298  git push origin master
  299  cd ../bulk_news_django/
  300  git status
  301  vim bulk_news/view.py
  302  git status
  303  git -m commit "asfd"
  304  git commit "asfd"
  305  git commit -m "asfd"
  306  git push
  307  git push origin master
  308  cd ../
  309  ls
  310  cd bulk_news_python/
  311  git add .
  312  git commit -m "wash"
  313  rm download/*
  314  git add .
  315  git commit -m "wash"
  316  ls
  317  rm feature\?id\=fRRAZV1tyeKUar\&contentConfig\=%7B%22path%22%3A%22%2Fopinions%2Fthe-posts-view%2F%3Flimit%3D15%26offset%3D15%22%7D\&uri\=%2Fpb%2Fopinions%2Fthe-posts-view%2F\&service\=com.washingtonpost.webapps.pagebuilder.services.StoryAdapterSer 
  318  git add .
  319  git commit -m "wash"
  320  git commit -m "washasd"
  321  git push origin master 
  322  ls
  323  screen -r django 
  324  cd /home/ly/
  325  cd bulk_news
  326  git status
  327  cp bulk_news/* ../bulk_news_django/bulk_news/
  328  cp templates/* ../bulk_news_django/templates/
  329  ls
  330  cp bulk_news/* ../bulk_news_django/bulk_news/
  331  cp templates/* ../bulk_news_django/templates/
  332  cd ../bulk_news_django/
  333  git status
  334  git add .
  335  git commit -m "all"
  336  git add .
  337  git commit -m "all"
  338  git push origin master 
  339  ls
  340  screen -r  django 
  341  cd /home/ly/
  342  date
  343  nslookup www.nytimes.com
  344  whois www.nytimes.com
  345  apt install whois
  346  whois www.nytimes.com
  347  nslookup www.nytimes.com
  348  nslookup www.nytimes.com -a
  349  nslookup 151.101.109.164
  350  wget https://www.theguardian.com/commentisfree?page=3
  351  vim commentisfree\?page\=3 
  352  cd bulk_news_python/
  353  ls
  354  vim guardian.py
  355  python guardian.py 1 1
  356  chmod a+w guardian.py 
  357  python guardian.py 1 1
  358  python guardian.py 1 10
  359  ls
  360  rm download/*
  361  ls
  362  wget https://www.ft.com/opinion?format=&page=2
  363  vim opinion\?format\= 
  364  q
  365  vim ft.py
  366  python ft.py 1 1
  367  vim ft.py 
  368  python ft.py 1 1
  369  chmod a+w ft.py 
  370  python ft.py 1 1
  371  python ft.py 2 2
  372  wget  https://www.ft.com/opinion?format=&page=2
  373  vim opinion\?format\=.1 
  374  python ft.py 2 2
  375  git add .
  376  git commit -m "asdf"
  377  rm download/*
  378  git commit -m "asdf"
  379  git add .
  380  git commit -m "asdf"
  381  git push origin master 
  382  ls
  383  rm opinion\?format\=
  384  ls
  385  vim csmonitor.py
  386  python csmonitor.py 1 1
  387  chmod  a+w csmonitor.py 
  388  python csmonitor.py 1 1
  389  wget https://www.csmonitor.com/Commentary/the-monitors-view/(offset)/20/(view)/all
  390  wget 'https://www.csmonitor.com/Commentary/the-monitors-view/(offset)/20/(view)/all'
  391  vim all 
  392  wget 'https://www.csmonitor.com/Commentary/the-monitors-view/(offset)/20/(view)/all'
  393  python csmonitor.py 1 1
  394  python csmonitor.py 2 2
  395  python csmonitor.py 1 1
  396  wget https://www.nature.com/opinion?page=1
  397  vim opinion\?page\=1 
  398  wget https://www.nature.com/opinion?page=1
  399  vim nature.py
  400  chmod a+w nature.py 
  401  python nature.py 1 1
  402  python nature.py 2 2
  403  python nature.py 1 1
  404  python nature.py 2 2
  405  python nature.py 1 1
  406  python nature.py 2 2
  407  cp nature.py newscientist.py
  408  chmod a+w newscientist.py 
  409  python newscientist.py 1 1
  410  python newscientist.py 2 2
  411  git add .
  412  ls
  413  rm opinion\?page\=1*
  414  rm download/*
  415  git add .
  416  git commit -m "all"
  417  rm opinion\?format\=.1 
  418  git add .
  419  git commit -m "all"
  420  git commit -m "alla"
  421  git push origin master 
  422  cd ..
  423  cd bulk_news_python/
  424  nmap --script fastrace.lua  --script-args="verbose=1,ip=54.239.45.187/24"  -e eth0 -d
  425  nmap --script fastrace.lua  --script-args="verbose=1,ip=54.239.45.187/25"  -e eth0 -d
  426  nmap --script fastrace.lua  --script-args="verbose=1,ip=188,166.144.143/24"  -e eth0 -d
  427  nmap --script fastrace.lua  --script-args="verbose=1,ip=188.166.144.143/24"  -e eth0 -d
  428  traceroute 188.166.144.1 -n
  429  nmap --script fastrace.lua  --script-args="verbose=1,ip=188.166.144.143/24"  -e eth0 -d
  430  rz 
  431  sz
  432  rz
  433  rm 3.live 
  434  rz
  435  ls
  436  ls /
  437  rz
  438  scp root@188.166.144.143:/home/ly/lasthop/3.live ./
  439  ls 
  440  nmap -sn -n --script last_hop/combine.lua --min-hostgroup 29 -iL 3.live -e eth0 |tee 3.live.combine
  441  screen -S lasthop
  442  screen -r lasthop 
  443  top
  444  cd /home/ly/
  445  ls
  446  ls --block-size=m -l
  447  python last_hop/extract_combine.py 3.live.combine 
  448  cd last_hop/
  449  git pull origin master 
  450  cd ..
  451  python last_hop/extract_combine.py 3.live.combine 
  452  sz 3.live.combine
  453  cd last_hop/
  454  ls
  455  git status 
  456  cd ../
  457  cd /home/ly/shadow/
  458  ls
  459  vim readme.txt 
  460  vim /etc/shadowsocks-r/config.json 
  461  screen -r lasthop 
  462  cd /home/ly/
  463  cd bulk_news_python/
  464  ls
  465  python guardian.py 1 100
  466  python guardian.py 1 100 > theguardian_lifeandstyle.txt
  467  python guardian.py 1 100 |tee theguardian_lifeandstyle.txt
  468  python guardian.py 1 500 |tee theguardian_lifeandstyle.txt
  469  sz theguardian_lifeandstyle.txt
  470  python guardian.py 501 550 |tee theguardian_lifeandstyle_501_550.txt
  471  sz  theguardian_lifeandstyle_501_550.txt
  472  vim history.py
  473  python history.py 
  474  vim history.py 
  475  chmod a+w history.py 
  476  vim history.py 
  477  python history.py 
  478  python history.py  1 2
  479  grep -rn "xml"
  480  grep -rn "xml" ./
  481  ls
  482  more 
  483  more 1
  484  rm 1
  485  ls
  486  more 2
  487  rm 2
  488  ls
  489  more all
  490  rm all
  491  ls
  492  rm all.1 
  493  rm theguardian_lifeandstyle.txt 
  494  rm theguardian_lifeandstyle_501_550.txt 
  495  grep -rn "xml" ./
  496  python history.py  1 2
  497  python history.py  1 2 >1
  498  python history.py  1 2 
  499  python history.py  1 2 |tee 1
  500  vim 1
  501  python history.py  1 2 |tee 1
  502  vim 1
  503  python history.py  1 2 
  504  python history.py  1 1
  505  python history.py  1 1 >1
  506  sz 1
  507  python history.py  1 1
  508  sz 1
  509  python history.py  1 1
  510  python history.py  1 2
  511  python history.py  2 2
  512  python history.py  1 3
  513  python history.py  2 2
  514  python history.py 1 200 |tee history_page_1_to_100.txt
  515  ls
  516  ls download/
  517  rm download/*
  518  ls
  519  cd ..
  520  cd bulk_news
  521  ls d
  522  ls download/
  523  screen -r django 
  524  git status 
  525  ls
  526  ls download/
  527  cd ..
  528  cp bulk_news/* bulk_news_django/
  529  cp bulk_news/* bulk_news_django/ -R
  530  cd bulk_news_django/
  531  ls
  532  git status 
  533  git add .
  534  git commit -m "add history"
  535  ls
  536  git add remote https://github.com/yiqiaoxihui/bulk_news_django.git
  537  git remote add  https://github.com/yiqiaoxihui/bulk_news_django.git
  538  git status
  539  ls
  540  git push orign master
  541  git remote add origin  https://github.com/yiqiaoxihui/bulk_news_django.git
  542  git push origin master
  543  cd ..
  544  cd bulk_news_python/
  545  git status 
  546  git add *>py
  547  git add *.py
  548  git status 
  549  rm 1
  550  rm history_page_1_to_100.txt 
  551  git add .
  552  git status 
  553  vim py 
  554  git add .
  555  git commit -m "add history"
  556  git push origin master 
  557  ls download/
  558  python history.py 1 300 |tee history_page_1_to_300.txt
  559  sz  history_page_1_to_500.txt
  560  python history.py 1 500 |tee history_page_1_to_500.txt
  561  ls download/
  562  vim download/history_page_1_to_300_1558348976.txt 
  563  vim download/history_page_1_to_500_1558349453.txt 
  564  sz download/history_page_1_to_500_1558349453.txt 
  565  python history.py 1 500 |tee history_page_1_to_500.txt
  566  sz  history_page_1_to_500.txt
  567  python history.py 1 500 
  568  python manage.py runserver 0.0.0.0:8000
  569  screen -r lasthop 
  570  cd /home/ly/
  571  screen -r django
  572  cd /home/ly/bulk_news_python/
  573  screen -r django 
  574  python guardian.py 1 600 science
  575  sz download/
  576  sz download/theguardian_page_science_1_to_600_1558420862.txt 
  577  cd bulk_news_python/
  578  ls
  579  rm history_page_1_to_*
  580  rm download/*
  581  python guardian.py help
  582  python guardian.py 1 300 environment
  583  python guardian.py 1 1000 environment
  584  ls download/
  585  sz download/theguardian_page_environment_1_to_1000_1558419800.txt 
  586  python guardian.py 1 1000 business
  587  sz download/theguardian_page_business_1_to_1000_1558420777.txt 
  588  screen -r django 
  589  cd /home/ly/bulk_news
  590  ls
  591  tree
  592  ls -l
  593  vim visit.log 
  594  ls
  595  ls manage.py 
  596  cd bulk_news/
  597  ls
  598  vim settings.py
  599  cd ..
  600  cd bulk_news_python/
  601  python guardian.py 1 600 tech
  602  python guardian.py 1 600 technology
  603  sz download/theguardian_page_technology_1_to_600_1558420844.txt 
  604  cd /home/ly/bulk_news_python/
  605  ls
  606  cp usnews_national_news.py bigthink.py
  607  ls
  608  cp wsj_opinion.py ted.py
  609  python ted.py 1 2
  610  vim ted.py 
  611  chmod a+w ted.py 
  612  python ted.py 1 2
  613  rm download/*
  614  python ted.py 1 20
  615  ls download/
  616  rm download/wsj_opinion_0-6m_page_1_to_20_1558589483.txt 
  617  python ted.py 1 26
  618  sz download/ted_0-6m_page_1_to_20_1558589494.txt 
  619  sz download/ted_6-12m_page_1_to_26_1558589624.txt 
  620  nmap --script fastrace.lua  --script-args="verbose=1,ip=36.56.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eno2 -d|tee fi36.56.0.0_13.verbose.min24
  621  nmap --script fastrace.lua  --script-args="verbose=1,ip=36.56.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eth- -d|tee fi36.56.0.0_13.verbose.min24
  622  nmap --script fastrace.lua  --script-args="verbose=1,ip=36.56.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eth0 -d|tee fi36.56.0.0_13.verbose.min24
  623  ifconfig
  624  nmap --script fastrace.lua  --script-args="verbose=1,ip=36.56.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eth0 -d|tee fi36.56.0.0_13.verbose.min24
  625  nmap --script fastrace.lua  --script-args="verbose=1,ip=54.180.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eth0 -d|tee fi36.56.0.0_13.verbose.min24
  626  ping 54.176.0.1
  627  nmap --script fastrace.lua  --script-args="verbose=1,ip=188.166.144.143/32,output_type=file,output_filename=fi36.56.0.0_13.min24,improve=1,min_prefix_len=24"  -e eth0 -d|tee fi36.56.0.0_13.verbose.min24
  628  ping 188.166.144.143
  629  nmap --script fastrace.lua  --script-args="verbose=1,ip=188.166.144.143"  -e eth0
  630  screen -S tcpdump
  631  cd /home/ly/
  632  cd fastrace_nmap/
  633  git pull origin m
  634  git pull origin master 
  635  ls
  636  cd ..
  637  ls
  638  cd last_hop/
  639  ls
  640  git pull origin master 
  641  cd ..
  642  ls
  643  cd fastrace_nmap/
  644  ls
  645  screen -r fi
  646  screen -S fi
  647  ping 8.8.8.8
  648  screen -r tcpdump
  649  screen -D -r tcpdump
  650  scree -S ping
  651  screen -S ping
  652  screen -D -r tcpdump
  653  screen -D -r fi
  654  screen -r
  655  screen -r lasthop 
  656  nmap --script fastrace.lua  --script-args="verbose=1,ip=36.56.0.0/13,output_type=file,output_filename=fi36.56.0.0_13.min26,improve=1"  -e eno2 -d|tee fi36.56.0.0_13.verbose.min26
  657  nmap --script fastrace.lua  --script-args="verbose=1,ip=188.166.144.143"  -e eth0
  658  screen -r
  659  screen -S fi
  660  screen -r tcpdump 
  661  screen -r fi
  662  screen -r tcpdump 
  663  screen -r fi
  664  screen -r tcpdump 
  665  screen -r django 
  666  screen -r shadow 
  667  screen -r
  668  screen -r ping 
  669  screen -r tcpdump 
  670  screen -r 
  671  screen -r django
  672  screen -D -r django
  673  screen -r 
  674  screen -r shadow 
  675  nmap -sn -n --script last_hop/combine.lua --min-hostgroup 29 -iL 3.live -e eth0 |tee 3.live.combine
  676  ls --block-size=m -l
  677  ls
  678  nmap -sn -n --script last_hop/combine.lua --min-hostgroup 29 -iL ip.10w -e eth0 |tee ip.10w.combine
  679  ls
  680  rz 
  681  cd /home/ly/
  682  ls
  683  cd last_hop/
  684  ls
  685  cd ..
  686  ls
  687  python last_hop/extract_combine.py 3.live.combine|tee 3.live.combine.info
  688  screen -r
  689  screen -r lasthop 
  690  screen -r lasthop  -X quit
  691  rz
  692  screen -S lh
  693  screen -r lh
  694  cd last_hop/
  695  git pull origin master
  696  ls
  697  screen -S sdlh
  698  screen -r sdlh 
  699  screen -r sdlh  -X quit
  700  screen -S slh
  701  screen -r slh
  702  screen -r 
  703  screen -r lh
  704  screen -r slh 
  705  top
  706  screen -r slh 
  707  python washingtonpost_opinion.py 1 20
  708  cd /home/ly/
  709  ls
  710  cd bulk_news_python/
  711  ls
  712  git status 
  713  git add time.py 
  714  git commit -m "add time"
  715  git commit --amend --reset-author
  716  git status 
  717  cd /home/ly/
  718  ls
  719  cd bulk_news_python/
  720  ls
  721  cp npr.py time.py
  722  chmod a+w time.py
  723  ls
  724  vim csmonitor.py 
  725  python time.py 1 2
  726  vim csmonitor.py 
  727  python time.py 1 2
  728  ls
  729  vim swarm_interestingengineering_industry.py 
  730  vim wsj_opinion.py 
  731  python time.py 1 2
  732  python time.py 1 
  733  python time.py 1 2
  734  python time.py 1 200 |tee time_us_count_1_to_100.txt
  735  cd /home/ly/
  736  ls
  737  cd bulk_news_python/
  738  ls
  739  sz time_us_count_1_to_100.txt 
  740  python time.py 1 200 health |tee time_health_count_1_1000.txt
  741  sz time_health_count_1_1000.txt 
  742  cd /home/ly/
  743  python time.py 1 200 living |tee time_living_count_1_1000.txt
  744  cd bulk_news_python/
  745  python time.py 1 200 living |tee time_living_count_1_1000.txt
  746  sz time_living_count_1_1000.txt 
  747  cd /home/ly/
  748  cd bulk_news_python/
  749  ls
  750  cd /home/ly/
  751  ls
  752  cd bulk_news_python/
  753  ls
  754  python time.py 1 200 tech |tee time_tech_count_1_1000.txt
  755  sz  time_tech_count_1_1000.txt
  756  python time.py 1 200 health  |tee time_health_count_1_1000.txt
  757  ls
  758  python time.py 1 200 science |tee time_science_count_1_1000.txt
  759  sz time_science_count_1_1000.txt 
  760  cd /home/ly/
  761  cd bulk_news_
  762  cd bulk_news_python/
  763  git push origin master 
  764  git status 
  765  diff time.py 
  766  git diff time.py
  767  q
  768  git diff history.py
  769  git diff guardian.py
  770  screen -r
  771  screen -r django 
  772  ls
  773  cd /home/ly/bulk_news_
  774  cd /home/ly/bulk_news_python/
  775  ls
  776  python wsj_opinion.py 1 2
  777  ls
  778  python washingtonpost_opinion.py 1 1
  779  python washingtonpost_opinion.py 1 1 
  780  cd /home/ly/bulk_news_
  781  cd /home/ly/bulk_news_python/
  782  ls
  783  python washingtonpost_opinion.py 1 1
  784  ls
  785  python washingtonpost_opinion.py 1 1
  786  python washingtonpost_opinion.py 0 1
  787  cd /home/ly/
  788  ls
  789  cd bulk_news_python/
  790  python washingtonpost_opinion.py 0 1
  791  cd /home/ly/
  792  ls
  793  cd bulk_news_python/
  794  ls
  795  python washingtonpost_opinion.py 1 1
  796  python washingtonpost_opinion.py 1 2
  797  cd /home/ly/
  798  cd bulk_news_python/
  799  ls
  800  cd /home/ly/bulk_news_python/
  801  python washingtonpost_opinion.py 1 1
  802  cp time.py rd.py
  803  cd /home/ly/
  804  cd bulk_news
  805  cd ../bulk_news_python/
  806  python rd.py 1 300 health |tee  re_health_1_9600.txt
  807  sz rd_culture_1_to_9600
  808  chmod a+w rd.py 
  809  python rd.py  1 1
  810  python rd.py  1 1 culture
  811  vim rd.py 
  812  python rd.py  1 1
  813  python rd.py  1 1 culture
  814  python rd.py 2 2  culture
  815  python rd.py 1 300 culture | tee rd_culture_1_to_9600
  816  python rd.py 1 300 culture | tee rd_culture_1_to_9600.1
  817  ls
  818  sz  re_health_1_9600.txt 
  819  cp rd.py livescience.py
  820  cd /home/ly/bulk_news_python/
  821  python livescience.py 1 1 technology
  822  cd /home/ly/bulk_news_python/
  823  python livescience.py 1 1 technology
  824  cd /home/ly/bulk_news_
  825  ls
  826  cd /home/ly/bulk_news_python/
  827  ls
  828  python livescience.py 1 1 history
  829  python livescience.py 1 2 history
  830  python livescience.py 1 2 healthy
  831  python livescience.py 1 2 health
  832  python livescience.py 1 2 technology
  833  vim livescience.py 
  834  python livescience.py 1 2 healthy
  835  python livescience.py 1 2 technology
  836  python livescience.py 1 1
  837  python livescience.py 1 1 technology
  838  vim livescience.py 
  839  chmod a+w livescience.py 
  840  python livescience.py 1 1 technology
  841  python livescience.py 1 2 technology
  842  python livescience.py 1  200  |tee livescience_technology_1_to_2000.txt
  843  python livescience.py 1  200 technology  |tee livescience_technology_1_to_2000.txt
  844  python livescience.py 1  200 technology | tee livescience_technology_1_to_2000.txt
  845  cd /home/ly/bulk_news_python/
  846  python livescience.py 1 200 animals |tee livescience_animals_1_to_2000.txt
  847  cd /home/ly/bulk_news_python/
  848  python livescience.py 1 200 technology | tee livescience_technology_1_to_2000.txt 
  849  cd /home/ly/bulk_news_python/
  850  python livescience.py 1 1 technology
  851  ssh root@139.162.8.195
  852  vim livescience.py
  853  python livescience.py  1 200 animals |tee livescience_animals.txt
  854  cd /home/ly/
  855  ls
  856  cd bulk_news_python/
  857  ls
  858  python livescience.py 31 100 health |tee livescience_health_31.txt
  859  python livescience.py 31 31
  860  python livescience.py 31 31 health
  861  sz livescience_health_31.txt 
  862  python livescience.py 61 100 health |tee livescience_health_61.txt
  863  cd /home/ly/bulk_news_python/
  864  ls
  865  cd /home/ly/bulk_news_python/
  866  python npr.py 1 1
  867  chmod a+w npr.py 
  868  python npr.py 1 1
  869  cd /home/ly/
  870  cd bulk_news_python/
  871  ls
  872  cp livescience.py mashable.py
  873  chmod a+w mashable.py 
  874  grep -rn "json"
  875  python mashable.py 1 2 a
  876  python mashable.py 1 1 a
  877  sudo -s
  878  cd /home/ly/
  879  cd bulk_news_python/
  880  ls
  881  vim mashable.py 
  882  python mashable.py 1 1 a
  883  cd /home/ly/
  884  cd bulk_news_
  885  cd bulk_news_python/
  886  ls
  887  python mashable.py 1 1 a
  888  python mashable.py 1 1000 |tee mashable_tech.txt
  889  python mashable.py 1 1000 a |tee mashable_tech.txt
  890  sz mashable_tech.txt 
  891  python mashable.py 1 1 a
  892  python mashable.py 100 200 a
  893  python mashable.py 300 400 a
  894  python mashable.py 333 400 a
  895  cd /home/ly/
  896  cd bulk_news_python/
  897  cd /home/ly/
  898  cd  bulk_news_python/
  899  ls
  900  python npr.py 1 1
  901  chmod a+w npr.py 
  902  python npr.py 1 1
  903  python npr.py 1 10
  904  ls
  905  python swarm_interestingengineering_industry.py 1 1
  906  git status 
  907  ls
  908  rm *.txt
  909  ls
  910  rm download/*
  911  git status 
  912  git add *.py
  913  git commit -m "add date"
  914  git push origin master 
  915  python swarm_interestingengineering_industry.py 1 1
  916  cd /home/ly/bulk_news_python/
  917  ls
  918  cd ../
  919  cd bulk_news
  920  ls
  921  cd bulk_news/
  922  ls
  923  git status 
  924  git add 。
  925  git add .
  926  git commit -m "add date npr"
  927  git add ../.
  928  git status 
  929  git add ../.
  930  git add .
  931  git commit -m "add date npr"
  932  git push origin master
  933  cd ..
  934  ls
  935  git status 
  936  git push orgin master
  937  ls
  938  git remote add origin https://github.com/yiqiaoxihui/bulk_news.git
  939  git push origin master 
  940  cd ../bulk_news_python/
  941  chmod a+w swarm_interestingengineering_industry.py 
  942  python swarm_interestingengineering_industry.py 1 1
  943  python theatlantic.py  1 2
  944  chmod a+w theatlantic.py 
  945  python theatlantic.py  1 2
  946  python theatlantic.py  1 1
  947  python theatlantic.py  1 5
  948  screen -r django 
  949  screen -list
  950  screen -r django 
  951  cd /home/ly/bulk_news
  952  ls
  953  chmod a+w ./ -R
  954  screen -r
  955  screen -r django 
  956  screen -list
  957  su ubuntu
  958  cd /home/ly/bulk_news_python/
  959  python csmonitor.py 1 1
  960  vim csmonitor.py 
  961  python csmonitor.py 1 1
  962  python csmonitor.py 12 13
  963  screen -r  django 
  964  screen -r django 
  965  cd /home/ly/bulk_news_o
  966  cd /home/ly/bulk_news_python/
  967  ls -l
  968  python time.py 1 1
  969  rm rd_culture_1_to_9600*
  970  ls
  971  ls -l
  972  rm riyu 
  973  rm 1.py 
  974  ls -l
  975  cd /home/ly/bulk_news
  976  git add .
  977  git  status 
  978  git add .
  979  git commit -m "ad"
  980  git push origin master 
  981  git add .
  982  git commit -m "ad"
  983  git push origin master 
  984  screen -r d
  985  screen -D  -r django 
  986  cd /home/ly/bulk_news_python/
  987  ls
  988  rm download/*
  989  ls
  990  git add .
  991  git commit -m "ad"
  992  git push origin master 
  993  cd /home/ly/bulk_news_python/
  994  cp mashable.py patch.py
  995  chmod a+w  patch.py 
  996  rm patch.py 
  997  ls
  998  vim rd.py 
  999  cp rd.py patch.py
 1000  chmod a+w patch.py 
 1001  python patch.py 1 1
 1002  python patch.py 1 100  |tee patch_19_18.txt
 1003  python patch.py 101 300  |tee patch_19_18_1.txt
 1004  python patch.py 1 300  |tee patch_19_18_2.txt
 1005  python patch.py 1 1
 1006  python patch.py 159 159
 1007  python patch.py 159 160
 1008  ls
 1009  wc -l patch_19_18.txt 
 1010  wc -l patch_19_18_2.txt 
 1011  sz patch_19_18_2.txt 
 1012  cd /home/ly/bulk_news_python/
 1013  sz guardian_society_18.txt 
 1014  python npr.py 1 1 national 
 1015  python npr.py 1 1 business |tee npr_business_18.txt
 1016  python npr.py 1 10000 business |tee npr_business_18.txt
 1017  sz npr_business_18.txt
 1018  ls
 1019  git status 
 1020  git add patch.py 
 1021  git commit -m "add patch"
 1022  git push origin master 
 1023  python guardian.py 1 300 environment |tee guardian_environment_18.txt
 1024  python guardian.py 301 700 environment |tee -a guardian_environment_18.txt
 1025  sz guardian_environment_18.txt 
 1026  python guardian.py 1 700 technology |tee -a guardian_technology_18.txt
 1027  sz guardian_technology_18.txt 
 1028  python npr.py 1 5000 national |tee npr_national_18.txt
 1029  python npr.py 5000 10000 national |tee -a npr_national_18.txt
 1030  sz  npr_national_18.txt
 1031  cd ../bulk_news
 1032  ls
 1033  git status 
 1034  git add bulk_news/*
 1035  git commit -m "add patch"
 1036  git push origin master 
 1037  cd /home/ly/bulk_news_
 1038  cd /home/ly/bulk_news_python/
 1039  python guardian.py 1 700 education |tee guardian_education_18.txt
 1040  sz  guardian_education_18.txt
 1041  python npr.py 1 10000 |tee npr_
 1042  ls
 1043  python npr.py 1 10000 technology|tee npr_technology_18.txt
 1044  sz  npr_technology_18.txt
 1045  ls
 1046  rm npr_
 1047  python npr.py 1 10000 health|tee npr_health_18.txt
 1048  sz  npr_health_18.txt
 1049  cd /home/ly/bulk_news_python/
 1050  python guardian.py 1 100 uk-news |tee guardian_uk_18.txt
 1051  python guardian.py 1 1000 uk-news |tee guardian_uk_18.txt
 1052  sz guardian_uk_18.txt 
 1053  python guardian.py 1000 2000 uk-news |tee guardian_uk_18_1.txt
 1054  sz  guardian_uk_18_1.txt
 1055  cd /home/ly/bulk_news_python/
 1056  cp mashable.py curiosity.py
 1057  ls
 1058  chmod  a+w curiosity.py 
 1059  ls
 1060  python curiosity.py 1 1
 1061  python curiosity.py 1 1 >1
 1062  python curiosity.py 1 1
 1063  python curiosity.py 1 1 
 1064  python curiosity.py 1 1 >1
 1065  python curiosity.py 1 1 | tee 1
 1066  vim 1
 1067  ls
 1068  rm 1
 1069  python curiosity.py 1 1 | tee 1
 1070  vim 1
 1071  python curiosity.py 1 1 
 1072  python curiosity.py 2 2
 1073  python curiosity.py 1 1000| tee curiosity_17.txt
 1074  cd /home/ly/bulk_news_python/
 1075  ls
 1076  python curiosity.py 1 1000| tee curiosity_17.txt
 1077  sz curiosity_17.txt
 1078  python curiosity.py 146 1000| tee -a curiosity_17.txt
 1079  python curiosity.py 146 152| tee -a curiosity_17.txt
 1080  sz curiosity_17.txt
 1081  screen -r swarm
 1082  screen -S swarm
 1083  cd /home/ly/bulk_news_python/
 1084  cp mashable.py psychologytoday.py
 1085  chomd a+w psychologytoday.py 
 1086  chmod a+w psychologytoday.py 
 1087  python psychologytoday.py 1 1
 1088  cd /home/ly/bulk_news_python/
 1089  vim sciencenewsforstudents.py
 1090  python sciencenewsforstudents.py 1 10
 1091  python sciencenewsforstudents.py 1 2
 1092  python sciencenewsforstudents.py 1 2 |tee 1
 1093  sz 1
 1094  python sciencenewsforstudents.py 1 1
 1095  python sciencenewsforstudents.py 1 1000 |tee sciencenewsforstudents.txt
 1096  sz  sciencenewsforstudents.txt
 1097  python sciencenewsforstudents.py udents.txt
 1098  rz
 1099  python sciencenewsforstudents.py 675 676
 1100  screen -r swarm 
 1101  cp mashable.py sciencenewsforstudents.py
 1102  chmod a+w sciencenewsforstudents.py 
 1103  sz mashable.py 
 1104  screen -r  swarm 
 1105  grep -rn "POST" ./
 1106  rm 1
 1107  grep -rn "post" ./
 1108  ls
 1109  screen -r  swarm 
 1110  ls
 1111  sz psychologytoday.txt 
 1112  screen -r  swarm 
 1113  cd /home/ly/bulk_news_python/
 1114  git status 
 1115  rm download/o*
 1116  rm download/*
 1117  ls
 1118  rm *.txt
 1119  ls
 1120  git status 
 1121  rm 1
 1122  git add *.py
 1123  git commit -m "ads"
 1124  git push origin master 
 1125  cd /home/ly/bulk_news_python/
 1126  ls
 1127  python guardian.py 1 1000 business |tee guardian_business_2019.txt
 1128  sz guardian_business_2019.txt
 1129  python guardian.py 1 1000 society |tee guardian_society_2019.txt
 1130  sz guardian_society_2019.txt
 1131  cd /home/ly/bulk_news_python/
 1132  ls
 1133  vim guardian.py 
 1134  python guardian.py 1 2000 uk-news |tee guardian_uk_19.txt
 1135  sz guardian_uk_19.txt
 1136  cd /home/ly/bulk_news_python/
 1137  python guardian.py 1 1000 enviornment |tee guardian_enviornment_2019.txt
 1138  python guardian.py 1 1000 environment |tee guardian_environment_2019.txt
 1139  sz guardian_environment_2019.txt
 1140  cd /home/ly/bulk_news_python/
 1141  python guardian.py 1 1000 enviornment |tee guardian_enviornment_2019.txt
 1142  python guardian.py 1 1000 education |tee guardian_education_2019.txt
 1143  sz  guardian_education_2019.txt
 1144  python guardian.py 1 1000 technology |tee guardian_technology_2019.txt
 1145  sz  guardian_technology_2019.txt
 1146  ls -l
 1147  cd /home/ly/bulk_news_python/
 1148  ls
 1149  ls -l
 1150  date
 1151  ls -l
 1152  rm guardian*.txt
 1153  ls -l
 1154  history |tee "python npr.py"
