from docx import Document


def main():


    txt = "Wheter you're new to programming or "+\
          "an experienced developer, it's easy "+\
          "to learn and use Python. "+\
          "Python source code and installers are "+\
          "avaiable for download for all versions!"

    docx = Document()

    header = docx.add_heading("Python Programing!", Level=0)

    docx.save("Some.docx")

    return


if __name__ == '__main__':
    main()