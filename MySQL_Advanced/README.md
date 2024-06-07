*For this project, we expect you to look at this concept:*

- [Advanced SQL](https://intranet.atlasschool.com/concepts/877)

## Resources

**Read or watch**:

- [MySQL cheatsheet](https://intranet.atlasschool.com/rltoken/XCHG-pgtifYRSw8ILB6DEw)
- [MySQL Performance: How To Leverage MySQL Database Indexing](https://intranet.atlasschool.com/rltoken/VXAPISdkpKg3YD3HmVQXlw)
- [Stored Procedure](https://intranet.atlasschool.com/rltoken/C37E-NvP8KxpI5Ds5w1oAQ)
- [Triggers](https://intranet.atlasschool.com/rltoken/0xFZu5AK0imLk70dxxcODA)
- [Views](https://intranet.atlasschool.com/rltoken/Q8butAms3BthfCFhXuQSPA)
- [Functions and Operators](https://intranet.atlasschool.com/rltoken/0ezATipRSpz1K8MixrD2Rg)
- [Trigger Syntax and Examples](https://intranet.atlasschool.com/rltoken/rc8oho9n7LAjtffC584tgA)
- [CREATE TABLE Statement](https://intranet.atlasschool.com/rltoken/F1SUJgWz-4YNNYLPkL9tPw)
- [CREATE PROCEDURE and CREATE FUNCTION Statements](https://intranet.atlasschool.com/rltoken/XhYdXik2tTMK2k81WxulpA)
- [CREATE INDEX Statement](https://intranet.atlasschool.com/rltoken/K90KZ3z4gL5mPpHROlEOcg)
- [CREATE VIEW Statement](https://intranet.atlasschool.com/rltoken/VJESVxV2V7jGqrR-50903A)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.atlasschool.com/rltoken/j63kEGfU7eLokEipk6jQCA), **without the help of Google**:

### General

- How to create tables with constraints
- How to optimize queries by adding indexes
- What is and how to implement stored procedures and functions in MySQL
- What is and how to implement views in MySQL
- What is and how to implement triggers in MySQL

## How to create tables with constraints?

Creating tables with constraints in SQL is crucial for maintaining data integrity and ensuring that the data stored in your database follows certain rules. Here's a basic guide to creating tables with constraints:

1. **CREATE TABLE Statement**: Begin by using the `CREATE TABLE` statement to define the structure of your table. Here's a basic syntax:
    
    ```sql
    CREATE TABLE table_name (
        column1 datatype constraint,
        column2 datatype constraint,
        ...
    );
    ```
    
2. **Primary Key Constraint**: A primary key constraint ensures that each record in a table is uniquely identifiable. Typically, it's a column or a combination of columns with unique values. Here's how to define a primary key constraint:
    
    ```sql
    CREATE TABLE table_name (
        column1 datatype,
        column2 datatype,
        PRIMARY KEY (column1)
    );
    ```
    
3. **Foreign Key Constraint**: A foreign key constraint establishes a relationship between two tables. It ensures that the values in a column (or columns) in one table match the values in another table's primary key or unique constraint. Here's how to define a foreign key constraint:
    
    ```sql
    CREATE TABLE table_name1 (
        column1 datatype PRIMARY KEY
    );
    
    CREATE TABLE table_name2 (
        column2 datatype,
        column3 datatype,
        FOREIGN KEY (column2) REFERENCES table_name1(column1)
    );
    ```
    
4. **Unique Constraint**: A unique constraint ensures that all values in a column (or columns) are unique. Unlike the primary key constraint, a table can have multiple unique constraints. Here's how to define a unique constraint:
    
    ```sql
    CREATE TABLE table_name (
        column1 datatype,
        column2 datatype,
        UNIQUE (column1)
    );
    ```
    
    ## How to optimize queries by adding indexes?
    
    Optimizing queries by adding indexes is a common technique in database optimization. Indexes help speed up query performance by allowing the database engine to quickly locate rows in a table. Here's how you can optimize queries by adding indexes:
    
    1. **Identify Slow Queries**: Before adding indexes, it's essential to identify the slow queries that need optimization. You can use database monitoring tools or analyze query execution plans to identify the queries that are taking the most time to execute.
    2. **Understand Query Patterns**: Understand the typical query patterns your application or system generates. Look for frequently executed queries or queries involving large data sets.
    3. **Choose Columns for Indexing**: Identify the columns involved in the WHERE, JOIN, ORDER BY, and GROUP BY clauses of your queries. These columns are good candidates for indexing.
    4. **Primary Key and Unique Constraints**: By default, most databases automatically create indexes on primary key columns and columns with unique constraints. If you haven't already, ensure that primary key and unique constraint columns are indexed.
    5. **Foreign Key Columns**: Columns that are frequently used in JOIN operations, especially foreign key columns, benefit from indexing.

## How to implement stored procedures and functions in MySQL

### **What is a Stored Procedure?**

A stored procedure is a precompiled collection of SQL statements stored in the database. It can accept input parameters, perform operations, and return results.

### **How to Implement a Stored Procedure**

To create a stored procedure in MySQL, you can use the `CREATE PROCEDURE` statement. Here's a basic syntax:

```sql
CREATE PROCEDURE procedure_name ([parameters])
BEGIN
    -- SQL statements
END;
```

## **Functions**

### **What is a Function?**

A function in MySQL is similar to a stored procedure but typically returns a single value. It can also accept input parameters and perform calculations or operations.

### How to implement a function

To create a function in MySQL, you can use the `CREATE FUNCTION` statement. Here's a basic syntax:

```sql
CREATE FUNCTION function_name ([parameters])
RETURNS return_datatype
BEGIN
    -- SQL statements
    RETURN value;
END;
```

## What/How to implement views in SQL

### What is a View?

A view in MySQL is a virtual table that does not store data itself but is defined by a SELECT query. When you query a view, MySQL executes the underlying SELECT statement and returns the result set as if you were querying a regular table.

### How to Implement a View:

To create a view in MySQL, you can use the `CREATE VIEW` statement. Here's a basic syntax:

```sql
CREATE VIEW view_name AS
SELECT column1, column2, ...
FROM table_name
WHERE condition;
```

### Example:

Let's create a view that displays employee information along with their department:

```sql
CREATE VIEW employee_department AS
SELECT e.emp_id, e.emp_name, e.salary, d.department_name
FROM employees e
JOIN departments d ON e.department_id = d.department_id
```

### Using Views:

Once you've created a view, you can query it like a regular table. For example:

```sql
SELECT * FROM employee_department;
```

## What/How to implement triggers in SQL

### What is a Trigger?

A trigger in MySQL is a set of SQL statements that are associated with a table and are automatically executed when certain events occur on that table. These events can include INSERT, UPDATE, DELETE, or even specific column-level changes.

### How to Implement a Trigger:

To create a trigger in MySQL, you use the `CREATE TRIGGER` statement. Here's a basic syntax:

```sql
CREATE TRIGGER trigger_name
    {BEFORE | AFTER} {INSERT | UPDATE | DELETE}
    ON table_name
    FOR EACH ROW
    BEGIN
        -- SQL statements
    END;
```

### Example:

Let's create a trigger that automatically updates a last modified timestamp column whenever a row in the `employees` table is updated:

```sql
CREATE TRIGGER update_last_modified
    BEFORE UPDATE
    ON employees
    FOR EACH ROW
    BEGIN
        SET NEW.last_modified = NOW();
    END;
```

### Types of Triggers:

MySQL supports two main types of triggers:

1. **BEFORE Triggers**: These triggers are fired before the triggering event (INSERT, UPDATE, DELETE) occurs. They can be used to modify data before it is inserted, updated, or deleted.
2. **AFTER Triggers**: These triggers are fired after the triggering event has occurred. They are often used for logging changes, enforcing constraints, or triggering additional actions.

### Trigger Events:

Triggers can be associated with one or more of the following events:

- **INSERT**: Triggered when a new row is inserted into the table.
- **UPDATE**: Triggered when an existing row is updated.
- **DELETE**: Triggered when a row is deleted from the table.

### Dropping Triggers:

To drop a trigger, you use the `DROP TRIGGER` statement:

```sql
DROP TRIGGER trigger_name;
```
