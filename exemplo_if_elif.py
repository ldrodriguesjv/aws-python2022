"""
Your module description
"""
userReply = input("Você gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Enter selos, envelope ou cópia) ")
if userReply == "selos":
    print("Temos muitos designs de selos para escolherem.")
elif userReply == "envelope":
    print("Temos muitos tamanhos de envelopes para escolher.")
elif userReply == "cópia":
    copies = input("Quantas cópias você gostaria? (Digite um número) ")
    print("Aqui estão {} cópias.".format(copies))
else:
    print("Obrigado, volte sempre.")
    
  
