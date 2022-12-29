a = "%0.4f" % 3.12341234

print(a)

b="aasdf"
print(b.count("a")) #개수가 몇개있는지
print(b.find("d")) #몇번째 있는지

c=",".join(["a","b","c"]) #추가하기
print(c)
d="hi"
print(d.upper()) #대문자 변경
e="HI"
print(d.lower()) #소문자 변경
f="     hi      " 
print(f.strip()) #공백제거

g =  "Life is too short"
print(g.replace("Life","hello")) #교체
print(g.split())

h=["이혜성","김지영","정가연",["김재원","man"]]
h[0]="김시민"
del h[0] #삭제
print(h)