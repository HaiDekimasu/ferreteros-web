from django.shortcuts import render

def home(request):
    # Lista de nombres extraídos directamente de image_d89dbf.png
    # Asegúrate de que los archivos en /static/pdfs/ se llamen exactamente así
    nombres_catalogos = [
        "ACCESORIOS HERRAMIENTAS - BAUKER",
        "ACCESORIOS UBERMANN",
        "AIRE LIBRE_V2",
        "ARTÍCULOS DE ASEO Y LIMPIEZA_V2 1",
        "BAÑOS Y COCINA_V2",
        "CERRAJERÍA",
        "CLIMATIZACIÓN Y ELECTRODOMÉSTICOS_V2",
        "CUERDAS Y AMARRES",
        "ELECTRICIDAD",
        "ESPECIAL FIESTAS PATRIAS_V2",
        "ESPECIAL NAVIDAD_V2",
        "GASFITERIA _PLOMERIA",
        "HERRAMIENTAS ELECTRICAS BAUKER",
        "HERRAMIENTAS ELECTRICAS UBERMANN",
        "HERRAMIENTAS MANUALES BAUKER-KARSON",
        "HERRAMIENTAS MANUALES UBERMANN (1)",
        "ILUMINACIÓN_V2",
        "JARDÍN - MAQUINARIA",
        "JARDÍN - RIEGO Y HERRAMIENTAS_V2",
        "MENAJE Y DECORACIÓN_V2",
        "MUEBLES Y ORGANIZACIÓN_V2",
        "PINTURAS",
        "PISOS Y REVESTIMIENTOS_V2",
        "QUINCALLERIA",
        "SEGURIDAD INDUSTRIAL - EPP"
    ]
    
    context = {
        'catalogos': nombres_catalogos
    }
    
    return render(request, 'Ferreteros/index.html', context)