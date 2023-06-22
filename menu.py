class padre():
    def __init__(self):
        print("Esta es la clase made")
        
    def menu(dish):
        if dish=="Hamburgesa":
            print("Pediste una hamburgesa")
            print("Si quieres puedes añadir queso o jalapeño a tu hamburgesa y tendria un costo extra")
            
        elif dish=="Cafe":
            print("Pediste un cafe")
            print("Si quieres puedes añadir caramelo o chocolate a tu cafe y tendria un costo extra")
            
        else :
            print("Ingresa algo valido")
            
    def addons(dish,new_addons):
        if dish=="Hamburgesa" and new_addons=="Queso":
            print("Pediste una hamburgesa con queso $10")
            
        elif dish=="Hamburgesa" and new_addons=="Jalapeño":
            print("Pediste una hamburgesa con jalapeños $10")
            
        elif dish=="Cafe" and new_addons=="Caramelo":
            print("Pediste un cafe con caramelo $10")
            
        elif dish=="Cafe" and new_addons=="Chocolate":
            print("Pediste un cafe con chocolate $10")
        
        
    
        
        
        
        
        
            
        
class hijo1(padre):
    def __init__(self,dish):
        self.new_dish=dish
        
    def get_menu(self):
        padre.menu(self.new_dish)

class hijo2(padre):
    def __init__(self,dish,addons):
        self.new_dish=dish
        self.new_addons=addons
        
    def get_addons(self):
        padre.addons(self.new_dish,self.new_addons)

        
niño1=hijo1("Cafe")
niño1.get_menu()
niño2=hijo2("Cafe", "Chocolate")
niño2.get_addons()    
    
    