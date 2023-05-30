# pseudo-distribution
Using python's multi-threaded module to mimic distribution to solve the flight with the most passengers counted
Assignment Case Study Description and Data Access Details for Task B
AComp_Passenger_data_no_error.csv	Top30_airports_LatLong.csv
The first data file contains details of passengers that have flown between airports over a certain period. The data is in a comma delimited text file, one line per record, using the following format:

Passenger id	Format: 
From airport IATA/FAA code	Format: 
Destination airport IATA/FAA code	Format: 
Departure time (GMT)	Format: 
Total flight time (mins)	Format:   (Unix ‘epoch’ time)
Format: 

Where  is Uppercase ASCII,  is digit 0..9 and  is the min/max range of the number of digits/characters in a string.
The second data file is a list of airport data comprising the name, IATA/FAA code, and location of the airport. The data is in a comma delimited text file, one line per record using the following format: 

Airport Name	Format: 
Airport IATA/FAA code	Format: 
Latitude	Format: 
Longitude	Format: 

Q：For this task in the development process, develop a MapReduce-like executable prototype, (in Java, C, C++, or Python). The objective is to develop the basic functional ‘building-blocks’ that will address the Task above, in a way that emulates the MapReduce/Hadoop framework. 
The solution may use multi-threading as required. The marking scheme reflects the appropriate use of coding techniques, succinct code comments as required, data structures and overall program design. The code should be subject to version control best-practices using a hosted repository under your university username.

Based on the understanding of appeal data and problems, combined with a multi-process data processing code written by myself in python before, to solve this problem, so as to imitate a MapReduce-like executable prototype, the specific process is as follows:
1. High-level description of the prototype software development:
   The development process of the MapReduce-like prototype in Python began with understanding the problem domain and the required computations. This was followed by designing the Map and Reduce functions to process the data and compute the required results. The software was then implemented and tested with a small set of data to verify its correctness. The software uses the MapReduce programming model and the Python's `concurrent.futures` module to parallelize the computations. The software processes passenger flight data and computes the number of passengers for each airport.

Figure 1 Code flow chart
2. Version control processes:
   The development process followed a basic version control workflow using Git. The initial version of the software was committed to the main branch. For each new feature or bug fix, a new branch was created. After the changes were implemented and tested, the branch was merged back into the main branch. This ensured that the main branch always contained a working version of the software.

3. Detailed description of the MapReduce functions:
   - Map Function: The `map_phase` function processes each record in the passenger data and returns a tuple of `(from_airport, 1)`. This represents a count of 1 for the `from_airport` in the record. The map function is applied to each record in parallel.

   - Reduce Function: The `reduce_phase` function takes a tuple of `(from_airport, passenger_counts)` where `passenger_counts` is a list of counts for the `from_airport`. It sums up all the counts to compute the total number of passengers for the `from_airport`. The reduce function is applied to each unique `from_airport` in parallel.

4. Output format:
   The job produces a report that lists each airport and the corresponding passenger count. The report is outputted to the console in the following format: `Airport: {airport}, Passenger count: {count}`. Each line of the report represents one airport.

5. Result analysis:
This output tells us that passenger UES9151GS5 has flown the most of all passengers, with a total of 25 flights.
1. User behavior analysis: If UES9151GS5 is a specific passenger ID, then the passenger is probably a very frequent traveler. He/she may be a business person who needs to travel a lot, or may be a travel enthusiast. This kind of information is important for airlines to use for marketing, such as offering customized travel packages or coupons to increase customer loyalty.
2. Service optimization: For airlines, knowing which passengers use their services most often can help them optimize their services, such as providing more convenient booking options, more flexible flight time choices, etc.
3. Risk Management: If a passenger flies very frequently, the airline may need to pay attention to the risk level of the passenger. For example, if the passenger booked a large number of flights in a short period of time, further scrutiny may be needed to prevent fraud.
Overall, this type of data analysis can help airlines better understand their customers, optimize service, increase revenue, and manage risk.
