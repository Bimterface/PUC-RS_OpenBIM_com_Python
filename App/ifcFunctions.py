import ifcopenshell, tempfile, io


def ifc_file_to_bytes(ifc_file):
    """
    Serializes an ifcopenshell.file object to bytes.
    """
    buffer = io.BytesIO()
    # Write IFC content as string to buffer
    buffer.write(ifc_file.to_string().encode('utf-8'))
    return buffer.getvalue()

def abrir_ifc(uploaded_file):

    # Read the file as bytes
    ifc_bytes = uploaded_file.read()
    # """Opens an IFC file in memory using a temporary file."""
    with tempfile.NamedTemporaryFile(suffix=".ifc") as tmp_file:
        tmp_file.write(ifc_bytes)
        ifc_model = ifcopenshell.open(tmp_file.name)
        return ifc_model


def guid_paredes(ifc_file):
    
    paredes = ifc_file.by_type("IfcWall")

    return paredes

def area_total_parts(ifc_file, material):


    builindElementParts = ifc_file.by_type("IfcBuildingElementPart")

    alvenarias = []

    for part in builindElementParts:
        if part.Name == material:
            alvenarias.append(part)

    lista_areas = []

    for alvenaria in alvenarias:
        area = area_building_element_part(alvenaria)
        lista_areas.append(area)

    area_total = {}
    
    try:
        for area in lista_areas:
            area_total.update({
                area['Material']: area['Área'] + area_total.get(area['Material'], 0)
            })
    except:
        pass

    return area_total

def area_building_element_part(part):

    for propertySet in part.IsDefinedBy:
        if propertySet.RelatingPropertyDefinition.Name == 'Component Quantities':
            for quantity in propertySet.RelatingPropertyDefinition.Quantities:
                if quantity.Name == 'Área de Componente Projetada (Líquida)':
                    return {
                        'Material': part.Name,
                        'Área': quantity.AreaValue,
                    }
                

def lista_de_materiais(ifc_file):

    buildindElementParts = ifc_file.by_type("IfcBuildingElementPart")

    materiais = []

    for part in buildindElementParts:
        materiais.append(part.Name)

    materiais_com_areas = {}

    materiais_unicos = list(set(materiais))

    for material in materiais_unicos:
        area = area_total_parts(ifc_file, material)
        materiais_com_areas.update(area)

    return materiais_com_areas

def renomear_paredes(ifc_file):

    paredes = ifc_file.by_type("IfcWall")

    for parede in paredes:
        relation = parede.IsDecomposedBy
        if relation:
            for relatedObject in relation[0].RelatedObjects:
                if relatedObject.Name == "Acabamento Externo":
                    parede.Name = "Parede Externa"
                else:
                    parede.Name = "Parede Interna"

    return paredes
            