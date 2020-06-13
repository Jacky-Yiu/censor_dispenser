# These are the emails you will be censoring. The open() function is opening the text file that the emails are contained in and the .read() method is allowing us to save their contexts to the following variables:
email_one = open("email_one.txt", "r").read()
email_two = open("email_two.txt", "r").read()
email_three = open("email_three.txt", "r").read()
email_four = open("email_four.txt", "r").read()


def split_word(string):
  sp = string.split("\n")
  sp_2 = []
  for i in sp:
    sp_2.append(i.split(" "))
  return sp_2 #return a list of word from a string

def join_string(lst):
  sp_3=[]
  for i in lst:
    sp_3.append(" ".join(i))
  return "\n".join(sp_3) #return a sring from list of word

def block_word(string): #maintain string lenght
  block=[]
  for i in range(len(string)):
    block.append("#")
  return "".join(block)

def no_word(string): # maintain before and after lenght
  block=[]
  for i in range(len(string)):
    block.append("*")
  return "".join(block)

#=========================================================
def censor(email,censor):
  splited_txt_lst = split_word(email)
  splited_censor_lst = censor.split(" ")

  #print(splited_txt_lst)

  for i in range(len(splited_txt_lst)):
    for k in range(len(splited_txt_lst[i])):
      counter=0
      for m in range(len(splited_censor_lst)):
        
        #print(f"txt[{i}][{k}]", splited_txt_lst[i][k].lower(), f"::txt[{j}]",splited_censor_lst[j])
        try:
          if splited_txt_lst[i][k+m].lower() == splited_censor_lst[m]:
            #print("found it")
            counter+=1
          if (splited_txt_lst[i][k+m].find(',') != -1): 
            splited_txt_lst[i][k+m] = splited_txt_lst[i][k+m].strip(",")
            if splited_txt_lst[i][k+m].lower() == splited_censor_lst[m]:
              counter+=1
            splited_txt_lst[i][k+m] = "".join([splited_txt_lst[i][k+m],","])

          elif (splited_txt_lst[i][k+m].find('.') != -1): 
            splited_txt_lst[i][k+m] = splited_txt_lst[i][k+m].strip(".")
            if splited_txt_lst[i][k+m].lower() == splited_censor_lst[m]:
              counter+=1
            splited_txt_lst[i][k+m] = "".join([splited_txt_lst[i][k+m],"."])

          else: 
            continue 
        #exclue index error
        except IndexError:
          continue

      #counter check

      if counter == len(splited_censor_lst):
        for m in range(len(splited_censor_lst)):
          splited_txt_lst[i][k+m]= splited_txt_lst[i][k+m].lower()
          splited_txt_lst[i][k+m]= splited_txt_lst[i][k+m].replace(splited_censor_lst[m], block_word(splited_censor_lst[m]))

  fixed_email = join_string(splited_txt_lst)
  return fixed_email

#print(censor(email_one,"learning algorithms"))

#==============================================================
def censor_list(email, lst):
  fixed_email = email
  for item in lst:
    fixed_email=censor(fixed_email,item)
  return fixed_email

proprietary_terms = ["she", "personality matrix", "sense of self", "self-preservation", "learning algorithm", "her", "herself"]

#print(censor_list(email_two, proprietary_terms))

#=================================================================

def censor_more_than_twice(email, lst):
  fixed_mail = email
  splited_txt_lst = split_word(email)
  #print(splited_txt_lst)

  for negative_word in lst:
    counter=0
    for i in range(len(splited_txt_lst)):
      for k in range(len(splited_txt_lst[i])):
        #print(f"txt[{i}][{k}]", splited_txt_lst[i][k].lower(), f"::{negative_word}")
        try:
          if splited_txt_lst[i][k].lower() == negative_word:
            #print("found it")
            counter+=1
          if (splited_txt_lst[i][k].find(',') != -1): 
            splited_txt_lst[i][k] = splited_txt_lst[i][k].strip(",")
            if splited_txt_lst[i][k].lower() == negative_word:
              counter+=1
            splited_txt_lst[i][k] = "".join([splited_txt_lst[i][k],","])
          else: 
            continue 
          #exclue index error
        except IndexError:
          continue
    #counter check
    print(negative_word,counter)
    if counter > 1:
      fixed_mail=censor(fixed_mail,negative_word)
    
  fixed_mail=censor_list(fixed_mail, proprietary_terms)
  return fixed_mail

negative_words = ["concerned", "behind", "danger", "dangerous", "alarming", "alarmed", "out of control", "help", "unhappy", "bad", "upset", "awful", "broken", "damage", "damaging", "dismal", "distressed", "distressed", "concerning", "horrible", "horribly", "questionable"]

#print(censor_more_than_twice(email_three, negative_words))
#=============================================================

def censor_before_after(email):
  fixed_email=censor_more_than_twice(email, negative_words)
  splited_txt_lst = split_word(fixed_email)
  #print(splited_txt_lst)
  for i in range(len(splited_txt_lst)):
    for k in range(len(splited_txt_lst[i])):
      try:
        if splited_txt_lst[i][k].find("#") != -1:
          b_word = no_word(splited_txt_lst[i][k-1])
          splited_txt_lst[i][k-1]= b_word
      except IndexError:
        a=1
      
      try:
        if splited_txt_lst[i][k].find("#") != -1:
          b_word = no_word(splited_txt_lst[i][k+1])
          splited_txt_lst[i][k+1]= b_word
      except IndexError:
        a=1
  fixed_email = join_string(splited_txt_lst)
  return fixed_email



print (censor_before_after(email_four))


  
  












