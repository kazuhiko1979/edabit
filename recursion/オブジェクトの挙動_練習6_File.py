"""
あなたは開発チームに所属しており、企業用向けのクラウドシステムを構築するタスクを与えられました。
このソフトウェアの一部には、ユーザーがファイルを保存したり、読み書きできる機能が含まれています。
ファイルを共有することもできるので、ユーザーは上書きがないように自分のファイルをロックする機能もついています。
"""

"""
// 状態
String fileName: // ファイル名
String fileExtension: // ファイルの拡張子。.word, .png, .js, .css, .html, .mp4, .mp3, .pdf
ではない場合、.txtに設定されます。
String content: // ファイルのすべての内容
bool locked: // ファイルの内容を上書きできるかどうかをきめるブーリンアン値。trueの場合、コンテンツがロック
されており、falseの場合、コンテンツがロックされていないことを示します。
String parentFolder: // ファイルが置かれているフォルダの名前
"""

"""
// 挙動

String getLifetimeBandwidthSize(): // サービス中に使われているファイルの最大容量を返します。
contentに含まれる文字につき、10MBとして計算してください。
例えば、1000文字含まれている場合、1000 * 10MB = 10,000MB = 10GBになります。

String getFileType(): // オブジェクトのファイルタイプを返します。
document(.pdf, .word, .txt). source-code(.js, .css, .html), video(.mp4), music(.mp3)があります。

String prependContent(String data): // もしファイルがロックされていなければ、
ファイルのcontentの先頭にデータ文字列を追加し、新しいcontentを返します。

String appendContent(String data): // もしファイルがロックされていなければ、
ファイルのcontentの末尾にデータ文字列を追加し、新しいcontentを返します。

String addContent(String data, int position): // もしファイルがロックされていなければ、
ファイルのcontentの指定した位置（インデックス）にデータ文字列を追加し、新しいcontentを返します。

String showFileLocation(): // 親ファイル > ファイル名.拡張子という形で返します。

"""

class File:

    def __init__(self, fileName, fileExtension, content, locked, parentFolder):

        self.fileName = fileName
        self.fileExtension = fileExtension
        self.content = content
        self.locked = locked
        self.parentFolder = parentFolder

    def getLifetimeBandwidthSize(self):

        return str(len(self.content) * 10) + "MB"

    def getFileType(self):

        if self.fileExtension in (".pdf", ".word", ".txt"):
            return "document"
        elif self.fileExtension in (".js", ".css", ".html"):
            return "source-code"
        elif self.fileExtension in (".mp4"):
            return "video"
        elif self.fileExtension in (".mp3"):
            return "music"

    def prependContent(self, data):

        if not self.locked:
            self.content = data + " " + self.content
        return self.content

    def appendContent(self, data):

        if not self.locked:
            self.content = self.content + " " + data
        return self.content

    def addContent(self, data, position):

        if not self.locked:
            self.content = self.content[:position] + data + " " + self.content[position:]
        return self.content

    def showFileLocation(self):

        return "{} > {}{}".format(self.parentFolder, self.fileName, self.fileExtension, )

assignment = File("assignment", ".word", "Something that occurs too early before preparations are ready. Starting too soon.", False, "homework")

print(assignment.getLifetimeBandwidthSize())
print(assignment.getFileType())
print(assignment.prependContent("good morning"))
print(assignment.appendContent("good evening"))
print(assignment.addContent("hello world", 13))
print(assignment.showFileLocation())


