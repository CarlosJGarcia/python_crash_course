def funcion(city, country, population=0):
    if population > 0:
        cad = f"{city}, {country} - population {population}"
        cad = cad.title()
    else:
        cad = f"{city}, {country}"
        cad = cad.title() 
    return cad
