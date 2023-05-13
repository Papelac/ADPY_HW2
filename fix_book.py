import re

def FIO(phone_book_string):
   lastname = phone_book_string[0].split()
   if len(lastname)>2:
      phone_book_string[0] = lastname[0] 
      phone_book_string[1] = lastname[1] 
      phone_book_string[2] = lastname[2] 
   elif len(lastname)>1:
      phone_book_string[0] = lastname[0] 
      phone_book_string[1] = lastname[1] 
   firstname = phone_book_string[1].split()
   if len(firstname)>1:
        phone_book_string[1] = firstname[0] 
        phone_book_string[2] = firstname[1] 

def Phone(phone_book_string):
    #+7(999)999-99-99 доб.9999
    pattern = r"(8|\+7)\s*\(*([0-9]{3})\)*[-\s+]?([0-9]{3})[-\s+]?([0-9]{2})[-\s+]?([0-9]{2})(\s+?\(?\доб.\s+(\d+))?"
    result = re.search(pattern, phone_book_string[5])
    if result:
      try:
         add_number = ' доб.' + result.group(7)
      except:
         add_number = ''
      #print('+7(' + result.group(2) + ')' + result.group(3) + '-' + result.group(4) + '-' + result.group(5) + add_number)
      phone_book_string[5] = '+7(' + result.group(2) + ')' + result.group(3) + '-' + result.group(4) + '-' + result.group(5) + add_number
            
def Equal_date(contacts_list):
   size_of_list = len(contacts_list)-1
   size_of_record = len(contacts_list[0])
   i = 1
   while i < size_of_list:
      FI = contacts_list[i][0] + contacts_list[i][1]
      #print(FI)
      x = i + 1
      while x < size_of_list+1:
         if FI == contacts_list[x][0] + contacts_list[x][1]:
            z = 3
            for z in range(size_of_record):
               if not contacts_list[i][z].strip():
                  contacts_list[i][z] = contacts_list[x][z]
            contacts_list.remove(contacts_list[x])
            size_of_list -=1
            x -=1
         x +=1
      i +=1
