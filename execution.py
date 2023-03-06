#importing my module 
import minciencias_convoc as mc

# main execution
if __name__ == "__main__":
    
    web = 'https://minciencias.gov.co/convocatorias/todas'
    main_web ='https://minciencias.gov.co'
    mailsList = ['lina.ruiz2@udea.edu.co','anderson.ruales@udea.edu.co']
    
    conv = mc.mincienciasConvoc(web, main_web, mailsList)# you can also set: the frequency to run and the nPages
    conv.run() 
    #conv.delete()
    #conv.get_table()
    #conv.comparing()
    #print(conv.newones)