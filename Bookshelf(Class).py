class Bookshelf:
    def __init__(self,name,author,price,publishing_year):
        self.citizin_name=name
        self.citizin_author=author
        self.citizin_price=price
        self.citizin_publishing_year=publishing_year
        
    def addbook(self):
        print("Name: "+self.citizin_name)
        print("Author: "+self.citizin_author)
        print("Price: "+self.citizin_price)
        print("Publishing Year: "+str(self.citizin_publishing_year))
        print("Book Added")
    
    def year_since_published(self):
        years_ago_publish=2022-self.citizin_publishing_year
        print("The book was published "+years_ago_publish+" ago.")
        
book1=Bookshelf("Harry Potter and the Philospher's stone","J.K. Rowling","R$ 57.13","1997")
book1.addbook()
book1.year_since_published()

book2=Bookshelf("Harry Potter and the Order of Pheonix","J.K. Rowling","R$ 295.51","2007")
        
book2.addbook()
book2.year_since_published()