(function(){

var TileRenderer = function() {
	this.initialize();
	this.bitmaps = new Array(5);
	for(var i = 0; i < this.bitmaps.length; i++) {
		this.bitmaps[i] = new Bitmap();
		this.addChild(this.bitmaps[i]);
	}
}

var p = TileRenderer.prototype = new Container();

p.clear = function() {
	for(var i = 0; i < this.bitmaps.length; i++) {
		this.bitmaps[i].image = null;
	}
}

this.TileRenderer = TileRenderer;

}());