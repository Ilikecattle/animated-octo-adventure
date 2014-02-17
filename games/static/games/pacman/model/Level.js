(function() {

var Level = function() {
	this.gameFactory = new DefaultGameFactory();
}

var p = Level.prototype;

p.setFactory = function(factory) {
	this.gameFactory = factory;
}

p.parseMap = function() {
	var parser = new MapParser(this.gameFactory);
	this.parseResult = parser.parseMap(this.map);
	return this.parseResult;
}

this.Level = Level;
}());