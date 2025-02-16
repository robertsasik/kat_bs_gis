import folium as fl
import json

data_source = "kataster_bs_exp_drp.geojson"
# 🔹 Mapa
m = fl.Map(
    tiles='CartoDB.Voyager',
    location=[48.446457119484, 18.906725918256523],
    zoom_start=13,
    control_scale=True
    )
# 🔹 Načítanie GeoJSON
with open(data_source, "r", encoding="utf-8") as f:
    data = json.load(f)

# 🔹 Mapa farieb podľa "drp"
color_map = {
    2: "#8B4513",   # Orná pôda 
    3: "#228B22",   # Chmeľnica 
    4: "#800000",   # Vinica 
    5: "#c5d89e",   # Záhrada 
    6: "#FFD700",   # Ovocný sad 
    7: "#ADFF2F",   # Trávnatý porast 
    10: "#7eb215",  # Lesný pozemok 
    11: "#4169E1",  # Vodná plocha 
    13: "#808080",  # Zastavaná plocha
    14: "#D3D3D3"   # Ostatná plocha 
}

# 🔹 Štýlovacia funkcia
def style_function(feature):
    drp_value = feature["properties"].get("drp", 0)  # Ak chýba, daj default 0
    return {
        "fillColor": color_map.get(drp_value, "white"),  # Farba podľa drp
        "color": "black",  # Obrys
        "weight": 0.1,
        "fillOpacity": 0.5
    }

# 🔹 Pridanie GeoJSON vrstvy s farbami
fl.GeoJson(
    data,
    name="Kataster Banská Štiavnica",
    style_function=style_function,
    popup = fl.GeoJsonPopup(fields=["parcela","druh_poz", "vym"], aliases=["Parcela","Druh pozemku", "Výmera v m²"]),  # Zobrazí sa po kliknutí 
    #tooltip=fl.GeoJsonTooltip(fields=["parcela"], aliases=["Parcela číslo"])  # Ukáže sa po prejdení myšou
).add_to(m)

# 🔹 Ovládanie vrstiev
fl.LayerControl().add_to(m)

# 🔹 Uloženie mapy
m.save("index.html")

print("Mapa bola uložená ako index.html. Otvor ju v prehliadači.")
