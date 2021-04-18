class budget:
  def __init__(self,food,clothing,entertainment):
    self.food = food
    self.clothing = clothing
    self.entertainment = entertainment
    self.balance_food = 1000
    self.balance_clothing = 500
    self.balance_entertainment = 100


  def deposit(self):
    print('what do you want to deposit for?')
    print('1. food')
    print('2. clothing')
    print('3. entertainment')

    option = int(input('select an option \n'))

    if option ==1:
      amount_Deposited = int(input('How much do you want to deposit for %s \n' %self.food))
      print('You have successfull deposited $%d for %s'%(amount_Deposited,self.food))
      self.balance_food = amount_Deposited + self.balance_food
      print('Your current balance on food is: ',self.balance_food)

    elif option ==2:
      amount_Deposited = int(input('How much do you want to deposit for %s \n' %self.clothing))
      print('You have successfull deposited $%d for %s'%(amount_Deposited,self.clothing))
      self.balance_clothing = amount_Deposited + self.balance_clothing
      print('Your current balance on clothing is: ',self.balance_clothing)

    elif option == 3:
      amount_Deposited = int(input('How much do you want to deposit for %s \n' %self.entertainment))
      print('You have successfull deposited $%d for %s'%(amount_Deposited,self.entertainment))
      self.balance_entertainment = amount_Deposited + self.balance_entertainment
      print('Your current balance on entertainment is: ',self.balance_entertainment)

    else:
      print('Invalid options')


  def withdraw(self):
    print('what category do you want to withdraw from?')
    print('1. food')
    print('2. clothing')
    print('3. entertainment')

    withdrawOption = int(input('select an option \n'))

    if withdrawOption ==1:
      amount_withdrew = int(input('How much do you want to withdraw from %s \n' %self.food))
      print('You have successfull withdrew $%d for %s'%(amount_withdrew,self.food))
      self.balance_food = self.balance_food - amount_withdrew
      print('Your current balance on food is: ', self.balance_food)

    elif withdrawOption ==2:
      amount_withdrew = int(input('How much do you want to withdraw from %s \n' %self.clothing))
      print('You have successfull withdrew $%d for %s'%(amount_withdrew,self.clothing))
      self.balance_clothing = self.balance_clothing - amount_withdrew
      print('Your current balance on clothing is: ', self.balance_clothing)

    elif withdrawOption == 3:
      amount_withdrew = int(input('How much do you want to withdraw from %s \n' %self.entertainment))
      print('You have successfull withdrew $%d for %s'%(amount_withdrew,self.entertainment))
      self.balance_entertainment = self.balance_entertainment - amount_withdrew
      print('Your current balance on entertainment is: ', self.balance_entertainment)

    else:
      print('Invalid options')



  def balance(self):
    print('Your current balance on clothing is: ', self.balance_clothing)
    print('Your current balance on entertainment is: ', self.balance_entertainment)
    print('Your current balance on Food is: ', self.balance_food)


  def transfer(self):  
    print('Take fund from:')
    print('1. Food')
    print('2. Clothing')
    print('3. entertainment')
    fund = int(input('select option from above \n'))

    print('what category do you what to tranfer money to:')
    print('1. Food')
    print('2. Clothing')
    print('3. entertainment')
    category = int(input('put your category \n'))

    amount = int(input('How much do you wish to transfer to selected category \n'))

    if fund == 1:
      if category == 2:
        new = self.balance_food - amount
        self.balance_clothing  = self.balance_clothing + new
        print('Your new clothing balance is : ',self.balance_clothing)
      elif category == 3:
        new = self.balance_food - amount
        self.balance_entertainment = self.balance_entertainment + new
        print('Your new entertainment balance is : ', self.balance_entertainment)
      else:
        exit()
    
    if fund == 2:
      if category == 1:
        new = self.balance_clothing - amount
        self.balance_food  = self.balance_food + new
        print('Your new Food balance is : ', self.balance_food)
      elif category == 3:
        new = self.balance_clothing - amount
        self.balance_entertainment = self.balance_entertainment + new
        print('Your new entertainment balance is : ', self.balance_entertainment)
      else:
        exit()

    if fund == 3:
      if category == 1:
        new = self.balance_entertainment - amount
        self.balance_food  = self.balance_food + new
        print('Your new Food balance is : ' ,self.balance_food)
      elif category == 2:
        new = self.balance_entertainment - amount
        self.balance_clothing = self.balance_clothing + new
        print('Your new clothing balance is : ', self.balance_clothing)
      else:
        exit()





  








customer_1 =budget('Amala','Cap','Games')
customer_1.deposit()
customer_1.withdraw()
customer_1.balance()
customer_1.transfer()