jQuery(document).ready(function() {
	jQuery(".logo").rotate({
		bind:{
			mouseover : function() {
				$(this).rotate({animateTo:180})
			},
			mouseout : function() {
				$(this).rotate({animateTo:0})
			}
		} 
 	});
});