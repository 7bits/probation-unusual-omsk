ymaps.ready(init);
    function init () {
    var map = new ymaps.Map('map', {
            center: [54.984634, 73.375038],
            zoom: 12
        }),
        // Создание макета содержимого балуна.
        // Макет создается с помощью фабрики макетов с помощью текстового шаблона.
        BalloonContentLayout = ymaps.templateLayoutFactory.createClass(
            '<div style="margin: 10px;">' +
                '<b>$[properties.name]</b><br />' +
                '<img class="img-map" src="$[properties.img]"/><br /> ' +
                '<b>$[properties.address]</b>' +
            '</div>'
        );
    $.ajax({
        url: "/map/",
        type: "GET",
        dataType: "json",
        success: function(data) {
            all_places = JSON.parse(data.all_places);            
            for (i in all_places) {
                map.geoObjects.add(new ymaps.Placemark([all_places[i].fields.latitude, all_places[i].fields.longitude], {
                    name: all_places[i].fields.title,
                    img: "/images/" + all_places[i].fields.image,
                    address: all_places[i].fields.address
                }, {
                    balloonContentLayout: BalloonContentLayout
                }));
            }
        },
    });
}