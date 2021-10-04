"""
あなたは、今ユーザーがハイキングの体験を共有することができる新しいソーシャルメディアアプリを設計しています。
以下の構造に沿ったユーザーの設計図を作成してください。

// 状態
String username: // ユーザーネーム
String firstName: // ユーザーの名
String lastName: // ユーザーの姓
String email: // 登録されたEメールアドレス
String passwordHashed: // ユーザーログインの確認に使われるハッシュ化されたパスワード
int birthMonth: // ユーザーが生まれた月。
int birthYear: // ユーザーが生まれた年
String biographyDescription: // ユーザーのプロフィールのbio
String favoriteHikingLocation: // ユーザーのお気に入りのハイキング場所

// 挙動
String getFullName(): // ユーザーのフルネームを返します。
int getAge(): // ユーザーの年齢を返します。
int birthdayCalculator(): // 誕生日まであと何ヶ月あるか計算して返します。
String showProfile(): // ユーザーのプロフィールを返します。
bool confirmPassword(String passwordString):
// 指定したpasswordStringが保存したpasswordHashedと一致しているかをブーリアン値で返します。
セキュリティのために、パスワードのハッシュ化されたバージョンがメモリ内の状態に保存されることに注意してください。
パスワードを文字列として受け取り、
その文字列をマップし、ハッシュ化されたパスワードhashedPassword返す関数を使う必要があります。
"""

"""
Pseudo-Code

String userPassword = "thisisasecret"
// これがハッシュ関数によってマップされ、DFDSFSXDFS343が返されると仮定します。
String hashedPassword = hashPassword(userPassword)

// trueを返します。
hashPassword(userPassword) == hashedPassword
// falseまたはtrueを返します。良いハッシュ関数はこの場合falseを返します。
hashPassword("testing") == hashedPassword
"""
import datetime

class HelperFunction:

    def hashPassword(passwordstring):

        hash = 5381
        for x in passwordstring:
            hash = ((hash << 5) + hash) + ord(x)
        return str(hash & 0xFFFFFFFF)

class User:

    def __init__(self, username, firstName, lastName, email, passwordString, birthMonth,
                 birthYear, biographyDescription, favoriteHikingLocation):

        self.username = username
        self.firstName = firstName
        self.lastName = lastName
        self.email = email
        self.passwordString = HelperFunction.hashPassword(passwordString)
        self.birthMonth = birthMonth
        self.birthYear = birthYear
        self.biographyDescription = biographyDescription
        self.favoriteHikingLocation = favoriteHikingLocation

    # ユーザーのフルネームを返します。
    def getFullName(self):
        return self.firstName + " " + self.lastName

    # ユーザーの年齢を返します。
    def getAge(self):
        currentYear = datetime.datetime.now().year
        currentMonth = datetime.datetime.now().month
        result = currentYear - self.birthYear
        return result if currentMonth >= self.birthMonth else result - 1

    # 誕生日まであと何か月あるか計算して返します
    def birthdayCalculator(self):

        currentMonth = datetime.datetime.now().month
        if currentMonth - self.birthMonth > 0:
            return 12 - (currentMonth - self.birthMonth)
        else:
            return self.birthMonth - currentMonth

    # ユーザープロフィールを返します
    def showProfile(self):

        return self.username + "\n" + str(self.getAge()) + " years old\n" \
         + str(self.biographyDescription) + "\nfavoroite place to hike: " + \
               self.favoriteHikingLocation

    # 指定したpasswordStringが保存したpasswordstringと一致しているかをブーリンアン値で
    # 返します。セキュリティのために、パスワードのハッシュ化されたバージョンがメモリ内の状態で保存
    def confirmPassword(self, passwordString):
        return self.passwordString == HelperFunction.hashPassword(passwordString)


claire = User("claireS", "Claire", "Simmons", "clairesimmons@gmail.com", \
              "lmnlmn", 9, 2007, "Passionate gamer. Evil internet aficionado. "
              "Student. Friendly tv specialist. Introvert.", \
              "Hollywood Sign Hike")


print(claire.getFullName())
print(claire.getAge())
print(claire.birthdayCalculator())
print(claire.showProfile())
print(claire.confirmPassword("lmnlmn"))
print(HelperFunction.hashPassword("lmnlmn"))













