(function() {
	var Tile = function(x, y) {
		this.x = x;
		this.y = y;
		this.sprites = new Array();
	}

	p = Tile.prototype;

	p.getX = function() {
		return this.x;
	}

	p.getY = function() {
		return this.y;
	}

	p.topSprite = function() {
		return this.sprites[this.sprites.length - 1];
	}

	p.containsSprite = function(sprite) {
		for(var i = 0; i < this.sprites.length; i++) {
			if(this.sprites[i] == sprite) {
				return true;
			}
		}
		return false;
	}

	p.containsSpriteType = function(type) {
		for(var i = 0; i < this.sprites.length; i++) {
			if(this.sprites[i].getSpriteType() == type) {
				return true;
			}
		}
		return false;
	}

	p.dropSprite = function(sprite) {
		for(var i = 0; i < this.sprites.length; i++) {
			if(this.sprites[i] == sprite) {
				this.sprites.splice(i, 1);
			}
		}
	}

	p.addSprite = function(sprite) {
		this.sprites.push(sprite);
	}

	p.toString = function() {
		return "[Tile] [" + this.getX() + ", " + this.getY() + "]";
	}

	this.Tile = Tile;

}());