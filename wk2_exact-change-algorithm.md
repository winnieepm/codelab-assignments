### Describe, in exacting detail, the algorithm to give exact change. Only assume basic arithmetic functions like addition and subtraction, but be sure to describe how to figure out what notes and coins to give back. Write this down in a new markdown file with the file extension .md (don't worry about formatting) in a Week 2 directory in your homework repo and commit/push it.

To clearly describe such algorithm, first we should define the occasion in question. When is exact change required? Whenever someone buying a product tries to pay with a currency unit that is higher than the price of the item.   

In such interaction, the most important pieces of information are the price of the item for sale, the amount of customer payment, and the surplus amount to be returned to the customer after the sale is finished. Since these details will represent the same piece of information, but they will change for every sale, it'd be useful to turn this information into _variables_ for the algorithm. For example:

* price. the cost of the purchased product or item.
* payment. the amount of money paid by customer. *It is important to note that this number will always be higher than that of the item's price, because otherwise there would be no need to give back any money to the customer.
* change. the amount left after paying for the item.

*variables: price, payment, change*  


Now that I've assessed the type of information needed to solve the question, I should decide which are the _actions_ or _transformations_ required to process the info from the variables and return a correct answer every time I run the algorithm.

An appropriate algorithm should be able to:
1. use or take the information from the provided variables 
2. determine the exact amount of surplus money (the exact change) from the payment
3. return the exact change amount

