
This project is about scraping through a bunch of wikipedia pages on disney movies and building up a data set on that information by using libraries like __Beautifulsoup, Requests__ and ultimately the real goal is learning how to solve real world problems by answering somes questions abouts movies worlds.

### Steps
- Web scraping with BeautifulSoup
- Cleaning data
- Testing code with Pytest
- Pattern matching with regular expressions
- Working with dates
- Saving & loading data with Pickle
- Accessing data from an API using Requests

__Wikipedia Disney movies Scraping.ipynb__, contain the data set creation

__dataset_checkpoints__, where dataset are saved 

__conversion.py__ , contain a fucntion given a money value and return it as integer or float then use this function in an other file __test_money_conversion.py__, which contain tests to see if the job is done for multiple cases when converting monetary value to numeric value.

 
we are trying to catch pattern so will be using __Regex__ : Regular Expression is used to extract a substring from a string. Almost each value followed by dollar sign so need to capture the number there , it is like key indicator , so we start simple and then build up .

we may not handle all cases but we try to clean as much as possible, then run the function on the tests with the pytest file 
          
          pytest test_money_conversion.py

![run pytest](https://user-images.githubusercontent.com/26963240/144080476-703820e2-65da-439e-b6c3-daca4a9b9cbc.png)
 
keep testing until we full fill all the tests

![clear tests](https://user-images.githubusercontent.com/26963240/145377825-0d482622-a0c2-41d8-b5d3-7c0480da94ac.png)

Then take all the code of the cleaning function and move it to jupyter notebook, then converting monetary variable into floats and converting dates into datetime objects using strptime from datetime library. 

At this point it was not possible to save the data cleaned into JSON file due to th object of type datetime is not JSON serializable so we used __Pickle__ to save and load data by creating two functions.

__Pickle__ module implements binary protocols for serializing and de-serializing a Python object structure unlike JSON which is a text serialization format (it outputs unicode text, although most of the time it is then encoded to utf-8). Since Pickle module is not secure, it will not be our final format to save the data in it .

Next, we added rattings and IMDB score using API such us OMDb API and get API Key for free from this website http://www.omdbapi.com/?apikey=[yourkey]&.

Final steps will be saving the final version of data into json and csv files, and the data will be ready for analysis which will be the next step for this project.
