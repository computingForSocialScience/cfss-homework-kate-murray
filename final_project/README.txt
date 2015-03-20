Kate Murray's Explanation

First, I picked 5 tablecodes from the website and passed them into the function. Then, I included the FIPs codes from the cfss website. I made the function gettabledata to get data from the census API and pass it into a mysql database. There are 2 tables in the database, one that provides information on the tables, and one that includes the table information, along with the geographic ids and the row IDs, row names, and estimates from each row.

Then, for each table ID, I went through all the FIPS codes, entering these into a api url, and getting the data from each url, skipping the ones that didn't have information. Then, I chose the information I wanted from the JSON data, and put it into the 2 mysql tables.

For creating the website, I hard-coded all of the census row ids in with their respective names, creating 2 drop down menus, along with a drop down menu for choosing the state.

For the individual graphs, I attempted to make a bokeh graph. I successfully retrieved the information from the drop down menus and passed it back into my equation, but when I got the corresponding rows from the mysql data, it was a list of tuples, which the bokeh graph wouldn't take.

So, the bokeh graph renders correctly on the webpage, it simply doesn't display anything because the information I'm passing it is in the wrong form.

The things I didn't get to were the regression, and also, the data took a long time to pass into the mysql database, which is a problem I never resolved, so I couldn't troubleshoot every url I was using because I only had time to get the information for 2 tables for 4 states. The ones I found that contained no data, I had the terminal print skipped instead of getting the json data.
