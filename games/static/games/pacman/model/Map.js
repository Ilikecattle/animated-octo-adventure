(function() {

var Map = function(w, h) {
	this.width = w;
	this.height = h;

	this.tiles = new Array(w);
	for (var x = 0; x < w; x++) {
		this.tiles[x] = new Array(h);
		for(var y = 0; y < h; y++) {
			this.tiles[x][y] = new Tile(x, y);
		}
	}
}

var p = Map.prototype;

p.getWidth = function() {
	return this.width;
}

p.getHeight = function() {
	return this.height;
}

p.put = function(sprite, x, y) {
	sprite.occupy(this.tileAt(x, y));
}

p.withinBorders = function(x, y) {
	return x >= 0 && x < width && y >= 0 && y < height;
}

p.spriteAt = function(x ,y) {
	return this.tileAt(x, y).topSprite();
}

p.spritesAt = function(x, y) {
	return this.tileAt(x, y).sprites;
}

p.spriteTypeAt = function(x, y) {
	var sprite = spriteAt( x, y );
	if( sprite == null ) {
		result = spriteType.EMPTY;
	} else {
		result = sprite.getSpriteType();
	}

	return result;
}

p.tileAt = function(x, y) {
	return this.tiles[x][y];
}

p.tileAtOffset = function(startTile, dx, dy) {
	var newX = startTile.getX() + dx;
	var newY = startTile.getY() + dy;

	if(newX >= this.getWidth() || newY >= this.getHeight() || newX < 0 || newY < 0)
		return;

	return this.tileAt(newX, newY);
}

p.tileAtDirection = function(tile, dir) {
	return this.tileAtOffset(tile, dir.getDx(), dir.getDy());
}

p.containsEnemy = function() {
	for (var x = 0; x < this.getWidth(); x++) {
		for(var y = 0; y < this.getHeight(); y++) {
			if( this.tiles[x][y].containsSpriteType(SpriteType.GHOST) )
				return true;
		}
	}
}

this.Map = Map;

}());