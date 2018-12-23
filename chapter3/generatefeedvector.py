# -*- coding: utf-8 -*-
import feedparser
import re

# Returns title and dictionary of word counts for an RSS feed
def getwordcounts(url):
  # Parse the feed
  #根据url，访问feed
  d=feedparser.parse(url)
  wc={}

  # Loop over all the entries
  #在feed中遍历其中的条目，选择‘摘要’或者‘描述’
  for e in d.entries:
    if 'summary' in e: summary=e.summary
    else: summary=e.description

    # Extract a list of words
    #然后对于其中的单词进行拆分
    words=getwords(e.title+' '+summary)
    for word in words:
      #wc字典中，包含了单词和单词的频度
      wc.setdefault(word,0)
      wc[word]+=1
  return d.feed.title,wc

def getwords(html):
  # Remove all the HTML tags
  #基于正则表达式，剔除<和>之间的内容为''
  txt=re.compile(r'<[^>]+>').sub('',html)

  # Split words by all non-alpha characters
  #基于非alpha字符近分解
  words=re.compile(r'[^A-Z^a-z]+').split(txt)

  # Convert to lowercase
  #转为小写返回
  return [word.lower() for word in words if word!='']


apcount={}
wordcounts={}
#遍历feddlist.txt中的每一行记录
feedlist=[line for line in file('feedlist.txt')]
for feedurl in feedlist:
  try:
    title,wc=getwordcounts(feedurl)
    #wordcounts中包含了基于feed title和单词内容的字段
    wordcounts[title]=wc
    for word,count in wc.items():
      #在apcount中记录了单词在多个feed中出现的频度
      apcount.setdefault(word,0)
      if count>1:
        apcount[word]+=1
  except:
    print 'Failed to parse feed %s' % feedurl

#计算了该单词在多少个feedlist中出现过
#选择一定的比例
wordlist=[]
for w,bc in apcount.items():
  frac=float(bc)/len(feedlist)
  if frac>0.1 and frac<0.5:
    wordlist.append(w)

out=file('blogdata1.txt','w')
out.write('Blog')
for word in wordlist: out.write('\t%s' % word)
out.write('\n')
for blog,wc in wordcounts.items():
  print blog
  out.write(blog)
  for word in wordlist:
    if word in wc: out.write('\t%d' % wc[word])
    else: out.write('\t0')
  out.write('\n')
