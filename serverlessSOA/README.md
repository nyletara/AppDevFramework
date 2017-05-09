# Server Based Service-Oriented Application

This section turns the monolithic application that was previously built into a standalone Server-based Service Oriented Application. In other words, each feature (or service) that built up the initial monolithic application is now split into individual servers that communicate with each other. This provides a variety of benefits which are highlighted in the following paper: *SOA paper link*

This section still uses Flask Application Servers that allow users to host applications locally or on cloud servers, hence, maximizes as much code-reuse as possible. 

#### The Orchestrator

The Orchestrator is the first component of this architecture but will be the last to be completed. The orchestrator facilitates communication between the User Interface as well as among all the different services that make up the application.