#Start:add the list 
library = []
wish = []

#Step1:BOOKS from library
own_book = input ("Enter the name of a book you own: ")
library. append (own_book)

another_own_book = input ("Enter the name of a book you own: (Or press Enter to skip): ")
if another_own_book :
    library . append (another_own_book)

print ("\nYour library list:" , library ,"\n" )

#Step2:BOOKS from wish 
wish_book_1 = input ("Enter the name of a book you wish to have in the future: ")
wish. append (wish_book_1) 

another_wish = input ("Enter the name of another book you wish to have: (Or press Enter to skip) ")
if another_wish :
    wish. append (another_wish)

print ("\nYour wish list:", wish ,"\n")

#Step3:acquired and donate
acquired = input ("Enter the name of a book from your wishlist that you've acquired: (Or press Enter to skip) ")
if acquired in wish :
    wish. remove (acquired)

print ("\nUpdate library:", library )
print ("Update wishlist:", wish ,"\n")

donate = input ("Enter the name of a book from your library you wish to donate: (Or press Enter to skip) ")
if donate in library :
    library. remove (donate)
print ("Final library after Donation:", library )
