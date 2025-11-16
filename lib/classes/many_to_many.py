class Article:
    all = []
    
    def __init__(self, author, magazine, title):
        self._author = author
        self._magazine = magazine
        self._title = title
        Article.all.append(self)
    
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        # Title is immutable - don't change it
        pass  # or simply return without doing anything
    
    @property
    def author(self):
        return self._author
    
    @author.setter 
    def author(self, value):
        self._author = value
    
    @property
    def magazine(self):
        return self._magazine
    
    @magazine.setter
    def magazine(self, value):
        self._magazine = value

class Author:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        # Name is immutable - don't change it
        pass  # or simply return without doing anything
    
    def articles(self):
        return [article for article in Article.all if article.author == self]
    
    def magazines(self):
        return list(set([article.magazine for article in self.articles()]))
    
    def add_article(self, magazine, title):
        return Article(self, magazine, title)
    
    def topic_areas(self):
        magazine_categories = list(set([article.magazine.category for article in self.articles()]))
        return magazine_categories if magazine_categories else None

class Magazine:
    all = []
    
    def __init__(self, name, category):
        self._name = name
        self._category = category
        Magazine.all.append(self)
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str) and 2 <= len(value) <= 16:
            self._name = value
    
    @property
    def category(self):
        return self._category
    
    @category.setter
    def category(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._category = value
    
    def articles(self):
        return [article for article in Article.all if article.magazine == self]
    
    def contributors(self):
        return list(set([article.author for article in self.articles()]))
    
    def article_titles(self):
        titles = [article.title for article in self.articles()]
        return titles if titles else None
    
    def contributing_authors(self):
        author_count = {}
        for article in self.articles():
            author = article.author
            author_count[author] = author_count.get(author, 0) + 1
        
        contributing_authors = [author for author, count in author_count.items() if count > 2]
        return contributing_authors if contributing_authors else None
    
    @classmethod
    def top_publisher(cls):
        if not Article.all:
            return None
        
        magazine_article_count = {}
        for article in Article.all:
            magazine = article.magazine
            magazine_article_count[magazine] = magazine_article_count.get(magazine, 0) + 1
        
        if not magazine_article_count:
            return None
            
        return max(magazine_article_count, key=magazine_article_count.get)