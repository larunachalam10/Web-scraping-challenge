# Web-scraping-challenge

MISSION TO MARS

Scrape various websites for data related to the Mission to Mars and displays the information in a single HTML page.

Scrapping:

Mars News
    Script collects the latest News title and Paragraph Text.

JPL Mars Space Image
    Script finds the image url for the current Featured mars image and assigns the url string of the full size image.

Mars Weather
    Visit the Mars Facts webpage here and use Pandas to scrape the table containing facts about the planet including Diameter, Mass, etc.

Mars Hemisphere
    Visit the USGS Astrogeology site here to obtain high resolution images for each of Mar's hemispheres.

    Save both the image url string for the full resolution hemisphere image, and the Hemisphere title containing the hemisphere name. Use a Python dictionary to store the data using the keys img_url and title.

MongoDB and Flask Application
    Use MongoDB with Flask templating to create a new HTML page that displays all of the information that was scraped from the URLs above.



