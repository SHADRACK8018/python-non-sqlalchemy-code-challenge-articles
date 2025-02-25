#!/usr/bin/env python3
import ipdb;

from classes.many_to_many import Article
from classes.many_to_many import Author
from classes.many_to_many import Magazine

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # Example of creating instances
    author1 = Author("John Doe")
    magazine1 = Magazine("TechWorld", "Technology")
    magazine2 = Magazine("HealthPlus", "Health")

    # Add articles
    article1 = author1.add_article(magazine1, "The Future of AI")
    article2 = author1.add_article(magazine2, "Healthy Eating Tips")

    # Check the author's articles and magazines
    print(author1.articles())
    print(author1.magazines())

    # Check magazine articles and contributors
    print(magazine1.article_titles())
    print(magazine1.contributors())


    # don't remove this line, it's for debugging!
    ipdb.set_trace()
