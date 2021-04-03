Create a simple python package (project) that crawls two different websites and is capable to be extended easily to add new sites. The sites you need to crawl for now:

- Pypi site: and get the 100 top trending packages in the topic of Scientific Engineering. Here is the [link](https://pypi.org/search/?q=&o=&c=Topic+%3A%3A+Scientific%2FEngineering)
- Packagist site: get the 100 top popular packages from the following [link](https://packagist.org/explore/popular)

The output of each crawler is a dataframe table containing the following columns:

Package|Description|link

This task is to test your object-oriented programming knowledge in python. So designing the package is more important than the actual solution.

*Hint: Try to find the mutual functionalities between the two crawlers and write an abstract class.*
**Bonus:** Add some unit tests.
