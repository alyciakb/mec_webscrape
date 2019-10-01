# Member Insights Analyst at MEC

## First Steps

Below is the steps I would take in approaching this position (given my current knowledge of the responsibilities of the position).

1. Talk to Member Insights team members - ask if they have any questions they want answered.
2. Talk to other relevant MEC teams (ex. customer service, product development, digital marketing) - ask for their intuitions and questions regarding members.
3. Combine, refine, and prioritize questions gathered.
4. Perform analysis to answer those questions or find insights into them: determine relevant data sources, clean and explore data, perform analysis, report results to relevant departments and/or use those results to launch other questions and further analysis.
5. If there are no questions that currently need addressing (or the questions are too broad), perform exploratory data analysis on data sources that are deemed relevant to member insights (ex. VOC outputs, customer surveys, customer service logs). This can help MEC understand what topics should be addressed and explored further to improve understanding of MEC members - continue to steps 3 and 4.
6. Develop benchmarks and metrics to be used to track member goals (member satisfaction - of products, services, customer support; retention rates, addition of new members).
7. Build automated systems that track the defined member insights benchmarks/metrics to allow for continual monitoring of progress.


## A Small Example of Step 5

### MEC Website: Questions and Insights

I recognize that the Member Insights Analyst would start with data more relevant to the team (such as customer surveys and other direct feedback from members), but I do not have access to that information and instead explored the MEC website. I performed a small MEC website scrape to access product names, product categories, subcategories, average product rating (number of stars), and number of ratings/reviews per product. After cleaning and exploring the data, I garnered a few insights and questions. *Please note all numbers are from the time the data was collected and they may change slightly as products are added/removed from the website.*


#### A Few Insights

1. There are 13,930 unique products on the website. Over 50% of products have no reviews and only 19% of products have 5+ reviews. The products with reviews have an average rating of 4.08/5 stars and 89% have a rating of 3+ stars.  
2. There are 1174 MEC branded products sold (8.4% of all products). Almost 74% of the MEC brand has 1+ reviews online and the average rating is 3.94 stars.
3. Products are divided into 11 categories: camping and hiking, run and fitness, climbing, clothing, footwear, packs and bags, watersports, snowsports, travel gear, cycling, and kids/youth. Of those categories:
    1. Camping and hiking is the largest with almost 40% of products included within that category
    2. Kids is the smallest with only 4% of products. 
    3. Climbing gear has the highest average rating, 4.3 stars, followed by packs and bags with 4.26 stars. 
    4. Cycling and kids have the lowest average rating, each with 3.99 stars. 
    5. Climbing has the lowest percentage of products with reviews under 3 stars (5.6%).
    6. Kids has the highest percentage of products with reviews under 3 stars (15.5%), followed by travel gear (13.3%) and cycling (12.7%).
4. Only 40% of products with a less than 3 star rating have more than 3 reviews and only 25% have more than 6 reviews.
5. Almost 50% of products that have a rating of less than 3 stars and 20 or more reviews are cycling products (tubes and accessories). 

#### Questions

1. Are products bought online that have no reviews more likely to be returned or is customer service more likely to be contacted with an issue regarding the product? 
2. Are products with a low rating online more likely to be returned (regardless of whether bought online or in-person)?
3. Are products with no reviews less likely to be purchased online than a competing product that has reviews?
4. How many online product reviews do we have vs. online sales?
5. Is there a marketing opportunity to increase number of reviews collected from online sales?
6. Is there a specific segment of members that are more likely to shop online instead of in-store?
7. Can increasing the number of product reviews we have increase online sales?
8. Is there a product type or product subcategory that has consistently low reviews that MEC does NOT have any products in? Would it be feasible for MEC to enter this product type and build a product that would better satisfy their members? Or are there similar versions/brands of those products on the market that MEC currently doesn't offer?


Notes: *There were more insights gained, but presenting too many percentages and numbers can get overwhelming. This was made to be a quick analysis, and therefore I did not include figures (graphs, etc) within this report - something I would do if presenting a more in-depth analysis. Some of the above questions relate to member insights in an indirect way and may be more relevant to other departments, but all can help in gaining a well-rounded look at MEC's members. I recognize that there are better data sources and more important questions for the member insights analyst to tackle first. Further, some of these questions may be the responsibility of an analyst within a different department. This was simply a look at some of the information housed on MEC's website and a few insights and questions it resulted in.*

[The full exploratory data analysis - included some visualizations - can be found here.](https://github.com/alyciakb/mec_webscrape/blob/master/mec-scrape.ipynb)