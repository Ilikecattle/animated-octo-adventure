(function() {

var DefaultGameFactory = function() {
}

var p = DefaultGameFactory.prototype;

p.makeGame = function() {
	this.game = new Game();
	return this.game;
}

p.makePlayer = function() {
	var p = new Player();
	this.getGame().addPlayer(p);
	return p;
}

p.makeRandomEnemy = function() {
	var enemy = new Sprite(SpriteType.GHOST);
	this.getGame().addEnemy(enemy);
	return enemy;
}

p.makeMap = function(w, h) {
	var m = new Map(w, h);
	this.getGame().setMap(m);
	return m;
}

p.makeGrass = function() {
	return new Sprite(SpriteType.GRASS);
}

p.makeRock = function() {
	return new Sprite(SpriteType.ROCK);
}

p.getGame = function() {
	return this.game;
}

this.DefaultGameFactory = DefaultGameFactory;

}());