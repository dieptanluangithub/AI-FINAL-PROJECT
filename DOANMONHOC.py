import  speech_recognition
from gtts import gTTS
import playsound
import os
import webbrowser
import datetime
import requests
import smtplib
from google_trans_new import google_translator 

#Những việc em làm thêm so với buổi 15: Kết hợp vừa chat bot vừa trợ lý ảo (thay vì chỉ chat bot như hôm trước)
#Thêm và cải tiến một số chức năng như: dịch ngôn ngữ AV- VA, xem nhiệt độ, dự báo thời tiết và cảnh báo sức khỏe
#Thêm chức năng nhắc lịch làm việc, tìm kiếm thông tin trên gg và youtube, mở ứng dụng word và excel
#Thêm chức năng phân tích kết quả học tập
# Đã gửi được gmail

you = ""
nghe = speech_recognition.Recognizer()
brain = ""
def maynoi(brain):
    output = gTTS(brain,lang='vi',slow= False)
    output.save('voice.mp3')
    playsound.playsound('voice.mp3')
    os.remove('voice.mp3')
def maynoien(brain):
    output = gTTS(brain,lang='en',slow= False)
    output.save('voice.mp3')
    playsound.playsound('voice.mp3')
    os.remove('voice.mp3')
def dichngonngugiongnoi():
    print("Bạn muốn dịch Anh - Việt hay Việt - Anh")
    maynoi("Bạn muốn dịch Anh - Việt hay Việt - Anh")
    with speech_recognition.Microphone() as mic:
        print("Bot: I'm Listening")
        audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
        print("Bot: ...")
        try:
            you = nghe.recognize_google(audio, language='vi-VN')
            print("Ngôn ngữ bạn chọn là: " + you)
        except:
            you = ""
            print ("Mình không nghe được gì cả")
            brain = "Mình không nghe được gì cả"
            maynoi(brain)
        if "Anh Việt" in you:
            maynoi("Từ bạn muốn dịch là?")
            with speech_recognition.Microphone() as mic:
                print("Bot: I'm Listening")
                audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
                print("Bot: ...")
                try:
                    you = nghe.recognize_google(audio, language='en')
                    print(you)
                except:
                    you = ""
                    print ("Mình không nghe được gì cả")
                    brain = "Mình không nghe được gì cả"
                    maynoi(brain)
                translator = google_translator()
                anhviet = translator.translate(you, lang_src='en', lang_tgt='vi')
                print("Tiếng Việt: " + anhviet)
                maynoi(anhviet)
        elif "Việt Anh" in you:
            maynoi("Từ bạn muốn dịch là?")
            with speech_recognition.Microphone() as mic:
                print("Bot: I'm Listening")
                audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
                print("Bot: ...")
                try:
                    you = nghe.recognize_google(audio, language='vi-VN')
                    print(you)
                except:
                    you = ""
                    print ("Mình không nghe được gì cả")
                    brain = "Mình không nghe được gì cả"
                    maynoi(brain)
                translator = google_translator()
                vietanh = translator.translate(you, lang_src='vi', lang_tgt='en')
                print("Tiếng anh: " + vietanh)
                maynoien(vietanh)
def dichngonngu():
    print("Bạn muốn dịch Anh - Việt hay Việt - Anh")
    maynoi("Bạn muốn dịch Anh - Việt hay Việt - Anh")
    you = input("Ngôn ngữ bạn chọn là: ")
    if "Anh Việt" in you or "anh việt" in you:
        you = input("Từ bạn muốn dịch là: ")
        translator = google_translator()
        anhviet = translator.translate(you, lang_src='en', lang_tgt='vi')
        print("Tiếng Việt: " + anhviet)
        maynoi(anhviet) 
                
    elif "Việt Anh" in you or "việt anh" in you:
        you = input("Từ bạn muốn dịch là: ")
        translator = google_translator()
        vietanh = translator.translate(you, lang_src='vi', lang_tgt='en')
        print("Tiếng Anh: " + vietanh)
        maynoien(vietanh)

def thoigian():
    thoigian= datetime.datetime.now().strftime("%I:%M:%p")
    maynoi(thoigian)
    
def welcome():
    hour = datetime.datetime.now().hour
    if hour >=0 and hour<11 :
        maynoi("Chào buổi sáng.Tôi là Bot của DTL")
    if hour >=11 and hour <13:
        maynoi("Chào buổi trưa.Tôi là Bot của DTL")
    if hour >= 13 and hour <18:
        maynoi("Chào buổi chiều.Tôi là Bot của DTL")
    if hour >= 18 and hour <24:
        maynoi("Chào buổi tối.Tôi là Bot của DTL")
        
def phantichketqua():
    print("Để phục vụ cho việc phân tích bạn vui lòng cho biết một só thông tin bạn nhé!")
    drl = int(input("Điểm rèn luyện = "))
    dht = float(input("Điểm học tập = "))
    ctxh = int(input("Điểm CTXH = "))
    av = float(input("Điểm anh văn = "))
    check = input("Bạn có bị rớt môn hay bị kỷ luật không?[y/n]: ")
    check1 = input("Bạn có tham gia hội thảo kỹ năng không?[y/n]: ")
    if ((drl >= 80) & (dht >= 7.5) & (ctxh >=20) & ((av>=7.5) | (av>= 420)) & (check == "n") & (check1 == "y")):
        brain = "Bạn có khả năng đạt danh hiệu sinh viên 5 tốt"
        print(brain)
        maynoi(brain)
    elif ((drl < 80) & (dht >= 7.5) & (ctxh >=20) & ((av>=7.5) | (av>= 420)) & (check == "n") & (check1 == "y")):
        brain = "Bạn thiếu điểm rèn luyện mất rồi. Cần cố gắng hơn"
        print(brain)
        maynoi(brain)
    elif ((drl >= 80) & (dht < 7.5) & (ctxh >=20) & ((av>=7.5) | (av>= 420)) & (check == "n") & (check1 == "y")):
        brain = "Bạn thiếu điểm học tập mất rồi. Cần cố gắng hơn"
        print(brain)
        maynoi(brain)
    elif ((drl >= 80) & (dht >= 7.5) & (ctxh <20) & ((av>=7.5) | (av>= 420)) & (check == "n") & (check1 == "y")):
        brain = "Bạn thiếu điểm công tác xã hội mất rồi. Cần cố gắng hơn"
        print(brain)
        maynoi(brain)
    elif ((drl >= 80) & (dht >= 7.5) & (ctxh >=20) & ((av<7.5) | (av<420)) & (check == "n") & (check1 == "y")):
        brain = "Bạn thiếu điểm ngoại ngữ mất rồi. Cần cố gắng hơn"
        print(brain)
        maynoi(brain)
    elif ((drl >= 80) & (dht >= 7.5) & (ctxh >=20) & ((av>=7.5) | (av>= 420)) & (check == "y") & (check1 == "y")):
        brain = "Bạn không đủ tiêu chuẩn để xét mất rồi"
        print(brain)
        maynoi(brain)
    elif ((drl >= 80) & (dht >= 7.5) & (ctxh >=20) & ((av>=7.5) | (av>= 420)) & (check == "n") & (check1 == "n")):
        brain = "Bạn nên tham gia nhiều hơn các buổi hội thảo kỹ năng bạn nhé"
        print(brain)
        maynoi(brain)   
    else:
        brain = "Bạn cần lưu ý các tiêu chí và cố gắng hơn bạn nhé"
        print(brain)
        maynoi(brain)
def dubaothoithiet():
    maynoi("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    city = input("Nhập thành phố của bạn: ")
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        nhietdo = city_res["temp"]
        now = datetime.datetime.now()
        if ((nhietdo >= 27) & (nhietdo<32)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này có thể mệt mỏi nếu hoạt động và phơi nắng kéo dài. Tiếp tục hoạt động có thể dẫn tới chuột rút do nóng.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
        elif ((nhietdo >=32) & (nhietdo >41)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này có thể gây ra chuột rút do nóng và kiệt sức do nóng. Tiếp tục hoạt động có thể dẫn tới sốc nhiệt.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
        elif ((nhietdo >=20) & (nhietdo <27)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này cơ thể cảm thấy dễ chịu, hoạt động tối ưu mà không thấy hoặc có rất ít các rối loạn xảy ra.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
    else:
        maynoi("Không tìm thấy địa chỉ của bạn")
def dubaothoitietgiongnoi():
    maynoi("Bạn muốn xem thời tiết ở đâu ạ.")
    ow_url = "http://api.openweathermap.org/data/2.5/weather?"
    with speech_recognition.Microphone() as mic:
        print("Bot: I'm Listening")
        audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
        print("Bot: ...")
        try:
            city = nghe.recognize_google(audio, language='vi-VN')
        except:
            city = ""
            print ("Mình không nghe được gì cả")
            brain = "Mình không nghe được gì cả"
            maynoi(brain)
    if not city:
        pass
    api_key = "fe8d8c65cf345889139d8e545f57819a"
    call_url = ow_url + "appid=" + api_key + "&q=" + city + "&units=metric"
    response = requests.get(call_url)
    data = response.json()
    if data["cod"] != "404":
        city_res = data["main"]
        nhietdo = city_res["temp"]
        now = datetime.datetime.now()
        if ((nhietdo >= 27) & (nhietdo<32)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này có thể mệt mỏi nếu hoạt động và phơi nắng kéo dài. Tiếp tục hoạt động có thể dẫn tới chuột rút do nóng.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
        elif ((nhietdo >=32) & (nhietdo >41)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này có thể gây ra chuột rút do nóng và kiệt sức do nóng. Tiếp tục hoạt động có thể dẫn tới sốc nhiệt.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
        elif ((nhietdo >=20) & (nhietdo <27)):
            content = """Nhiệt độ ngày {day}/{month}/{year} là {temp} độ C
Trời hôm nay nhiều mây. Dự báo mưa rải rác ở một số nơi. 
Nhiệt độ này cơ thể cảm thấy dễ chịu, hoạt động tối ưu mà không thấy hoặc có rất ít các rối loạn xảy ra.""".format(day = now.day,month = now.month, year= now.year,temp = nhietdo)
            maynoi(content)
            print (content)
    else:
        maynoi("Không tìm thấy địa chỉ của bạn")
def send_email():
    maynoi('Bạn muốn gửi email cho ai nhỉ')
    recipient = input()
    print("You: " + recipient)
    
    if 'tôi' in recipient:
        maynoi('Nội dung bạn muốn gửi là gì')
        content = input()
        print("You: " + content)
        mail = smtplib.SMTP('smtp.gmail.com', 587)
        mail.ehlo()
        mail.starttls()
        mail.login('dieptanluanhcmute@gmail.com', '0898654463')
        mail.sendmail('dieptanluancanhan@gmail.com','dieptanluantvq@gmail.com', content.encode('utf-8'))
        mail.close()
        maynoi('Email của bạn vùa được gửi. Bạn check lại email nhé.')
        print("Bot: Email của bạn vùa được gửi. Bạn check lại email nhé.")
    else:
        print('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
        maynoi('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
def guimailgiongnoi():
    maynoi('Bạn muốn gửi email cho ai nhỉ')
    with speech_recognition.Microphone() as mic:
            print("Bot: I'm Listening")
            audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
            print("Bot: ...")
            try:
                you = nghe.recognize_google(audio, language='vi-VN')
            except:
                you = ""
                print ("Mình không nghe được gì cả")
                brain = "Mình không nghe được gì cả"
                maynoi(brain)
            if 'tôi' in you:
                maynoi('Nội dung bạn muốn gửi là gì')
                with speech_recognition.Microphone() as mic:
                    print("Bot: I'm Listening")
                    audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
                    print("Bot: ...")
                    try:
                        you = nghe.recognize_google(audio, language='vi-VN')
                    except:
                        you = ""
                        print ("Mình không nghe được gì cả")
                        brain = "Mình không nghe được gì cả"
                        maynoi(brain)
                mail = smtplib.SMTP('smtp.gmail.com', 587)
                mail.ehlo()
                mail.starttls()
                mail.login('dieptanluanhcmute@gmail.com', '0898654463')
                mail.sendmail('dieptanluancanhan@gmail.com',
                                  'dieptanluantvq@gmail.com', you.encode('utf-8'))
                mail.close()
                print("Bot: Email của bạn vùa được gửi. Bạn check lại email nhé.")
                maynoi('Email của bạn vùa được gửi. Bạn check lại email nhé hihi.')
            else:
                print('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
                maynoi('Bot không hiểu bạn muốn gửi email cho ai. Bạn nói lại được không?')
                   
exit_list = ['exit', 'see you later', 'bye', 'tạm biệt', 'thoát', 'quit', 'dừng lại', 'dừng']
chaohoi_list = ['xin chào', 'chào',' hi','hello', 'hey', 'alo']
phantich_list = ['tôi muốn', 'khả năng', 'đạt', 'sv5t', 'phân tích', 'kết quả']
lichlamviec = {'thứ tư' : 'Thi cuối kì môn Cơ sở dữ liệu lúc 12h30',
    'hôm nay': 'Thứ năm ngày 10/6/2021, Bạn sẽ thi cuối kì môn Anh Văn lúc 9h00 và báo cáo đồ án môn Trí tuệ nhân tạo lúc 13h30'}
def tralichlamviec():
    brain = "Bạn muốn xem lịch làm việc ngày nào"
    print(brain)
    maynoi(brain)
    date = input()
    print("You: " + date)
    if date in lichlamviec:
        a = lichlamviec[date]
        print("Bot: " + a)
        maynoi(a)
    else:
        print("Bot: Bạn không có lịch làm việc nào")
        maynoi("Bạn không có lịch làm việc nào")
def tralichlamviecgiongnoi():
    brain = "Bạn muốn xem lịch làm việc ngày nào"
    maynoi(brain)
    with speech_recognition.Microphone() as mic:
        print("Bot: I'm Listening")
        audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
        print("Bot: ...")
        try:
            date = nghe.recognize_google(audio, language='vi-VN')
        except:
            date = ""
            print ("Mình không nghe được gì cả")
            brain = "Mình không nghe được gì cả"
            maynoi(brain)
    if date in lichlamviec:
        a = lichlamviec[date]
        print(a)
        maynoi(a)
    else:
        print("Bot: Bạn không có lịch làm việc nào")
        maynoi("Bạn không có lịch làm việc nào")

    
#Hàm main
welcome()
brain = """Bạn muốn trao đổi bằng cách nào:
    1. Text chat.
    2. Voice chat"""
print("DTL's Bot: " + brain)
maynoi(brain)
choose = int(input("Lựa chọn của bạn là: "))
if (choose == 1):
    print("Chúng tôi có thể giúp gì được cho bạn?")
    maynoi("Chúng tôi có thể giúp gì được cho bạn?")
    while True:
        try:
            you = input("Bạn: ");
        except:
            you = ""
            print ("DTL's Bot: Mình không nghe được gì cả")
            brain = "Mình không nghe được gì cả"
            maynoi(brain)
        #Dịch ngôn ngữ Anh - Việt or Việt - Anh
        if "dịch" in you or "tiếng" in you or "ngôn ngữ" in you:
            dichngonngu()
        #Phân tích kết quả học tập
        if you.lower() in phantich_list:
            phantichketqua()
        #Xem lịch làm việc
        if "lịch làm việc" in you or "lịch" in you:
            tralichlamviec()
        #Tra cứu trên google
        elif "google" in you or "gg" in you:
            brain = "Bạn muốn tìm kiếm gì ở google?"
            print("DTL's Bot: " + brain)
            maynoi(brain)
            search = input("Bạn: ").lower();
            url =f"https://www.google.com.vn/search?q={search}"
            webbrowser.get().open(url)
            maynoi(f"Đây là kết quả của {search} ở google")
        #Tra cứu trên youtube
        elif "youtube" in you or "ytb" in you:
            brain = "Bạn muốn tìm kiếm gì ở Youtube?"
            print("DTL's Bot: " + brain)
            maynoi(brain)
            search = input("Bạn: ").lower();
            url =f"https://www.youtube.com/search?q={search}"
            webbrowser.get().open(url)
            maynoi(f"Đây là kết quả của {search} ở Youtube")
        #Mở ứng dụng trên máy tính
        elif 'word' in you or 'soạn thảo' in you or 'văn bản' in you:
            os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
            maynoi("Đây là ứng dụng Word bạn cần")
        elif 'excel' in you or 'trang tính' in you:
            os.startfile("C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
            maynoi("Đây là ứng dụng Excel bạn cần")
        #Gửi mail
        elif 'gửi mail' in you:
            send_email()
        #Mở facebook
        elif "mở" in you or "fb" in you or "facebook" in you:
            webbrowser.open("https://www.facebook.com/")
            brain = "Facebook đã được mở"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        #Dự báo thời tiết
        elif 'thời tiết' in you or "nhiệt độ" in you:
            dubaothoithiet()
        #Bài hát yêu thích
        elif 'mở' in you or "yêu thích" in you or "bài hát" in you:
            webbrowser.open("https://www.youtube.com/watch?v=JINe0-Ojtng&ab_channel=B-WildOfficialB-WildOfficial")
            brain = "Đây là bài hát yêu thích của bạn"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        #Những thứ cần cho hồ sơ
        elif "cần" in you or "hồ sơ" in you:
            webbrowser.open("https://www.facebook.com/groups/itute.sv5t/permalink/1276509442714733/")
            brain = "Đây là những thứ cần cho hồ sơ của bạn"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "nộp hồ sơ" in you or "ở đâu" in you:
            brain = "Để nộp hồ sơ, bạn vui lòng gửi file mềm về mail: yit@hcmute.edu.vn bạn nhé!"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "tiêu chí" in you or "5 tiêu chí" in you:
            brain = "5 tiêu chí để đạt sinh viên 5 tốt là: Đạo đức tốt, học tập tốt, thể lực tốt, tình nguyện tốt, hội nhập tốt"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "đạo đức tốt" in you or "đạo đức" in you:
            brain = "Để đạt được tiêu chí đạo đức tốt. Bạn cần KHÔNG VI PHẠM NỘI QUY NHÀ TRƯỜNG. Điểm rèn luyện trung bình năm học 2020 2021 đạt từ 80 điểm trở lên."
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "học tập tốt" in you  or "học tập" in you:
            brain = "Để đạt được tiêu chí học tập tốt. Bạn cần Không nợ môn. Điểm trung bình chung học tập cả năm đạt từ 7 chấm 5 trở lên và Tham gia đóng góp ít nhất 1 ý tưởng sáng tạo trên Cổng thông tin ý tưởng sáng tạo Thành phố Hồ Chí Minh."
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "thể lực tốt" in you or "thể lực" in you:
            brain = "Để đạt được tiêu chí thể lực tốt. Bạn cần tham gia các hoạt động sát hạch thể chất và đạt danh hiệu “Thanh niên khỏe” từ cấp trường trở lên"
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "tình nguyện tốt" in you or "tình nguyện" in you:
            brain = "Để đạt được tiêu chí tình nguyện tốt. Bạn cần tham gia và nhận giấy chứng nhận hoàn thành 1 trong các chiến dịch, chương trình sau: Chiến dịch Mùa hè xanh 2021, chiến dịch Xuân tình nguyện 2021, chương trình Tiếp sức mùa thi 2021 HOẶC Tham gia và đạt được ít nhất 20 điểm công tác xã hội/năm học."
            print("DTL's Bot: " + brain)
            maynoi(brain)
        elif "hội nhập tốt" in you or "hội nhập" in you:
            brain = "Để đạt được tiêu chí hội nhập tốt. Bạn cần đạt chứng chỉ tiếng Anh trình độ B1 hoặc có điểm trung bình các học phần ngoại ngữ đạt từ 7 chấm 5 trở lên. Đối với K19, K20 phải đạt TOEIC 420 điểm và K17,K18 phải đạt TOEIC 450 điểm"
            print("DTL's Bot: " + brain)
            maynoi(brain)   
        #Thoát
        elif you.lower() in exit_list:
            brain = "Xin chào và hẹn gặp lại"
            print("DTL's Bot: " + brain)
            maynoi(brain)
            break
        
#Bằng giọng nói
elif (choose == 2):
    print("Chúng tôi có thể giúp gì được cho bạn?")
    maynoi("Chúng tôi có thể giúp gì được cho bạn?")
    while True:
        with speech_recognition.Microphone() as mic:
            print("Bot: I'm Listening")
            audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
            print("Bot: ...")
            try:
                you = nghe.recognize_google(audio, language='vi-VN')
            except:
                you = ""
                print ("Mình không nghe được gì cả")
                brain = "Mình không nghe được gì cả"
                maynoi(brain)
            #Dịch ngôn ngữ Anh - Việt or Việt - Anh
            if "dịch" in you or "tiếng" in you or "ngôn ngữ" in you:
                dichngonngugiongnoi()
            #Phân tích kết quả học tập
            if you in phantich_list:
                phantichketqua()
            #Gửi mail
            elif "gửi mail" in you:
                guimailgiongnoi()
            #Xem lịch làm việc
            elif "lịch làm việc" in you or "lịch" in you:
                tralichlamviecgiongnoi()
            #Tra cứu trên google
            elif "google" in you or "tra" in you:
                brain = "Bạn muốn tìm kiếm gì ở google?"
                print("DTL's Bot: " + brain)
                maynoi(brain)
                with speech_recognition.Microphone() as mic:
                    print("Bot: I'm Listening")
                    audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
                    print("Bot: ...")
                    try:
                        you = nghe.recognize_google(audio, language='vi-VN')
                    except:
                        you = ""
                        print ("Mình không nghe được gì cả")
                        brain = "Mình không nghe được gì cả"
                        maynoi(brain)
                url =f"https://www.google.com.vn/search?q={you}"
                webbrowser.get().open(url)
                maynoi(f"Đây là kết quả của {you} ở google")
            #Tra cứu trên youtube
            elif "youtube" in you or "tìm kiếm" in you:
                brain = "Bạn muốn tìm kiếm gì ở youtube?"
                print("DTL's Bot: " + brain)
                maynoi(brain)
                with speech_recognition.Microphone() as mic:
                    print("Bot: I'm Listening")
                    audio = nghe.listen(mic, timeout=5, phrase_time_limit=5)
                    print("Bot: ...")
                    try:
                        you = nghe.recognize_google(audio, language='vi-VN')
                    except:
                        you = ""
                        print ("Mình không nghe được gì cả")
                        brain = "Mình không nghe được gì cả"
                        maynoi(brain)
                url =f"https://www.youtube.com/search?q={you}"
                webbrowser.get().open(url)
                maynoi(f"Đây là kết quả của {you} ở youtube")
            #Mở ứng dụng trên máy tính
            elif 'word' in you or 'soạn thảo' in you or 'văn bản' in you:
                os.startfile("C:/Program Files (x86)/Microsoft Office/root/Office16/WINWORD.EXE")
                maynoi("Đây là ứng dụng Word bạn cần")
            elif 'excel' in you or 'trang tính' in you:
                os.startfile("C:\Program Files (x86)\Microsoft Office\root\Office16\EXCEL.EXE")
                maynoi("Đây là ứng dụng Excel bạn cần")
            #Mở facebook
            elif "facebook" in you or "mở" in you:
                webbrowser.open("https://www.facebook.com/")
                brain = "Facebook đã được mở"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            #Dự báo thời tiết
            if 'thời tiết' in you or "nhiệt độ" in you:
                dubaothoitietgiongnoi()
            #Bài hát yêu thích
            elif "yêu thích" in you or "bài hát" in you:
                webbrowser.open("https://www.youtube.com/watch?v=JINe0-Ojtng&ab_channel=B-WildOfficialB-WildOfficial")
                brain = "Đây là bài hát yêu thích của bạn"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            #Những thứ cần cho hồ sơ
            elif "cần" in you or "hồ sơ" in you:
                webbrowser.open("https://www.facebook.com/groups/itute.sv5t/permalink/1276509442714733/")
                brain = "Đây là những thứ cần cho hồ sơ của bạn"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "nộp" in you or "ở đâu" in you or "cách thức" in you:
                brain = "Để nộp hồ sơ, bạn vui lòng gửi file mềm về mail: yit@hcmute.edu.vn bạn nhé!"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "tiêu chí" in you or "5 tiêu chí" in you:
                brain = "5 tiêu chí để đạt sinh viên 5 tốt là: Đạo đức tốt, học tập tốt, thể lực tốt, tình nguyện tốt, hội nhập tốt"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "đạo đức tốt" in you or "đạo đức" in you:
                brain = "Để đạt được tiêu chí đạo đức tốt. Bạn cần KHÔNG VI PHẠM NỘI QUY NHÀ TRƯỜNG. Điểm rèn luyện trung bình năm học 2020 2021 đạt từ 80 điểm trở lên."
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "học tập tốt" in you  or "học tập" in you:
                brain = "Để đạt được tiêu chí học tập tốt. Bạn cần Không nợ môn. Điểm trung bình chung học tập cả năm đạt từ 7 chấm 5 trở lên và Tham gia đóng góp ít nhất 1 ý tưởng sáng tạo trên Cổng thông tin ý tưởng sáng tạo Thành phố Hồ Chí Minh."
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "thể lực tốt" in you or "thể lực" in you:
                brain = "Để đạt được tiêu chí thể lực tốt. Bạn cần tham gia các hoạt động sát hạch thể chất và đạt danh hiệu “Thanh niên khỏe” từ cấp trường trở lên"
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "tình nguyện tốt" in you or "tình nguyện" in you:
                brain = "Để đạt được tiêu chí tình nguyện tốt. Bạn cần tham gia và nhận giấy chứng nhận hoàn thành 1 trong các chiến dịch, chương trình sau: Chiến dịch Mùa hè xanh 2021, chiến dịch Xuân tình nguyện 2021, chương trình Tiếp sức mùa thi 2021 HOẶC Tham gia và đạt được ít nhất 20 điểm công tác xã hội/năm học."
                print("DTL's Bot: " + brain)
                maynoi(brain)
            elif "hội nhập tốt" in you or "hội nhập" in you:
                brain = "Để đạt được tiêu chí hội nhập tốt. Bạn cần đạt chứng chỉ tiếng Anh trình độ B1 hoặc có điểm trung bình các học phần ngoại ngữ đạt từ 7 chấm 5 trở lên. Đối với K19, K20 phải đạt TOEIC 420 điểm và K17,K18 phải đạt TOEIC 450 điểm"
                print("DTL's Bot: " + brain)
                maynoi(brain)   
            #Thoát
            elif you in exit_list:
                brain = "Xin chào và hẹn gặp lại"
                print("DTL's Bot: " + brain)
                maynoi(brain)
                break
elif ((choose !=1) & (choose != 2)): 
    brain = "Lựa chọn của bạn chưa đúng"
    maynoi(brain)