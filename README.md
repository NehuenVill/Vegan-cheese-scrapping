# **CPU Benchmarks scrapping program**


## Goal of the project

The goal of the project is to retrieve information about different vegan cheese products and the different tags used to describe them. from Australian store: =="vegangrocerystore"==.

## Technologies used

* **Python.**
* **API management.**
* **Insomnia.**
* **Request Library.**
* **Excel Spreadsheets.**
* **Pandas library.**

## Description of the scrapping process

Before any coding is done, I searched the *vegangrocerystore* web page for an internal API that requests the information about the vegan cheese products, so that I could avoid the usage of **BeautifulSoup4** or **Selenium**.

Once found this API, I made a request with the **Insomnia tool** for testing APIs so that I could analyze the *JSON output* to write the right functions in the python program **Scrapper**.

Next, I generated the python code for the request inside **Insomnia** and pasted it into the **Scrapper program**. With these parameters, the program can access directly to the API and get the information about the products without having to use any other library.

Now, regarding the scrapping process, The function **GetData** gets the **Title** and all the **Tags** (as a string) of each product on the API response.

The **SaveData** function is called with the **GetData** function as an argument (since it returns all the Data retrieved). This function Exports the information into an Excel file called **Vegan cheese products.xls**.
