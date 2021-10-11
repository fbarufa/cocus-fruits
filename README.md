
## harvest.py
Fabiano Barufaldi (barufa@gmail.com)

Cocus challenge #2 - Farmers collecting and cleaning fruits

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)


#### Definition

In this exercise we will be testing your multithreading skills.
Suppose that you want to simulate a fruit farm:

1. Three farmers are collecting fruits from a single tree to a single dirty fruit basket.
2. In parallel, three other farmers are getting the fruits from the dirty fruit basket,
cleaning them, and pushing them into the single cleaned fruit basket.
3. All the farmers are managing the fruit individually
4. The tree has 50 fruits (and only one farmer at one time can pick fruit from the tree)
5. Time to collect fruits from the trees into the basket: random(3,6) seconds
6. Time to clean the fruits into the cleaned fruit basket: random(2,4) seconds
7. The simulation ends when all the fruits from the tree are collected and cleaned.
8. The number of fruits in the tree and in the baskets must be logged every second.

#### Expected deliverable
Your code should be executable with the following call “yourScript.py”, with a similar output log to the one below:

- 2020-12-01 19:02:00 Tree (50 fruits) - dirty basket ( 0 ) - Clean Basket ( 0 ) – farmer1 (0) – farmer2 (0) – cleaner1(0) – cleaner2 (0)
- 2020-12-01 19:03:00 Tree (45 fruits) - dirty basket ( 3 ) - Clean Basket ( 1 ) – farmer1 (1) – farmer2 (0) – cleaner1(0) – cleaner2 (0)
- 2020-12-01 19:10:00 Tree (0 fruits) - dirty basket ( 0 ) - Clean Basket ( 50 ) – farmer1 (0) – farmer2 (0) – cleaner1(0) – cleaner2 (0)

### Running
```
python3 -m pip install -r requirements.txt
python3 harvest.py
```
