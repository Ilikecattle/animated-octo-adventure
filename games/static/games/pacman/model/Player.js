(function() {
var Player = function() {
	
}

var p = Player.prototype = new Sprite();

p.direction = Direction.RIGHT;

p.getSpriteType = function() {
	return SpriteType.PLAYER;
}

p.getDirection = function() {
	return this.direction;
}

p.setDirection = function(dir) {
	this.direction = dir;
}

this.Player = Player;

}());