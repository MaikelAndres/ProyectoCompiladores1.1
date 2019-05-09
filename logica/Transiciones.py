import Pila
#clase padre
class Trans:
    
    def __init__(self):
        self.pila = Pila.Pila()
        self.p_1 = True
        self.q_2 = False
        self.r_final = False

    def getP_1(self):
        return self.p_1
    def getQ_2(self):
        return self.q_2
    def getR_final(self):
        return self.r_final

    def activaP_1(self):
        self.p_1=True
        self.q_2=False
        self.r_final=False

    def activaQ_2(self):
        self.q_2=True
        self.p_1=False
        self.r_final=False

    def activaR_final(self):
        self.r_final=True
        self.p_1=False
        self.q_2=False

    #transiciones con b
    def b_b_bb(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('b')
        self.activaP_1()

    def b_a_ab(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('b')
        self.activaP_1()
    def b_n_nb(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('b')
        self.activaP_1()
        
    #transiciones con a
    def a_b_ba(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.pila.apilar('a')
        self.activaP_1()
    def a_n_na(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.pila.apilar('a')
        self.activaP_1()
    def a_a_aa(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.pila.apilar('a')
        self.activaP_1()
        
    #transiciones con c
    def c_n_n(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.activaQ_2()
    def c_b_b(self):
        self.pila.quitar()
        self.pila.apilar('b')
        self.activaQ_2()
    def c_a_a(self):
        self.pila.quitar()
        self.pila.apilar('a')
        self.activaQ_2()

    def b_b_y(self):
        self.pila.quitar()
        self.activaQ_2()

    def a_a_y(self):
        self.pila.quitar()
        self.activaQ_2()

    def y_n_n(self):
        self.pila.quitar()
        self.pila.apilar('#')
        self.activaR_final()

    def validar(self):
        return True
      
      
