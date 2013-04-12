'''This web-crawler module makes use of the urllib2 and
urlparse module. The urrlib2 is used for establishing and 
maintaining a connection with a host while the urlparse is
used in the process of converting relative URL(s) into
absolute URL(s)'''
import urllib2
from urlparse import urljoin

'''The get_html method is where the crawler establishes a
connection to a given URL using the urllib2 module. It reads
the source code or the html coding of a web-page and returns it
to the calling method.'''
def get_html(url):
    try:
        return urllib2.urlopen(url).read()
    except:
        return ""    

'''The get_next_target method is where the crawler performs its
basic function i.e. identifying and parsing the links given on a web-page.
It searches for the anchor tag in the html coding and separate the links.
The basic functionality of this method is to provide the calling method 
with the next link occurrence on the page. It takes the html coding of a
given web-page as a parameter.'''
def get_next_target(page):
    start_link = page.find("<a href=")
    if start_link == -1:
       start_link = page.find("<A HREF=")
    if start_link == -1:
       return None, 0, None
    start_quote = page.find('"', start_link)
    end_quote = page.find('"', start_quote+1)
    url = page[start_quote+1:end_quote]
    start_tag = page.find('>', end_quote)
    if "<A HREF=" in page:
       end_tag = page.find('</A>', end_quote)
    else:
       end_tag = page.find('</a>', end_quote)
    tag = page[start_tag+1:end_tag]
    url = urllib2.quote(url, safe="%/:=&?~+!$,;()*[]")
    return url, end_quote, tag


'''The get_all_links method calls the get_next_target method to fetch the
next available link from the web page. The link, if happens to be a relative
url is being converted into absolute url and is added to the index in the
dictionary with the keyword associated with the url as the key and the
actual url as the value in the dictionary. The method returns the list of
the links and the index.'''
def get_all_links(page, base_url, index):
    links = []
    while True:
          url, endpos, tag = get_next_target(page)
          if url:
             url = urljoin(base_url, url)
             if url not in links:
                links.append(url)
             page = page[endpos:]
             add_page_to_index(index, url, tag)
          else:
             break 
    return links, index


def add_to_index(index, keyword, url):
    if keyword in index:
       if url not in index[keyword]:
          index[keyword].append(url)
    else:
       index[keyword] = [url]
    return index

def add_page_to_index(index, url, content):
    index = add_to_index(index, content, url)
    return index


def union(list1, list2):
    for element in list2:
        if element not in list1:
           list1.append(element)


def crawl_web(seed_page, max_depth):
    to_crawl = [seed_page]
    crawled = []
    index = {}
    next_depth = []
    depth = 0
    while to_crawl and depth <= max_depth:
          current_crawl = to_crawl.pop()
          if current_crawl not in crawled:
             content = get_html(current_crawl)
             links, index = get_all_links(content, current_crawl, index)
             union(next_depth, links)
             crawled.append(current_crawl)
          if not to_crawl:
             to_crawl, next_depth = next_depth, []
             depth = depth + 1
    return index
