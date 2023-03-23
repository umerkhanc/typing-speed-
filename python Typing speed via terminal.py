import time

# Get the text to type
text_to_type = input("Type the following text: ")
#user_input = input("What was most unique about the terrorist attacks of 11 September were not the acts themselves but the response to them, beginning with the US President· s response on 12 September. No war on terrorism had been declared after the Oklahoma City bombing. There was no suspensi,m nr fundamental constitutional protections and no rush to legislate even greater restrictions. No indefinite detention without charge or trial. No denial of legal advice and representation. No suggestion that torture should be permitted and authorised. The US President's response on 12 September was unique, unleashing a global colT'mitment to fight terrorism without regard for national boundaries or international law. Worldwide sympathy for the United States and worldwide condemnation of terrorism followed the attacks on 11 September. There is no dispute about the nature of terrorism or about its intrinsic evil. But there is grave dispute about the nature of the response to terrorism, most manifest now in relation to the War against Iraq. Around the world the war on terrorism has led to increased security, increased surveillance of the general population and of specific groups and increased powers for police and intelligence agencies.The United States led the way with the mass detentions of hundreds of inunigrants who were West Asian or North African in origin or Islamic in belief. Very few of these people were charged with any criminal offence. Many were held for periods of many months on immigration grounds. Theywere denied their right to silence, denied access to legal advice and representation, prevented from contacting their families and brought before closed courts to be dealt with in secret. The United States also led the way with new legislation to restrict human rights. The most extreme expression of this new US approach is found in the situation in Camp X-ray at the US base at Guantanamo Bay in Cuba. Captured Taliban and Al Qaida suspects are held there without the protection either of international humanitarian law or international human rights law. The  US Administration has said that the provisions in Geneva Conventions on the treatinent of prisoners of war do not apply to these detainees. And so those protections have been violated. Detainees have also been denied the protection of rights guaranteed under the US constitution and the US courts have refused to intervene. They are held in inhumane conditions, subjected to inhuman and degrading treatinent and perhaps torture and denied due process rights, including the right to legal advice and representation and the right to be charged and tried openly before an independent tribunal. International human rights law itself permits restrictions on the enjoyment of human rights in emergency circumstances. Article 4 of the International Covenant on Civil and Political Rights provides that some human rights may he restricted in "time of public emergency which threatens the life of the nation" provided that the emergency is officially proclaimed and is notified to the United Nations Secretary General, that measures taken under the state of eme1gency are no more than what is "strictly required by the exigencies of the situation" and that the measures do not discriminate 011 the basis of race, colour, sex, language, religion or social origin.Dew;c,oes in U.K. prisons have complained oflong penods of isolation; lack of access to health car~, t:xercise of :eligion, and educational services; lack of exercise; obstacles to visits from friends: ")

# Get the start time
start_time = time.time()

# Ask the user to type the text
user_input = input("Type the text again: ")

# Get the end time
end_time = time.time()

# Calculate the typing speed in words per minute
num_words = len(text_to_type.split())
typing_time = end_time - start_time
typing_speed = num_words / typing_time * 60

# Print the typing speed
print("Your typing speed is {:.2f} WPM.".format(typing_speed))