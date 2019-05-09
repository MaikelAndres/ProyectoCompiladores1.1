from Transiciones import Trans

class Automatapila(Trans):

    def __init__(self):
        Trans.__init__(self)
        self.resultado=[]
        self.transiciones=[]
        self.palabra="aababcbabaa"
    
    def __init__(self,palabra):
        Trans.__init__(self)
        self.resultado=[]
        self.transiciones=[]
        self.palabra=palabra

    

    def validar(self):
        palabra=self.palabra+'  '
        
      

        for caracter in palabra:
            paso = "{:6} |  {:6}  |  {:6} |   {:4} | {:4} ".format(str(self.getP_1()), str(self.getQ_2()),
                                                                                                               str(self.getR_final()),str(caracter),str(self.pila.tope()))
            self.resultado.append(paso)

            if (caracter != 'a' and caracter != 'b' and caracter != 'c'  and caracter != ' '):
                invali='El caracter es invalido!!!'
                self.resultado.append(invali)
                break
            elif (self.getP_1()):
                if (caracter=='b'):
                    if (self.pila.tope()== 'b'):
                        self.b_b_bb()
                        trans='|b/b/bb|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.b_a_ab()
                        trans='|b/a/ab|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.b_n_nb()
                        trans='|b/#/#b|'
                        self.transiciones.append('      '+trans)
                elif (caracter ==  'a'):
                    if (self.pila.tope()== 'b'):
                        self.a_b_ba()
                        trans='|a/b/ba|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.a_a_aa()
                        trans='|a/a/aa|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.a_n_na()
                        trans='|a/#/#a|'
                        self.transiciones.append('      '+trans)
                elif (caracter == 'c'):
                    if (self.pila.tope()== 'b'):
                        self.c_b_b()
                        trans='|c/b/b|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope()== 'a'):
                        self.c_a_a()
                        trans='|c/a/a|'
                        self.transiciones.append('      '+trans)
                    elif (self.pila.tope() == '#'):
                        self.c_n_n()
                        trans='|c/#/#|'
                        self.transiciones.append('      '+trans)
            elif (self.getQ_2()):
                if (caracter == 'b'):
                    if (self.pila.tope() == 'b'):
                        self.b_b_y()
                        trans='|b/b/y|'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif (caracter == 'a'):
                    if (self.pila.tope() == 'a'):
                        self.a_a_y()
                        trans='|a/a/y|'
                        self.transiciones.append('      '+trans)
                    else:
                        break
                elif(caracter == ' '):
                    
                    if (self.pila.tope() == '#' and self.getQ_2()):
                        self.y_n_n()
                        trans='|y/#/#|'
                        self.transiciones.append('      '+trans)


        nega='*No es palondrime*'
        if (self.getR_final()):
            acept='*Es palindrome*'
            self.resultado.append(acept)
        elif(self.getP_1()):
            error='*Deben llevar por lo  menos una C *'
            self.resultado.append(error)
            self.resultado.append(nega)
        else:
            self.resultado.append(nega)

auto=Automatapila("abbcbba")
auto.validar()

