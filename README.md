===================
basic-search-engine
===================

This is the basic model of a search engine. It includes a web-crawler which is
responsible for  crawling the web and building up the index for the search engine.

________________

web-crawler.py
________________

The web-crawler module implements various methods to crawl the web from a given
seed page and index all the collected links in a python dictionary data type in
the form of key-value pairs. For each key there may be one or more than one value
i.e for every keyword stored in the dictionary data-type there may be one or more 
than one URL corresponding to the keyword.

To crawl the web and build an index, use the crawl_web method located in the 
web-crawler module. The crawl_web method takes two parameters, the first is the
seed page i.e. the page from where the crawler will commence the crawling and 
the second is the depth to which the crawler should crawl. This is necessary 
because the crawler will not get caught up crawling the links to an indefinite
depth. Any natural number may be used for the max_depth as long as it satisfies
your requirement.Initialize the python console, make sure you are working in the
cloned directory. Following are the commands:

<b>>>> from web-crawler import crawl_web</b><br>
<b>>>> index = crawl_web(seed_page_url_in_quotes, max_depth)</b><br>
<b>#crawl_web("http://www.personal.kent.edu/~rmuhamma/OpSystems/os.html", 1)</b><br>

The first command imports the crawl_web method from the web-crawler module. In 
the next command we crawl the web starting from the seed page(first parameter) upto
a given depth(second parameter). The crawler crawls the web and builds an index of
keywords mapping to their respective URL(s) in a dictionary data-type. On completion
the method returns the index which is being stored in the variable <i>index</i>.<br><br>


______________

lookup.py
______________

The lookup module implements the lookup method which in it's basic form is responsible
for querying the search engine. The lookup method uses two parameters. First is the
index in which the query is to be searched for while the second is the query itself.
The query is passed as a string type. The method may or or may not return a URL for a
given query depending on whether the keyword is associated with any URL(s) or not.
Make sure you have built an index using the web-crawler module. Following is a
sample lookup query:

<b>>>> from lookup import lookup</b><br>
<b>>>> lookup(index, query)</b><br>
<b># lookup(index, "Deadlock")</b><br><br>

