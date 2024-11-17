# örnek kullanıcı bilgileri

usersPhone = "5123456789"
usersUserName = "zehraa"
usersEmail = "zehra@compruarge.com"
usersPassword = "sinopsinop2"

#kullanıcı girişi uygulaması

while True:
    identifier = input("Telefon numarası, kullanıcı adı ya da e-posta giriniz: ")
    enteredPassword = input("şifre giriniz: ")

    if (identifier == usersPhone or identifier == usersUserName or identifier == usersEmail) and enteredPassword == usersPassword:
        #hem kullanıcı bilgisi hem şifre doğruysa sisteme giriş yapar
        print("Giriş Başarılı. Hoşgeldin!")
        break
    elif (identifier == usersPhone or identifier == usersUserName or identifier == usersEmail) and enteredPassword != usersPassword:
        #şifre yanlışsa tekrar dener
        print("Üzgünüz, şifren yanlış. Lütfen şifreni dikkatlice kontrol et.")
    elif (identifier != usersPhone or identifier != usersUserName or identifier != usersEmail) and enteredPassword == usersPassword:
        #kullanıcı bilgisi yanlışsa tekrar dener
        print("Üzgünüz, kullanıcı bilgilerin hatalı. Lütfen bilgilerini dikkatlice kontrol et.")
    else:
        #hem kullanıcı bilgisi hem şifre yanlışsa tekrar dener
        print("Üzgünüz, kullanıcı bilgilerin hatalı. Lütfen bilgilerini dikkatlice kontrol et.")

