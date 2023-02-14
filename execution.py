

#importing my module 

import minciencias_convoc as mc

# main execution
if __name__ == "__main__":
    web = 'https://minciencias.gov.co/convocatorias/todas'
    main_web ='https://minciencias.gov.co'
    conv = mc.mincienciasConvoc(web, main_web)
    conv.get_links()
