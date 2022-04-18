---
layout: default
course_number: CS335
title: Code Snippets - Create Table
---

Create Table

```sql
create table employee (
    Id int (6) not null auto_increment,
    Name varchar(30) not null,
    EID varchar(7) not null,
    Password varchar(5),
    Salary int(10),
    SSN varchar(10),
    Primary Key (Id)
    );  
  ```
