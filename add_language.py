import os

def getLanguages():
    """ Get languages by directories """
    languages = ""
    for folder in os.listdir("."):
        if not '.' in folder:
            languages += f"\n* [{folder}](./{folder})"

    return languages

def setReadme(content: str):
    """ Write to the readme file """
    with open("README.md", "w") as f:
        f.write(content)
        f.close()

def getReadme():
    """ read content from readme """
    file = open("README.md", "r")
    data = file.read()
    file.close()
    return data

def main():
    text = getReadme()
    splited = text.split("### Languages")[0]
    langs = getLanguages()

    setReadme(splited + "### Languages\n" + langs)

if __name__ == "__main__":
    main()