(function() {

var ImageLoader = function() {

}

var p = ImageLoader.prototype;

p.loadImages = function() {
	this.playerImage = this.loadImage("img/PacManright.gif");
	this.ghostImage = this.loadImage("img/ghost.gif");
	this.grassImage = this.loadImage("img/grass.png");
	this.rockImage = this.loadImage("img/rock.png");
}

p.loadImage = function(filename) {
	var img = new Image();
	img.src = filename;
	return img;
}

p.player = function(dir) {
	return this.playerImage;
}

p.grass = function() {
	return this.grassImage;
}

p.ghost = function() {
	return this.ghostImage;
}

p.rock = function() {
	return this.rockImage;
}

this.ImageLoader = ImageLoader;

}());