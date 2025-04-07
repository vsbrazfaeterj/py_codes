class Conversor_ps:
   def __init__(self):
      self.pa = 100000
      self.psi = 14.5038
      self.pa_por_psi = 6894.76
   
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
      
   def converter_paXpsi(self, pa):

      if pa != 0:
         result = pa / self.pa_por_psi
         return result
      else:
         return "divisão por zero imposivel!"
  
   def converter_psiXpa(self, psi):
      
      result = psi * self.pa_por_psi
      return result        
   
conv = Conversor_ps()

#teste
print(f"{conv.converter_barXpsi(2):.4f} psi")
print(f"{conv.converter_psiXbar(14.5038 ):.4f} bar")
print(f"{conv.converter_barXpa(0.0003):.4f} pa")
print(f"{conv.converter_paXbar(1):.15f} bar")
print(f"{conv.converter_paXpsi(1):.9f} psi")
print(f"{conv.converter_psiXpa(1):.4f} pa")