-- SQL script that creates a trigger that decreases the quantity of an item
-- after adding a new order
CREATE TRIGGER Buy
AFTER SELECT
ON quantity
FOR EACH ROW
set quantity = quantity-1;
