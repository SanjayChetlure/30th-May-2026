#Super class
class WhatsAppV1:
   def chat(self):
       print("chat feature")

#Super/sub class
class WhatsAppV2(WhatsAppV1):
   def audioCalling(self):
       print("Audio Calling Feature")

   # def chat(self):
   #     print("chat feature")

#sub class
class WhatsAppV3(WhatsAppV2):
   def videoCalling(self):
       print("Audio Calling Feature")

   # def audioCalling(self):
   #     print("Audio Calling Feature")

   # def chat(self):
   #     print("chat feature")


w3=WhatsAppV3()
w3.chat()
w3.audioCalling()
w3.videoCalling()
