(function() {

var PlayerInteraction = function() {
	this.currentState = RoomState.BATTLE;
	this.controllers = new Array();
}

var p = PlayerInteraction.prototype;

RoomState = {
	BATTLE : "Battle",
	CLEARED : "Cleared",
	PAUSED : "Paused"
}

p.withGameInteractor = function(interactor) {
	this.gameInteractor = interactor;
}

p.controlling = function(controller) {
	this.controllers.push(controller);
	return this;
}

p.getGame = function() {
	return this.gameInteractor;
}

p.start = function() {
	this.startControllers();
}

p.up = function() {
	this.movePlayer(Dir.UP);
}

p.down = function() {
	this.movePlayer(Dir.DOWN);
}

p.right = function() {
	this.movePlayer(Dir.RIGHT);
}

p.left = function() {
	this.movePlayer(Dir.LEFT);
}

p.movePlayer = function(dir) {
	if(this.currentState != RoomState.PAUSED) {
		this.gameInteractor.movePlayer(dir);
		this.updateState();
	}
}

p.updateState = function() {
	if(this.currentState == RoomState.BATTLE && this.gameInteractor.isRoomCleared()) {
		this.updateStateTo(RoomState.CLEARED);
		this.stopControllers();
	}
}

p.updateStateTo = function(nextState) {
	this.currentState = nextState;
}

p.startControllers = function() {
	for(var i = 0; i < this.controllers.length; i++) {
		this.controllers[i].start();
	}
}

p.stopControllers = function() {
	for(var i = 0; i < this.controllers.length; i++) {
		this.controllers[i].stop();
	}
}

this.PlayerInteraction = PlayerInteraction;

}());