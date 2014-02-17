(function() {
	var Sprite = function(spriteType) {
		this.spriteType = spriteType;
	}

	var p = Sprite.prototype;

	p.getTile = function() {
		return this.tile;
	}

	p.occupy = function(nextTile) {
		this.tile = nextTile;
		this.tile.addSprite(this);
	}

	p.deoccupy = function() {
		if(this.tile == null)
			return;
		this.tile.dropSprite(this);
		this.tile = null;
	}

	p.getSpriteType = function() {
		return this.spriteType;
	}

	p.toString = function() {
		return this.getSpriteType().toString() + " occupying " + this.tile;
	}

	this.Sprite = Sprite;

}());