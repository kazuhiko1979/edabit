"""
You are in the midst of organizing all of your coding projects.
It's a mess! Every file you've ever created is located in the same folder.

To clean it up, you've decided that you will use one of two organization methods.

The prefix method: You will group all files with the same project name under the same folder.
The suffix method: You will group all files with the same extension under the same folder.
Create a function that takes in the current folder sorts the files according to the organization method
(prefix or suffix). A folder is a grouping of files in the same list.

Examples
# Sorting by project name (ex1 and ex2)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix") ➞ [
  ["ex1.html", "ex1.js"],
  ["ex2.html", "ex2.js"]
]

# Sorting by extension (.html and .js)
clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "suffix") ➞ [
  ["ex1.html", "ex2.html"],
  ["ex1.js", "ex2.js"]
]

clean_up(["music_app.js", "music_app.png", "music_app.wav", "tetris.png", "tetris.js"], "prefix") ➞ [
  ["music_app.js", "music_app.png", "music_app.wav"],
  ["tetris.png", "tetris.js"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "suffix") ➞ [
  ["_1.rb", "_2.rb", "_3.rb", "_4.rb"]
]

clean_up(["_1.rb", "_2.rb", "_3.rb", "_4.rb"], "prefix") ➞ [
  ["_1.rb"], ["_2.rb"],
  ["_3.rb"], ["_4.rb"]
]
Notes
Keep elements in the same relative order.
"""

def clean_up(files, sort):

    res = []
    for f in files:
        name, ext = f.split('.')

        group = [i for i in files if (i.startswith(name) if sort == 'prefix' else i.endswith(ext))]

        if group not in res:
            res.append(group)
    return res

print(clean_up(["ex1.html", "ex1.js", "ex2.html", "ex2.js"], "prefix"))