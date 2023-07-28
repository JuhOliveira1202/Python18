#Exercício 21:
#Escreva uma função que calcule a seguinte função
#x/(Y-6)
#Mas que imprima uma mensagem sempre que o denominador for igual a zero.

def divisao():
    try:
        x=int(input("valor de x"))
        y=int(input("valor de y"))
        resultado = x/(y-6)
        
    except ZeroDivisionError:
        print("erro não é possível dividir por zero")

    except ValueError:
        print ("erro não é introduziu valores inteiros!")

    except:
        print("outro tipo de erro")

    else:
        print("resultado = ", resultado)

    finally:
        print("Obrigado, volte sempre")

divisao() 
    
    
    
