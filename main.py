import turtle
sc = turtle.Screen()
sc.setup(1000,500)
turtle.title("PeyintTR")
kalem = turtle.Turtle()
import pygame
pygame.mixer.init()
pygame.mixer.music.load("muzik.wav")
import time
kalem.color("black","black")
print(" ")
print(" ")
print(" ")
print(" ")
print(" ")
print("PeyintTR v3.0.1")
print("©Arda Saplıoğlu & ®Saplıoğlu Yazılım")
print(" ")
print(" ")
time.sleep(2)
print("yükleniyor")
time.sleep(0.5)
print("yükleniyor.")
time.sleep(0.5)
print("yükleniyor..")
time.sleep(0.5)
print("yükleniyor...")
time.sleep(1)
print(" ")
print(" ")
print(" ")
pygame.mixer.music.play()
print("merhaba PeyintTR ye hoşgeldiniz")
print("bu uygulama komut tabanlı bir grafik çizim uygulamasıdır")
print("komutları buradan girebilirsiniz")
print(" ")
print(" ")
print(" ")
print("tam komut listesi için yardım yazın")
print(" ")
print(" ")


cikis = (False)
while cikis == False:
    print(" ")
    time.sleep(1)
    komut = input(("komutu girin\n"))
    if komut == ("yardım"):
        print("çıkış = programdan çıkar")
        print("yardım = tam komut listesini açar")
        print("sağ = sağa döner")
        print("sol = sola döner")
        print("ileri = dilediğiniz kadar ileri gider")
        print("geri = dilediğiniz kadar geri gider")
        print("çember = dilediğiniz yarıçapta çember çizer")
        print("daire = dilediğiniz yarıçapta dolu daire çizer")
        print("çokgen = çokgen çizer")
        print("dolu çokgen = dolu çokgen çizer")
        print("yıldız = yıldız çizer")
        print("dolu yıldız = dolu yıldız çizer")
        print("renk = kalem rengini seçtirir")
        print("arka renk = arka plan rengini seçtirir")
        print("özel 1 /.../ özel 6  = özel desen çizer")
        print("temizle = herşeyi siler")
        print("korona bitirici = koronayı yok eder")
        print("başa dön = başa döner")
        print("nokta = nokta koyar")
        print("geri al = son yapılanı geri alır")
        print("hız = hızı ayarlar")
        print("indir = kalemi bastırır")
        print("kaldır = kalemi kaldırır")
        print("kalem ucu boyu = uç boyunu ayarlar")
        print("dolum başlat = bakınız: begin_fill()")
        print("dolum bitir = bakınız: end_fill()")
        print("sürükle aç = bu komutu yazınca imleci sürükleyerek çizme açılır")
    elif komut == ("ileri"):
        kalem.forward(int(input("kaç adım ileri gitmek istersiniz \n")))
        print("komut başarılı")
    elif komut == ("geri"):
        kalem.backward(int(input("kaç adım geri gitmek istersiniz \n")))
        print("komut başarılı")
    elif komut == ("çokgen"):
        c=int(input("kenar sayısı girin \n"))
        d = int(input("kenar uzunluğu girin \n"))
        e=(c)
        for i in range (e):
            kalem.forward(d)
            kalem.left((180-((c-2)*180)/c))

    elif komut == ("dolu çokgen"):
        c=int(input("kenar sayısı girin \n"))
        d=int(input("kenar uzunluğu girin \n"))
        kalem.begin_fill()
        for i in range(c):
            kalem.forward(d)
            kalem.left((180-((c-2)*180)/c))
        kalem.end_fill()
    elif komut == ("dolu yıldız"):
        kalem.begin_fill()
        for i in range(5):
            kalem.forward(50)
            kalem.right(144)
        kalem.end_fill()
    elif komut == ("yıldız"):
        for i in range(5):
            kalem.forward(50)
            kalem.right(144)
    elif komut == ("çember"):
        kalem.circle(int(input("yarıçap kaç olsun \n")))
        print("komut başarılı")
    elif komut == ("çıkış"):
        print("programdan çıkılıyor")
        time.sleep(2)
        cikis = (True)
    elif komut == ("daire"):
        kalem.begin_fill()
        kalem.circle(int(input("yarıçap kaç olsun \n")))
        kalem.end_fill()
    elif komut == ("renk"):
        kalem.color(input("1. rengi ingilizce olarak girin \n"), input("2. rengi ingilizce olarak girin \n"))
        print("komut başarılı")
    elif komut == ("sağ"):
        kalem.right(int(input("kaç derece dönsün \n")))
        print("komut başarılı")
    elif komut == ("sol"):
        kalem.left(int(input("kaç derece dönsün \n")))
        print("komut başarılı")
    elif komut == ("temizle"):
        kalem.clear()
        print("komut başarılı")
    elif komut == ("arka renk"):
        sc.bgcolor(input("rengi ingilizce olarak girin \n"))
        print("komut başarılı")
    elif komut == ("korona bitirici"):
        import turtle



        sc.bgcolor("black")
        kalem.pencolor("red")

        a = 0
        b = 0
        kalem.speed(0)
        kalem.penup()
        kalem.goto(0, 200)
        kalem.pendown()
        while (True):
            kalem.forward(a)
            kalem.right(b)
            a += 3
            b += 1
            if b == 210:
                break
            kalem.hideturtle()
        a=input("koronayı bitirmek için enter a basın")
        kalem.clear()
        print("tebrikler koronayı yok ettiniz")
    elif komut == ("özel 1"):
        liste1 = ["red","orange","yellow","green","blue","purple"]
        turtle.bgcolor("black")
        for i in range(200):
            kalem.color(liste1[i % 6])
            kalem.pensize(i / 10 + 1)
            kalem.forward(i)
            kalem.left(59)
    elif komut == ("özel 2"):
        kalem.speed(10)

        for i in range(180):
            kalem.forward(100)
            kalem.right(30)
            kalem.forward(20)
            kalem.left(60)
            kalem.forward(50)
            kalem.right(30)

            kalem.penup()
            kalem.setposition(0, 0)
            kalem.pendown()

            kalem.right(2)
    elif komut == ("özel 3"):
        sc.bgcolor('black')
        for i in range(6):
            for colors in ["red", "blue", "magenta", "green", "yellow", "white"]:
                kalem.color(colors)
                kalem.circle(100)
                kalem.left(10)
    elif komut == ("özel 4"):
        kalem.speed(10)
        colors = ['red', 'purple', 'blue', 'green', 'yellow', 'orange']
        sc.bgcolor('black')
        for x in range(360):
            kalem.pencolor(colors[x % 6])
            kalem.width(x / 100 + 1)
            kalem.forward(x)
            kalem.left(59)
    elif komut == ("özel 5"):
        t = turtle.Turtle()
        s = turtle.Screen()
        s.bgcolor("black")

        turtle.pensize(2)



        def curve():
            for i in range(200):
                t.right(1)
                t.forward(1)


        t.speed(3)
        t.color("red", "pink")

        t.begin_fill()
        t.left(140)
        t.forward(111.65)
        curve()

        t.left(120)
        curve()
        t.forward(111.65)
        t.end_fill()
    elif komut == ("özel 6"):
        for i in range(20):
            kalem.forward(i * 10)
            kalem.right(144)
    elif komut == ("başa dön"):
        kalem.home()
        print("komut başarılı")
    elif komut == ("nokta"):
        kalem.dot()
        print("komut başarılı")
    elif komut == ("geri al"):
        kalem.undo()
        print("komut başarılı")
    elif komut == ("hız"):
        kalem.speed(int(input("hız girin (1/11)\n")))
        print("komut başarılı")
    elif komut == ("indir"):
        kalem.pendown()
        print("komut başarılı")
    elif komut == ("kaldır"):
        kalem.penup
        print("komut başarılı")
    elif komut == ("kalem ucu boyu"):
        kalem.pensize(int(input("boy girin\n")))
        print("komut başarılı")
    elif komut == ("dolum başlat"):
        kalem.begin_fill()
        print("komut başarılı")
    elif komut == ("dolum bitir"):
        kalem.end_fill()
        print("komut başarılı")
    elif komut == ("sürükle aç"):
        def goto(x,y):
            kalem.goto(x,y)
        kalem.ondrag(goto)
        print("komut başarılı")
    else:
        print("hatalı komut girdiniz tekrar deneyin")
        time.sleep(1)
