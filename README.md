## **Ella Jones - Term 2, Assessment 2 - API Web Server**
### **Contents**
[Set-Up Instructions](/README.md#set-up-instructions)

[R1 - Identification of Problem](/README.md#r1---identification-of-the-problem-you-are-trying-to-solve-by-building-this-particular-app)

[R2 - Why Problem needs solving](/README.md#r2---why-is-it-a-problem-that-needs-solving)

[R3 - Database System](/README.md#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others)

[R4 - ORMs](/README.md#r4---identify-and-discuss-the-key-functionalities-and-benefits-of-an-orm)

[R5 - Endpoints of API](/README.md#r5---document-all-endpoints-of-your-api)

[R6 - ERD of app](/README.md#r6---an-erd-for-your-app)

[R7 - Third Party Services](/README.md#r7---detail-any-third-party-services-that-your-app-will-use)

[R8 - Relationships Between Project Models](/README.md#r8---describe-your-project-models-in-terms-of-the-relationship-they-have-with-each-other)

[R9 - Database Relations](/README.md#r9---discuss-the-database-relations-to-be-implemented-in-your-application)

[R10 - Task Allocation & Tracking](/README.md#r10---describe-the-way-tasks-are-allocated-and-tracked-in-your-project)

[References](/README.md#references)

### Set Up Instructions
Clone or download the repository from Github.

GitHub link: https://github.com/ella-jones/EllaJones_T2A2.git

Ensure that Python 3 and PostgreSQL are installed. 

Open the command line/terminal and run the following PostgreSQL command:
>psql

Create the database: 
>CREATE DATABASE dog_rescue_db;

Connect to the database: 
> \c dog_rescue_db

Create a user and set a password: 
> CREATE USER dog_rescue_dev WITH PASSWORD ‘123456’;

Grant the user all privileges: 
> GRANT ALL PRIVILEGES ON DATABASE dog_rescue_db TO dog_rescue_dev;

Open another command line/terminal and run the following commands:

Cd into the src folder inside the project folder and create/activate the virtual environment:
> python3 -m venv .venv
> source .venv/bin/activate

Install dependencies: 
> pip install -r requirements.txt

In the /src folder, rename the .envexample file to .env and set the database connection and JWT secret key.

Create and seed the database:
> flask db create
“flask db seed”

Run the application: 
> flask run

You should be able to use the application in your browser with the URL prefix http://localhost:8080/, or through setup with Insomnia or Postman (localhost:8080). Please refer to [R5 - Endpoints](/README.md#r5---document-all-endpoints-of-your-api)

### R1 - Identification of the problem you are trying to solve by building this particular app.
The problem that this API is trying to solve is the lack of easily accessible and up-to-date information about dogs available for adoption from a dog rescue. Many potential adopters are interested in finding a dog, but they often struggle to find reliable and comprehensive information about dogs that are currently available for adoption. This can lead to frustration, wasted time, and missed opportunities for both potential adopters and the rescue.

By building this API, I aim to centralise and streamline the process of finding information about dogs available for adoption. The API will serve as a single access point for developers and applications to retrieve comprehensive data about adoptable dogs, including their descriptions, breeds, ages, and any other relevant data or specific adoption requirements. This way, potential adopters, developers, and other interested parties can easily retrieve up-to-date information about dogs needing a loving home.

The API’s purpose is to bridge the gap between adopters and dog rescues, making it easier for people to find and connect with the right dog for adoption, ultimately increasing the chances of successful adoptions and finding loving homes for as many dogs as possible.

### R2 - Why is it a problem that needs solving?
This problem needs solving for several reasons:

#### Increasing Adoption Rates
By making it easier for potential adopters to find and learn about dogs, we can increase the chances of these dogs finding loving homes. Many people interested in adopting a dog may not be aware of all the options or may find the process overwhelming. By providing a user-friendly API, we can simplify the search process and connect more potential adopters with suitable dogs.

#### Time and Effort Efficiency
Searching for a dog to adopt can be time-consuming and challenging. Potential adopters often need to visit multiple adoption agency websites or physically visit shelters to gather information. This process can be discouraging and may deter some individuals from considering adoption altogether. By centralising the information in an API, potential adopters can access comprehensive data about available dogs from various sources in one place, saving time and effort.

#### Transparency and Accessibility
An API that provides detailed information about adoptable dogs promotes transparency and accessibility. It allows potential adopters to make informed decisions by providing accurate and up-to-date data on each dog. This transparency builds trust between the adoption agency and the adopters, ensuring that they have a clear understanding of the dog’s background and requirements before making a commitment.

#### Promoting Animal Welfare
By facilitating the adoption process and making it more accessible, the API can contribute to reducing the number of dogs in shelters. Shelters often struggle with limited resources and overcrowding, leading to the euthanasia of healthy, adoptable dogs. By efficiently connecting potential adopters with available dogs, we can alleviate the burden on shelters and increase the chances of these dogs finding permanent homes, thereby improving their overall welfare.

### R3 - Why have you chosen this database system? What are the drawbacks compared to others?
I have chosen to work with a **PostgreSQL** database system for this project. PostgreSQL is “an object-relational DBMS where user-defined objects and table approaches are combined to build more complex data structures.” (AltexSoft 2023).

I have chosen PostgreSQL as it is considered favourable over other database systems in the following areas:

#### Feature-Rich and Extensible
PostgreSQL offers various advanced features, including support for complex data types, indexing methods, custom functions, and procedural languages. Its extensibility allows users to create custom data types and functions, making it highly adaptable to unique application needs. (Ostezer & Drake 2022)

#### ACID Compliance
PostgreSQL ensures data integrity and reliability by adhering to the ACID (Atomicity, Consistency, Isolation, Durability) properties, making it suitable for applications requiring transactional consistency. (AltexSoft 2023).

#### Cost-Effective Licensing
PostgreSQL is an open-source DBMS released under the PostgreSQL License, making it free to use and distribute without any licensing costs. This can be particularly appealing for organisations seeking to minimise expenses. This would be more ideal than a commercial DBMS such as Oracle Database or Microsoft SQL Server, which can require significant licensing costs. (Dhruv 2019)

#### Strong Performance
PostgreSQL’s query optimiser and indexing mechanisms contribute to its high-performance capabilities. It can efficiently handle complex queries and large datasets. This is more suitable than a DBMS like MySQL, which can struggle with complex transactions and analytical queries. (Ostezer & Drake 2022)

While PostgreSQL has numerous advantages, it is also important to have an understanding of the **drawbacks** of the DBMS:

#### Complexity
While PostgreSQL’s extensibility is a strength, it can also increase complexity for database administrators and developers. (Dhruv 2019)

#### Learning Curve
PostgreSQL may have a steeper learning curve compared to some other DBMSs, especially for users familiar with simpler systems. (AltexSoft 2023).

#### Performance Scaling
In certain scenarios with extremely high concurrent read/write operations, PostgreSQL might face challenges in scaling compared to NoSQL databases like Cassandra or Mongo DB. (AltexSoft 2023).

#### Replication Complexity
While PostgreSQL offers replication capabilities, setting up and managing replication configurations can be complex compared to some dedicated distributed databases (Ostezer & Drake 2022).

PostgreSQL’s selection as a database management system is often motivated by its extensibility, ACID properties, Licencing costs, and strong performance. However, it is essential to also recognise that other database systems, such as MySQL, Oracle Database, Microsoft SQL Server, MongoDB, etc., also have their strengths and may be better suited for certain scenarios. For this particular project, I came to the conclusion that PostgreSQL was the best database management system to use.


### **R4 -  Identify and discuss the key functionalities and benefits of an ORM.**
Object Relational Mapping (ORM) is a software technique that facilitates the interaction between object-oriented programming languages and relational databases. It acts as a bridge between the application’s object model and the underlying database structure, offering several functionalities and benefits. (Abba I.V. 2022)

#### **KEY FUNCTIONALITIES OF ORM**

#### Object-Oriented Abstraction
ORM allows developers to work with database entities as objects in their programming language, abstracting away the complexities of database tables, queries, and joins. This object-oriented approach enhances code readability, reusability, and maintainability (Awati 2023)

#### Data Persistence & Query Generation
ORM frameworks handle data persistence, ensuring that objects’ states are synchronised with the corresponding database records. They also automatically generate SQL queries based on the object-oriented queries provided by developers. This eliminates the need for manual SQL statements, reducing development time and potential errors (Awati 2023).

#### Relationship Mapping
ORM establishes associations between objects and their relationships in the database, such as one-to-one, one-to-many, or many-to-many relationships. This simplifies data retrieval and management, promoting efficient data modelling (Awati 2023).

#### Transaction Management
ORM frameworks support transaction management, allowing developers to execute multiple database operations as a single unit of work. Transactions ensure data integrity and consistency during complex operations (Abba I.V. 2022)

#### **BENEFITS OF ORM**

#### Improved Productivity
By abstracting away low-level database interactions, ORM enables developers to focus on business logic and application development. This results in increased productivity and faster application deployment (Schaeferle 2012).

#### Database Independence 
ORM allows applications to switch between different database systems without significant code changes, promoting database independence and flexibility (Hoyos 2018)

#### Security and Parameterisation
ORM frameworks employ parameterised queries, preventing SQL injection attacks and enhancing application security (Hoyos 2018).

#### Code Reusability
ORM promotes code reusability by encapsulating database access logic in a central location. This simplifies maintenance and reduces code duplication across different modules of the application (Schaeferle 2012).

#### Testing and Mocking
ORM facilitates unit testing by providing mock objects for database interactions. This enables developers to test application logic without relying on an actual database, leading to more efficient testing practices (Schaeferle 2012).

### **R5 -  Document all endpoints of your API.**
My endpoints are documented below in the following format:

Route:"/"
* Method:
* @decorator
* Description
* User required to be logged in:
* is_employee required:
* Local host URL: 
* JSON Body
* Example of expected response
* Validation for route:
* Error handling for route:

Local host URL will be in the format localhost:8080/ - this can be entered directly into a browser as http://localhost:8080/ 

Actions which require the user to be an employee are marked by ‘is_employee required’. An employee's bearer token is required to be entered for authorisation.

Actions which require the user to be logged in are marked by ‘User required to be logged in’. A bearer token is required to be entered for authorisation.

/int:id – Enter the integer id value (e.g. for User with id: 1 | int:id = 1)

### Auth (URL prefix = "/auth")

#### Route: "/register"
* Method: POST
* auth_bp.route('/register', methods=['POST'])
* Description: Create a new user. "is_employee" field not required to be inputed and defaults to "false" unless specified.
* User required to be logged in: No.
* is_employee required: No
* Local host URL: localhost:8080/auth/register
* JSON Body:
```JSON
{
    "full_name": "User 2",
    "email": "user2@email.com",
    "password": "user2pw"
}
```
* Expected response (returns the user that was just registered):
```JSON
{
    "is_employee": false,
    "id": 3,
    "adoptions": [],
    "full_name": "User 2",
    "email": "user2@email.com"
}
```
* Error Handling / Validation for route:
* If a user attemps to register with an email that has already been used, they will receive the following Unique Violation error message:
```JSON
{
    "error": "Email address already in use"
}
```
* If a user does not enter one of the required fields, they will receive the following NOT Nul Violation error message: (the field will be specified in the message. For this example, the missing field was "email".)
```JSON
{
    "error": "The email is required"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

#### Route: "/login"
* Method: POST
* auth_bp.route('/login', methods=['POST'])
* Desctiption: User login. Requires "email" and "password".
* User required to be logged in: N/A (this route will log the user in)
* Is_employee required: No
* Local Host URL: localhost:8080/auth/login
* JSON body (example):
```Json
{
    "email": "user1@email.com",
    "password": "user1pw"
}
```
* Expected response returns the user’s email address, employee status, and encrypted password token (JWT):
```JSON
{
    "email": "user1@email.com",
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJmcmVzaCI6ZmFsc2UsImlhdCI6MTY5MDYxNjk5MCwianRpIjoiNWYyYTgzYzUtNzhlNS00Y2JkLTgyYTMtNGFjYTM4ZDg3YTBhIiwidHlwZSI6ImFjY2VzcyIsInN1YiI6IjIiLCJuYmYiOjE2OTA2MTY5OTAsImV4cCI6MTY5MDcwMzM5MH0.CAr_JaDqGQ44a4Bk2bwEox5SHLdZvTmudrdN9b8mFT0",
    "is_employee": false
}
```
* If user enters an invalid email address, the following error message will be returned to the user:
```JSON
{
    "error": "Invalid email or password"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

### Dogs (URL prefix = "/dogs")

#### Route "/"
* Method: GET
* @dogs_bp.route('/')
* Description: Returns a list of all dogs.
* User required to be logged in: No
* is_employee required: No
* Local host URL: localhost:8080/dogs
* JSON body: None
* Example expected response:
```JSON
[
    {
        "id": 1,
        "name": "Dog 1",
        "age": "3 and a half",
        "breed": {
            "breed_name": "Labrador"
        },
        "gender": "Female",
        "description": "Dog 1 desc",
        "adoption": {
            "id": 1,
            "adopter": {
                "email": "user1@email.com",
                "full_name": "John Smith"
            },
            "adoption_date": "2023-08-01",
            "notes": "Adoption 1 notes",
            "dog_id": 1,
            "adopter_id": 2
        },
        "breed_id": 1
    },
    {
        "id": 2,
        "name": "Dog 2",
        "age": "5",
        "breed": {
            "breed_name": "Boston Terrier"
        },
        "gender": "Male",
        "description": "Dog 2 desc",
        "adoption": {
            "id": 2,
            "adopter": {
                "email": "user1@email.com",
                "full_name": "John Smith"
            },
            "adoption_date": "2023-08-01",
            "notes": "Adoption 2 notes",
            "dog_id": 2,
            "adopter_id": 2
        },
        "breed_id": 2
    },
    {
        "id": 3,
        "name": "Dog 3",
        "age": "1",
        "breed": {
            "breed_name": "Labrador"
        },
        "gender": "Male",
        "description": "Dog 3 desc",
        "adoption": null,
        "breed_id": 1
    },
    {
        "id": 4,
        "name": "Dog 4",
        "age": "4",
        "breed": {
            "breed_name": "Golden Retriever"
        },
        "gender": "Female",
        "description": "Dog 4 desc",
        "adoption": null,
        "breed_id": 3
    },
    {
        "id": 5,
        "name": "Test Dog",
        "age": "4",
        "breed": {
            "breed_name": "Golden Retriever"
        },
        "gender": "Female",
        "description": "Test Dog desc",
        "adoption": null,
        "breed_id": 3
    }
]
```
* Error Handling / Validation: N/A

#### Route: "/< int:id >"
* Method: GET
* @dogs_bp.route('/< int:id >')
* Description: Return a dog specified by id.
* User required to be logged in: No
* Is_employee required: No
* Local Host URL: localhost:8080/dogs/< int:id >
* JSON Body: None
* Example expected response when searching for dog with id: 1, localhost8080/dogs/1:
```JSON
{
    "id": 1,
    "name": "Dog 1",
    "age": "3 and a half",
    "breed": {
        "breed_name": "Labrador"
    },
    "gender": "Female",
    "description": "Dog 1 desc",
    "adoption": {
        "id": 1,
        "adopter": {
            "email": "user1@email.com",
            "full_name": "John Smith"
        },
        "adoption_date": "2023-08-01",
        "notes": "Adoption 1 notes",
        "dog_id": 1,
        "adopter_id": 2
    },
    "breed_id": 1
}
```
* Error Handling / Validation:
* If the user specifies an id for which a dog does not exist, the following error message will be returned to the user:
```JSON
{
    "error": "Dog not found with id 10"
}
```

Route "/"
* Method: POST
* @dogs_bp.route('/', method=['POST'])
* Description: Creates a dog record
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/dogs
* JSON Body:
```JSON
{
    "name": "Test Dog",
    "age": "4",
    "breed_id": 3,
    "gender": "Female",
    "description": "Test Dog desc"
}
```
* Example expected response - this will be the same as the JSON Body input, plus additional fields of and assigned “id”, "breed" (nested field), and "adoption" (nested field).
```JSON
{
    "id": 5,
    "name": "Test Dog",
    "age": "4",
    "breed": {
        "breed_name": "Golden Retriever"
    },
    "gender": "Female",
    "description": "Test Dog desc",
    "adoption": null,
    "breed_id": 3
}
```
* Errorhandling:
* If the user enters a "breed_id" that does not exist, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_id": [
            "No breed with that id exists"
        ]
    }
}
```
* If the user does not enter one of the required fields, the following Not Null Violation error message will be returned to the user (the missing field will be specified in the message. In the following case, the missing field was "breed_id"):
```JSON
{
    "error": "The breed_id is required"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: DELETE
* @dogs_bp.route('/< int:id >', methods=['DELETE'])
* Description: Deletes a dog record with specified id.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/dogs/< int:id >
* JSON Body: None
* Example expected response when deleting dog with id: 5, localhost8080/dogs/5: - The dog's name that was just deleted will be displayed in the message. In the below exampe, Test Dog was the name of the dog with id 5.
```JSON
{
    "message": "Dog: Test Dog deleted successfully"
}
```
* Errorhandling / Validation:
* If the user enters an id into the route for which a dog does not exist, the following error message will be thrown:
```JSON
{
    "error": "Dog not found with id 10"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: PUT or PATCH (uses the PATCH method, however, will work with both PUT and PATCH)
* @dogs_bp.route('/< int:id >', methods=['PUT', 'PATCH'])
* Description: Updates an existing dog record.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/dogs/< int:id >
* JSON Body - in the following example, only the age and description of the dog are being updated:
```JSON
{
    "age": "4",
    "description": "Test Dog desc update"
}
```
* Example expected response when updating dog with id: 4, localhost8080/dogs/4: - this will be the same as the JSON Body input, plus additional fields of and assigned “id”, "breed" (nested field), and "adoption" (nested field).
```JSON
{
    "id": 4,
    "name": "Dog 4",
    "age": "4",
    "breed": {
        "breed_name": "Golden Retriever"
    },
    "gender": "Female",
    "description": "Test Dog desc update",
    "adoption": null,
    "breed_id": 3
}
```
* Errorhandling:
* If the user enters a "breed_id" that does not exist, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_id": [
            "No breed with that id exists"
        ]
    }
}
```
* Any other errors will be caught by a general error handler which will display the error message.

### Breeds (URL prefix = "/breeds")

#### Route "/"
* Method: GET
* @breeds_bp.route('/')
* Description: Returns a list of all breeds.
* User required to be logged in: No
* is_employee required: No
* Local host URL: localhost:8080/breeds
* JSON body: None
* Example expected response:
```JSON
[
    {
        "id": 1,
        "breed_name": "Labrador",
        "dogs": [
            {
                "id": 1,
                "name": "Dog 1",
                "age": "3 and a half",
                "gender": "Female",
                "description": "Dog 1 desc",
                "adoption": {
                    "id": 1,
                    "adopter": {
                        "email": "user1@email.com",
                        "full_name": "John Smith"
                    },
                    "adoption_date": "2023-08-01",
                    "notes": "Adoption 1 notes",
                    "dog_id": 1,
                    "adopter_id": 2
                },
                "breed_id": 1
            },
            {
                "id": 3,
                "name": "Dog 3",
                "age": "1",
                "gender": "Male",
                "description": "Dog 3 desc",
                "adoption": null,
                "breed_id": 1
            }
        ]
    },
    {
        "id": 2,
        "breed_name": "Boston Terrier",
        "dogs": [
            {
                "id": 2,
                "name": "Dog 2",
                "age": "5",
                "gender": "Male",
                "description": "Dog 2 desc",
                "adoption": {
                    "id": 2,
                    "adopter": {
                        "email": "user1@email.com",
                        "full_name": "John Smith"
                    },
                    "adoption_date": "2023-08-01",
                    "notes": "Adoption 2 notes",
                    "dog_id": 2,
                    "adopter_id": 2
                },
                "breed_id": 2
            }
        ]
    },
    {
        "id": 3,
        "breed_name": "Golden Retriever",
        "dogs": [
            {
                "id": 4,
                "name": "Dog 4",
                "age": "4",
                "gender": "Female",
                "description": "Test Dog desc update",
                "adoption": null,
                "breed_id": 3
            }
        ]
    },
    {
        "id": 4,
        "breed_name": "German Shepard",
        "dogs": []
    },
    {
        "id": 5,
        "breed_name": "Pug",
        "dogs": []
    }
]
```
* Error Handling / Validation: N/A

#### Route: "/< int:id >"
* Method: GET
* @breeds_bp.route('/< int:id >')
* Description: Return a breed specified by id.
* User required to be logged in: No
* Is_employee required: No
* Local Host URL: localhost:8080/breeds/< int:id >
* JSON Body: None
* Example expected response when searching for breed with id: 1, localhost8080/breeds/1:
```JSON
{
    "id": 1,
    "breed_name": "Labrador",
    "dogs": [
        {
            "id": 1,
            "name": "Dog 1",
            "age": "3 and a half",
            "gender": "Female",
            "description": "Dog 1 desc",
            "adoption": {
                "id": 1,
                "adopter": {
                    "email": "user1@email.com",
                    "full_name": "John Smith"
                },
                "adoption_date": "2023-08-01",
                "notes": "Adoption 1 notes",
                "dog_id": 1,
                "adopter_id": 2
            },
            "breed_id": 1
        },
        {
            "id": 3,
            "name": "Dog 3",
            "age": "1",
            "gender": "Male",
            "description": "Dog 3 desc",
            "adoption": null,
            "breed_id": 1
        }
    ]
}
```
* Error Handling / Validation:
* If the user specifies an id for which a breed does not exist, the following error message will be returned to the user:
```JSON
{
    "error": "Breed not found with id 10"
}
```

Route "/"
* Method: POST
* @breeds_bp.route('/', method=['POST'])
* Description: Creates a breed record
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/breeds
* JSON Body:
```JSON
{
    "breed_name": "New"
}
```
* Example expected response - this will be the same as the JSON Body input, plus the additional fields of an assigned “id” and any dogs associated with the breed.
```JSON
{
    "id": 6,
    "breed_name": "New",
    "dogs": []
}
```
* Errorhandling:
* If the user enters a "breed_name" with less than two characters, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_name": [
            "Name must be at least 2 characters long"
        ]
    }
}
```
* If the user enters a "breed_name" with any special characters, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_name": [
            "Only letters, spaces and numbers are allowed"
        ]
    }
}
```
* If the user does not enter the required field of "breed_name", the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_name": [
            "Missing data for required field."
        ]
    }
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: DELETE
* @breeds_bp.route('/< int:id >', methods=['DELETE'])
* Description: Deletes a breed record with specified id.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/breeds/< int:id >
* JSON Body: None
* Example expected response when deleting breed with id: 5, localhost8080/breeds/5: - The breed's name that was just deleted will be displayed in the message. In the below exampe, Pug was the name of the dog with id 5.
```JSON
{
    "message": "Breed: Pug deleted successfully"
}
```
* Errorhandling / Validation:
* If the user enters an id into the route for which a breed does not exist, the following error message will be thrown:
```JSON
{
    "error": "Breed not found with id 10"
}
```
* If a user attempts to delete a breed that contains dogs, the following error message will be returned:
```JSON
{
    "error": "Cannot delete breed with id 1 as it has dogs associated."
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: PUT or PATCH (uses the PATCH method, however, will work with both PUT and PATCH)
* @breeds_bp.route('/< int:id >', methods=['PUT', 'PATCH'])
* Description: Updates an existing breed record.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/breeds/< int:id >
* JSON Body
```JSON
{
    "breed_name": "Updated Name"
}
```
* Example expected response when updating dog with id: 4, localhost8080/breeds/4: - this will be the same as the JSON Body input, plus additional fields of and assigned “id”, and "dogs" (nested field - list).
```JSON
{
    "id": 4,
    "breed_name": "Updated Name",
    "dogs": []
}
```
* Errorhandling:
* If the user enters a "breed_name" with less than two characters, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_name": [
            "Name must be at least 2 characters long"
        ]
    }
}
```
* If the user enters a "breed_name" with any special characters, the following error message will be returned to the user:
```JSON
{
    "error": {
        "breed_name": [
            "Only letters, spaces and numbers are allowed"
        ]
    }
}
```
* If the user enters an id into the route for which a breed does not exist, the following error message will be thrown:
```JSON
{
    "error": "Breed not found with id 10"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

### Adoptions (URL prefix = "/adoptions")

#### Route "/"
* Method: GET
* @adoptions_bp.route('/')
* Description: Returns a list of all adoptions.
* User required to be logged in: No
* is_employee required: No
* Local host URL: localhost:8080/adoptions
* JSON body: None
* Example expected response:
```JSON
[
    {
        "id": 1,
        "dog": {
            "name": "Dog 1"
        },
        "adopter": {
            "email": "user1@email.com",
            "full_name": "John Smith"
        },
        "adoption_date": "2023-08-01",
        "notes": "Adoption 1 notes",
        "dog_id": 1,
        "adopter_id": 2
    },
    {
        "id": 2,
        "dog": {
            "name": "Dog 2"
        },
        "adopter": {
            "email": "user1@email.com",
            "full_name": "John Smith"
        },
        "adoption_date": "2023-08-01",
        "notes": "Adoption 2 notes",
        "dog_id": 2,
        "adopter_id": 2
    }
]
```
* Error Handling / Validation: N/A

#### Route: "/< int:id >"
* Method: GET
* @adoptions_bp.route('/< int:id >')
* Description: Return an adoption specified by id.
* User required to be logged in: No
* Is_employee required: No
* Local Host URL: localhost:8080/adoptions/< int:id >
* JSON Body: None
* Example expected response when searching for adoption with id: 1, localhost8080/adoptions/1:
```JSON
{
    "id": 1,
    "dog": {
        "name": "Dog 1"
    },
    "adopter": {
        "email": "user1@email.com",
        "full_name": "John Smith"
    },
    "adoption_date": "2023-08-01",
    "notes": "Adoption 1 notes",
    "dog_id": 1,
    "adopter_id": 2
}
```
* Error Handling / Validation:
* If the user specifies an id for which an adoption does not exist, the following error message will be returned to the user:
```JSON
{
    "error": "Adoption not found with id 10"
}
```

Route "/"
* Method: POST
* @adoptions_bp.route('/', method=['POST'])
* Description: Creates an adoption record
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/adoptions
* JSON Body - the "date" field is not required as the date will automatically default to the date the adoption record was created:
```JSON
{
    "dog_id": 3,
    "adopter_id": 1,
    "notes": "Test notes"
}
```
* Example expected response - this will be the same as the JSON Body input, plus the additional fields of an assigned “id”, "date" (defaults to current date), and both the dog and adopters information (both as nested fields).
```JSON
{
    "id": 3,
    "dog": {
        "name": "Dog 3"
    },
    "adopter": {
        "email": "employee1@email.com",
        "full_name": "Jane Doe"
    },
    "adoption_date": "2023-08-01",
    "notes": "Test notes",
    "dog_id": 3,
    "adopter_id": 1
}
```
* Errorhandling:
* If the user enters a "dog_id" that does not exist, the following error message will be returned to the user:
```JSON
{
    "error": {
        "dog_id": [
            "No dog with that id exists"
        ]
    }
}
```
* If the user enters an "adopter_id" that does not exist, the following error message will be returned to the user:
```JSON
{
    "error": {
        "adopter_id": [
            "No user with that id exists"
        ]
    }
}
```
* If the user does not enter one of the required fields, the following error message will be returned to the user (the field that is missing will be stated in the message - in the below example, "dog_id" was the missing field):
```JSON
{
    "error": "The dog_id is required"
}
```
* If the user attemps to create an adoption record for a dog that has already been adopted, the following error message will be returned to the user:
```JSON
{
    "error": "An adoption record for that dog already exists"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: DELETE
* @adoptions_bp.route('/< int:id >', methods=['DELETE'])
* Description: Deletes an adoption record with specified id.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/adoptions/< int:id >
* JSON Body: None
* Example expected response when deleting adoption with id: 2, localhost8080/adoptions/2: - The adoption's id that was just deleted will be displayed in the message.
```JSON
{
    "message": "Adoption with 2 was deleted successfully"
}
```
* Errorhandling / Validation:
* If the user enters an id into the route for which an adoption does not exist, the following error message will be thrown:
```JSON
{
    "error": "Adoption not found with id 10"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

Route "/< int:id >"
* Method: PUT or PATCH (uses the PATCH method, however, will work with both PUT and PATCH)
* @adoptions.route('/< int:id >', methods=['PUT', 'PATCH'])
* Description: Updates an existing adoption record.
* User required to be logged in: Yes
* Is_employee required: yes
* Local Host URL: localhost:8080/adoptions/< int:id >
* JSON Body
```JSON
{
    "notes": "Adoption 1 updated"
}
```
* Example expected response when updating adoption with id: 1, localhost8080/adoptions/1:
```JSON
{
    "id": 1,
    "dog": {
        "name": "Dog 1"
    },
    "adopter": {
        "email": "user1@email.com",
        "full_name": "John Smith"
    },
    "adoption_date": "2023-08-01",
    "notes": "Adoption 1 updated",
    "dog_id": 1,
    "adopter_id": 2
}
```
* Errorhandling:
* If the user enters an id into the route for which an adoption does not exist, the following error message will be thrown:
```JSON
{
    "error": "Adoption not found with id 10"
}
```
* Any other errors will be caught by a general error handler which will display the error message.

R6 -  An ERD for your app.**
![ERD for Dog Adoption API](./docs/Dog_Adoption.png)

*Futher explanation of this ERD can be found here: [R9 - Database Relations](/README.md#r9---discuss-the-database-relations-to-be-implemented-in-your-application)*

### **R7 -  Detail any third party services that your app will use.**
#### PostgreSQL
PostgreSQL was used as the database management system for this project. For further information on PostgreSQL, view [R3](/README.md#r3---why-have-you-chosen-this-database-system-what-are-the-drawbacks-compared-to-others).

#### Flask
My RESTful API was built using Flask, a lightweight Python web framework known for its simplicity, flexibility, and ease of use. It enables developers to build web applications and APIs by providing essential features like routing, templating, and handling HTTP requests. Although referred to as a “micro-framework,” it allows easy extension through third-party libraries. Flask’s straightforward nature and versatility have made it a popular choice for building small to medium-sized web projects (Python Tutorial 2021).

Below is a description of all third-party packages that I have used to build this project. The “requirements.txt” file contains all of the dependencies and required packages needed for the app to run.

#### SQLAlchemy
SQLAlchemy is a Python ORM library that simplifies database interactions by mapping Python classes to database tables. It supports various database engines, provides a high-level Query API, and abstracts away database-specific complexities. SQLAlchemy’s popularity stems from its ability to make database operations more Pythonic, intuitive, and efficient, making it a popular choice for developing Python applications with database integration (Krebs 2017).

In my app, it is used with Flask-SQLAlchemy, an extension that combines the SQLAlchemy ORM with Flask web applications. I have used this to map defined models (User, Breed, Dog, Adoption) to tables on the database (PostgreSQL). By using SQLAlchemy, no SQL queries were required are needed to communicate with the database.

#### Marshmallow
Marshmallow (Flask-Marshmallow) is a Flask library for object serialisation and deserialization. It simplifies data validation, conversion, and handling using defined schemas. Marshmallow ensures data integrity for APIs, supporting custom rules and relationships. With its powerful features, it streamlines data processing and enhances the efficiency of Flask applications. In my application, Marshmallow allows Python code to be converted to JSON format and vice versa seamlessly, which was the main purpose of Marshmallow in my application (Mwaura 2021).

#### Psycopg2
Psycopg2 is a mature Python library used to connect to PostgreSQL databases. It enables developers to execute SQL queries, handle data retrieval, and manage transactions efficiently. With support for parameterised queries, it enhances security and performance (Pipi n.d.)

I have used Psycopg2 in my app in order to connect to the PostgreSQL database, and perform CRUD (Create, Read, Update, Delete) operations by executing SQL commands, such as SELECT, INSERT, UPDATE, and DELETE, and retrieving the results.

#### Bcrypt
Bcrypt is a secure password-hashing function commonly used in web applications to protect user passwords. It employs adaptive work factors, salting, and slow hashing to enhance security against brute-force attacks. The fixed-length output makes It suitable for storing password hashes in databases. The package I used to access this function in my Flask app was Flask-Bcrypt (Grigutyté 2023).

In my application, I used Flask-Bcrypt in order to hash and store user passwords when an account is created or a password is updated by a user. When a user then logs into the app, their password is compared to the stored hashed password and then verified if they match (or not verified if they do not match). This helps to secure the user’s information as their password is directly associated with their User record.

#### JSON Web Tokens (JWT)
JSON Web Tokens are a secure and compact way to represent information as a JSON object for data exchange between parties, through the use of a digital signature, using a secret or public/private key pair. They consist of a header, payload, and signature, containing claims about the user and additional data. The signature ensures data integrity, and JWTs are commonly used in web applications and APIs for secure authentication and data sharing between services (JWT n.d.)

In my application, I used JWT-Flask-Extended as a flask extension to provide integration between Flask and JWT. JWTs have been used in my app for authentication and authorisation. Once a user logs in via the “/auth/login” route, a JWT token is created for the user (this will expire after 1 day). This token will then be entered as a bearer token for routes that require authorisation. This ensures that only authorised users (employees) are able to perform certain actions, such as DELETE, PATCH, PUT, and POST.

#### Dotenv
Dotenv (Python-Dotenv) is a Python library that simplifies the management of environment variables by loading them from a “.env” file into the application’s environment during runtime. It provides a secure and organised way to store sensitive information and configuration settings separately from the code. Developers can easily access these variables as regular environment variables within their Python applications. This approach ensures better security and compatibility with various Python frameworks (Brown 2023).

In my application, Python-Dotenv is utilised together with Flask’s config object, which facilitates the management of application-wide configuration variables. The config object allows developers to define default values for configuration variables and enables loading values from environment variables or configuration files like .env. 

#### Postman
I used **Postman** throughout the project to test the functionality of my API endpoints.
![Postman Screenshot](./docs/postman.png)


### **R8 -  Describe your project models in terms of the relationship they have with each other.**
The models in my app are User, Breed, Dog, and Adoption (all can be found in their respective file within the “/src/models” folder). These models were implemented using SQLAlchemy ORM for handling database operations. Each class inherits from db.Model, where db = SQLAlchemy from flask_sqlalchemy, and which is a base class for all models in SQLAlchemy.

#### User model (user.py):
Represents a user in the system. A User may have employee permissions, which allows for the full functionality of a regular user with additional permissions (e.g. creating, updating and deleting dogs).

```Python
class User(db.Model):
    __tablename__= 'users'

    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    email = db.Column(db.String, nullable=False, unique=True)
    password = db.Column(db.String, nullable=False)
    is_employee = db.Column(db.Boolean, default=False)

    adoptions = db.relationship('Adoption', back_populates='adopter')
```

* **```__tablename__```**: Sets the name of the table in the database to “users”, which will be mapped to the model.

* **```“id = db.Column(db.Integer, primary_key=True)”```**: Creates a primary key column titled ‘id’, with auto-incrementing integer values. This value is not to be set by the user but instead looked after by SQLAlchemy.

* The remaining attribute fields ("full_name", "email", "password", "is_employee") are established, with their data type (e.g. String, Boolean, etc.) and character limit. Mandatory fields are noted by the "nullable=" clause and fields which are required to be unique (not already existing) are noted with Boolean clause “unique=”.

* The “is_employee” attribute is not mandatory and will revert to false if not included upon creation. “is_employee is used to determine if a user is authorised for certain routes (see endpoints for more information on this).

#### User Model Relationships
* One to many relationship between a User and Adoptions
* One to many relationship between a User and Dogs

#### Dog model (dog.py):
Represents a dog in the system. 

```Python
class Dog(db.Model):
    __tablename__ = "dogs"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable = False)
    age = db.Column(db.String)
    breed_id = db.Column(db.Integer, db.ForeignKey('breeds.id'), nullable = False)
    gender = db.Column(db.String)
    description = db.Column(db.Text)

    breed = db.relationship('Breed', back_populates='dogs')
    adoption = db.relationship('Adoption', back_populates='dog', uselist=False)
```
* **```__tablename__```**: Sets the name of the table in the database to "dogs", which will be mapped to the model.

* **```“id = db.Column(db.Integer, primary_key=True)”```**: Creates a primary key column titled ‘id’, with auto-incrementing integer values. This value is not to be set by the user but instead looked after by SQLAlchemy.

* The remaining attribute fields ("name", "age", "breed_id", "gender" & "description") are established, with their data type (e.g. String, Boolean, etc.) and character limit. Mandatory fields are noted by the "nullable=" clause.

* "breed_id" is a foreign key which relates to the id column on the breeds table.

* "breed" is a relationship (db.relationship) that establishes a one-to-many relationship between the Dog model and the Breed model, as a "breed" (singular) back_populates to "dogs" (multiple).

* "adoption" is a relationship (db.relationship) that establishes a one-to-one relationship between the Dog model and the Adoption model, as an "adoption"(singular) back_populates to a "dog" (singular).

#### Dog Model Relationships
* One-to-many relationship between a Breed and Dogs
* One-to-one relationship between a Dog and Adoption

#### Breed model (breed.py):
Represents a breed in the system. 

```Python
class Breed(db.Model):
    __tablename__ = "breeds"

    id = db.Column(db.Integer, primary_key=True)
    breed_name = db.Column(db.String(100), nullable=False)

    dogs = db.relationship ('Dog', back_populates='breed', cascade='all, delete')
```
* **```__tablename__```**: Sets the name of the table in the database to "breeds", which will be mapped to the model.

* **```“id = db.Column(db.Integer, primary_key=True)”```**: Creates a primary key column titled ‘id’, with auto-incrementing integer values. This value is not to be set by the user but instead looked after by SQLAlchemy.

* "breed_name" is established, with its data type (String) and character limit(100). This field is mandatory and is therefore noted by the "nullable=False" clause.

* "dogs" is a relationship (db.relationship) that establishes a one-to-many relationship between the Breed model and the Dog model, as "dogs" (multiple) back_populates to a "breed" (singular). The cascade parameter ensures that when a parent record is deleted, all related child records are deleted as well.

#### Breed Model Relationships
* One-to-many relationship between a Breed and Dogs

#### Adoption model (dog.py):
Represents an adoption in the system. 

```Python
class Adoption(db.Model):
    __tablename__ = 'adoptions'

    id = db.Column(db.Integer, primary_key=True)
    dog_id = db.Column(db.Integer, db.ForeignKey('dogs.id'), nullable=False, unique=True)
    adopter_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    adoption_date = db.Column(db.Date, default=date.today()) # date record is created
    notes = db.Column(db.Text)

    adopter = db.relationship('User', back_populates='adoptions')
    dog = db.relationship('Dog', back_populates='adoption')
```
* **```__tablename__```**: Sets the name of the table in the database to "adoptions", which will be mapped to the model.

* **```“id = db.Column(db.Integer, primary_key=True)”```**: Creates a primary key column titled ‘id’, with auto-incrementing integer values. This value is not to be set by the user but instead looked after by SQLAlchemy.

* The remaining attribute fields ("dog_id", "adopter_id", "adoption_date" & "notes") are established, with their data type (e.g. String, Boolean, Date, Text etc.). Mandatory fields are noted by the "nullable=" clause and fields which are required to be unique (not already existing) are noted with Boolean clause “unique=”.

* The "adoption_date" field will default to today's data, as this is the date that the adoption record was created.

* "dog_id" is a foreign key which relates to the id column on the dogs table.

* "adopter_id" is a foreign key which relates to the id column on the users table.

* "adopter" is a relationship (db.relationship) that establishes a one-to-many relationship between the User model and the Adoption model, as an "adopter" (singular) back_populates to "adoptions" (multiple).

* "dog" is a relationship (db.relationship) that establishes a one-to-one relationship between the Dog model and the Adoption model, as a "dog"(singular) back_populates to an "adoption" (singular).

#### Adoption Model Relationships
* One-to-many relationship between a User (adopter) and Adoptions
* One-to-one relationship between a Dog and Adoption

### **R9 -  Discuss the database relations to be implemented in your application.**

#### **ENTITIES & RELATIONSHIPS**
For further clarification on the below information, please view my [ERD in R6](/README.md#r6---an-erd-for-your-app).
#### Users
The Users table stores the information of users who wish to view information about dogs available for adoption and employees who will post, update, and delete this information. The Users table has a primary key of id, which is an integer value. Other attributes include; full_name, email (used for user identification), password (used for user authentication) and is_employee (holds a boolean value regarding whether the user is an employee or not). 

#### Users Relationships
As demonstrated by my ERD in R6, Users can have zero to multiple adoptions, however, adoptions can have one and only one adopter (user), creating a one-to-many relationship. The relationship between users and dogs is not direct but through a join-table of “Adoptions”. Users can adopt zero to multiple dogs, however, dogs can only be adopted by one and only one adopter (user), therefore creating a one-to-many relationship through the join-table of “Adoptions”.

#### Dogs
The Dogs table is used to store the information of dogs who are currently available for adoption, as well as dogs who have already been adopted. The Dogs table has a primary key of id, which is an integer value. Other attributes include; name, age, breed_id (a foreign key that links directly to the Breeds table), gender, and description.

#### Dogs Relationships
Dogs can have one and only one breed, whereas a breed can contain zero to multiple dogs, therefore creating a one-to-many relationship between breeds and dogs. Dogs can only be adopted once (or never), and an adoption can contain one and only one dog, therefore creating a one-to-one relationship between dogs and adoptions. The relationship between dogs and users is not direct, but rather through a join-table of “Adoptions”. A dog can be adopted by only one (or none) users, however, a user can adopt zero to multiple dogs, therefore creating a one-to-many relationship between dogs and users.

#### Breeds
The Breeds table is used to store the information about the breeds that are available for adoption at the dog rescue. The Breeds table has a primary key of id, which is an integer value. The only other attribute is the breed_name, which is not nullable as it specifies the name of the breed. 

#### Breeds Relationships
Breeds can contain zero to multiple dogs, whereas a dog can have one and only one breed, therefore creating a one-to-many relationship between dogs and breeds. The relationship between breeds and adoptions is not direct, but rather through a join-table of “Dogs”. As breeds can have zero to multiple dogs, they can therefore have zero to multiple adoptions within them, however, an adoption can contain one and only one dog and can therefore contain one and only one breed, therefore creating a one-to-many relationship between breeds and adoptions through the join-table of “Dogs”

#### Adoptions
The Adoptions table is used to store the information about the adoptions that have taken place at the dog rescue. The Adoptions table has a primary key of id, which is an integer value. Other attributes include dog_id (which is a foreign key that links directly to the Dogs table), adopter_id (which is a foreign key that links directly to the users table), adoption_date (which contains the date the adoption record was created on), and notes. 

#### Adoptions Relationships
An adoption can contain one and only one dog, and dogs can only be adopted once (or never), therefore creating a one-to-one relationship between adoptions and dogs. Adoptions can contain one and only one adopter (user), whereas a user can have zero to multiple adoptions, therefore creating a one-to-many relationship between adoptions and users. The adoptions table does not have a direct relationship to the Breeds table, however, the two are linked through the join table of “Dogs”. As an Adoption can contain one and only one dog, it can therefore contain one and only one breed, whereas a breed can contain zero to multiple dogs and can therefore contain zero to multiple adoptions, therefore creating a one-to-many relationship between Adoptions and Breeds.

#### Relationships (Re-stated & Simplified)
* *Users & Adoptions:* one-to-many (a user can have zero to many adoptions, however, an adoption can have one and only one user)

* *Users & Dogs* (linked through join-table “Adoptions”: one-to-many (a user can adopt zero to many dogs, however, a dog can only be adopted by one or no users).

* *Adoptions & Dogs:* one-to-one (an Adoption can contain one and only one dog, and a dog can be adopted once or never).

* *Breeds & Dogs*: one-to-many (a breed can contain zero to many dogs, however, a dog can have one and only one breed).

* *Adoptions & Breeds* (linked through join-table “Dogs”): one-to-many (an adoption can contain one and only one breed, and a breed can have zero to many adoptions).

### **R10 -  Describe the way tasks are allocated and tracked in your project.**
For this project, I allocated and tracked tasks through the use of a Trello board.

Link to Trello board: https://trello.com/b/kXGtFIMK/dog-adoption-api

I created each feature as a seperate card in the "To Do"" section. When I began working on a feature, I moved the card to the "In Progess" section on the board. When I begin review on that feature, I moved it to the "Review" section, and when the card was complete I moved it to the "Done" section.
See screenshot below:

![Trello Board Overview](./docs/trello_board.png)

In each of the cards, I included a checklist for tasks to complete within each feature and a due date for the completion. See screenshot example below. To view each individual card, please visit my Trello board (linked above).

![Trello Board - Individual Card](./docs/trello_card.png)

### **References**
Abba I.V. 2022, What is an ORM – The meaning of Object Relational Mapping database tools, Free Code Camp, viewed 23 July 2023, https://www.freecodecamp.org/news/what-is-an-orm-the-meaning-of-object-relational-mapping-database-tools/.

AltexSoft 2023, Comparing Database Management Systems: MySQL, PostgreSQL, MSSQL Server, MongoDB, Elasticsearch, and others, AltexSoft, viewed 23 July 2023, https://www.altexsoft.com/blog/business/comparing-database-management-systems-mysql-postgresql-mssql-server-mongodb-elasticsearch-and-others/. 

Awati, R 2023, Object-Relational Mapping, TechTarget, viewed 23 July 2023, https://www.theserverside.com/definition/object-relational-mapping-ORM. 

Brown, O 2023, How to use Dotenv and why you need it in all your projects, Medium, viewed 24 July 2023, https://javascript.plainenglish.io/how-to-use-dotenv-and-why-you-need-it-in-all-your-projects-a7319e16124a. 

Dhruv, S 2019, PostgreSQL advantages and disadvantages, Aalpha, viewed 23 July 2023, https://www.aalpha.net/blog/pros-and-cons-of-using-postgresql-for-application-development/. 

Grigutyté, M 2023, What is bcrypt and how does it work?, NordVNP, viewed 24 July 2023, https://nordvpn.com/blog/what-is-bcrypt/. 

Hoyos, M 2018, What is an ORM and why you should use it, Medium, viewed 23 July 2023, https://blog.bitsrc.io/what-is-an-orm-and-why-you-should-use-it-b2b6f75f5e2a. 

JWT n.d., Introduction to JSON Web Tokens, JWT, viewed 24 July 2023, https://jwt.io/introduction. 

Krebs, B 2017, SQLAlchemy ORM tutorial for Python developers, Auth 0 Blog, viewed 24 July 2023, https://auth0.com/blog/sqlalchemy-orm-tutorial-for-python-developers/. 

Mwaura, W 2021, Object validation and conversion with Marshmallow in Python, CircleCI Blog, viewed 24 July 2023, https://circleci.com/blog/object-validation-and-conversion-with-marshamallow/#:~:text=structure%20to%20another.-,Marshmallow%20is%20a%20Python%20library%20that%20converts%20complex%20data%20types,floats%2C%20sets%2C%20and%20arrays.. 

Ostezer & Drake, M 2022, SQLite vs MySQL vs PostgreSQL: A comparison of Relational Database Management Systems, Digital Ocean, viewed 23 July 2023, https://www.digitalocean.com/community/tutorials/sqlite-vs-mysql-vs-postgresql-a-comparison-of-relational-database-management-systems. 

Pipi n.d., Psycogp2 2.9.6, Pipi, viewed 24 July 2023, https://pypi.org/project/psycopg2/. 

Python Tutorial 2021, What is Flask Python, Python Tutorial, viewed 24 July 2023, https://pythonbasics.org/what-is-flask-python/. 

Schaeferle, M 2012, 4 benefits of Object-Relational Mapping (ORM), Learn Now Online, viewed 23 July 2023, https://www.learnnowonline.com/blogs/2012/08/28/4-benefits-of-object-relational-mapping-orm. 

