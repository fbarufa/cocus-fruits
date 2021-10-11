#!/usr/bin/python3
# harvest.py
# Fabiano Barufaldi - barufa@gmail.com - 2021-10-10.
# Cocus challenge #2 - Farmers collecting and cleaning fruits

from threading import Thread
import random
import time
from os import system

# Initialize global variables
fruits_on_tree = 50
fruits_on_dirty_basket = 0
fruits_on_clean_basket = 0
num_of_farmers = 3
num_of_cleaners = 3
dict_farmers = dict()   # control # of fruits on farmers hands
dict_cleaners = dict()  # control # of fruits on cleaners hands

# collecting task
# pick fruit from tree
# farmer has fruit in his/her hands
# put fruit in the dirty basket


def farming(farmer):

    global fruits_on_tree
    global fruits_on_dirty_basket
    global dict_farmers

    while(fruits_on_tree > 0):

        # fruit goes from tree to farmer hand
        fruits_on_tree -= 1
        dict_farmers.update({farmer: dict_farmers[farmer]+1})

        time.sleep(random.randint(3, 6))         # 3-6 secs to process

        # fruit goes from farmer hand to dirty basket
        dict_farmers.update({farmer: dict_farmers[farmer]-1})
        fruits_on_dirty_basket += 1     # put it in the dirty basket


# cleaning task
# pick fruit from dirty basket
# cleaner has fruit in his/her hands
# put fruit in the clean basket


def cleaning(cleaner):

    global fruits_on_dirty_basket
    global fruits_on_clean_basket
    global dict_cleaners

    while (fruits_on_tree > 0 or fruits_on_dirty_basket > 0):

        if (fruits_on_dirty_basket > 0):

            # fruit goes from dirty basket to cleaner hands
            fruits_on_dirty_basket -= 1
            dict_cleaners.update({cleaner: dict_cleaners[cleaner]+1})

            time.sleep(random.randint(2, 4))         # 2-4 secs to process

            # fruit goes from cleaner hands to clean basket
            dict_cleaners.update({cleaner: dict_cleaners[cleaner]-1})
            fruits_on_clean_basket += 1     # put in the clean basket


def print_log():

    while (fruits_on_tree > 0 or
           fruits_on_dirty_basket > 0 or
           sum(dict_farmers.values()) > 0 or
           sum(dict_cleaners.values()) > 0):

        time.sleep(1)     # 1 sec between prints

        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
              "Tree (" + str(fruits_on_tree) + ") fruits,",
              "Dirty Basket (" + str(fruits_on_dirty_basket) + ") - ",
              "Clean Basket (" + str(fruits_on_clean_basket) + ") - ",
              ["farmer" + str(x) + ' (' + str(dict_farmers[x]) +
               ')' for x in dict_farmers.keys()],
              ["cleaner" + str(x) + ' (' + str(dict_cleaners[x]) +
               ')' for x in dict_cleaners.keys()],
              "Total --> " + str(fruits_on_tree + fruits_on_dirty_basket +
                                 fruits_on_clean_basket +
                                 sum(dict_farmers.values()) +
                                 sum(dict_cleaners.values())),
              "\n"
              )


def main():

    # add farming workers to the pool
    for farmer in range(num_of_farmers):
        dict_farmers.update({farmer+1: 0})    # init the farmers dict
        t1 = Thread(target=farming, args=(farmer+1,))
        t1.start()

    # adding cleaning workers to the pool
    for cleaner in range(num_of_cleaners):
        dict_cleaners.update({cleaner+1: 0})  # init the cleaners dict
        t2 = Thread(target=cleaning, args=(cleaner+1,))
        t2.start()

    # logger task
    t3 = Thread(target=print_log)
    t3.start()


if __name__ == '__main__':

    system('cls||clear')

    main()
