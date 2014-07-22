(function() {

var PlayerInputListener = function(modelEvents) {
	this.modelEvents = modelEvents;
	$(stage.canvas).keydown(this.onKeyDown);
	$(stage.canvas).click(this.onClick);
}

var p = PlayerInputListener.prototype;

KeyCode = {
	UP : 87,
	LEFT : 65,
	DOWN : 83,
	RIGHT : 68
}

p.onClick = function(event) {
	var x = event.clientX;
	var y = event.clientY;

	if(x < 230) {
		playerInputListener.modelEvents.left();
	} else if(x > 615) {
		playerInputListener.modelEvents.right();
	} else if(y < 200) {
		playerInputListener.modelEvents.up();
	} else if(y < 400) {
		playerInputListener.modelEvents.down();
	}
}

p.onKeyDown = function(event) {
	var keyCode = event.keyCode;

	switch(keyCode) {
		case KeyCode.LEFT:
			playerInputListener.modelEvents.left();
			break;
		case KeyCode.RIGHT:
			playerInputListener.modelEvents.right();
			break;
		case KeyCode.UP:
			playerInputListener.modelEvents.up();
			break;
		case KeyCode.DOWN:
			playerInputListener.modelEvents.down();
			break;
		default:
			break;
	}
}

this.PlayerInputListener = PlayerInputListener;

}());