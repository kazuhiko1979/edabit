#!/usr/bin/env python
import cgi

# Set the content type to HTML
print("Content-Type: text/html")
print()

# Get the form data from standard input
form = cgi.FieldStorage()

# Check if the form data exists
if "lastname" not in form or "firstname" not in form:
    print("エラーです： フォームにデータが入力されていません。")
else:
    # Get the last name and first name values from the form data
    lastname = form["lastname"].value
    firstname = form["firstname"].value

    # Check if the last name and first name values are double-byte characters
    if not all(ord(c) > 255 for c in lastname) or not all(ord(c) > 255 for c in firstname):
        print("エラーです： 入力が無効です。全角文字のみ入力してください。")
    elif len(lastname) > 16 or len(firstname) > 16:
        print("エラーです： 入力が最大文字数16文字を超えました。")
    else:
        # Reverse the last name and duplicate each character in the first name
        reversed_lastname = lastname[::-1]
        duplicated_firstname = "".join([c+c for c in firstname])

        # Display the processed data
        print("<h2>性: {}</h2>".format(reversed_lastname))
        print("<h2>名: {}</h2>".format(duplicated_firstname))
