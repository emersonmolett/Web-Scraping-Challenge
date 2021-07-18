Building off my HTML knowledge, this assignment creates a web application that scrapes various websites for data related to the planet Mars. This information is displayed in a single HTML page. The assignment uses Jupyter Notbook, Python, Flask, BeautifulSoup, and MongoDB.
<br>

Web Scraping in Jupyter Notebook:</br>
Accomplished deploying code that:
<li>Scrapes the most recent NASA news</li>
<li>Scrapes the URL for the featured image</li>
<li>Scrapes all four (4) hemisphere image URLs</li>
<li>Scrapes the Mars Facts HTML table</li> 

<br>
Flask App:</br>
A Flask App was created to:
<li>Route loading the webpage and scraping the content</li> 
<li>Connects, fetches, and inserts data to and from MongoDB </li> 
<li>Returns a rendered template and passes it a variable of the scraped data</li> 
<li>Calls scrape method from an external Python module</li>   

<br>

A website was designed that displays a landing page prior to scraping. A button is used to initiate the scraping feature. Jinja is used to load data from the variable passed by Flask. The website is styled with the use of Bootstrap. 


