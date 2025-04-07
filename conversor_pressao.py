class Conversor_ps:
  def __init__(self):
   
     self.pca = 100000
     self.psi = 14.5038
   
  def converter_barXpsi(self, bar):
     
     result = bar * self.psi 
     return result
   
  def converter_psiXbar(self, psi):
      if psi != 0: 
         result = psi / self.psi
         return result
      else:
         return "divisão por zero invalida"
      

conv = Conversor_ps()

#teste
print(conv.converter_barXpsi(2), "psi")
print(conv.converter_psiXbar(14.5038 * 2))