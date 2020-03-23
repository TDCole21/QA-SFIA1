# Skills Framework for the Information Age (SFIA) - Project 1
---
# Hollywood Film and Actor Database

This is a project, worked on independently of others, in reference to the QA Learning Academy training base project specification; Fundamental Project Specification - DevOps Core. The purpose of this project is to fulfill the specification defined for the assignment due Monday 23rd March 2020, 09:00.


## Contents
1. [Brief](#brief)
    1. [MVP](#mvp)
    1. [Tech Stack Requirements](#tech_stack)
2. [Project Management](#project_management)
    1. [Agile Methodology](#agile)
    2. [Kanban Board](#kanban_board)
        1. [Initial Plan](#first_kanban_board)
        2. [Dynamic Updates](#kanban_board_changes)
        3. [Final Board](#final_kanban_board)
    
3. [Entity Relationship Diagrams](#entity_relationship_diagrams)
4. [Risk Assessment](#risk_assessment)
5. [Testing](#testing)
    1. [Pytest](#report)
    2. [Coverage Report](#coverage_report)
4. [Deployment](#deployment)
    1. [Feature Branch Model](#branch_merge)
5. [Front End Design](#front_end_design)
6. [Improvements for the Future](#improvements_for_the_future)
7. [Authors](#authors)
8. [Acknowledgements](#acknowledgements)

## Brief <a name="brief"></a>
This section of the document will serve as the introduction for the requirements of the project.

The purpose of this project is to create an application that involves the concepts learnt from the core training modules; more specifically, this will involve:
+ Agile
+ Python Fundamentals, Testing and Web Development
+ Git
+ Basic Linux
+ Continuous Integration (CI)
+ Cloud Fundamentals
+ Databases

The resulting aim of the project is to produce an application that must manipulate two tables displaying full Create, Read, Update and Delete (CRUD) functionality with the utilisation of supporting tools, methodologies and technologies that encapsulate all the above modules.

### Minimum Viable Product (MVP) <a name="mvp"></a>
The Minimum Viable Product (MVP) for the project has the following requirements:
+ A Kanban board with full expansion on user stories, use cases and tasks needed to complete the project.
+ A relational database used to store data persistently for the project, this database needs to have at least 2 tables and are also required to model the relationship using an Entity Relationship Diagram (ERD).
+ Clear Documentation describing the architecture used for the project in addition to a detailed Risk assessment.
+ A functional CRUD application created in Python.
+ Fully designed test suites for the application, as well as automated tests for validation of the application. Must also demonstrate high test coverage in the backend and provide consistent reports and evidence to support a Test Driven Development (TDD) approach.
+ A functioning front-end website and integrated Application Programming Interfaces (API), using Flask.
+ Code fully integrated into a Version Control System using the Feature-Branch model which will subsequently be built through a CI server and deployed to a cloud-based virtual machine.

### Tech Stack Requirements <a name="tech_stack"></a>
The Tech Stack requirements are the following:
|Technology Required|Used in this project|
|---|---|
|Kanban Board|Trello|
|Database|Google Cloud Platform (GCP) SQL Server|
|Programming language|Python (including MySQL)|
|Unit Testing with Python|Pytest|
|Integration Testing with Python|Unit, Database|
|Front-end|Flask (including Jinja2) and HTML (including CSS and Bootstrap)|
|Version Control System (VCS)|Git|
|CI Server|Jenkins|
|Cloud server|GCP Compute Engine|

## Project Management <a name="project_management"></a>
This section will detail the project management tools and techniques used to plan the project, and how they were utilised and adapted throughout the project.

I implemented an Agile methodology over the Waterfall methodology due to Agile's values and principles allowing for testing to be completed in the same iteration as programming, dynamic project aims and working code over comprehensive documentation; again adapting best industry practices.

### Agile Methodology <a name="agile"></a>
Due to the nature of my project, some of the values and principles of Agile had to be adapted:
+ **Individuals and Interactions over processes and tools:**
The project was an individual project, so there was no need for team interactions such as daily scrums.
+ **Working Software over comprehensive documentation:**
The purpose of this project is to show my understanding of the content taught in the first five weeks.
So comprehensive documentation is important, however, I took adapted this value to mean that the application must be functional over beautiful.
+ **Customer Collaboration over contract negotiation:**
This project had no customer, other than users and the trainers at QA. So, I imagined virtual users and treated my trainer as a customer.
+ **Responding to Change over following a plan:**
Although I did not know at the start, the project objectives did not change throughout the five weeks, but my planning allowed for easy response to change.

### Kanban Board <a name="kanban_board"></a>
As stated for the MVP, I was required to follow best practices within industry and use a Kanban board to manage my project. I chose to use the Trello application to create my Kanban board, due to my familiarity with the software, having seen it used at QA.

The board is designed around user stories to test the CRUD functionalities of the application. These stories are then represented in the product backlog, along with other features needed for the specifics of the project (create this README file for example). These product backlogs are then further broken down in to a sprint backlog, tasks, progress, done and bugs list. These additional lists allow for dynamic progress updates of the project and to maintain specific obtainable objectives throughout the project to allow for a deliverable product by the deadline.

I defined "done" as to mean that the feature had been successfully implemented into the application, and had no negative effect on the pytest application which is detailed later.
Any implemented feature that negatively effected the performance of the application were logged into the bugs column.

##### Initial Plan <a name="first_kanban_board"></a>
![Initial Kanban board designed with Trello.](https://i.imgur.com/AsHnjOt.png)


#### Dynamic Updates <a name="kanban_board_changes"></a>
+ As the project proceeded, I stopped using the labels on the board to associate the products/sprints/tasks to one another.
+ I only focused on adding User Stories to the board
+ Bugs were reported and fixed as the project proceeded. No bugs by the end of the project.

##### Final Board <a name="final_kanban_board"></a>
![Final Kanban board designed with Trello.](https://i.imgur.com/fnV0YjI.png)



## Entity Relationship Diagrams (ERD) <a name="entity_relationship_diagrams"></a>
I used an ERD to help draft my database. I opted for the MoSCow Prioritisation Method, so that I could aim for a MVP without losing focus.

![ERD designed with draw.io](https://i.imgur.com/HLg5EdF.png)

As shown in my ERD, my priority was to have two tables Films and Actors, with a many-to-many relationship. This relationship would require a joining table to house the foreign keys which I called film_actor.
Time-permitted, I would expand on the Films table and create a new tables, Directors, which would have a one-to-many relationship with the Films table.

## Risk Assessment <a name="risk_assessment"></a>
The Risk Analysis categories are: Risk ID, Description, Likelihood, Impact, Consequence and Response Strategy.
The Risk Management categories are: Response Strategy.
Risk IDs 1.X are Operational Risks and 2.X are Objective Risks.

|Risk ID|Description|Likelihood (1 -> 10)|Impact (1->10)|Consequence|Response Strategy|
|---|---|---|---|---|---|
|1.1|Data compromised|4|8|Potential loss of large sections of the project, resulting in setbacks|Using the branch feature in git, and ensuring a frequently updated branch method|
|1.2|GCP (Google Cloud Processing) budget limit exceeded|1|1|Personal financial cost, whilst minimal setback to project progress|Google provides $300 initial budget for all users, and disables the autopayment if the allowance runs out. To prevent this from becoming a problem, I have to ensure that feature doesn't become enabled, and to keep an eye on my remaining budget.|
|1.3|Internet Connectivity Problems|7|9|A lot of the work for this project is done on virtual machines and requires a constant internet connection. Missing this would require large periods of time without being able to work on or update the project|There is some work that can be drafted offline before being pushed up to the cloud. If the problem seriously effects the work, then let the trainer know, such that it can be taken into consideration|
|2.1|Time mismanagement|5|8|Falling behind on tasks means rushing on certain aspects of the project and can result in a lower quality of work.|Using methods such as a Trello board and gantt chart to track my progress and ensure I don't fall behind on my work. If my work starts to fall behind, I can work on my project before/after training hours. |
|2.2|Lack of content knowledge|5|7|A lack of understanding of the content covered in the academy will mean that I am unable to fulfill requirements needed for the project|I will first search the internet fo the answers to any questions I have, then seek peer help if I cannot find the answer, before finally approaching my trainer|
|2.3|Jenkins pipeline error|3|3|A problem with Jenkins compatibility with the GitHub webhooks would mean that the pipeline would not automatically run for every push to GitHub, compromising the autonomy of the continuous integration|If not able to be resolved by the deadline, then manual build requests in Jenkins can be used.|


## Testing <a name="testing"></a>
I used both pytest and a coverage report to test my application

### Pytest <a name="pytest"></a>
Both pytest programs passed all the tests, showing that the features in the site were functioning as I expected.
![URL pytest](https://i.imgur.com/92ec1pg.png)

![DB pytest](https://i.imgur.com/d7pgoVT.png)

### Coverage Report <a name="coverage_report"></a>
The URL coverage report showed 43%.
![URL coverage report](https://i.imgur.com/qWGRYVc.png)
The Database (DB) coverage report showed %37. The aim was to have both coverage reports as close to 80% as possible.
![DB coverage report](https://i.imgur.com/SxhTjeq.png)

## Deployment <a name="deployment"></a>
Once I have edited my code in Visual Code, I push the changes up to my developer branch on GitHub. Once a feature has been completed, I merge the developer branch into the master branch which activates a GitHub webhook with my Jenkins CI server. Jenkins can then deploy the app as a service. With the use of the Pipeline, Jenkins is able to install all the necessary packages needed to run the application, wait for the packages to be installed, deploy the application as a service and finally perform the tests mentioned in the section above. The results of these tests are printed in the console output of Jenkis, giving the user the ability to improve the testing stage if results are not satisfactory.

![Deployment Architecture designed with Google Drawings](https://i.imgur.com/2f7vt4V.png)

### Feature Branch Model <a name="branch_merge"></a>
At the start of the project I had a single branch on my version control; the master branch.
Once I had a functioning application running on a server and could be accessed through port 5000, I used git checkout -b developer to create a new developer branch from which all changes would be made too before merging with the master branch after a task had been placed into "done" on my Kanban board.

## Front End Design <a name="front_end_design"></a>
As mentioned previously, the design aspect of the site was not of importance in this project.
Instead, my aim was to make the CRUD functionalities as easy as possible for the User.
My home page has a majority of the many to many CRUD functionalities and the Actors and Films pages are for single database manipulation.

Home Page
![Home page](https://i.imgur.com/Wgr7rVH.png)
Actors Page
![Actors page](https://i.imgur.com/5a0GnDL.png)
Films Page
![Films page](https://i.imgur.com/xWaYEZS.png)

## Improvements for the Future <a name="improvements_for_the_future"></a>
If I had more time dedicated to this project I would have implemented the following:
+ **A User/Developer log-in feature:**
This would have allowed for the Developer profiles to have have full access to the film and actors database, allowing them full CRUD functionalities.
The User profiles would have only been permitted to view the databases, and searched for which actors/films they would have wanted to see. Maybe even a request feature, so that they could suggests additions/updates/removals to the database.
+ **Increased Testing coverage:**
As shown previous in the coverage report section of the readme file, there was little coverage of the application, even though a lot of its core features where tested. This is definitely an area i would like to improve in later projects.
+ **Improved UI:**
Due to the nature of Agile, I prioritised working CRUD functionality over the documentation and presentation of the project. This meant I did not spend time on the design aspects of the site.
+ **Selenium Testing:**
My testing protocol only included unit and database testing. Had more time been allowed, I would have researched and implemented further methods of testing.
+ **More Complex Tables and Relationships:**
My project uses a many-to-many relationship between two tables. However, given more time, I would have prioritised including new tables such as directors, which would have shown much greater understanding of the material covered.
Also included would have been more columns in the tables, genres for example, which would have allowed for more features on the the application.
+ **More CRUD Functionalities:**
Although, I included a diverse amount of CRUD functionalities in my project, there were more to be tested. An update many to many relationship for example, or a multi-select drop down list instead of either text boxes or single-select dropdown lists. 
+ **Complex Version Control Branch Model:**
I only used two branches in my project; a master branch and developer branch. To help prepare better for best practice in industry, I would have further branches underneath the developer branch for each product backlog then further branches for the sprint backlogs and then again for the tasks.


## Authors <a name="authors"></a>
Thomas Cole - QA Academy Trainee

## Acknowledgements <a name="acknowledgements"></a>
I would like to acknowledge the QA trainers and other members of my cohort, who were able to help me with any problems I had with my project.