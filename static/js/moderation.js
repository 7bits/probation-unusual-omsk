var myMap;

ymaps.ready(init);

function init () {
    $.ajax({
        url: "/moderation/",
        type: "GET",
        dataType: "json",
        success: function(data) {
            all_places = JSON.parse(data.all_places);            
            for (i in all_places) {
                divmap = "map" + i
                myMap = new ymaps.Map(divmap, {
                    center:[all_places[i].fields.latitude, all_places[i].fields.longitude],
                    zoom:16
                }),
                BalloonContentLayout = ymaps.templateLayoutFactory.createClass(
                    '<div style="margin: 10px;">' +
                        '<b>$[properties.name]</b><br />' +
                        '<img class="img-map" src="$[properties.img]"/><br /> ' +
                        '<b>$[properties.address]</b>' +
                    '</div>'
                );
                myMap.geoObjects.add(new ymaps.Placemark([all_places[i].fields.latitude, all_places[i].fields.longitude], {
                    name: all_places[i].fields.title,
                    img: '/images/' + all_places[i].fields.image,
                    address: all_places[i].fields.address
                    }, {
                        balloonContentLayout: BalloonContentLayout
                }));
            }
        },
    });
}