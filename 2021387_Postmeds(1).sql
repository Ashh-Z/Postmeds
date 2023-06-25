Select Product_id, Product_name from product where Product_id  IN
(Select Product_id from belongs_to where Category_id='21' and Product_id NOT IN
(SELECT Product_id from product where Product_name='Amoxicillin' or Product_name='Paracetamol'));





SELECT product_id, SUM(product_quantity) AS Quant
FROM orders
GROUP BY product_id
ORDER BY Quant  DESC
LIMIT 5;




update product p
set p.product_price=product_price + 20 
where p.product_name = 'Eyedrops';




SELECT O.Order_id, U.Customer_name AS "Customer Ordered", O.Order_Delivery_Address, S.Partner_id
FROM orders O NATURAL JOIN Delivery_Partner S INNER JOIN USER U ON U.customer_id=O.Order_id
WHERE S.Partner_username="Orpha Altenwerth";



UPDATE Belongs_To
SET Category_id = 21
WHERE Belongs_To.ProductID = 53;




SELECT AVG(Cart_value) AS AverageOrderVal FROM cart;


select count(product_id), category_id
from belongs_to
group by category_id;


delete from coupons where coupons.Coupon_expiry < CURRENT_DATE;



insert into rates(Customer_id, Product_id) values (6,13);


SELECT P.Product_name, P.Product_price
FROM PRODUCT P
JOIN belongs_to B ON P.Product_id = B.Product_id
WHERE B.Category_id = '66';



SELECT SUM(O.Order_price)
FROM orders O, delivery D where O.order_id in
(Select D.Order_id where D.Partner_id = '10' and Customer_id is NOT NULL);



SELECT o.order_id, user.customer_id, dp.Partner_username
FROM Orders o, user
CROSS JOIN delivery_partner dp;