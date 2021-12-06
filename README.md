# python-task-weatherman

###main python file is weatherman.py

#####note: Before try to run the code please double check the folder path which contain the text file data 

To run the code you have to pass the argument from the termial e.g 
  1. python3 weatherman.py -e 2006 /lahore_weather
  2. python3 weatherman.py -a 2005/5 /Dubai_weather
  3. python3 weatherman.py -c 2010/06 /Muree_weather

In the above examples 
  (1) it will read all the records of the year(all months and days) and print the highest max temperature, lowest temperature and highest humidity level recorded on which day and month
  
  (2) it will read all the records of the mention month of the year(all days) and print the highest max temperature average, lowest temperature average and highest humidty level average recorded on the whole month
  (3) it will read all the records of the mention month of the year(all days) and print highest record temperature and lowest recoded temperature of all the days in red and blue color(red for highest and blue for lowest).

if the the input argument structure does not match the above example it will it produced the wrong command line message and print the example command at which it will run the code

if it program can not fine the file it will print the error message that there is no file with that name and exit the program.

