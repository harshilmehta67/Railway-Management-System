# Railway-Management-System

Starting off, we have tried to model a mini online railway reservation system. 
To do so, we have used PostgreSQL for database design and query mode and other back - end activity. 
We have used python language as our medium , html web pages for frontend and flask for connecting frontend with postgresql. 

For booking tickets, a user must log in to the system or create a new account and get his user ID which is used to book tickets and further reservation purposes through a Login Module.

For the process of Booking tickets, a schedule of trains is shown to users with appropriate filters. 
Schedule of the train includes train details with timings, stations,seats left and ticket price. 
There are many types of seat Category and if booked on any specific train and specific date, a unique ‘pnr’ is generated for that booking. 
Also, passengers are queued, if there are no more seats available then this passenger is added to the ‘waiting’ queue.
The passenger also has the ‘cancel’ ticket feature. If any passenger cancels the ticket, the queue is pushed and the front of the queue is booked. 
Meaning the passenger got his ticket status changed from ‘waiting’ to ‘confirmed’. 
The payment is processed through the user’s wallet. The minimum balance of ticket price needs to be there in the user’s wallet.

Admin side Functionalities include Inquiry functions such as Inquiry for trains traveling from point A to point B, 
details of all trains traveling between two dates, details of any station, the revenue generated on the given date for a train, 
details of deleted tickets, and inquiries like booking status and other formal inquiries.

In addition to other features, we’ve also included the technical aspect of deletion of any records by any user/administrator which in return deletes all child records via triggers and functions/procedures. 
We’ve also created a record for tracking all the user-driven activities. Input details are validated for safe data handling.

We also have our special function and we are happy that our team was able to implement that. 
Say a user wants to go from station A to B, have some time to spend at Station B because of his work and go from station B to C. 
So the user has the flexibility to avail such special options and appropriate output is displayed.

All these functionalities are implemented with appropriate procedures/functions and triggers.

