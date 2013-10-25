ymaps.ready(init);
var myMap;

function init () {
    myMap = new ymaps.Map("map", {
        center: [54.984634, 73.375038],
        zoom: 11
    }, {
        balloonMaxWidth: 200
    });
    myMap.controls
        // Кнопка изменения масштаба.
        .add('zoomControl', { left: 5, top: 5 })
        // Список типов карты
        .add('typeSelector')
        // Стандартный набор кнопок
        .add('mapTools', { left: 35, top: 5 });
    myMap.events.add('click', function (e) {
    	if (!myMap.balloon.isOpen()) {
	        var coords = e.get('coordPosition');
	        jQuery("#id_latitude").val(coords[0].toPrecision(8));
	        jQuery("#id_longitude").val(coords[1].toPrecision(8));
	        myMap.balloon.open(coords, {
	            contentHeader:'',
	            contentBody:'место находиться здесь'
	        });
	    }
	    else {
            myMap.balloon.close();
        }
    });
}