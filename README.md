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
depth. Following are the commands:

<b>>>>from web-crawler import crawl_web</b><br>
<b>>>>crawl_web(seed_page_url_in_quotes, max_depth)</b><br>
/*crawl_web("http://www.dit.edu.in", 1) */
