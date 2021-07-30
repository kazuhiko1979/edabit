"""
Your task is to create a class to handle paginated content in a website. A pagination is used to divide long lists of content in a series of pages.

Example

The pagination class will accept 2 parameters:

items (default: []): A list of contents to paginate.

pageSize (default: 10): The amount of items to show in each page.

So for example we could initialize our pagination like this:

alphabetList = "abcdefghijklmnopqrstuvwxyz".split('')

p = Pagination(alphabetList, 4)
And then use the method getVisibleItems to show the contents of the paginated list.

p.getVisibleItems() # ["a", "b", "c", "d"]
You will have to implement various methods to go through the pages such as:

prevPage
nextPage
firstPage
lastPage
goToPage

Here's a continuation of the example above using nextPage and lastPage:

p.nextPage()

p.getVisibleItems()
# ["e", "f", "g", "h"]

p.lastPage()

p.getVisibleItems()
# ["y", "z"]
Notes
The second argument (pageSize) could be a float, in that case just convert it to an int (this is also the case for the goToPage method)
The methods used to change page should be chainable, so you can call them one after the other like this: p.nextPage().nextPage()
Please set the p.totalPages and p.currentPage attributes to the appropriate number as there cannot be a page 0.
If a page is outside of the totalPages attribute, then the goToPage method should go to the closest page to the number provided (e.g. there are only 5 total pages, but p.goToPage(10) is given: the p.currentPage should be set to 5; if 0 or a negative number is given, p.currentPage should be set to 1).
Please remove the comments I provided before publishing your solution.
"""
import math

class Pagination:

    def __init__(self, items=[], pageSize=10):
        self.items = items
        self.pageSize = pageSize
        self.totalPages = math.ceil(len(items) / pageSize)
        self.currentPage = 1

    def getItems(self):

        return self.items

    def getPageSize(self):

        return self.pageSize

    def getCurrentPage(self):

        return self.currentPage

    # Goes to the previous page
    def prevPage(self):

        self.currentPage = max(self.currentPage - 1, 1)
        return self

    # Goes to the next page
    def nextPage(self):

        self.currentPage = min(self.totalPages, self.currentPage + 1)
        return self

    # Goes to the first page
    def firstPage(self):

        self.currentPage = 1
        return self

    # Goes to the last page
    def lastPage(self):

        self.currentPage = self.totalPages
        return self

    # Goes to a page determined by the `page` argument
    def goToPage(self, page):

        page = max(page, 1)
        page = min(page, self.totalPages)
        self.currentPage = int(page)
        return self

    # Returns the currently visible items as an array
    def getVisibleItems(self):

        f = (self.currentPage - 1) * self.pageSize
        t = min(self.currentPage * self.pageSize, len(self.items))
        return self.items[f:t]

defaultPagination = Pagination()
print(defaultPagination.getPageSize())
print(defaultPagination.getItems())

p1 = Pagination([None]*69, 5)

print(p1.nextPage().getCurrentPage())
print(p1.lastPage().getCurrentPage())
print(p1.nextPage().getCurrentPage())
print(p1.prevPage().getCurrentPage())
print(p1.firstPage().getCurrentPage())
print(p1.prevPage().getCurrentPage())
print(p1.goToPage(99).getCurrentPage())
print(p1.goToPage(  4).getCurrentPage())
print(p1.goToPage(6.5).getCurrentPage())
print(p1.goToPage(-99).getCurrentPage())


ids = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
p2 = Pagination(ids, 5)

print(p2.getVisibleItems())
print(p2.nextPage().getVisibleItems())
print(p2.nextPage().getVisibleItems())

