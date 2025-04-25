/* DESCRIPTION:
You will be given a table numbers, with one column number.
Return a dataset with two columns: number and is_even, where number contains the original 
input value, and is_even containing "Even" or "Odd" depending on number column values. */

SELECT 
    number,
    CASE 
        WHEN number % 2 = 0 THEN 'Even' 
        ELSE 'Odd' 
        END as is_even
FROM
    numbers