
# Log Analysis Project

This project is to create a reporting tool that will print out reports in plain text. The Python program queries a PostgreSQL database, and returns a report that answers these questions:

1. **What are the most popular three articles of all time?** 
1. **Who are the most popular article authors of all time?** 
1. **On which days did more than 1% of requests lead to errors?**  

## Setup

1. Install [Vagrant](https://www.vagrantup.com/)
1. Install [VirtualBox](https://www.virtualbox.org/)
1. Clone repository

## Run
1. cd into the correct  directory: ``` cd /vagrant/news_log_analysis ```
2.  Load the data by running this command:  `psql -d news -f newsdata.sql`
3. Run the program : ``` python news_log_analysis.py ```

##  Output  
    Question 1:
        What are the most popular three articles of all time?
    Answer:
        "Candidate is jerk, alleges rival" - was viewed 338647 times
	    "Bears love berries, alleges bear" - was viewed 253801 times
	    "Bad things gone, say good people" - was viewed 170098 times
	
	Question 2:
		Who are the most popular article authors of all time?
	Answer:
		Ursula La Multa - was viewed 507594 times
		Rudolf von Treppenwitz - was viewed 423457 times
		Anonymous Contributor - was viewed 170098 times
		Markoff Chaney - was viewed 84557 times
	
	Question 3:
		On which days did more than 1% of requests lead to errors?
	Answer:
		On July 17, 2016 - 2.3% requests lead to errors