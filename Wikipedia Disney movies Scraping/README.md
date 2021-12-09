
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

![run test 1 failed](https://user-images.githubusercontent.com/26963240/145377441-ecc4d0b7-0864-41d5-ab90-5b271ec1ebe9.png)
