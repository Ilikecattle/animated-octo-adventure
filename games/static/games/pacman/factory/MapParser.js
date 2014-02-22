(function() {

var MapParser = function(factory) {
	this.factory = factory;
}

MapLegend = {
	PLAYER : "p",
	GRASS : 'g',
	ROCK : "R",
	RAND_ENEMY : '*'
}

	var p = MapParser.prototype;
	
	p.parseMap = function(map) {
		var height = map.length;
		var width = map[0].length;

		this.game = this.factory.makeGame();
		this.map = this.factory.makeMap(width, height);

		for(var y = 0; y < height; y++) {
			if(map[y].length != width) {
				console.log("Row " + y + " has incorrect length");
			}
			for(var x = 0; x < width; x++) {
				for(var i = 0; i < map[y][x].length; i++) {
					this.addSprite(map[y][x].charAt(i), x, y);
				}
			}
		}
		return this.game;
	}

	p.addSprite = function(spriteCode, x, y) {
		var sprite = this.getSprite(spriteCode);
		if(sprite != null) {
			this.map.put(sprite, x, y);
		}
		return sprite;
	}

	p.getSprite = function(spriteCode) {
		var sprite = null;
		switch(spriteCode) {
			case MapLegend.PLAYER:
				sprite = this.factory.makePlayer();
				break;
			case MapLegend.GRASS:
				sprite = this.factory.makeGrass();
				break;
			case MapLegend.ROCK:
				sprite = this.factory.makeRock();
				break;
			case MapLegend.RAND_ENEMY:
				sprite = this.factory.makeRandomEnemy();
				break;
		}
		return sprite;
	}

	/**
	 * Returns a string representation of this object.
	 * @method toString
	 * @return {String} a string representation of the instance.
	 **/
	p.toString = function() {
		return "MapParser";
	}

	this.MapParser = MapParser;
}());