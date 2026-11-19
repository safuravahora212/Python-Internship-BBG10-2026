library={101:{"title":"java","author":"jane","copies":3},
          102:{ "title":"python","author":"john","copies":5},
          103:{"title":"data science","author":"r.patel","copies":3}
        }

book_id=102
library[book_id]["copies"]-=1 
print(library)