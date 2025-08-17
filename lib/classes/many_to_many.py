class Article:
    all = [] # Class variable to store all Article instances

    def __init__(self, author, magazine, title):
        if not (5 <= len(title) <= 50): # Validate title length
            raise ValueError("Title must be between 5 and 50 characters long.")

        self.author = author
        self.magazine = magazine
        self._title = title
        Article.all.append(self) # Store all instances in a class variable(Article.all)

    @property # make author read-only(immutable getter)
    def title(self):
        return self._title
    
    @title.setter # make title read-only (immutable setter)
    def title(self, value):
        raise ValueError("Title cannot be changed directly.")


class Author:
    def __init__(self, name):
        if not isinstance(name, str): #if name is not a string, raise TypeError
            raise TypeError("Name must be a string")
        self._name = name 

    # make name immutable (read-only property)
    @property # make name read-only (immutable getter)
    def name(self):
        return self._name

    @name.setter # make name immutable (read-only setter)
    def name(self, value):
        raise AttributeError("Name cannot be changed once set.")

    def articles(self):
        #Return all Article instances by this author
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        #Return all unique magazines this author has written for
        return list({article.magazine for article in self.articles()})

    def add_article(self, magazine, title):
        #Create a new article for this author and return it
        return Article(self, magazine, title)

    def topic_areas(self):
        areas = {magazine.category for magazine in self.magazines()} # Get unique categories of magazines
        return list(areas) if areas else None # return unique categories as a list or None if no magazines


class Magazine:
    def __init__(self, name, category):
        self._name = None # none initially
        self._category = None # none initially

        # use setters for validation
        self.name = name
        self.category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Magazine name must be a string")
        if not (2 <= len(value) <= 16):
            raise ValueError("Magazine name must be between 2 and 16 characters")
        self._name = value

    
    @property 
    def category(self):
        return self._category

    @category.setter #setter used for validation
    def category(self, value):
        if not isinstance(value, str):
            raise TypeError("Category must be a string")
        if len(value) < 1: 
            raise ValueError("Category must have length greater than 0")
        self._category = value


    def articles(self):
        #all Article instances that reference this magazine
        return [article for article in Article.all if article.magazine is self]

    def contributors(self):
        #all unique Authors who wrote for this magazine
        authors = [article.author for article in self.articles()]
        return list(set(authors)) if authors else None

    def article_titles(self):
        #titles of all articles for this magazine
        titles = [article.title for article in self.articles()]
        return titles if titles else None

    def contributing_authors(self):

        authors = {}
        for article in self.articles():
            authors[article.author] = authors.get(article.author, 0) + 1 # count occurrences
        # Return authors with more than 2 articles
        result = [author for author, count in authors.items() if count > 2]
        return result if result else None