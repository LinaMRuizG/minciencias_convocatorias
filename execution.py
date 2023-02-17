

#importing my module 

import minciencias_convoc as mc

# main execution
if __name__ == "__main__":
    web = 'https://minciencias.gov.co/convocatorias/todas'
    main_web ='https://minciencias.gov.co'
    conv = mc.mincienciasConvoc(web, main_web)
    conv.run() 
    #conv.get_table()
    #conv.save()
    #conv.comparing()
    #conv.emailing()
    #print(conv.newones)

    # delete and uncoment the last 2 lines after test the function to read and compare tables
    #setting -I JUST PUT THIS TO SAVE THE TEST FILES TO THE NEXT FUNCTION
    #from datetime import date, timedelta
    #first_table = conv.get_table()
    #uno = first_table[:20].reset_index(drop = True) # this is the most new table because have the first most recent convocatorias
    #other7 = first_table[2:].reset_index(drop = True)
    #other14 = first_table[5:].reset_index(drop = True)
    #other7.to_pickle(f"df_{ date.today() - timedelta(days=7)}")
    #other14.to_pickle(f"df_{ date.today() - timedelta(days=14)}")
