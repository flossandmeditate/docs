#!/usr/bin/env python

import sys
import os


langs = ['en', 'tr', 'zh-CN', 'hu', 'fr']


cmd_clean = " echo 'Clean up...\n'; rm -r html xetex; "
cmd_pdf =   " echo '------------\nBuild PDF...\n------------'; sphinx-build -b latex . xetex && cd xetex; xelatex *.tex; cp -f LittlevGL.pdf ../LittlevGL.pdf; cd ..; "
cmd_html =  " echo '------------\nBuild HTML...\n------------'; sphinx-build -b html . html; "

cmd_build = cmd_clean + cmd_pdf + cmd_html + " "

for lang in langs:
  cmd = " echo '\n\n************\nStart " + lang + "\n************'; cd " + lang + "; " + cmd_build + " cd ..; "
  os.system(cmd)
  
  
