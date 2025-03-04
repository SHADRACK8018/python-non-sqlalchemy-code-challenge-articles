class Article:
    all = []  # Class-level attribute to store all articles globally

    def __init__(self, author, magazine, title):
        # Ensure valid input types and title length constraints
        if not isinstance(author, Author):
            raise ValueError("Author must be an instance of Author")
        if not isinstance(magazine, Magazine):
            raise ValueError("Magazine must be an instance of Magazine")
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters.")
        
        self._title = title  # Make title immutable
        self.author = author
        self.magazine = magazine

        # Add this article to the author's and magazine's article lists
        author._articles.append(self)
        magazine._articles.append(self)

        # Add the article to the global list
        Article.all.append(self)

    @property
    def title(self):
        return self._title  # Immutable title property

    def __repr__(self):
        return f"Article(title={self.title}, author={self.author.name}, magazine={self.magazine.name})"


class Author:
    def __init__(self, name):
        # Ensure valid name input
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string.")
        
        self._name = name
        self._articles = []  # Stores the articles the author has written

    @property
    def name(self):
        return self._name  # Immutable name property

    def articles(self):
        return self._articles  # Return all articles written by the author

    def magazines(self):
        # Return a unique list of magazines the author has written for
        return list(set(article.magazine for article in self._articles))

    def add_article(self, magazine, title):
        # Creates and returns a new article associated with the author and magazine
        article = Article(self, magazine, title)
        return article

    def topic_areas(self):
        # Return unique categories of the magazines the author has contributed to
        magazines = self.magazines()
        return list(set(magazine.category for magazine in magazines)) or None

    def __repr__(self):
        return f"Author(name={self.name})"


class Magazine:
    all = []  # Class-level attribute to store all magazines globally

    def __init__(self, name, category):
        # Ensure valid magazine name
        if not isinstance(name, str) or len(name) < 2 or len(name) > 16:
            raise Exception("Magazine name must be a string between 2 and 16 characters.")
        
        # Ensure valid category
        if not isinstance(category, str) or len(category) == 0:
            raise Exception("Category must be a non-empty string.")
        
        self._name = name
        self._category = category
        self._articles = []  # List of articles for this magazine

        # Add the magazine to the global 'all' list
        Magazine.all.append(self)

    @property
    def name(self):
        return self._name  # Immutable name property

    @name.setter
    def name(self, new_name):
        if isinstance(new_name, str) and 2 <= len(new_name) <= 16:
            self._name = new_name
        else:
            raise Exception("Magazine name must be between 2 and 16 characters.")

    @property
    def category(self):
        return self._category  # Immutable category property

    @category.setter
    def category(self, new_category):
        if isinstance(new_category, str) and len(new_category) > 0:
            self._category = new_category
        else:
            raise Exception("Category must be a non-empty string.")

    def articles(self):
        return self._articles  # Return all articles in the magazine

    def contributors(self):
        # Return unique authors who have contributed to this magazine
        return list(set(article.author for article in self._articles))

    def article_titles(self):
        # Return a list of titles of all articles in the magazine
        if not self._articles:
            return None
        return [article.title for article in self._articles]

    def contributing_authors(self):
        # Return authors who have written more than 2 articles for this magazine
        contributing = [
            author for author in self.contributors()
            if len([article for article in author.articles() if article.magazine == self]) > 2
        ]
        return contributing if contributing else None

    @classmethod
    def top_publisher(cls):
        # Return the magazine with the most articles, or None if no articles exist
        if not Article.all:
            return None
        return max(cls.all, key=lambda magazine: len(magazine._articles))

    def __repr__(self):
        return f"Magazine(name={self.name}, category={self.category})"
