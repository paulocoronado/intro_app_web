var map = L.map('map').setView([4.627911598272655, -74.06621993742053], 13);

L.tileLayer('https://tile.openstreetmap.org/{z}/{x}/{y}.png', {
    maxZoom: 19,
    attribution: '&copy; <a href="http://www.openstreetmap.org/copyright">OpenStreetMap</a>'
}).addTo(map);

//Manejar el evento de hacer click en el mapa

    function onMapClick(e) {
        var marker = L.marker(e.latlng).addTo(map);
    }

map.on('click', onMapClick);