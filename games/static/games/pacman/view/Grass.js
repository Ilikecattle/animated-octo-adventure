(function(){

var Grass = function() {

}

var p = Grass.prototype = new Sprite();

p.getSpriteType = function() {
	return SpriteType.GRASS;
}

this.Grass = Grass;

}());