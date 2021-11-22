## Introduction

Web scraping is an automated method used to extract large amounts of data from websites which are ususally unstructured so web scraping helps collect 
these unstructured data and store it in a structured form.
There are different ways to scrape websites such as online Services, APIs or writing your own code. 

Some websites allow web scraping and some don’t. To know whether a website allows web scraping or not, you can look at the website’s “robots.txt” file by 
appending it to the URL that need to be scraped.

In this repository , we’ll see how to implement web scraping with python because it is easy to use with a large collection of libraries, 
don't need to define datatypes for variables since it is dynamically typed also python syntax is easily understandable plus writing small code can do large tasks with 
the biggest and most active communities.

Web Scraping is done when runing the code for web scraping, a request is sent to the URL mentioned. As a response to the request, the server sends the data and allows
the user to read the HTML or XML page. The code then, parses the HTML or XML page, finds the data and extracts it. 

## Steps:

1. Find the URL to scrape.
2. Inspecting the Page.
3. Find the data need to be extracted.
4. Write the code.
5. Run the code and extract the data.
6. Store the data in the required format.

## Libraries:
- __Selenium__: is a web testing library used to automate browser activities.
- __BeautifulSoup__: is a Python package for parsing HTML and XML documents. It creates parse trees that is helpful to extract the data easily.
- __Requests__: is a library allows to get a web page by using get() on the URL
- __Pandas__: is a library used for data manipulation and analysis used to extract the data and store it in the desired format. 
