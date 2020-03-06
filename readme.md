Designed as a basic back-end software for use in a store like environment all we had to do was make a system that could add remove, and edit items but I was having a lot of fun so I added a shopping cart and a bunch of extra features. The original project couldn't save changes so I added a .txt file to store the changes. I've also added some things like if you checkout before you quit it says Thank you but if you quit before checking out it shows the checkout.

Project Files:

ims.py 

stock.txt

There are other unrelated python project files as well in the folder "Other ICS3U Files".
<br>
<br>
What it does:
1. Opens the text file with the current items and stock of each item
2. Loads this information into dictionaries
3. Allows the user to add an item, remove an item, edit the specifics of an item, list all the items, look up an item, purchase an item, checkout or remove an item from the cart.
4. All purchased items go into the cart and the cost is totalled on checkout.
5. Saves all the changes by writing them to the text file.
