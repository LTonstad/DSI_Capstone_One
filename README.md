# Capstone 1 - Proposals

## 1st Proposal - [Beer Production](https://www.ttb.gov/beer/statistics)
In honor of the new Denver Beer Company opening in my neighborhood I thought it'd be interesting to try and better understand what is going on with production & sales within the beer industry.

### Dataset
This data set comes directly from the Brewer's Report of Operations to the US Department of Treasury and is updated roughly every 90 days (COVID strikes again). Looks like there may be a few hurdles to jump through for importing since they are all .xls files and it's not formatted in a particularly helpful way.

Here are some of the columns that there is to work with from yearly data:

* Number of Breweries (based on production size)
* Total Barrels produced
* Total Barrels exported
* Taxable Removals

From monthly production data:

* In Bottles & Cans
* In Kegs
* Tax Determined
* For Export
* For Vessels & Aircraft
* Consumed on brewery premises
* Stock on hand at end of the month

### Possible Visualizations

* Plot changes in trends of sales overtime (Take deeper look at impact of COVID on things like exports, stock on hand or trends in keg to bottles/canned production)
* Histogram showing changes in the number of breweries in production overtime (and again checking COVID affects, particularly the affect on small vs. large productions)
* Bar chart comparing the actual amount of barrels produced per production size group (There is a great disparity in the number of breweries between the groups: Largest group has only 15 breweries, where there are over 4,500 smaller breweries)

### Possible Hypothesis

* Breweries producing under 6 million barrels will have a larger market share than largest breweries by 2040
* Long term affects of COVID will lead to middle-market breweries rising overtime, cutting out a portion of the market share from both top and bottom production groups

## 2nd Proposal - [Whats up with these crazy drug prices?](https://data.medicaid.gov/Drug-Pricing-and-Payment/NADAC-as-of-2021-02-17/g5hm-kcb7)

### Dataset

With over 24,000 rows of data, data.medicaid.gov keeps weekly records on drug pricing that would be very interesting to explore. Based on a quick look, there will likely be a decent amount of working with NaNs. Some of the important columns include:

* NDC (National Drug Code)
* Description
* Drug Class
* Classification_for_rate_setting - Indicates whether the drug is classified as name brand or generic
* NADAC_per_unit ([Apparently complicated enough to have a 56 page pdf description](https://www.medicaid.gov/medicaid-chip-program-information/by-topics/prescription-drugs/ful-nadac-downloads/nadacmethodology.pdf))
* Pharmacy Type
* Explanation Code - Code (1-6) that indicates how the NADAC price was calculated


### Possible Visualizations

* Histogram showing difference in price based on generic vs. OTC
* Plot and compare distributions of NADAC rates of generic and over the counter drugs

### Possible Hypothesis

* Would love to add some of these smaller [first time NADAC rate](https://data.medicaid.gov/Drug-Pricing-and-Payment/First-Time-NADAC-Rates-as-of-12-23-2020/ek62-5cwy) tables to compare how the prices have changed over time
* Name brand drugs are roughly double the price on average

## 3rd Proposal - [Podcast Reviews](https://www.kaggle.com/thoughtvector/podcastreviews)

### Dataset

This dataset contains over 1 million podcast reviews from Apple podcast in an SQLite file. The dataset has 4 different tables:

* Categories - Stats the genre of the podcast
* Podcasts - Title, ID's, slug (ID)
* Reviews - Title (of review), content, rating, created_at
* Runs - Times that the db has been updated

### Possible Visualizations

* Word map (maybe histogram) of most popular words used in reviews, perhaps multiple plots with same categories
* Scatterplots showing ratings overtime within their respective categories.

### Possible Hypothesis

* 5 Star reviews will get a much higher word count than the 1 star reviews
* As time goes on ratings will skew towards 5 stars
