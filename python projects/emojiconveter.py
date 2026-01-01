# mini project : Emoji conveter 
# convert text - besed emotions into emojs

emoji= input("Enter your sentance and  emotion here  :) 😊   , :( 😌 :D 😀 , ;)😉, :: 😍 ;;❤️ :--")
emoji= emoji.replace(":)","😊")
emoji=emoji.replace(":(","😌")
emoji=emoji.replace(":D","😀")
emoji= emoji.replace(";)","😉")
emoji= emoji.replace("::","😍")
emoji=emoji.replace(";;","❤️")
print(emoji)