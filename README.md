# Application Development Framework

### Application development framework that facilitates quick and easy setups for three different architectures of a Flask application: monolithic, service-oriented with servers, and service-oriented without servers. 

## Framework Details
Each architecture is separated into its own subfolder in this repository. Each application structure is set up to run once the user fills in the dummy functions. Files needed for setting up continuous integration with Travis CI are also included in the subfolders.

### Monolithic Architecture
Monolithic applications are built as a single unit/file that increase over time. As one of the first "design" principles we are taught, many COMS4156 students aren't familiar with other design principles that could be extremely beneficial to their software development. Over time, monolithic architectured applications can become cluttered, heavyweight, slow, and highly coupled. To address this issue, we propose that students learn how to convert their monolithic architectures into Service-Oriented Architectures!

### Service-Oriented Architecture with Servers
The Service-Oriented Architecture design principle is all about <b>services</b>. Any given application could have a number of features that we can split into a unique uncoupled "service". Each of these services act independently of each other to complete their assigned task. To communicate with these services, we use an <b>orchestrator</b> which makes calls to the necessary services. By designing their codebase in such a way, COMS4156 students will be able to separate their different features for readability purposes and easily build scalable applications. In the ./serverSOA folder, students will be able to find a framework to easily convert a monolithic architecture to a service-oriented architecture!

### Serverless Service-Oriented Architecture
One subset further into Service-Oriented Architectures is the Serverless Service-Oriented Architecture. Here, we use Amazon Web Services Lambda along with the SOA design principle to create an application that should save costs on the cloud. By using AWS Lambda, we use only the computing power necessary to run a function/service rather than continuously running a server. This should save the user on costs by taking advantage of the pricing model. Though the idea might seem daunting, within our ./serverlessSOA folder, students will find the necessary tools to transition from SOA with Servers to Serverless SOA quite easily!

Take a look!
