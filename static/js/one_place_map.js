ymaps.ready(init);

var myMap;

function init () {
    // Инициализация табов.
    // После исполнения команды tab-2 получит style='display:none'.
    // Карта будет инициализированная, но будет иметь нулевой размер.
    // В данном случае это хорошо, так как невидимая карта не будет загружать невидимые тайлы.
    $.ajax({
        type: "GET",
        dataType: "json",
        success: function(data) {
            place = JSON.parse(data.place);
            place = place[0];            
            $('#tabs').tabs();
            myMap = new ymaps.Map('tab-2', {
                center: [place.fields.latitude, place.fields.longitude],
        	    zoom: 16
            });

            BalloonContentLayout = ymaps.templateLayoutFactory.createClass(
        	            '<div style="margin: 10px;">' +
        	                '<b>$[properties.name]</b><br />' +
        	                '<img class="img-map" src="$[properties.img]"/><br /> ' +
        	                '<b>$[properties.address]</b>' +
        	            '</div>'
        	        );	
            myMap.geoObjects.add(new ymaps.Placemark([place.fields.latitude, place.fields.longitude], {
        	            name: place.fields.title,
        	            img: '/images/' + place.fields.image,
        	        address: place.fields.address
        	        }, {
        	            balloonContentLayout: BalloonContentLayout
        	        }));
            // В момент показа нового таба будем пересчитывать размер карты.
            // Карта примет максимально возможные значения при активации ее таба,
            // и нулевые как только будет выбран первый таб.
            // Требуется слушать именно tabsshow, а не tabsselect, так как требуется
            // чтобы элемент, где располагается карта, уже был виден.
            $('#tabs').bind('tabsshow', function (event, ui) {
                myMap.container.fitToViewport();
            });
        },
    });
}
