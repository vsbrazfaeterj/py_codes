class Conversor_ps:
   def __init__(self):
      self.paxpsi = 0.000145038
      self.pa = 100000
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

   def converter_barXpa(self, bar):
      
      result = bar * self.pa
      return result
  
   def converter_paXbar(self, pa):
     
      if pa != 0:
         result = pa / self.pa  
         return result
      else:
         return "divisão por zero imposivel!"
      
   def converter_psiXpa(self, psi):
     
     result = psi * (self.psi / self.pa) 
     return result
        
   
conv = Conversor_ps()

#teste
print(f"{conv.converter_barXpsi(2):.4f} psi")
print(f"{conv.converter_psiXbar(14.5038 ):.4f} bar")
print(f"{conv.converter_barXpa(0.0003):.4f} pa")
print(f"{conv.converter_paXbar(3):.15f} bar")
print(f"{conv.converter_psiXpa(0.0001):.15f} pa")