
ANSWER INCOMPLETE!!

### Prompt
##### Describe, in exacting detail, the algorithm to give exact change. Only assume basic arithmetic functions like addition and subtraction, but be sure to describe how to figure out what notes and coins to give back. Write this down in a new markdown file with the file extension .md (don't worry about formatting) in a Week 2 directory in your homework repo and commit/push it.

To clearly describe such algorithm, first we should define the occasion in question. When is exact change required? Whenever someone buying a product tries to pay with a currency unit that is higher than the price of the item.   

In such interaction, the key pieces of information are the price of the item for sale, the amount of customer payment, and the surplus amount to be returned to the customer after the sale is finished. Since these details will represent the same piece of information, but they will change for every sale, it'd be useful to turn this information into **variables** for the proposed algorithm. For example:

List of variables:
* price = the cost of the purchased product or item.
* payment = the amount of money paid by customer.
* change = the amount left after paying for the item.

<br/>

Now that I've assessed the type of information needed to solve the question, I should decide which are the **actions** or **transformations** required to process the info from the variables and return a correct answer every time I run the algorithm.

An appropriate algorithm should be able to:
1. gather the required values for the variables price and payment.
2. assign the corresponding value to each known variable
3. compare the variables to determine whether exact change is required or not
4. if exact change is needed, determine the exact amount of surplus money (the exact change) from the payment
5. return the exact change amount every time  

For action #1 and #2 we'd need some kind of input form or dataset from which to gather the values needed for the variables **payment** and **price**. The first part of the algorithm would request the values for the two variables, where: 

price = item cost  

payment = customer's money for the item

Action #3 depends on having the correct amounts assigned to the known variables. Here, the algorithm must ensure sure that the given amounts meet the criteria of a situation where exact change is required by comparing both amounts. If **payment** is greater than **price**, then exact change is required and the algorithm can proceed to the next stage to determine the value of **change**.

For actions #4 and #5, given that **payment** is always greater than **price**, I'd just have to substract price from payment to get the amount of the exact change.


#### Summary

Given variables **payment** and **price**, determine the value of **change** as needed. If **payment** > **price**, then **payment** - **price** = **change**





