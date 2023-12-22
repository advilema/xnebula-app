function createInteractiveMap(containerId, mapFile, markersData) {
    var map = L.map(containerId).setView([0, 0], 2);

    L.imageOverlay(mapFile, [[-90, -180], [90, 180]]).addTo(map);

    markersData.forEach(function (markerData, index) {
        var marker = L.marker([markerData.latitude, markerData.longitude])
            .addTo(map)
            .bindPopup(markerData.popupContent);

        marker.bindTooltip(markerData.popupContent, { permanent: true, direction: 'right', className: 'marker-tooltip' });
    });

    function getColor(index) {
        // You can customize the colors based on the index or any other criteria
        var colors = ['red', 'blue', 'green', 'yellow', 'purple'];
        return colors[index % colors.length];
    }
}
