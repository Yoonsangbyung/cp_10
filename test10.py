
def create_mail(name):
    contents = "한국교통대학교 천하제일 탁구대회" + name + "님 안녕하세요"
    return contents


pingpong_list = ["나영","예진","원빈","현빈"]

for name in pingpong_list :
    contents_of_mail = create_mail(name)
    print(contents_of_mail)


