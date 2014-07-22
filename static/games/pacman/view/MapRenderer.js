(function() {

var MapRenderer = function(map) {
	this.map = map;
	this.imageLoader = new ImageLoader(this.CELL_WIDTH, this.CELL_HEIGHT);
	this.imageLoader.loadImages();
	this.createTiles(this.worldWidth(), this.worldHeight());
	this.addGrid();
	this.x = -this.CELL_HGAP * 2;
	this.y = -this.CELL_VGAP * 2;
}

var p = MapRenderer.prototype = new Container();

p.CELL_WIDTH = 64;
p.CELL_HEIGHT = 64;
p.CELL_HGAP = 0;
p.CELL_VGAP = 0;

p.addGrid = function() {
	var graphics = new Graphics().beginFill("#333333");
	var numVerticalLines = this.worldWidth() - 1;
	var numHorizontalLines = this.worldHeight() - 1;
	var totalWidth = this.worldWidth() * (this.CELL_WIDTH + this.CELL_HGAP);
	var totalHeight = this.worldHeight() * (this.CELL_HEIGHT + this.CELL_VGAP);
	var xOffset = 1;
	var yOffset = 1;
	var horizontalLineThickness = this.CELL_VGAP > 0 ? this.CELL_VGAP : 2;
	var verticalLineThickness = this.CELL_HGAP > 0 ? this.CELL_HGAP : 2;

	for(var x = 0; x < numVerticalLines; x++) {
		graphics.drawRect(
			2 * this.CELL_HGAP + (this.CELL_WIDTH + this.CELL_HGAP) * (x + xOffset) - (this.CELL_HGAP * 0.5) - (verticalLineThickness * 0.5),
			this.CELL_VGAP * 2,
			verticalLineThickness,
			totalHeight - this.CELL_VGAP
		);
		for(var y = 0; y < numHorizontalLines; y++) {
			graphics.drawRect(
				this.CELL_HGAP * 2,
				2 * this.CELL_VGAP + (this.CELL_HEIGHT + this.CELL_VGAP) * (y + yOffset) - (this.CELL_VGAP * 0.5) - (horizontalLineThickness * 0.5),
				totalWidth - this.CELL_HGAP,
				horizontalLineThickness
			);
		}
	}
	var shape = new Shape(graphics);
	shape.alpha = 0.25;
	this.addChild(shape);
}

p.createTiles = function(w, h) {
	this.tiles = new Array(w);
	for(var x = 0; x < w; x++) {
		this.tiles[x] = new Array(h);
		for( var y = 0; y < h; y++) {
			this.tiles[x][y] = new TileRenderer();
			this.addChild(this.tiles[x][y]);
		}
	}
}

p.render = function() {
	this.drawCells();
}

p.drawCells = function() {
	for (var x = 0; x < this.worldWidth(); x++) {
        for (var y = 0; y < this.worldHeight(); y++) {
            this.drawCell(x, y);
        }
    }
}

p.drawCell = function(x, y) {
	var startX = 2 * this.CELL_HGAP + (this.CELL_WIDTH + this.CELL_HGAP) * x;
	var startY = 2 * this.CELL_VGAP + (this.CELL_HEIGHT + this.CELL_VGAP) * y;

	var tileRenderer = this.tiles[x][y];
	var sprites = this.map.spritesAt(x, y);
	tileRenderer.clear();

	if(sprites.length == 0)
		return;

	var img = null;
	for(var i = 0; i < sprites.length; i++) {
		img = this.spriteImage(sprites[i]);
		tileRenderer.bitmaps[i].image = img;
		tileRenderer.bitmaps[i].setWidth(this.CELL_WIDTH);
		tileRenderer.bitmaps[i].setHeight(this.CELL_HEIGHT);
	}

	tileRenderer.x = startX;
	tileRenderer.y = startY;
}

p.worldWidth = function() {
    return this.map.getWidth();
}

p.worldHeight = function() {
    return this.map.getHeight();
}

p.windowWidth = function() {
    return (this.CELL_WIDTH + this.CELL_HGAP) * (this.worldWidth() + 1);
}

p.windowHeight = function() {
    return (this.CELL_HEIGHT + this.CELL_VGAP) * (this.worldHeight() + 1);
}

p.spriteImage = function(sprite) {
	if(sprite == null) {
		return null;
	}

	var bitmap = null;
	var spriteType = sprite.getSpriteType();

	switch(spriteType) {
		case SpriteType.PLAYER:
			return this.imageLoader.player();
		case SpriteType.GRASS:
			return this.imageLoader.grass();
		case SpriteType.GHOST:
			return this.imageLoader.ghost();
		case SpriteType.ROCK:
			return this.imageLoader.rock();
	}
}

this.MapRenderer = MapRenderer;

}());